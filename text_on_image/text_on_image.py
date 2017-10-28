from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def main():
    img_height = 800
    img_width = 600
    bg_color = (255, 255, 255)
    font_color = (0, 0, 0)
    txt_height = 30
    txt_pos = (0, 0)
    txt = 'This is a sample'

    img = Image.new('RGB', (img_width, img_height), bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Amble-Bold.ttf", txt_height)
    draw.text(txt_pos, txt, font_color, font=font)
    img.save('sample.png')


if __name__ == '__main__':
    main()
