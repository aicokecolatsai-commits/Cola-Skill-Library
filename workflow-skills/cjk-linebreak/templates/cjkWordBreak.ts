// 模板來源：動齡 App（web-main/lib/cjkWordBreak.ts）。複製到專案後，把 PROTECTED_TERMS 的產品詞換成自己專案的品牌詞與專業用語。
// Split Chinese copy into words so lines only break between words (paired with `word-break: keep-all`).
// Intl.Segmenter (ICU dictionary) mis-splits a few product and common terms; keep those whole.
const PROTECTED_TERMS = [
  // Product terms
  "動齡", "福幣", "福站", "網頁版", "健康護照", "Health Connect",
  // Health and assessment terms the ICU dictionary splits
  "體適能", "常模", "肌耐力", "肌力", "量測", "步數", "構面", "判讀", "正確率", "中位數", "百分點", "完成度", "局數",
  "細懸浮微粒", "版本化", "活動度",
  // Common words split by the dictionary
  "每一次", "計入", "載入", "時區", "等同", "量血壓", "小獎勵", "認知遊戲", "很重", "拿得到", "拿到的",
]

const protectedPattern = new RegExp(`(${PROTECTED_TERMS.map((term) => term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|")})`)

const CLOSING = /^[。，、；：！？」』）〉》】…—,.;:!?)\]]+$/
const OPENING = /[「『（〈《【(\[]$/

type Segmenter = { segment: (text: string) => Iterable<{ segment: string }> }

function createSegmenter(): Segmenter | null {
  const Ctor = (Intl as unknown as { Segmenter?: new (locale: string, options: { granularity: string }) => Segmenter }).Segmenter
  return Ctor ? new Ctor("zh-Hant", { granularity: "word" }) : null
}

let segmenter: Segmenter | null | undefined

/** Words of `text` in order; joining them returns the original text. Without Intl.Segmenter, the whole text is one word. */
export function splitCjkWords(text: string): string[] {
  if (segmenter === undefined) segmenter = createSegmenter()
  if (!segmenter) return [text]
  const pieces: string[] = []
  for (const part of text.split(protectedPattern)) {
    if (!part) continue
    if (PROTECTED_TERMS.includes(part)) pieces.push(part)
    else for (const { segment } of segmenter.segment(part)) pieces.push(segment)
  }
  // Never start a line with closing punctuation or end one with opening punctuation.
  const words: string[] = []
  for (const piece of pieces) {
    const last = words.length - 1
    if (last >= 0 && (CLOSING.test(piece) || OPENING.test(words[last]))) words[last] += piece
    else words.push(piece)
  }
  return words
}
