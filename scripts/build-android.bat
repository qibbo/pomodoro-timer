@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 启动安卓版构建...
call ..\android\build.bat
