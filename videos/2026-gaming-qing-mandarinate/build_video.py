import json,math
exec(open('build.py',encoding='utf8').read().split('# Frame 1')[0])
fpdata=open('fpdata.json',encoding='utf8').read(); beats=open('beats.json',encoding='utf8').read()
CW=820; X0,Y0=150,150; CH=CW*2128/2110
def at(fx,fy): return X0+fx*CW, Y0+fy*CH
c1=at(0.857,0.986); c66=at(0.629,0.661); rx0,ry0=at(0.344,0.436); rx1,ry1=at(0.643,0.651)
P0=(c1[0]-30,c1[1]-40);P1=(c1[0]-160,c1[1]-260);P2=(c66[0]+200,c66[1]+260);P3=(c66[0]+30,c66[1]+36)
bz=lambda i:(P0[i]+3*P1[i]+3*P2[i]+P3[i])/8
def badge(x,y,n,r=20): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{VIO}"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Fira" font-weight="700" font-size="22" fill="#fff">{n}</text>'
def hbadge(n): return f'<span style="display:inline-flex;width:40px;height:40px;border-radius:50%;background:{VIO};color:#fff;font-weight:700;font-size:22px;align-items:center;justify-content:center;flex:none">{n}</span>'
kick=lambda t,c=None: f'<div class="kicker" style="color:{c or G2}">{t}</div>'
src=lambda t,i: f'<div class="src" id="{i}">{t}</div>'
rules=[('Start','Your first throw decides your background,<br>from official’s son to medicine student.'),('Move','Each throw moves you from office to office,<br>up or down the ranks.'),('Goal','Retire at the highest rank you can reach,<br>and collect the most chips.'),('Shortcuts','Lucky throws let you jump ahead,<br>or you pay to buy an office.')]
rl=''.join(f'<div id="r{i}" style="display:flex;gap:20px;align-items:flex-start;margin-top:{0 if i==0 else 28}px">{hbadge(i+1)}<div style="font-size:25px;line-height:1.4"><b>{t}</b> <span style="color:{G2}">· {x}</span></div></div>' for i,(t,x) in enumerate(rules))
# S3 left
groups=[('Level up','▲',[(4,'德','Virtue'),(6,'才','Talent'),(5,'功','Effort')]),('Stay on probation','●',[(3,'良','Mediocre'),(2,'柔','Weak')]),('Penalty','▼',[(1,'賍','Corrupt')])]
y=250; s3l=''; d3=[]
for gi,(gname,ic,items) in enumerate(groups):
    s3l+=f'<div class="abs" id="ag{gi}" style="left:96px;top:{y}px;width:860px;height:220px"><div style="font-size:20px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:{G2}">{ic}&nbsp; {gname}</div>'
    for j,(n,h,e) in enumerate(items):
        s3l+=f'<div class="abs" style="left:{j*270}px;top:40px;display:flex;align-items:center;gap:16px"><span class="han" style="font-size:72px;font-weight:700;line-height:1">{h}</span><span style="font-size:24px">{e}</span></div>'
        x=96+j*270; d3+= [[x+22,y+150,n,40],[x+70,y+150,n,40]]
    s3l+='</div>'; y+=235
