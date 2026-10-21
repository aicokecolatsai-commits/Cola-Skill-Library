// 模板來源：動齡 App 的 Vitest 測試。範例句子和詞彙請換成自己專案的文案。
import { expect, it } from "vitest"
import { splitCjkWords } from "./cjkWordBreak"

it("splits Chinese copy into whole words and keeps the original text", () => {
  const text = "動齡 App 上架後，您可下載並開啟支援的手機健康資料同步。"
  const words = splitCjkWords(text)
  expect(words.join("")).toBe(text)
  for (const word of ["動齡", "下載", "開啟", "手機", "健康", "資料", "同步。"]) expect(words).toContain(word)
})

it("keeps punctuation attached so no line starts with 。 or ends with 「", () => {
  const words = splitCjkWords("讀取手機資料。請按「同步」，完成後回來。")
  expect(words.some((word) => /^[。，」]/.test(word))).toBe(false)
  expect(words.some((word) => /「$/.test(word))).toBe(false)
  expect(words).toContain("資料。")
})

it("keeps protected terms whole even when the dictionary would split them", () => {
  expect(splitCjkWords("網頁版無法直接讀取")).toContain("網頁版")
  expect(splitCjkWords("每一次完成，都是照顧自己的累積。")).toContain("每一次")
})

it("keeps health and assessment terms whole", () => {
  const words = splitCjkWords("65 歲以下常模尚未設定，因此不顯示體適能年齡判讀。肌力肌耐力、量測不重複計入，步數與構面不等同能力。")
  for (const term of ["常模", "體適能", "判讀。", "肌力", "肌耐力、", "量測", "計入，", "步數", "構面", "等同"]) expect(words).toContain(term)
})
