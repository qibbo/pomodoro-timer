import os
import sys
import webview


def get_html_path():
    """获取核心 HTML 文件的路径，兼容开发模式和 PyInstaller 打包模式"""
    if getattr(sys, 'frozen', False):
        # PyInstaller 打包后，资源在临时目录
        return os.path.join(sys._MEIPASS, 'index.html')
    else:
        # 开发模式：读取 core/index.html
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'core', 'index.html')


def main():
    html_path = get_html_path()
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    window = webview.create_window(
        title='番茄钟',
        html=html_content,
        width=720,
        height=420,
        resizable=False,
        confirm_close=False
    )
    webview.start()


if __name__ == '__main__':
    main()
