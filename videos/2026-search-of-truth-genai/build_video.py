"""Build video.html from video.src.html (injects the fingerprint data, copies the logo strip).
Run from this folder:  py build_video.py"""
import shutil, os
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
src = open('video.src.html', encoding='utf8').read()
fp = open('fpdata.json', encoding='utf8').read()
open('video.html', 'w', encoding='utf8').write(src.replace('/*FPDATA*/', fp))
shutil.copy('../../shared/logos/logos-uni-c2dh-degruyter.png', 'logos.png')
shutil.copy('../../shared/logos/jdh-logo-text.svg', 'jdh-logo.svg')
print('ok')
# make the logo strip's light background transparent (keeps dark logo pixels)
from PIL import Image
im = Image.open('logos.png').convert('RGB'); bg = im.getpixel((2, 2)); px = im.load()
out = Image.new('RGBA', im.size)
for y in range(im.size[1]):
    for x in range(im.size[0]):
        r, g, b = px[x, y]; d = max(0, sum(bg) / 3 - (r + g + b) / 3) / (sum(bg) / 3)
        out.putpixel((x, y), (int(r * 0), int(g * 0), int(b * 0), 0) if d < .02 else (max(0, int((r - bg[0] * (1 - d)) / d)) if d > 0 else 0, max(0, int((g - bg[1] * (1 - d)) / d)), max(0, int((b - bg[2] * (1 - d)) / d)), int(255 * d)))
out.save('logos.png'); print('logos transparent, bg was', bg)
