# MCP 工具設定

## Playwright MCP

用途：操作瀏覽器、截圖、處理需互動的頁面

```toml
[mcp_servers.playwright]
command = "npx.cmd"
args = ["-y", "@playwright/mcp"]
```

安裝瀏覽器：
```powershell
npx.cmd -y playwright install chromium
```

## Firecrawl MCP

用途：網頁內容抓取、整理、摘要

```toml
[mcp_servers.firecrawl]
command = "npx.cmd"
args = ["-y", "firecrawl-mcp"]

[mcp_servers.firecrawl.env]
FIRECRAWL_API_KEY = "your-api-key-here"
```

注意：Firecrawl 需要 API Key，請勿公開。
