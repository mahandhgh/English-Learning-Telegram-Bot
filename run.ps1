$ErrorActionPreference = 'Stop'
$botPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $botPython)) {
    throw 'Python environment is missing. Follow README.md first.'
}
$botSecret = Read-Host 'Paste your BotFather token (input is hidden)' -AsSecureString
try {
    $env:TELEGRAM_BOT_TOKEN = [System.Net.NetworkCredential]::new('', $botSecret).Password
    $env:TELEGRAM_BOT_TOKEN = $env:TELEGRAM_BOT_TOKEN.Trim()
    if ($env:TELEGRAM_BOT_TOKEN -cnotmatch '\A[0-9]+:[A-Za-z0-9_-]+\z') {
        throw 'Invalid token format. Copy only the token from BotFather. Try right-click paste or type it manually instead of Ctrl+V.'
    }
    & $botPython (Join-Path $PSScriptRoot 'bot.py')
} finally {
    Remove-Item Env:\TELEGRAM_BOT_TOKEN -ErrorAction SilentlyContinue
    $botSecret.Dispose()
}