PX,PY,PW=1010,250,814; ps=PW/1019; hx0,hx1=505*ps+PX,612*ps+PX
# S5 bars
G=[('Hereditary privilege',[19.6,40.5,36.9],True),('Imperial grace',[22.6,31.2],False),('Examinations',[7.5,10.5,3.4,-11],False),('Patronage',[-11.1,-8.2],False),('Clerks & specialists',[-22.2,-18.2,-27.2,-31.8],False)]
ICONS={'rank':'<path d="M14 30 L24 20 L34 30 M14 38 L24 28 L34 38" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>',
'money':f'<circle cx="20" cy="27" r="8.5" fill="none" stroke="#fff" stroke-width="3"/><circle cx="29" cy="21" r="8.5" fill="{G2}" stroke="#fff" stroke-width="3"/>',
'ladder':'<path d="M18 12 L18 36 M30 12 L30 36 M18 18 L30 18 M18 24 L30 24 M18 30 L30 30" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'}
icon=lambda s: f'<span style="flex:none;font-size:30px;line-height:1.25;font-weight:600;color:{VIO}">→</span>'
res=[('rank','Rank','Everyone eventually ends up near the top.'),('money','Money','Your background decides: the more privileged, the more chips you win.'),('ladder','Buying office','Almost everyone buys, early. Careers get faster, but the privileged stay ahead.')]
rr=''.join(f'<div id="e{i}" style="display:flex;gap:18px;margin-bottom:40px">{icon(s)}<div style="font-size:27px;line-height:1.4"><b>{t}</b><br><span style="color:{G2}">{x}</span></div></div>' for i,(s,t,x) in enumerate(res))
check=f'<svg width="64" height="64" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{VIO}"/><path id="ckp" d="M18 33 L28 43 L47 22" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="45" stroke-dashoffset="45"/></svg>'

