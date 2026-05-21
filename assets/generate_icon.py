"""生成番茄图标，输出多尺寸 .ico 文件"""
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
img.save(
    'tomato.ico',
    format='ICO',
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (256, 256)]
)
print('tomato.ico 已生成（含 16/32/48/64/256 尺寸）')
