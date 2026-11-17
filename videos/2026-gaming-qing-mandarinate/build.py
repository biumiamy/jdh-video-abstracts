import math
fp=open('fp.svg').read()
BG='#F3F1F7';INK='#1F2021';G1='#ADB5BD';G2='#495057';VIO='#5E2BFF';TEAL='#51F6E0';RED='#C23B3B'
css=f"""
@font-face{{font-family:Fira;src:url(fira-sans-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:Fira;src:url(fira-sans-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:Fira;src:url(fira-sans-latin-600-normal.woff2);font-weight:600}}
@font-face{{font-family:Fira;src:url(fira-sans-latin-700-normal.woff2);font-weight:700}}
*{{margin:0;box-sizing:border-box}}
body{{width:1920px;height:1080px;overflow:hidden;background:{BG};color:{INK};font-family:Fira,sans-serif;position:relative;
background-image:radial-gradient(circle,rgba(31,32,33,.07) 1.1px,transparent 1.3px);background-size:28px 28px}}
.han{{font-family:'Noto Serif CJK TC',serif}}
.kicker{{font-size:22px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:{G2}}}
.brand{{position:absolute;left:96px;top:72px;font-size:22px;font-weight:500;letter-spacing:.04em;color:{G2}}}
.brand b{{color:{INK};font-weight:600}}
"""
def page(body): return f"<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>{body}</body></html>"
brand=f'<div class="brand"><b>Journal of Digital History</b> &nbsp;·&nbsp; video abstract</div>'

# Frame 1
legend=f"""
<div style="position:absolute;left:0;right:0;bottom:88px;display:flex;justify-content:center;gap:56px;font-size:26px;color:{G2};align-items:center">
 <span style="display:flex;align-items:center;gap:14px"><i style="width:40px;height:3px;background:{G1};display:inline-block"></i>narrative</span>
 <span style="display:flex;align-items:center;gap:14px"><i style="width:40px;height:3px;background:{TEAL};display:inline-block"></i>hermeneutics</span>
 <span style="display:flex;align-items:center;gap:14px"><i style="width:40px;height:3px;background:{VIO};display:inline-block"></i>code</span>
</div>"""
f1=brand+f"""
<div style="position:absolute;left:50%;top:70px;transform:translateX(-50%);width:800px;height:800px">{fp}</div>
<div style="position:absolute;left:0;right:0;top:446px;text-align:center">
  <div style="font-size:30px;font-weight:600">182 cells.</div>
  <div style="font-size:30px;font-weight:400;color:{G2}">One article.</div>
</div>"""+legend
open('f1.html','w').write(page(f1))

# Frame 2: schematic board
cx,cy=600,560
parts=[]
rings=[(410,330,34,'Realm · entry, examinations, provinces'),(318,240,20,'Capital · the six ministries'),(228,150,12,'Court · titles and honours')]
for ro,ri,n,label in rings:
    gap=1.6
    for k in range(n):
        a0=math.radians(k*360/n+gap/2-90); a1=math.radians((k+1)*360/n-gap/2-90)
        def p(r,a): return f"{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}"
        d=f"M{p(ro,a0)} A{ro},{ro} 0 0 1 {p(ro,a1)} L{p(ri,a1)} A{ri},{ri} 0 0 0 {p(ri,a0)} Z"
        parts.append(f'<path d="{d}" fill="{BG}" stroke="{G1}" stroke-width="1.2"/>')
        # tiny position ticks
        for j in range(3):
            aa=a0+(a1-a0)*(j+1)/4; rr=(ro+ri)/2
            parts.append(f'<circle cx="{cx+rr*math.cos(aa):.1f}" cy="{cy+rr*math.sin(aa):.1f}" r="2" fill="{G2}"/>')
