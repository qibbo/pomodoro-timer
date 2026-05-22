"""生成番茄图标，输出多尺寸 .ico 文件"""
import os
from PIL import Image, ImageDraw

SIZE = 256

def draw_tomato(size):
    """绘制番茄图标，返回 RGBA Image"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    margin = max(2, size * 0.06)
    cx, cy = size / 2, size / 2

    # 番茄主体（红色椭圆）
    body_top = margin + size * 0.10
    body_bottom = size - margin
    d.ellipse(
        [margin, body_top, size - margin, body_bottom],
        fill=(220, 50, 50),
        outline=(180, 30, 30),
        width=max(2, size // 64)
    )

    # 高光
    hl_r = size * 0.12
    hl_x = cx - size * 0.15
    hl_y = cy - size * 0.15
    d.ellipse(
        [hl_x - hl_r, hl_y - hl_r, hl_x + hl_r, hl_y + hl_r],
        fill=(255, 150, 140, 160)
    )

    # 茎
    stem_w = max(3, size * 0.08)
    stem_h = size * 0.16
    stem_cx = cx
    d.rectangle(
        [stem_cx - stem_w / 2, margin,
         stem_cx + stem_w / 2, body_top + size * 0.05],
        fill=(50, 170, 60)
    )

    # 叶子
    leaf_w = size * 0.13
    leaf_h = size * 0.10
    d.ellipse(
        [stem_cx + stem_w * 0.2, margin + stem_h * 0.15,
         stem_cx + stem_w * 0.2 + leaf_w, margin + stem_h * 0.15 + leaf_h],
        fill=(50, 170, 60)
    )

    return img


img = draw_tomato(SIZE)
# 将生成的番茄图像保存为 .ico 文件，包含多种常用尺寸以适配不同平台需求
# 这样在 Windows 桌面快捷方式、应用图标等场景下能清晰显示
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tomato.ico')
img.save(
    output_path,                  # 始终保存到脚本所在的 assets/ 目录
    format='ICO',                 # 保存为 ICO 格式（Windows 图标）
    sizes=[                       # 包含多种常用图标尺寸
        (16, 16),                 # 小尺寸：用于任务栏或列表
        (32, 32),                 # 常见中图标
        (48, 48),                 # 兼容老式系统
        (64, 64),                 # 高清/缩放支持
        (256, 256)                # 大图标，现代 Windows 支持
    ]
)
print(f'tomato.ico 已生成 → {output_path}')
