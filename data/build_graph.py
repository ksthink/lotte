import json,csv,heapq,math
SPEED=60.0      # m/min, crowded evening walking
ADV=0.283       # m per px (1600px render), 1F ice rink 65 m ≈ 230 px
MI=0.35         # m per px on Magic Island page (assumed)
VERT=1.5        # min per floor by escalator
BRIDGE=4.0      # min, 2F west ↔ Magic Island entrance
OVER=1.0        # fixed overhead per trip
N=[ # id, name, area, x, y (px on 1600-wide render of the official guide map PDF)
 ('gate','정문 게이트(B1F)','B1',775,235),
 ('f1_meet','만남의 광장 · 디저트 왕국','1F',775,235),
 ('f1_garden','가든스테이지','1F',605,465),
 ('f1_parade','퍼레이드 코스(가든스테이지 앞)','1F',560,505),
 ('sin','신밧드의 모험','1F',403,396),
 ('trn','로티트레인','1F',862,453),
 ('flu','후룸라이드','1F',475,568),
 ('fly','플라이벤처','1F',1033,381),
 ('pubg','배틀그라운드','1F',972,401),
 ('kart','카트라이더','1F',759,250),
 ('c1_w','1F 서쪽 에스컬레이터','1F',412,345),
 ('c1_m','1F 북쪽 에스컬레이터','1F',790,205),
 ('c1_e','1F 동쪽 에스컬레이터','1F',1145,265),
 ('c2_w','2F 서쪽(매직아일랜드 연결)','2F',175,300),
 ('c2_m','2F 중앙 에스컬레이터','2F',590,225),
 ('c2_e','2F 동쪽 에스컬레이터','2F',770,330),
 ('fre','후렌치레볼루션','2F',754,310),
 ('bmp','범퍼카','2F',668,157),
 ('c3_w','3F 서쪽 에스컬레이터','3F',530,397),
 ('c3_m','3F 중앙 에스컬레이터','3F',900,380),
 ('c3_e','3F 동쪽 에스컬레이터','3F',1030,480),
 ('kong','콩X고질라','3F',932,382),
 ('c4_w','4F 서쪽 에스컬레이터','4F',900,566),
 ('c4_m','4F 중앙 에스컬레이터','4F',1230,532),
 ('c4_e','4F 동쪽 에스컬레이터','4F',1395,600),
 ('phr','파라오의 분노','4F',1299,545),
 ('bal','풍선비행','4F',1447,599),
 ('mi_br','매직아일랜드 입구(다리)','MI',785,600),
 ('atl','아틀란티스','MI',663,277),
 ('gsw','자이로스윙','MI',626,200),
 ('gdr','자이로드롭','MI',422,338),
 ('com','혜성특급','MI',407,453),
 ('gsp','자이로스핀','MI',389,488),
 ('castle','매직캐슬','MI',580,330),
 ('out','크리스마스 마켓(월드파크)','OUT',0,0),
]
# AUTO-ATTR: add every guide-map attraction that has a marker coordinate
import os
_J=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'attractions.json')))['attractions']
KNOWN={6:'sin',10:'trn',8:'flu',12:'fly',11:'pubg',25:'kart',26:'fre',27:'bmp',28:'kong',31:'phr',30:'bal',33:'atl',34:'gsw',36:'gdr',38:'com',39:'gsp'}
NODE_OF=dict(KNOWN);B1N=[]
for o in _J:
    no=o['guide_no']
    if not no or no in KNOWN or not o['map_xy']:continue
    ar=o['area'];fl='MI' if o['map_page']==4 else 'B1' if o['map_page']==1 else '1F' if o['map_page']==2 else ('2F' if '2층' in ar else '3F' if '3층' in ar else '4F')
    nid='g%d'%no;N.append((nid,o['name'],fl,round(o['map_xy'][0]*1600/1920),round(o['map_xy'][1]*1600/1920)));NODE_OF[no]=nid
    if fl=='B1':B1N.append(nid)
