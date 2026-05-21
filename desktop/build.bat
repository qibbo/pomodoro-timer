@echo off
chcp 65001 >nul
echo ============================
echo   番茄钟 - 桌面版构建
echo ============================
echo.
cd /d "%~dp0"
echo [1/2] 打包为 exe...
..\venv\Scripts\pyinstaller.exe 番茄钟.spec --noconfirm --distpath .\dist --workpath .\build
if %errorlevel% neq 0 (
    echo 构建失败！
    pause
    exit /b 1
)
echo.
echo [2/2] 复制图标...
echo.
echo ============================
echo   构建成功！
echo   产物: desktop\dist\番茄钟.exe
echo ============================
pause
