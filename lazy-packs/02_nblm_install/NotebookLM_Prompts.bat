@echo off
chcp 65001 >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0NotebookLM_Prompts.ps1"
if %errorlevel% neq 0 (
    echo.
    echo [錯誤] PowerShell 執行失敗，錯誤碼：%errorlevel%
    pause
)