html=f"""<!doctype html><html><head><meta charset=utf-8><style>{css}
.L{{position:absolute;left:0;top:0;width:1920px;height:1080px;opacity:0}} .abs{{position:absolute}}
.src{{position:absolute;left:96px;bottom:48px;font-size:17px;color:{G2};opacity:.8}}
.han{{font-family:'Noto Serif CJK TC',serif}}
</style></head><body>
<div class="brand" id="brand"><b>Journal of Digital History</b> &nbsp;·&nbsp; video abstract</div>

<div class="L" id="S1">
 <div class="abs" style="left:1130px;top:0;height:1080px;display:flex;align-items:center"><div style="font-size:60px;font-weight:600;line-height:1.2">
  <div id="l0">In 19th-century China,</div><div id="l1">you could <span style="position:relative;display:inline-block;padding:0 8px;margin:0 -2px"><span id="hl" style="position:absolute;left:0;right:0;top:12%;bottom:4%;background:{VIO};transform-origin:left center;transform:scaleX(0)"></span><span style="position:relative">play</span><span id="hlt" style="position:absolute;left:8px;top:0;color:#FFFFFF;clip-path:inset(0 100% 0 0)">play</span></span> your way</div><div id="l2">to the top of the imperial</div><div id="l3">bureaucracy.</div></div></div>
 <div class="abs" id="h3" style="left:255px;top:610px;width:780px;text-align:center;font-size:32px;line-height:1.35;color:{G2}">Four 4s: the luckiest throw in the game<br>– about 1 in 1,296</div>
</div>
<div class="L" id="S2">
 <div class="abs" id="cw" style="left:{X0}px;top:{Y0}px;width:{CW}px;height:{CH}px;transform-origin:{(rx0+rx1)/2-X0}px {(ry0+ry1)/2-Y0}px;mix-blend-mode:multiply"><img src="assets/chart.png" style="width:100%;height:100%;filter:saturate(.55) contrast(1.05)"></div>
 <svg class="abs" width="1920" height="1080">
  <g id="o1"><circle cx="{c1[0]}" cy="{c1[1]}" r="28" fill="none" stroke="{VIO}" stroke-width="4"/>{badge(c1[0]-44,c1[1]-34,1)}</g>
  <path id="o2p" d="M{P0[0]},{P0[1]} C {P1[0]},{P1[1]} {P2[0]},{P2[1]} {P3[0]},{P3[1]}" fill="none" stroke="{VIO}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
  <g id="o2b">{badge(bz(0)+26,bz(1),2)}</g>
  <g id="o3"><circle cx="{c66[0]}" cy="{c66[1]}" r="28" fill="none" stroke="{VIO}" stroke-width="4"/>{badge(c66[0]+44,c66[1]-34,3)}</g>
  <g id="o4"><rect x="{rx0}" y="{ry0}" width="{rx1-rx0}" height="{ry1-ry0}" fill="none" stroke="{VIO}" stroke-width="3" stroke-dasharray="8 6"/>{badge(rx0+28,ry0+28,4)}</g>
 </svg>
 <div class="abs" style="left:1056px;top:150px;width:780px">
  <div id="k0">{kick('Mandarin Promotions')}</div>
  <div id="k1" style="display:flex;align-items:baseline;gap:26px;margin-top:10px"><span class="han" style="font-size:96px;font-weight:700;letter-spacing:.05em">陞官圖</span><span style="font-size:28px;color:{G2}"><i>Shēngguāntú</i></span></div>
  <div id="k2" style="display:flex;gap:44px;margin-top:20px">
   {''.join(f'<div><div class="cnt" data-n="{n}" style="font-size:48px;font-weight:600;color:{VIO};line-height:1;font-variant-numeric:tabular-nums">{n}</div><div style="font-size:20px;color:{G2};margin-top:6px">{t}</div></div>' for n,t in [(434,'offices'),(66,'departments'),(22,'starting points'),(18,'final ranks')])}
  </div></div>
 <div class="abs" style="left:1056px;bottom:{1080-(Y0+CH):.0f}px;width:800px"><div id="k3">{kick('How to play',VIO)}</div><div style="margin-top:22px">{rl}</div></div>
 {src('Figure 1 · Game chart, reproduced by Puk Wing Kin (2011), courtesy of Puk Wing Kin','k4')}
</div>

<div class="L" id="S3">
 <div class="abs" id="a0" style="left:96px;top:150px">{kick('Roll a double',VIO)}<div style="font-size:30px;color:{G2};margin-top:10px">Each double has a name, and decides your next move.</div></div>
 {s3l}
 <svg class="abs" width="1920" height="1080" id="dice3"><line id="a9" x1="960" y1="170" x2="960" y2="980" stroke="{G1}" stroke-width="1.2"/></svg>
 <div class="abs" id="b0" style="left:{PX}px;top:150px">{kick('On the board',VIO)}<div style="font-size:30px;color:{G2};margin-top:10px">Every office lists where each double takes you.</div></div>
 <div class="abs" id="b1" style="left:{PX}px;top:{PY}px;width:{PW}px;mix-blend-mode:multiply"><img src="assets/purchase.jpg" style="width:{PW}px;display:block;filter:saturate(.6)"></div>
 <svg class="abs" width="1920" height="1080"><rect id="b2" x="{hx0}" y="{PY}" width="{hx1-hx0}" height="{526*ps}" fill="none" stroke="{VIO}" stroke-width="4"/></svg>
 <div class="abs" style="left:{PX}px;top:{PY+526*ps+26}px;width:{PW}px;font-size:24px;line-height:1.5">
  <div id="b3" style="color:{G2}">Example · <span class="han">候補道</span> expectant circuit intendant</div>
  <div style="display:grid;grid-template-columns:auto auto;gap:2px 30px;margin-top:8px">
   <span class="bx"><span class="han">德</span> Virtue → grain intendant</span><span class="bx"><span class="han">良柔</span> Mediocre, Weak → probation</span>
   <span class="bx"><span class="han">才</span> Talent → salt intendant</span><span class="bx"><span class="han">賍</span> Corrupt → suspended</span>
   <span class="bx"><span class="han">功</span> Effort → circuit intendant</span><span></span></div></div>
 {src('Dice names from the game rules · Figure 9 · Expectant officials by purchase (捐班候補), from the game chart','b4')}
</div>

<div class="L" id="S4">
 <div class="abs" id="c0" style="left:96px;top:150px">{kick('Just a game?',VIO)}<div style="font-size:30px;color:{G2};margin-top:10px">The authors mapped every possible promotion path, in the official rule book and on the board.</div></div>
 <div class="abs" id="c1" style="left:80px;top:250px;width:790px;mix-blend-mode:multiply"><img src="assets/net-statute.png" style="width:790px;display:block"></div>
 <div class="abs" id="c2" style="left:1010px;top:235px;width:800px;mix-blend-mode:multiply"><img src="assets/net-game.png" style="width:800px;display:block"></div>
 <div class="abs" id="c3" style="left:130px;top:800px;font-size:24px"><b>Figure 4 · Examination of Rank-Classes</b> <span style="color:{G2}">(official rules)</span></div>
 <div class="abs" id="c4" style="left:1060px;top:800px;font-size:24px"><b>Figure 6 · Mandarin Promotions</b> <span style="color:{G2}">(game)</span></div>
 <div class="abs" style="left:0;right:0;top:880px;display:flex;flex-direction:column;align-items:center;gap:10px">
  <div id="c5" style="display:flex;align-items:center;gap:20px">{check}<span style="font-size:48px;font-weight:600">Close match!</span></div>
  <div id="c6" style="font-size:24px;color:{G2}">The game follows the promotion rules in force before 1843.</div></div>
</div>

<div class="L" id="S5">
 <div class="abs" style="left:96px;top:150px;width:1700px"><div id="d0">{kick('Fairness check',VIO)}</div>
  <div id="d1" style="display:flex;align-items:baseline;gap:22px;margin-top:10px"><span id="cnt" style="font-size:64px;font-weight:600;color:{VIO};font-variant-numeric:tabular-nums;min-width:250px">100,000</span><span style="font-size:32px;font-weight:600">games played by computer</span></div>
  <div id="d2" style="font-size:26px;color:{G2};margin-top:4px">to compare how players fared, depending on their background (their first throw)</div></div>
 <div class="abs" id="d3" style="left:96px;top:392px;font-size:22px;color:{G2}">Average chips won or lost per player</div>
 <svg class="abs" width="1920" height="1080" id="bars"></svg>
 <div class="abs" style="left:1060px;top:450px;width:760px">{rr}</div>
 {src('Table 8 · without purchase. Bars: group mean; circles: single starting positions. “Clerks &amp; specialists” = the article’s “incipient professionalism”','d4')}
</div>

<div class="L" id="S6">
 <svg class="abs" width="1920" height="1080" id="dice6"></svg>
 <div class="abs" style="left:0;right:0;top:400px;text-align:center">
  <div id="p0" style="font-size:52px;line-height:1.5;color:{G2}">Merit and fame, on paper, come like a dream.</div>
  <div id="p1" style="font-size:52px;line-height:1.5;font-weight:600">Good offices in fact are all up for pay.</div>
  <div id="p2" style="font-size:24px;color:{G2};margin-top:26px">Poem on a game of Mandarin Promotions, <i>Shanghai Daily</i>, New Year 1887</div></div>
 <div class="abs" id="m0" style="left:0;right:0;top:740px;text-align:center">
  <div style="width:80px;height:2px;background:{G1};margin:0 auto 34px"></div>{kick('What it means',VIO)}
  <div style="font-size:32px;line-height:1.4;margin:16px auto 0;width:1100px">The game pictured a world where your birth counts more than your merit, and money buys shortcuts.</div></div>
</div>

<div class="L" id="S7">
 <svg id="fp7" class="abs" style="left:110px;top:150px" width="780" height="780" viewBox="-208 -208 416 416"></svg>
 <div class="abs" style="left:1000px;top:250px;width:820px">
  <div class="kicker" id="e0x" style="color:{VIO}">Read the article</div>
  <div id="e1x" style="font-size:54px;font-weight:600;line-height:1.18;margin-top:24px">Gaming the Qing Mandarinate: Digital Approaches to a Nineteenth-Century Chinese Board Game</div>
  <div id="e2x" style="font-size:36px;font-weight:700;margin-top:56px;line-height:1.45">Elisabeth Kaske<br>Florian Keßler</div>
</div>
 <img id="e3x" src="jdh-logo.svg" class="abs" style="left:96px;top:66px;height:52px">
 <img id="e4x" src="logos.png" class="abs" style="left:1000px;bottom:110px;height:110px">
</div>

<svg class="abs" width="1920" height="1080" id="gd" style="left:0;top:0"></svg>

<script>
const FP={fpdata}; const BEATS={beats};
const C={{TEAL:'{TEAL}',BG:'{BG}',INK:'{INK}',G1:'{G1}',G2:'{G2}',VIO:'{VIO}',RED:'{RED}'}};
const G={json.dumps(G)}; const D3={json.dumps(d3)};
const NS='http://www.w3.org/2000/svg';
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)); const lin=(t,a,b)=>cl((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3); const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const eb=x=>{{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);}};
const B=t=>BEATS.reduce((a,b)=>Math.abs(b-t)<Math.abs(a-t)?b:a); // snap to nearest beat
const $=id=>document.getElementById(id);
function fade(el,t,a,d=.5,dy=16){{const p=eo(lin(t,a,a+d));el.style.opacity=p;el.style.transform=`translateY(${{(1-p)*dy}}px)`;}}
function fadeX(el,t,a,d=.5,dx=-20){{const p=eo(lin(t,a,a+d));el.style.opacity=p;el.style.transform=`translateX(${{(1-p)*dx}}px)`;}}
function dieSVG(n,s){{const P={{1:[[0,0]],2:[[-1,-1],[1,1]],3:[[-1,-1],[0,0],[1,1]],4:[[-1,-1],[1,-1],[-1,1],[1,1]],5:[[-1,-1],[1,-1],[0,0],[-1,1],[1,1]],6:[[-1,-1],[1,-1],[-1,0],[1,0],[-1,1],[1,1]]}}[n];
 const col=(n==1||n==4)?C.RED:C.INK;let h=`<rect x="${{-s/2}}" y="${{-s/2}}" width="${{s}}" height="${{s}}" rx="${{s*.17}}" fill="#fff" stroke="${{C.INK}}" stroke-width="${{Math.max(1.5,s/45)}}"/>`;
 P.forEach(([x,y])=>h+=`<circle cx="${{x*s*.25}}" cy="${{y*s*.25}}" r="${{n==1?s*.13:s*.085}}" fill="${{col}}"/>`);return h;}}
function mk(svg,list){{return list.map(([x,y,n,s])=>{{const g=document.createElementNS(NS,'g');g.innerHTML=dieSVG(n,s);svg.appendChild(g);return {{g,x,y,n,s}};}});}}
function land(d,t,t0,dur=.45,drop=140,sc=1,x=null,y=null){{const p=lin(t,t0-dur,t0);const e=eo(p);const rot=(1-e)*((d.n*53)%70-35);
 d.g.setAttribute('transform',`translate(${{x??d.x}},${{(y??d.y)-(1-e)*drop}}) rotate(${{rot}}) scale(${{sc*(0.85+0.15*e)}})`);d.g.style.opacity=cl(p*4);}}
const gd=mk($('gd'),[0,1,2,3].map(i=>[330+i*190,500,4,150]));
const d3=mk($('dice3'),D3);
const d6=mk($('dice6'),[4,4,6,2].map((n,i)=>[960+(i-1.5)*150,260,n,116]));
// fingerprint
function buildFP(svg){{const items=[];FP.forEach(g=>{{const G_=document.createElementNS(NS,'g');const[x1,y1,x2,y2,st,sw]=g.l;
 const L=document.createElementNS(NS,'line');L.setAttribute('stroke',st);L.setAttribute('stroke-width',sw);G_.appendChild(L);
 const cs=g.o.map(o=>{{const c=document.createElementNS(NS,'circle');c.setAttribute('r',o[2]);c.setAttribute('fill',o[3]||'none');c.setAttribute('stroke',o[4]||'none');c.setAttribute('stroke-width',.75);G_.appendChild(c);return [c,o];}});
 svg.appendChild(G_);items.push({{G:G_,L,cs,x1,y1,x2,y2}});}});return items;}}
function drawFP(items,p){{const n=items.length;items.forEach((it,i)=>{{const k=eo(cl((p*(n+12)-i)/12));it.G.style.opacity=k>0?Math.min(1,k*3):0;
 it.L.setAttribute('x1',it.x1);it.L.setAttribute('y1',it.y1);it.L.setAttribute('x2',it.x1+(it.x2-it.x1)*k);it.L.setAttribute('y2',it.y1+(it.y2-it.y1)*k);
 it.cs.forEach(([c,o])=>{{c.setAttribute('cx',it.x1+(o[0]-it.x1)*k);c.setAttribute('cy',it.y1+(o[1]-it.y1)*k);}});}});}}
const fp7=buildFP($('fp7'));
// bars
const zx=660,sc=6,TOP=460;let bh='';
[-30,0,30].forEach(v=>bh+=`<line x1="${{zx+v*sc}}" y1="${{TOP-20}}" x2="${{zx+v*sc}}" y2="${{TOP+430}}" stroke="${{v==0?C.INK:C.G1}}" stroke-width="${{v==0?1.5:1}}" ${{v==0?'':'stroke-dasharray="2 6"'}}/><text x="${{zx+v*sc}}" y="${{TOP+458}}" text-anchor="middle" font-family="Fira" font-size="18" fill="${{C.G2}}">${{v>0?'+':''}}${{v}}</text>`);
G.forEach(([name,vals,h],i)=>{{const y=TOP+i*86;const m=vals.reduce((a,b)=>a+b)/vals.length;
 bh+=`<rect id="br${{i}}" y="${{y}}" height="40" fill="${{h?C.VIO:C.G2}}" opacity="${{h?1:.55}}"/>`;
 vals.forEach(v=>bh+=`<circle class="bd${{i}}" cx="${{zx+v*sc}}" cy="${{y+20}}" r="5" fill="${{C.BG}}" stroke="${{C.INK}}" stroke-width="1.8"/>`);
 bh+=`<text id="bl${{i}}" x="380" y="${{y+28}}" text-anchor="end" font-family="Fira" font-size="23" font-weight="${{h?600:400}}" fill="${{C.INK}}">${{name}}</text><text id="bv${{i}}" x="394" y="${{y+28}}" font-family="Fira" font-size="22" font-weight="600" fill="${{h?C.VIO:C.G2}}">${{m>0?'+':''}}${{Math.round(m)}}</text>`;}});
bh+=`<line id="bdiv" x1="1000" y1="440" x2="1000" y2="900" stroke="${{C.G1}}" stroke-width="1.2"/>`;
$('bars').innerHTML=bh;
const fmt=n=>n.toLocaleString('en-US');
// timeline — ONE RULE FOR ALL SCENES (seconds)
//  • Pictures arrive fast: QUICK between dice / bars / markers, GAP between blocks.
//  • Text waits only as long as it takes to read: READ seconds per word (≈4.5 words/s, a fast "shorts" pace), never less than STEP.
//  • HOLD after the last element, then the scene changes.
const IN=.4, STEP=.5, QUICK=.25, GAP=.4, READ=.22, HOLD=1.2, DTR=.7;
const rd=w=>Math.max(STEP,w*READ);
const S={{}};
(function(){{
 let c;
 // S1 hook
 S.dice1=[.8,.8+QUICK,.8+2*QUICK,.8+3*QUICK]; c=S.dice1[3]+GAP;
 S.title1=c; S.hl=c+IN+.2; S.cap1=c+rd(12); S.TR=S.cap1+rd(10)+HOLD; S.s2=S.TR+DTR*.85;
 // S2 board: map → title + Chinese → counter → rules 1-4 (each read before the next)
 c=S.s2+.3; S.k0=c; S.k1=c+QUICK; S.k2=c+2*QUICK; S.cntEnd=S.k2+.8; c=S.cntEnd+GAP;
 S.k3=c; c+=STEP; S.rt=[0,1,2].map(i=>c+i*1.5).concat([c+4.5]); S.s3=S.rt[3]+rd(13)+HOLD;
 // S3 roll a double
 c=S.s3+.3; S.a0=c; c+=rd(12)*.6; S.rows=[c,c+.9,c+1.8]; c=S.rows[2]+.9;
 S.b0=c; S.b1=S.b0+QUICK; S.b2=S.b1+.7; S.b3=S.b2+QUICK; c=S.b3+.4;
 S.bx=[]; for(let i=0;i<5;i++){{S.bx.push(c); c+=.45;}} S.dl=S.rows[0]; S.s4=c+2.4+HOLD;
 // S4 just a game
 c=S.s4+.3; S.w1=c; S.w2=c+.6; S.c0=S.w2+1.3; S.ck=S.c0+rd(18)*.7; S.c6=S.ck+STEP; S.s5=S.c6+rd(9)+HOLD;
 // S5 fairness check
 c=S.s5+.3; S.d0=c; S.d1=c+QUICK; S.d2=S.d1+.3; S.cntEnd5=S.d1+1.0; S.d3=S.cntEnd5;
 S.BT=[0,1,2,3,4].map(i=>S.cntEnd5+.1+i*.35); c=S.BT[4]+IN+.3; S.res=[c,c+1.5,c+3.0]; S.s6=S.res[2]+rd(15)+HOLD;
 // S6 poem → meaning
 c=S.s6+.3; S.dice6=[0,1,2,3].map(i=>c+.4+i*.18); c=S.dice6[3]+.2;
 S.p0=c; S.p1=c+1.3; S.p2=S.p1+1.0; S.m0=S.p2+.8; S.s7=S.m0+rd(19)*.8+.8;
 // S7 end card
 S.end=S.s7+2.2+rd(16)+HOLD;
}})();
const T={{s2:S.s2,s3:S.s3,s4:S.s4,s5:S.s5,s6:S.s6,s7:S.s7,end:S.end}};
const W={{S1:[0,T.s2],S2:[T.s2,T.s3],S3:[T.s3,T.s4],S4:[T.s4,T.s5],S5:[T.s5,T.s6],S6:[T.s6,T.s7],S7:[T.s7,T.end]}};
function layer(id,t){{const[a,b]=W[id];const o=Math.min(eo(lin(t,a-.05,a+.25)),1-lin(t,b-.3,b));const el=$(id);el.style.opacity=(t<a-.05||t>b)?0:o;el.style.display=(t<a-.1||t>b+.05)?'none':'block';}}
const F=IN;
window.seek=function(t){{
 Object.keys(W).forEach(k=>layer(k,t));
 $('brand').style.opacity=eo(lin(t,0,.4))*(1-lin(t,T.s7-.3,T.s7));
 const tc=[{(rx0+rx1)/2},{(ry0+ry1)/2}]; const TR=S.TR;
 gd.forEach((d,i)=>{{const mv=eio(lin(t,TR,TR+DTR));const tx=tc[0]+(i%2?24:-24),ty=tc[1]+(i<2?-24:24);
  if(t<TR) land(d,t,S.dice1[i],.4,140,1);
  else {{d.g.setAttribute('transform',`translate(${{d.x+(tx-d.x)*mv}},${{d.y+(ty-d.y)*mv}}) rotate(${{mv*(i*90+45)}}) scale(${{1-0.72*mv}})`);d.g.style.opacity=1-lin(t,T.s2+.6,T.s2+1.1);}}}});
 if(t>T.s2+1.2) gd.forEach(d=>d.g.style.opacity=0);
 [0,1,2,3].forEach(i=>fade($('l'+i),t,S.title1,F,14));fade($('h3'),t,S.cap1,F,10);
 {{const hp=eio(lin(t,S.hl,S.hl+IN));$('hl').style.transform=`scaleX(${{hp}})`;$('hlt').style.clipPath=`inset(0 ${{(1-hp)*100}}% 0 0)`;}}
 // S2
 const s2=T.s2; const zc=1.25-0.25*eio(lin(t,s2-.3,s2+.6));$('cw').style.transform=`scale(${{zc}})`;$('cw').style.opacity=eo(lin(t,s2-.3,s2+.4));
 fade($('k0'),t,S.k0,F);fade($('k1'),t,S.k1,F);fade($('k2'),t,S.k2,F);fade($('k4'),t,S.k1,.6,0);
 document.querySelectorAll('.cnt').forEach(e=>e.textContent=Math.round(+e.dataset.n*eo(lin(t,S.k2,S.cntEnd))));
 fade($('k3'),t,S.k3,F);
 const rt=S.rt; rt.forEach((a,i)=>fadeX($('r'+i),t,a,F));
 const pop=(el,a)=>{{const p=lin(t,a,a+.4);el.style.opacity=cl(p*3);el.style.transformOrigin='center';el.style.transformBox='fill-box';el.style.transform=`scale(${{0.6+0.4*eb(p)}})`;}};
 pop($('o1'),rt[0]);pop($('o3'),rt[2]);pop($('o4'),rt[3]);
 const pp=eio(lin(t,rt[1],rt[1]+.5));$('o2p').style.opacity=pp>0?1:0;$('o2p').style.clipPath=`inset(${{(1-pp)*100}}% 0 0 0)`;pop($('o2b'),rt[1]+.2);
 // S3
 fade($('a0'),t,S.a0,F); d3.forEach((d,j)=>land(d,t,S.rows[j<6?0:(j<10?1:2)]+.15,.4,90)); [0,1,2].forEach(i=>fade($('ag'+i),t,S.rows[i],F,10));
 $('a9').style.opacity=lin(t,S.a0,S.a0+.5);
 fade($('b0'),t,S.b0,F);
 const pw=eio(lin(t,S.b1,S.b1+.6));$('b1').style.clipPath=`inset(0 ${{100-pw*100}}% 0 0)`;$('b1').style.opacity=pw>0?1:0;
 $('b2').style.opacity=lin(t,S.b2,S.b2+.25);
 fade($('b3'),t,S.b3,F);document.querySelectorAll('.bx').forEach((e,i)=>fade(e,t,S.bx[i],F,6));
 fade($('b4'),t,S.b1,.6,0);
 // S4
 fade($('c0'),t,S.c0,F);
 const w1=eio(lin(t,S.w1,S.w1+.9)),w2=eio(lin(t,S.w2,S.w2+.9));
 $('c1').style.clipPath=`inset(0 ${{100-w1*100}}% 0 0)`;$('c2').style.clipPath=`inset(0 ${{100-w2*100}}% 0 0)`;
 fade($('c3'),t,S.w1+.4,F);fade($('c4'),t,S.w2+.4,F);
 const cp=lin(t,S.ck,S.ck+.45);$('c5').style.opacity=cl(cp*3);$('c5').style.transform=`scale(${{0.7+0.3*eb(cp)}})`;
 $('ckp').setAttribute('stroke-dashoffset',45*(1-eo(lin(t,S.ck+.1,S.ck+.5))));
 fade($('c6'),t,S.c6,F);
 // S5
 fade($('d0'),t,S.d0,F);fade($('d1'),t,S.d1,F);
 $('cnt').textContent=fmt(Math.round(100000*eio(lin(t,S.d1,S.cntEnd5))/100)*100);
 fade($('d2'),t,S.d2,F);fade($('d3'),t,S.d3,F);fade($('d4'),t,S.d3,.6,0);
 const BT=S.BT;
 G.forEach(([n,vals,h],i)=>{{const m=vals.reduce((a,b)=>a+b)/vals.length;const a=BT[i];const p=eo(lin(t,a,a+.45));const w=Math.abs(m*sc)*p;
  const r=$('br'+i);r.setAttribute('x',m>0?zx:zx-w);r.setAttribute('width',w);$('bl'+i).style.opacity=lin(t,a-.15,a+.1);$('bv'+i).style.opacity=lin(t,a+.3,a+.5);
  document.querySelectorAll('.bd'+i).forEach(c=>c.style.opacity=lin(t,a+.35,a+.55));}});
 $('bdiv').style.opacity=lin(t,BT[0],BT[0]+.6);
 S.res.forEach((a,i)=>fadeX($('e'+i),t,a,F));
 // S6
 d6.forEach((d,i)=>land(d,t,S.dice6[i],.4,120));
 fade($('p0'),t,S.p0,F);fade($('p1'),t,S.p1,F);fade($('p2'),t,S.p2,F);fade($('m0'),t,S.m0,F);
 // S7
 const s7=T.s7; drawFP(fp7,eio(lin(t,s7,s7+2.0)));
 fade($('e0x'),t,s7+.4,F);fade($('e1x'),t,s7+.7,F);fade($('e2x'),t,s7+1.2,F);fade($('e3x'),t,s7,F,0);fade($('e4x'),t,s7+2.0,.5,0);
}};
window.seek(0);
</script></body></html>"""
open('video.html','w',encoding='utf8').write(html)
print('ok')
