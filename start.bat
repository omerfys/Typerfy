@echo off
title Typerfy — Generative Botanical Typography
cd /d "%~dp0"

echo ===================================================
echo              Typerfy Baslatiliyor...
echo ===================================================
echo.

where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [UYARI] Node.js bulunamadi. index.html dogrudan tarayicida aciliyor...
    start "" "%~dp0index.html"
    exit /b
)

echo [*] Tarayici aciliyor: http://localhost:3001/
start "" http://localhost:3001/
echo [*] Sunucu calisiyor. Kapatmak icin bu pencereyi kapatabilir veya Ctrl+C yapabilirsiniz.
echo.
node server.js
