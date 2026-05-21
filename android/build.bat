@echo off
chcp 65001 >nul
echo ============================
echo   番茄钟 - 安卓版构建
echo ============================
echo.
cd /d "%~dp0"

set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot
set ANDROID_SDK_ROOT=C:\Android\sdk
set ANDROID_HOME=C:\Android\sdk
set PATH=%JAVA_HOME%\bin;%ANDROID_SDK_ROOT%\platform-tools;%PATH%

echo [1/2] 同步 web 资源到 Android 工程...
call npx cap sync
if %errorlevel% neq 0 (
    echo 同步失败！
    pause
    exit /b 1
)
echo.
echo [2/2] 编译 APK...
cd android
call gradlew assembleDebug
if %errorlevel% neq 0 (
    echo 编译失败！
    pause
    exit /b 1
)
cd ..
echo.
echo [3/3] 复制 APK...
copy /Y android\app\build\outputs\apk\debug\app-debug.apk 番茄钟.apk
echo.
echo ============================
echo   构建成功！
echo   产物: android\番茄钟.apk
echo ============================
pause
