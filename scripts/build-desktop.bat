@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 启动桌面版构建...
call ..\desktop\build.bat
