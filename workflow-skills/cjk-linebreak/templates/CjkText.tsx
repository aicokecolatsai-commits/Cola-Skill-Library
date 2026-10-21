import { Fragment } from "react"
import { splitCjkWords } from "@/lib/cjkWordBreak" // 依專案路徑調整

/** Chinese text that only wraps between words: inserts <wbr> at word boundaries; style the parent with `.cjk` (word-break: keep-all). */
export default function CjkText({ children }: { children: string }) {
  const words = splitCjkWords(children)
  return <>{words.map((word, index) => <Fragment key={index}>{index > 0 ? <wbr /> : null}{word}</Fragment>)}</>
}
