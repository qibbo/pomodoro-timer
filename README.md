# 番茄钟

一个跨平台番茄钟（Pomodoro Timer），支持桌面（Windows exe）和安卓（apk）。

## 设计

陶艺工坊风格 — 温暖的赤陶色调、SVG 噪点纹理、圆润的 Nunito 字体、计时中圆环呼吸光晕动画。以计时器为视觉核心的纵向居中布局，营造专注冥想的氛围。

## 功能

- 专注 / 短休 / 长休三种模式，计时结束自动切换（每 4 个专注周期自动进入长休）
- **自定义时长**：可通过 +/- 按钮或直接输入数字调节各模式时长（1-120 分钟），偏好自动保存
- **深色/浅色主题**：一键切换，自动保存主题偏好
- 计时结束浏览器通知 + Web Audio API 提示音
- 键盘快捷键：`Space` 开始/暂停，`R` 重置，`1-3` 切换模式
- 番茄计数指示灯（4 个圆点，每完成一个专注周期亮起一个）
- 重置按钮恢复默认时长（专注 25min / 短休 5min / 长休 15min）

## 项目结构

```
├── core/              ← 唯一核心界面（HTML/CSS/JS），所有平台共享
├── desktop/           ← 桌面版（pywebview + PyInstaller 打包，窗口 480×700）
├── android/           ← 安卓版（Capacitor + Gradle 打包）
├── assets/            ← 共用资源（图标等）
├── scripts/           ← 顶层构建脚本
└── venv/              ← Python 虚拟环境
```

## 修改界面

只需编辑 `core/index.html`，两个平台同时生效。

## 构建

- 桌面版：`scripts/build-desktop.bat` 或 `desktop/build.bat`
- 安卓版：`scripts/build-android.bat` 或 `android/build.bat`

## 构建产物

- 桌面版：`desktop/dist/番茄钟.exe`（约 13 MB）
- 安卓版：`android/番茄钟.apk`（约 4 MB）

## 版本

**v1.1.0** — UI 重设计（陶艺工坊主题）