idx={n[0]:n for n in N}
E={}
def add(a,b,w,kind):
    E.setdefault(a,[]).append((b,w,kind));E.setdefault(b,[]).append((a,w,kind))
def walk(a,b):
    A,B=idx[a],idx[b];s=MI if A[2]=='MI' else ADV
    return math.hypot(A[3]-B[3],A[4]-B[4])*s/SPEED
areas={}
for n in N:areas.setdefault(n[2],[]).append(n[0])
edges=[]
for ar,ids in areas.items():
    if ar=='OUT':continue
    if ar=='B1':ids=[i for i in ids if i!='gate']
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            a,b=ids[i],ids[j]
            if {a,b}=={'gate','f1_meet'}:continue
            w=walk(a,b);add(a,b,w,'walk');edges.append((a,b,round(w,2),'walk'))
for s in ('w','m','e'):
    for f in (1,2,3):
        a,b=f'c{f}_{s}',f'c{f+1}_{s}';add(a,b,VERT,'escalator');edges.append((a,b,VERT,'escalator'))
for _b in B1N:
    add('gate',_b,3.0,'walk');edges.append(('gate',_b,3.0,'walk(B1F, 가정)'))
add('gate','f1_meet',2.0,'escalator');edges.append(('gate','f1_meet',2.0,'escalator(B1F→1F)'))
add('c2_w','mi_br',BRIDGE,'bridge');edges.append(('c2_w','mi_br',BRIDGE,'bridge'))
add('gate','out',8.0,'walk');edges.append(('gate','out',8.0,'walk(지하 연결통로)'))
def dij(src):
    d={src:0};pq=[(0,src)]
    while pq:
        c,u=heapq.heappop(pq)
        if c>d[u]:continue
        for v,w,_ in E.get(u,[]):
            if c+w<d.get(v,1e9):d[v]=c+w;heapq.heappush(pq,(c+w,v))
    return d
P=['gate','f1_meet','f1_garden','f1_parade','sin','trn','flu','fly','pubg','kart','fre','bmp','kong','phr','bal','atl','gsw','gdr','com','gsp','castle','out']
P=P[:-1]+['mi_br']+[n[0] for n in N if n[0].startswith('g') and n[0][1:].isdigit()]+['out']
M={a:{} for a in P}
for a in P:
    d=dij(a)
    for b in P:M[a][b]=2 if a==b else max(2,round(d[b]+OVER))
json.dump({'meta':{'source':'롯데월드 어드벤처 2026 가이드맵(국문) PDF, 마커 좌표는 1600px 렌더 기준',
  'scale_m_per_px':{'adventure':ADV,'magic_island':MI},'walk_m_per_min':SPEED,'escalator_min_per_floor':VERT,
  'bridge_min':BRIDGE,'overhead_min':OVER,
  'notes':['층별 그림은 조감도라 축척이 일정하지 않음','에스컬레이터는 층마다 서·중앙·동 3곳이 위아래로 이어진다고 단순화','매직아일랜드 축척과 다리 시간은 가정값']},
  'nodes':[{'id':n[0],'name':n[1],'area':n[2],'x':n[3],'y':n[4]} for n in N],
  'edges':[{'a':a,'b':b,'min':w,'kind':k} for a,b,w,k in edges],
  'travel_min':M},open('data/lotteworld-graph.json','w'),ensure_ascii=False,indent=1)
with open('data/travel-minutes.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['from\\to']+P)
    for a in P:w.writerow([a]+[M[a][b] for b in P])
json.dump(NODE_OF,open('/tmp/nodeof.json','w'))
open('/tmp/matrix.js','w').write('const TRAVEL='+json.dumps(M,separators=(',',':'))+';\n')
for a in ['gate','f1_parade','fre','kong','atl']:
    print(a,{b:M[a][b] for b in ['f1_garden','fre','kong','phr','atl','com','gdr','out']})
