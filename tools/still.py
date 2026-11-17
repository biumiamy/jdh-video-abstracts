"""Save still frames of an animated page.  Usage: python tools/still.py videos/<name>/video.html 3.5 10 22"""
import sys, os
from playwright.sync_api import sync_playwright
html = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://' + os.path.abspath(html)); pg.wait_for_timeout(1000)
    for t in sys.argv[2:]:
        pg.evaluate(f'seek({t})'); out = os.path.join(os.path.dirname(html), f'still_{t}s.png'); pg.screenshot(path=out); print(out)
    b.close()
