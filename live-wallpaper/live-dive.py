from PIL import Image, ImageDraw, ImageFont
import datetime
import subprocess

base = Image.open('coool2.png').convert('RGBA')
wheel = Image.open('coool.png').convert('RGBA')

txt = Image.new('RGBA', base.size, (255,255,255,0))
#fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 18)
fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 14)
d = ImageDraw.Draw(txt)

d.text((60,60), subprocess.run('grep -v "danspena" /home/alex/irclogs/Skynet/#twitter.log | tail | cut -d " " -f2-', stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8'), font=fnt, fill=(255,255,255,255))
d.text((60,300), subprocess.run('tail /home/alex/irclogs/Skynet/#twitter2.log | cut -d " " -f2-', stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8'), font=fnt, fill=(255,255,255,255))
d.text((10,1016), subprocess.run('date', stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8'), font=fnt, fill=(255,255,255,90))

now = datetime.datetime.now()
preout = Image.alpha_composite(base, wheel.rotate( -(now.minute/0.1666) ))
out = Image.alpha_composite(preout, txt)

out.save("/home/alex/out.png")
