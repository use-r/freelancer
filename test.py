from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img_height = 800
img_width = 600
txt_height = 40
txt = 'Sample Text'

img = Image.new('RGB', (img_width, img_height))
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("Amble-Bold.ttf", txt_height)
# draw.text((x, y),"your text",(r,g,b))
draw.text((0, 0),txt,(255,255,255),font=font)
img.save('sample-out.jpg')
