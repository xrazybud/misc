from PIL import Image, ImageDraw, ImageFont
import datetime
import subprocess

base = Image.open('coool2.png').convert('RGBA')
wheel = Image.open('coool.png').convert('RGBA')

txt = Image.new('RGBA', base.size, (255,255,255,0))
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 18)
d = ImageDraw.Draw(txt)

d.text((10,60), subprocess.run(['tail', '/home/alex/irclogs/Skynet/#twitter.log'], stdout=subprocess.PIPE).stdout.decode('utf-8'), font=fnt, fill=(255,255,255,255))
d.text((10,300), subprocess.run(['tail', '/home/alex/irclogs/Skynet/#twitter2.log'], stdout=subprocess.PIPE).stdout.decode('utf-8'), font=fnt, fill=(255,255,255,255))

now = datetime.datetime.now()
preout = Image.alpha_composite(base, wheel.rotate( (now.minute/66)*100) )
out = Image.alpha_composite(preout, txt)

out.save("/home/alex/out.png")