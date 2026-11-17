"""Convert a JDH article fingerprint SVG (from the journal site) into fpdata.json for the end-card animation.
Usage: py tools/fp2json.py fingerprint.svg out.json"""
import sys, re, json
s = open(sys.argv[1], encoding='utf8').read()
def st(tag, key):
    m = re.search(r'style="[^"]*?(?:^|;|")' + key + r':([^;"]+)', tag) or re.search(key + r':([^;"]+)', tag)
    return m.group(1).strip() if m else None
def a(tag, k):
    m = re.search(r'\s' + k + r'="([^"]+)"', tag); return m.group(1) if m else None
out = []
for g in re.findall(r'<g class="([^"]*)"[^>]*>(.*?)</g>', s, re.S):
    cls, body = g
    ln = re.search(r'<line[^>]*/>', body)
    if not ln: continue
    L = ln.group(0)
    item = {'c': cls, 'l': [round(float(a(L, k)), 2) for k in ('x1', 'y1', 'x2', 'y2')] + [st(L, 'stroke'), float(a(L, 'stroke-width') or 1)], 'o': []}
    for C in re.findall(r'<circle[^>]*/>', body):
        fill = st(C.replace('style="fill', 'style=";fill'), 'fill'); stroke = re.findall(r';stroke:([^;"]+)', C)
        item['o'].append([round(float(a(C, 'cx')), 2), round(float(a(C, 'cy')), 2), float(a(C, 'r')), fill, stroke[0].strip() if stroke else None, a(C, 'class') or ''])
    out.append(item)
json.dump(out, open(sys.argv[2], 'w')); print(len(out), 'cells')
