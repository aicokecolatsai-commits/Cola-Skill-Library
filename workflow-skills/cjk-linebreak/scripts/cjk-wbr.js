/*!
 * cjk-wbr.js：通用的中文斷詞換行腳本（不需要建置、不需要任何套件）
 *
 * 在網頁載入後，用瀏覽器內建的 Intl.Segmenter 把中文切成詞，在詞與詞之間插入 <wbr>，
 * 再替處理過的區塊加上 word-break: keep-all，讓中文只在詞與詞之間換行。
 * 適用於不能跑建置腳本的平台：Google Blogger、WordPress、Wix、自架網站、任何 HTML 頁面。
 *
 * 用法：放在 </body> 前面
 *   <script>
 *     window.CJK_WBR = {
 *       selector: ".post-body",          // 只處理這些區塊；預設是整個 body
 *       terms: ["福聚徠", "動齡"],         // 專案自己的保護詞彙（不可拆開的詞）
 *       observe: false,                  // 內容會動態載入（例如無限捲動、留言區）時設成 true
 *     }
 *   </script>
 *   <script src="cjk-wbr.js"></script>   （或把本檔內容直接貼進 <script>…</script>）
 *
 * 不支援 Intl.Segmenter 的舊瀏覽器（Chrome 87、Safari 14.1、Firefox 125 以前）會直接略過，頁面維持原樣。
 */
(function () {
  "use strict"

  var config = window.CJK_WBR || {}
  var Segmenter = window.Intl && Intl.Segmenter
  if (!Segmenter) return

  // 通用保護詞彙：瀏覽器的斷詞字典常拆錯這些詞
  var COMMON_TERMS = [
    "物理治療師", "物理治療", "人體工學", "心理諮商", "體適能", "肌耐力", "中高齡", "量血壓", "血壓",
    "上班族", "使用者", "量測", "步數", "判讀", "常模", "正確率", "載入", "計入", "等同", "自己", "日常", "生活", "理解", "了解", "數位", "紀錄", "下載", "工具",
    "不只", "不是", "而是", "每一次", "下一步", "做得到", "用得上", "有跡可循", "五分鐘",
    "一次", "一下", "一個", "一天", "一點", "有限公司",
  ]
  var terms = COMMON_TERMS.concat(config.terms || []).sort(function (a, b) { return b.length - a.length })
  var escape = function (s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") }
  var protectedPattern = new RegExp("(" + terms.map(escape).join("|") + ")")

  var HAN = /[㐀-鿿豈-﫿]/
  var CLOSING = /^[。，、；：！？」』）〉》】…—,.;:!?)\]]+$/
  var OPENING = /[「『（〈《【(\[]$/
  var SKIP = /^(SCRIPT|STYLE|NOSCRIPT|TEXTAREA|INPUT|SELECT|OPTION|CODE|PRE|KBD|SAMP|SVG|MATH|TITLE)$/
  var segmenter = new Segmenter("zh-Hant", { granularity: "word" })

  function splitWords(text) {
    var pieces = []
    text.split(protectedPattern).forEach(function (part) {
      if (!part) return
      if (terms.indexOf(part) >= 0) { pieces.push(part); return }
      for (var it = segmenter.segment(part)[Symbol.iterator](), step = it.next(); !step.done; step = it.next()) pieces.push(step.value.segment)
    })
    // 標點跟著前一個詞；英文、數字、網址這類連續的半形字元不拆開
    var words = []
    pieces.forEach(function (piece) {
      var last = words.length - 1
      var glue = last >= 0 && (
        CLOSING.test(piece) || OPENING.test(words[last]) ||
        /\s$/.test(words[last]) || /^\s/.test(piece) ||
        (/[!-~]$/.test(words[last]) && /^[!-~]/.test(piece))
      )
      if (glue) words[last] += piece
      else words.push(piece)
    })
    return words
  }

  function processText(node) {
    var text = node.nodeValue
    if (!HAN.test(text)) return
    var words = splitWords(text)
    if (words.length < 2) return
    var fragment = document.createDocumentFragment()
    words.forEach(function (word, index) {
      if (index > 0) fragment.appendChild(document.createElement("wbr"))
      fragment.appendChild(document.createTextNode(word))
    })
    node.parentNode.replaceChild(fragment, node)
  }

  function processRoot(root) {
    if (!root || root.nodeType !== 1 || root.hasAttribute("data-cjk-wbr")) return
    if (SKIP.test(root.tagName) || root.isContentEditable) return
    root.setAttribute("data-cjk-wbr", "")
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        for (var el = node.parentElement; el && el !== root; el = el.parentElement) {
          if (SKIP.test(el.tagName) || el.isContentEditable || el.hasAttribute("data-cjk-wbr-skip")) return NodeFilter.FILTER_REJECT
        }
        return NodeFilter.FILTER_ACCEPT
      },
    })
    var nodes = []
    for (var node = walker.nextNode(); node; node = walker.nextNode()) nodes.push(node)
    nodes.forEach(processText)
  }

  function injectStyle() {
    if (document.getElementById("cjk-wbr-style")) return
    var style = document.createElement("style")
    style.id = "cjk-wbr-style"
    // 只套用在處理過的區塊；需要保底時只用 break-word，不用 anywhere
    style.textContent = "[data-cjk-wbr]{word-break:keep-all;overflow-wrap:break-word;line-break:strict}"
    document.head.appendChild(style)
  }

  function run() {
    injectStyle()
    var selector = config.selector || "body"
    var roots = document.querySelectorAll(selector)
    for (var i = 0; i < roots.length; i++) processRoot(roots[i])
    if (config.observe) {
      // 之後才載入的內容：只要落在指定區塊裡面，就處理新加入的元素
      new MutationObserver(function (records) {
        records.forEach(function (record) {
          record.addedNodes.forEach(function (added) {
            if (added.nodeType !== 1 || added.tagName === "WBR") return
            if (added.matches(selector) || added.closest(selector)) processRoot(added)
          })
        })
      }).observe(document.body, { childList: true, subtree: true })
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run)
  else run()
})()