# goal C66 highlight on inner ring segment
a=math.radians(-90+360/12*0.5); rr=189
parts.append(f'<circle cx="{cx+rr*math.cos(a):.1f}" cy="{cy+rr*math.sin(a):.1f}" r="9" fill="{VIO}"/>')
# center square: dice bowl
parts.append(f'<rect x="{cx-110}" y="{cy-110}" width="220" height="220" fill="none" stroke="{G1}" stroke-width="1.2" stroke-dasharray="4 6"/>')
def die(x,y,n,s=64):
    pip={1:[(0,0)],2:[(-1,-1),(1,1)],3:[(-1,-1),(0,0),(1,1)],4:[(-1,-1),(1,-1),(-1,1),(1,1)],5:[(-1,-1),(1,-1),(0,0),(-1,1),(1,1)],6:[(-1,-1),(1,-1),(-1,0),(1,0),(-1,1),(1,1)]}[n]
    col=RED if n in (1,4) else INK
    out=[f'<rect x="{x-s/2}" y="{y-s/2}" width="{s}" height="{s}" rx="11" fill="#FFFFFF" stroke="{INK}" stroke-width="1.5"/>']
    for px,py in pip:
        r=s*0.13 if n==1 else s*0.085
        out.append(f'<circle cx="{x+px*s*0.25}" cy="{y+py*s*0.25}" r="{r}" fill="{col}"/>')
    return ''.join(out)
for (dx,dy),n in zip([(-40,-40),(40,-40),(-40,40),(40,40)],[4,4,6,2]):
    parts.append(die(cx+dx,cy+dy,n))
svg=f'<svg width="1920" height="1080" style="position:absolute;left:0;top:0">{"".join(parts)}</svg>'
labels=f"""
<div style="position:absolute;left:{cx}px;top:{cy-410-44}px;transform:translateX(-50%);font-size:20px;color:{G2};white-space:nowrap">Realm · entry, examinations, provinces</div>
<div style="position:absolute;left:{cx}px;top:{cy-318+22}px;transform:translateX(-50%);font-size:20px;color:{G2};white-space:nowrap;display:none"></div>
<div style="position:absolute;left:{cx+300}px;top:{cy+300}px;font-size:20px;color:{G2};white-space:nowrap"></div>
"""
right=f"""
<div style="position:absolute;left:1120px;top:250px;width:720px">
 <div class="kicker">Mandarin Promotions · c. 1840</div>
 <div class="han" style="font-size:150px;font-weight:700;line-height:1.1;margin-top:22px;letter-spacing:.06em">陞官圖</div>
 <div style="font-size:30px;color:{G2};margin-top:6px"><i>Shēngguāntú</i> — a dice game of official careers</div>
 <div style="display:grid;grid-template-columns:repeat(4,auto);gap:8px 44px;margin-top:64px;justify-content:start">
  {''.join(f'<div><div style="font-size:64px;font-weight:600;color:{VIO};line-height:1">{n}</div><div style="font-size:22px;color:{G2};margin-top:8px">{t}</div></div>' for n,t in [('434','positions'),('66','departments'),('22','starting points'),('18','final ranks')])}
 </div>
 <div style="display:flex;flex-direction:column;gap:10px;margin-top:64px;font-size:21px;color:{G2}">
  <span>outer ring · realm: entry, examinations, provinces</span>
  <span>middle ring · capital: the six ministries</span>
  <span>inner ring · court: titles and honours &nbsp;<b style="color:{VIO}">●</b> goal</span>
 </div>
</div>
<div style="position:absolute;left:96px;bottom:48px;font-size:17px;color:{G1}">Schematic after the game chart reproduced by Puk Wing Kin (2011)</div>"""
open('f2.html','w').write(page(brand+svg+right))

# Frame 3: end card
f3=f"""
<div style="position:absolute;left:110px;top:150px;width:780px;height:780px">{fp}</div>
<div style="position:absolute;left:1000px;top:250px;width:820px">
 <div class="kicker" style="color:{VIO}">Read the article</div>
 <div style="font-size:54px;font-weight:600;line-height:1.18;margin-top:24px">Gaming the Qing Mandarinate: Digital Approaches to a Nineteenth-Century Chinese Board Game</div>
 <div style="font-size:36px;font-weight:700;margin-top:56px;line-height:1.45">Elisabeth Kaske<br>Florian Keßler</div>
 <div style="font-size:24px;color:{G2};margin-top:20px">Journal of Digital History</div>
</div>
<img src="logos.png" style="position:absolute;left:1000px;bottom:110px;height:110px">
"""
open('f3.html','w').write(page(f3))
