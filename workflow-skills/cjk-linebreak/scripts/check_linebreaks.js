// 中文換行檢查：找出畫面上每一個實際換行的位置，回報「在兩個中文字中間換行、而且那裡沒有 <wbr> 或空白」的地方。
// 用法：貼到瀏覽器 DevTools 的 Console 執行，或交給 agent 的瀏覽器工具執行。
// 至少在 360、390、768、1280px 寬度各跑一次；通過標準是 midWordBreaks 為 0、horizontalScroll 為 false。
// 只檢查目前畫面上看得到的內容：摺疊選單、分頁、對話框要先打開再跑一次。
(() => {
  const HAN = /[㐀-鿿豈-﫿]/
  const SKIP = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEXTAREA", "INPUT", "SELECT", "OPTION", "SVG", "CANVAS"])
  const range = document.createRange()
  const issues = []
  let lineBreaks = 0
  let prev = null // 上一個字：{ char, top, height, sawWbr, box }

  // 不同的區塊（block、flex、grid、inline-block……）本來就會分行，只比較同一個區塊裡的文字
  const isBox = (el) => { const d = getComputedStyle(el).display; return d !== "inline" && d !== "contents" }
  const boxOf = (el) => { while (el && !isBox(el)) el = el.parentElement; return el }
  const isHidden = (el) => { const s = getComputedStyle(el); return s.display === "none" || s.visibility === "hidden" }

  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      if (node.nodeType === Node.ELEMENT_NODE && (SKIP.has(node.tagName.toUpperCase()) || isHidden(node))) return NodeFilter.FILTER_REJECT
      return NodeFilter.FILTER_ACCEPT
    },
  })

  for (let node = walker.nextNode(); node; node = walker.nextNode()) {
    if (node.nodeType === Node.ELEMENT_NODE) {
      if (node.tagName === "WBR") { if (prev) prev.sawWbr = true }
      else if (node.tagName === "BR") prev = null
      continue
    }
    const box = boxOf(node.parentElement)
    if (prev && prev.box !== box) prev = null
    const text = node.textContent
    for (let i = 0; i < text.length; i++) {
      const char = text[i]
      if (/\s/.test(char)) { if (prev) prev.sawWbr = true; continue } // 空白本來就能換行
      range.setStart(node, i)
      range.setEnd(node, i + 1)
      const rect = range.getBoundingClientRect()
      if (!rect.width && !rect.height) continue
      if (prev && rect.top > prev.top + prev.height / 2) {
        lineBreaks++
        if (HAN.test(prev.char) && HAN.test(char) && !prev.sawWbr) {
          const before = i ? text.slice(Math.max(0, i - 6), i) : prev.char
          issues.push({ context: before + "｜" + text.slice(i, i + 6), tag: node.parentElement.tagName.toLowerCase() })
        }
      }
      prev = { char, top: rect.top, height: rect.height, sawWbr: false, box }
    }
  }

  return {
    width: window.innerWidth,
    lineBreaks,
    midWordBreaks: issues.length,
    horizontalScroll: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    samples: issues.slice(0, 20),
  }
})()
