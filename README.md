# 番茄钟

一个跨平台番茄钟（Pomodoro Timer），支持桌面（Windows exe）和安卓（apk）。

## 功能

- 专注 / 短休 / 长休三种模式，计时结束自动切换
- **自定义时长**：可通过 +/- 按钮或直接输入数字调节各模式时长（1-120 分钟）
- **深色/浅色主题**：一键切换，自动保存主题偏好
- 计时结束浏览器通知 + 声音提示
- 键盘快捷键：`Space` 开始/暂停，`R` 重置，`1-3` 切换模式
- 重置按钮恢复默认时长（专注 25min / 短休 5min / 长休 15min）

## 项目结构

```
├── core/              ← 唯一核心界面（HTML/CSS/JS），所有平台共享
├── desktop/           ← 桌面版（pywebview + PyInstaller 打包）
├── android/           ← 安卓版（Capacitor + Gradle 打包）
├── assets/            ← 共用资源（图标等）
├── scripts/           ← 顶层构建脚本
└── venv/              ← Python 虚拟环境
```

## 修改界面

只需编辑 `core/index.html`，两个平台同时生效。

## 构建

- 桌面版：运行 `scripts/build-desktop.bat` 或 `desktop/build.bat`
- 安卓版：运行 `scripts/build-android.bat` 或 `android/build.bat`

## 构建产物

- 桌面版：`desktop/dist/番茄钟.exe`
- 安卓版：`android/番茄钟.apk`
