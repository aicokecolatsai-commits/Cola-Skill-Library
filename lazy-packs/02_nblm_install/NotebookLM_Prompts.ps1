$OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false

# 用來在 4A → 4B 之間保存原文段落
$script:savedDraft = ""

function Show-Menu {
    Clear-Host
    Write-Host "==========================================================" -ForegroundColor Cyan
    Write-Host "   Google NotebookLM 文獻查證 Prompt 產生器" -ForegroundColor Yellow
    Write-Host "==========================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host " [1]  輸入研究主題" -ForegroundColor White
    Write-Host "      由 AI 自動展開問題、撰寫文獻回顧，並自我驗證引用" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host " [2]  直接輸入你的問題" -ForegroundColor White
    Write-Host "      AI 先深化問題、查詢文獻，再自我驗證引用" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host " [3]  貼入半完成的論文草稿" -ForegroundColor White
    Write-Host "      核實引用正確性，再改寫為格式嚴謹、邏輯完整的論文段落" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host " [4A] 術語查證 ─ 生成查證 Prompt" -ForegroundColor White
    Write-Host "      貼入論文段落與術語清單 → 產生 Prompt → 貼到 NotebookLM 取得查證結果" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host " [4B] 段落改寫 ─ 根據查證結果改寫原文（需先完成 4A）" -ForegroundColor White
    Write-Host "      複製 NotebookLM 的查證結果 → 產生改寫 Prompt → 貼到 NotebookLM 取得修正段落" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host " [5]  回填 Wiki 卡 ─ 將自我核對結果寫入對應的 wiki 卡" -ForegroundColor White
    Write-Host "      複製 NotebookLM 的自我核對結果 → 自動比對作者年份 → 回填至 wiki 卡查證記錄" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host " [0]  退出" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "==========================================================" -ForegroundColor Cyan
}

$citationRule = "`n`n[引用格式規範]`n" +
    "引用文獻一律採用 APA 第七版行內引用格式，即在論點後方加上（作者姓氏, 年份），例如（Malar et al., 2011）。`n" +
    "禁止使用數字標籤（如 [1]、上標數字）作為引用記號。`n" +
    "禁止以作者為主詞的句型（如：某某指出…、某某認為…、某某發現…）。`n" +
    "應直接陳述論點，再於句末或適當位置插入引用標記。`n" +
    "範例（正確）：真實自我一致性對情感品牌依附的影響大於理想自我一致性（Malar et al., 2011）。`n" +
    "範例（錯誤）：Malar 等人（2011）指出，真實自我一致性的影響大於理想自我一致性。"

$verifyBlock = "`n`n完成後，請立刻對你剛剛自己生成的段落進行自我核對，確認以下三點並按下方格式輸出：`n" +
    "第一，該引用的論點是否確實出現在對應文獻中。`n" +
    "第二，該論點是否被正確歸因於該作者，而非二手引用。`n" +
    "第三，原文的實際論述與段落中的呈現方式是否存在誤差或過度推論。`n`n" +
    "重要：若某篇文獻不在你的資料庫中，請在驗證結果欄位明確標示「文獻不在資料庫中」，並於說明欄位提示使用者需自行取得該文獻原文核實，切勿推測或捏造文獻內容。`n`n" +
    "輸出驗證結果的格式如下：`n" +
    "[引用來源]作者（年份）`n" +
    "[段落中的主張]你生成的段落中的引用內容`n" +
    "[文獻中的實際論述]從原文找到的對應段落（若文獻不在資料庫中，填入「無法查證」）`n" +
    "[驗證結果]正確／部分正確／錯誤／文獻不在資料庫中`n" +
    "[說明]若有誤差或問題，具體說明差異所在；若文獻不在資料庫中，請提示使用者自行取得原文"

