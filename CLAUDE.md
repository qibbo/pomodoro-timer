# CLAUDE.md

本文件为 Claude Code（claude.ai/code）在此仓库中工作时提供指导。

## 构建命令

- 桌面版：`desktop/build.bat`（先确保 `venv/` 已就绪，见下方"环境初始化"）
- 安卓版：`android/build.bat`（先确保已安装 `npx cap` 和 Android SDK，**中国大陆用户需配置 Gradle 代理或镜像**）

## 环境初始化

```bash
python -m venv venv
venv/Scripts/pip install -r requirements.txt
```

## 项目架构

### 核心理念：单一界面源

`core/index.html` 是唯一的界面文件（HTML + CSS + JS），桌面版和安卓版都直接使用它。修改界面只需改这一个文件，两个平台同步生效。

### 桌面版（desktop/）

- `launcher.py` — 入口脚本，用 pywebview 创建原生窗口加载 `core/index.html`
- `番茄钟.spec` — PyInstaller 打包配置，将 launcher.py + index.html + 图标打包为单个 exe
- 窗口固定 480×700，不可调整大小，无窗口装饰下的关闭确认

### 安卓版（android/）

- 使用 Capacitor 将 `core/index.html` 包装为 WebView 应用
- `capacitor.config.json` 中 `webDir` 指向 `../core`
- `android/build.bat` 先执行 `npx cap sync` 复制 web 资源，再通过 Gradle 编译 debug APK
- 构建环境变量：`JAVA_HOME`、`ANDROID_SDK_ROOT` 在 build.bat 内硬编码，换机器需修改

### 资源（assets/）

- `generate_icon.py` — 用 Pillow 绘制番茄图标，输出多尺寸 `.ico` 文件
- `tomato.ico` — 已生成的图标文件，桌面版打包时使用

## 项目特点

- 无外部运行时依赖：桌面版打包为单个 exe，安卓版打包为单个 apk
- 所有数据（主题偏好、自定义时长）存储在浏览器 localStorage 中，无需后端
- 计时结束通知使用 Web Audio API 合成提示音，无需外部音频文件
- 三种模式（专注/短休/长休），每 4 个专注周期自动进入长休
- 桌面版入口文件名含中文（`番茄钟.spec`），PyInstaller 打包产物也含中文（`番茄钟.exe`）

## 项目约定

- **每次大的修改后必须更新 README.md**，保持功能描述与代码同步
