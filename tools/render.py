"""Render an animated HTML page (with a global seek(t) function) to MP4, then add music.

Usage:  python tools/render.py videos/<name>/video.html <seconds> [out.mp4] [music.mp3] [fade_seconds]
        Music defaults to music/Birds - Corbyn Kites.mp3, output to video.mp4 next to the HTML.
Needs:  pip install playwright && playwright install chromium ; ffmpeg on PATH (or: pip install imageio-ffmpeg)
"""
import sys, os, subprocess, tempfile, shutil
from playwright.sync_api import sync_playwright
html, dur = sys.argv[1], float(sys.argv[2])
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(html)), 'video.mp4')
music = sys.argv[4] if len(sys.argv) > 4 else os.path.join(root, 'music', 'Birds - Corbyn Kites.mp3')
fade = float(sys.argv[5]) if len(sys.argv) > 5 else 3.5
assert os.path.exists(music), f'music file not found: {music}'
# ffmpeg: use the one on PATH, else the bundled one from `pip install imageio-ffmpeg`
FF = shutil.which('ffmpeg')
if not FF:
    import imageio_ffmpeg; FF = imageio_ffmpeg.get_ffmpeg_exe()
fps = 30; n = round(dur * fps)
tmp = tempfile.mkdtemp(); silent = os.path.join(tmp, 'silent.mp4')
ff = subprocess.Popen([FF,'-y','-loglevel','error','-f','image2pipe','-framerate',str(fps),'-c:v','mjpeg','-i','-',
                       '-c:v','libx264','-crf','18','-preset','veryfast','-vf','scale=in_range=pc:out_range=tv,format=yuv420p','-color_range','tv','-r',str(fps),silent], stdin=subprocess.PIPE)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1920,'height':1080})
    from pathlib import Path; pg.goto(Path(html).resolve().as_uri()); pg.wait_for_timeout(1200)
    for i in range(n):
        pg.evaluate(f'seek({i/fps})'); ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
        if i % 300 == 0: print(f'{i/fps:.0f}s / {dur:.0f}s', flush=True)
    b.close()
ff.stdin.close(); assert ff.wait() == 0
subprocess.run([FF,'-y','-loglevel','error','-i',silent,'-i',music,'-map','0:v','-map','1:a','-c:v','copy',
                '-af',f'atrim=0:{dur},afade=t=out:st={max(0,dur-fade)}:d={fade}','-c:a','aac','-b:a','192k','-shortest',
                '-movflags','+faststart',out], check=True)
print('done:', out)