while ($true) {
    Show-Menu
    $mode = Read-Host "請選擇模式 (1 / 2 / 3 / 4A / 4B / 5 / 0)"
    $mode = $mode.Trim().ToUpper()

    if ($mode -eq "0") { exit }

    # ── [1] 輸入研究主題 ────────────────────────────────────────────────────
    if ($mode -eq "1") {
        Write-Host ""
        $topic = Read-Host "請輸入研究主題（例如：科技接受度模型、消費者購買意願）"
        if ([string]::IsNullOrWhiteSpace($topic)) { continue }

        $prompt = "我目前正在進行文獻探討，研究主題為：$topic。`n`n" +
            "請針對上傳的文獻，基於這個研究主題，主動幫我提出 3 到 5 個深入的學術研究問題（包含但不限於：核心變數定義、研究架構與假設、研究方法、實證結果、文獻間的交叉比較與研究缺口）。`n`n" +
            "接著，請根據你提出的問題，對文獻進行深度彙整，撰寫成一篇邏輯連貫的學術文獻回顧。" +
            $citationRule + $verifyBlock

    # ── [2] 直接輸入問題 ────────────────────────────────────────────────────
    } elseif ($mode -eq "2") {
        Write-Host ""
        Write-Host "請直接輸入你要查詢的具體問題，例如：" -ForegroundColor DarkGray
        Write-Host "  自我一致性對品牌依附的影響" -ForegroundColor DarkGray
        Write-Host "  中介變數 C 在 A 與 B 之間的角色為何？" -ForegroundColor DarkGray
        Write-Host ""
        $question = Read-Host "請輸入你的問題"
        if ([string]::IsNullOrWhiteSpace($question)) { continue }

        $prompt = "我目前正在進行學術研究，我的初步問題是：$question`n`n" +
            "[第一步：問題深化]`n" +
            "請先將這個問題學術化並展開，提出 3 到 5 個更具體、更嚴謹的學術子問題。子問題應涵蓋以下一個或多個面向：概念的操作型定義、變數之間的因果或中介關係、相關理論框架的適用性、實證研究的方法論設計、以及現有文獻的研究缺口。`n`n" +
            "[第二步：文獻整合回答]`n" +
            "請針對上傳的文獻，逐一回答你剛才提出的學術子問題，整合相關文獻中的論述與實證結果，撰寫成一段邏輯連貫的學術說明。" +
            $citationRule + $verifyBlock

    # ── [3] 貼入論文草稿 ────────────────────────────────────────────────────
    } elseif ($mode -eq "3") {
        Write-Host ""
        Write-Host "請先「複製 (Ctrl+C)」你要檢查的半完成論文段落草稿。" -ForegroundColor DarkGray
        Write-Host ""
        Read-Host "複製完成後，請按 Enter 鍵繼續，程式會自動讀取..."
        $draft = Get-Clipboard -Raw
        if ([string]::IsNullOrWhiteSpace($draft)) {
            Write-Host "剪貼簿是空的，請重新操作。" -ForegroundColor Red
            Start-Sleep -Seconds 2
            continue
        }

        $prompt = "以下是我目前尚未完成的論文段落草稿：`n`n---`n$draft`n---`n`n" +
            "請依照以下三個步驟處理這份草稿：`n`n" +
            "[第一步：引用核實]`n" +
            "請逐一核對草稿中的每一個引用，確認以下三點並按格式輸出：`n" +
            "第一，該引用的論點是否確實出現在對應文獻中。`n" +
            "第二，該論點是否被正確歸因於該作者，而非二手引用。`n" +
            "第三，原文的實際論述與草稿中的呈現方式是否存在誤差或過度推論。`n`n" +
            "驗證格式：`n" +
            "[引用來源]作者（年份）`n[草稿中的主張]`n[文獻中的實際論述]`n[驗證結果]正確／部分正確／錯誤／無法確認`n[說明]差異說明`n`n" +
            "[第二步：問題診斷]`n" +
            "請指出草稿在以下面向的不足：論點之間的邏輯銜接是否流暢、段落結構是否符合學術論文規範（總分總或問題-文獻-小結）、是否有主張缺乏引用支撐、以及是否有冗餘或模糊的表達。`n`n" +
            "[第三步：改寫輸出]`n" +
            "根據以上核實與診斷結果，將草稿改寫為一段格式嚴謹、引用正確、句子前後邏輯連貫的學術論文段落。改寫時請保留原始論點的核心意涵，修正錯誤引用，補強邏輯銜接，並確保符合第三人稱學術寫作風格。" +
            $citationRule + $verifyBlock

    # ── [4A] 術語查證 ───────────────────────────────────────────────────────
    } elseif ($mode -eq "4A") {
        Write-Host ""
        Write-Host "=== [4A] 術語查證 — 生成查證 Prompt ===" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "步驟 1：請「複製 (Ctrl+C)」你要修改的論文段落原文。" -ForegroundColor DarkGray
        Write-Host "       （這段文字會保存在程式中，供 4B 改寫時使用）" -ForegroundColor DarkGray
        Write-Host ""
        Read-Host "複製完成後按 Enter..."
        $script:savedDraft = Get-Clipboard -Raw
        if ([string]::IsNullOrWhiteSpace($script:savedDraft)) {
            Write-Host "剪貼簿是空的，請重新操作。" -ForegroundColor Red
            Start-Sleep -Seconds 2
            continue
        }

        Write-Host ""
        Write-Host "步驟 2：請「複製 (Ctrl+C)」你想查證的中文學術術語清單。" -ForegroundColor DarkGray
        Write-Host "       （格式不限，可逐行或逗號分隔，例如：品牌依附、自我一致性）" -ForegroundColor DarkGray
        Write-Host ""
        Read-Host "複製完成後按 Enter..."
        $terms = Get-Clipboard -Raw
        if ([string]::IsNullOrWhiteSpace($terms)) {
            Write-Host "剪貼簿是空的，請重新操作。" -ForegroundColor Red
            Start-Sleep -Seconds 2
            continue
        }

        $prompt = "以下是我的中文論文段落原文：`n`n---`n$($script:savedDraft)`n---`n`n" +
            "以下是我想查證的學術術語清單：`n`n---`n$terms`n---`n`n" +
            "我擔心其中部分術語是由 AI 自行翻譯或生成，在英文學術文獻上找不到對應的原文或明確來源。`n`n" +
            "[第一步：英文對應詞查證]`n" +
            "針對每個術語，請從已上傳的文獻中找出：`n" +
            "（1）對應的英文術語原文（例如：品牌依附 → Brand Attachment）`n" +
            "（2）在文獻中明確使用或定義該術語的作者與年份`n" +
            "（3）該術語在文獻中的原始英文定義或核心描述（引用原句）`n`n" +
            "[第二步：可信度評估]`n" +
            "針對每個術語，給出以下其中一種判斷：`n" +
            "✅ 有明確文獻來源：可在上傳文獻中找到對應英文術語與定義`n" +
            "⚠️ 有對應概念但命名不同：英文文獻有此概念，但使用的術語與中文翻譯有出入，請說明差異`n" +
            "❌ 查無文獻依據：上傳文獻中找不到此術語或對應概念，可能為 AI 生成或需另行查找來源`n`n" +
            "輸出格式（每個術語一組）：`n" +
            "[中文術語] `n" +
            "[英文對應] `n" +
            "[文獻來源] 作者（年份）`n" +
            "[原文定義或描述] `n" +
            "[可信度評估] ✅ / ⚠️ / ❌`n" +
            "[說明] "

        Set-Clipboard -Value $prompt
        Write-Host ""
        Write-Host "==========================================================" -ForegroundColor Green
        Write-Host "[成功] 查證 Prompt 已複製到剪貼簿！" -ForegroundColor Green
        Write-Host ""
        Write-Host "  下一步：" -ForegroundColor White
        Write-Host "  1. 切換到 NotebookLM，按 Ctrl+V 貼上，等待查證結果" -ForegroundColor White
        Write-Host "  2. 查證結果出來後，全選並複製 NotebookLM 的回覆" -ForegroundColor White
        Write-Host "  3. 回到這個視窗，選擇 [4B] 生成改寫 Prompt" -ForegroundColor White
        Write-Host "==========================================================" -ForegroundColor Green
        Write-Host ""
        Read-Host "按 Enter 返回選單..."
        continue

    # ── [4B] 段落改寫 ───────────────────────────────────────────────────────
    } elseif ($mode -eq "4B") {
        Write-Host ""
        Write-Host "=== [4B] 段落改寫 — 生成改寫 Prompt ===" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "4B 是接在 4A 同一個 NotebookLM 對話裡的後續訊息。" -ForegroundColor DarkGray
        Write-Host "NotebookLM 已有原文與查證結果，不需要重新貼入。" -ForegroundColor DarkGray
        Write-Host ""

        $prompt = "根據你剛才的查證結果，請將我一開始提供的論文段落原文改寫為格式嚴謹的學術論文正文，要求如下：`n`n" +
            "（1）將 ⚠️ 的術語替換為查證結果中建議的正確中文對應詞`n" +
            "（2）將 ❌ 的術語以【待查證：原術語】的方式保留，提示作者需自行補充來源後再定稿`n" +
            "（3）為每個論點補充或修正 APA 第七版行內引用格式，即在論點後方加上（作者姓氏, 年份）`n" +
            "（4）禁止使用作者為主詞的句型（如：某某指出…、某某認為…）；應直接陳述論點，再於句末插入引用標記`n" +
            "（5）保留原文的核心論點與段落結構，不增加原文未有的新論述`n`n" +
            "改寫完成後，請條列說明每處修改的理由：`n" +
            "[改寫說明]（術語更正理由、引用補充、或標示待查證的原因）"

        Set-Clipboard -Value $prompt
        Write-Host "==========================================================" -ForegroundColor Green
        Write-Host "[成功] 改寫 Prompt 已複製到剪貼簿！" -ForegroundColor Green
        Write-Host ""
        Write-Host "  下一步：回到剛才的 NotebookLM 對話，按 Ctrl+V 貼上。" -ForegroundColor White
        Write-Host "  （請在同一個對話視窗，不要開新對話）" -ForegroundColor DarkGray
        Write-Host "==========================================================" -ForegroundColor Green
        Write-Host ""
        Read-Host "按 Enter 返回選單..."
        continue

    # ── [5] 回填 Wiki 卡 ────────────────────────────────────────────────────
    } elseif ($mode -eq "5") {
        Write-Host ""
        Write-Host "=== [5] 回填 Wiki 卡 ===" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "請確認已複製 NotebookLM 的「自我核對」結果到剪貼簿。" -ForegroundColor DarkGray
        Write-Host ""
        Read-Host "複製完成後按 Enter..."
        Write-Host ""
        python "$PSScriptRoot\notebooklm_patch_wiki.py"
        Write-Host ""
        Read-Host "按 Enter 返回選單..."
        continue

    # ── 無效選項 ─────────────────────────────────────────────────────────────
    } else {
        Write-Host ""
        Write-Host "無效選項，請輸入 1、2、3、4A、4B、5 或 0。" -ForegroundColor Red
        Start-Sleep -Seconds 1
        continue
    }

    # ── 共用輸出區（選項 1 / 2 / 3）────────────────────────────────────────
    Set-Clipboard -Value $prompt
    Write-Host ""
    Write-Host "==========================================================" -ForegroundColor Green
    Write-Host "[成功] 指令已複製到剪貼簿！" -ForegroundColor Green
    Write-Host ""
    Write-Host "請切換到瀏覽器，在 NotebookLM 的對話框中按下 Ctrl+V 貼上。"
    Write-Host "==========================================================" -ForegroundColor Green
    Write-Host ""
    $again = Read-Host "按 Enter 返回選單，或輸入 0 退出"
    if ($again -eq "0") { exit }
}
