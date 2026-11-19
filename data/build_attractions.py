import re,json,csv
from PIL import Image
A=[ # no,name,zone,floor,desc,solo,guardian,age,kids
(1,'드림보트','언더랜드','B1F','신비한 요정의 숲으로 떠나는 판타지 보트 라이드','110cm 이상 어린이','90cm ~ 110cm','',1),
(2,'4D슈팅씨어터','언더랜드','B1F','4D로 즐기는 짜릿한 슈팅 어드벤처','120cm 이상','110cm ~ 120cm','',0),
(3,'와일드밸리','언더랜드','B1F','보트를 타고 급류를 지나는 미스터리 동굴 모험','110cm 이상','','',0),
(4,'와일드정글','언더랜드','B1F','지프차를 타고 고대 유적을 찾아 떠나는 신전 탐험','110cm 이상','','',0),
(5,'와일드윙','언더랜드','B1F','강렬한 바람을 가르며 하늘을 비행하는 아찔한 체험','110cm 이상','','',0),
(6,'신밧드의모험','어드벤처','1F','보트를 타고 떠나는 지하 속 신밧드의 모험 이야기','110cm 이상','100cm ~ 110cm','',0),
(7,'스페인해적선','어드벤처','1F','75도 각도까지 올라가는 스릴 넘치는 해적선','110cm 이상','','',0),
(8,'후룸라이드','어드벤처','1F','보트를 타고 급류에 밀려 폭포에서 떨어지는 스릴!','110cm 이상','','65세 이하',0),
(9,'회전바구니','어드벤처','1F','빙글빙글 손잡이를 돌릴수록 빠르게 회전하는 바구니','110cm 이상','100cm ~ 110cm','',0),
(10,'로티트레인','어드벤처','1F','꼬마 기차를 타고 떠나는 어드벤처 한바퀴','','5세 이하','',1),
(11,'배틀그라운드','어드벤처','1F','적들에게 맞서 생존을 위한 섬 탈출기 워크스루 슈팅 시어터','130cm 이상','','',0),
(12,'플라이벤처','어드벤처','1F','괴짜과학자가 발명한 플라잉머신을 타고 떠나는 시공간 초월 비행','140cm ~ 195cm','120cm ~ 140cm','',0),
(13,'회전목마','어드벤처','1F','64필의 아름다운 백마를 타고 보내는 로맨틱한 시간','100cm 이상','100cm 미만','',0),
(14,'황야의무법자','어드벤처','1F','서부시대 보안관이 되어 악당을 물리치는 슈팅 배틀','(말) 120cm 이상','(마차) 120cm 미만','',0),
(15,'키즈토리아','어드벤처','1F','맨발로 마음껏 뛰어 놀 수 있는 거대한 동화 속 세상','','125cm 미만','',1),
(16,'드래곤와일드슈팅','어드벤처','1F','로티성에 쳐들어온 드래곤들을 슈팅건으로 무찔러봐요','110cm 이상','100cm ~ 110cm','',0),
(17,'어린이범퍼카','어드벤처','1F','뛰뛰빵빵! 어린이들을 위한 범퍼카','110cm ~ 125cm 어린이','90cm ~ 110cm 미만','',1),
(18,'햇님달님','어드벤처','1F','호랑이를 피해 햇님달님 오누이와 하늘 위로 점프!','90cm ~ 140cm 어린이','','',1),
(19,'점핑피쉬','어드벤처','1F','무서운 상어를 피해 빙글빙글 점프하는 물고기','110cm 이상 어린이','90cm ~ 110cm 미만','',1),
(20,'언더씨킹덤','어드벤처','1F','맨발로 마음껏 뛰어 놀 수 있는 바다왕국 놀이터','','125cm 미만','',1),
(21,'유레카','어드벤처','1F','영차!영차! 하늘을 나는 꼬마 요술배','110cm 이상 어린이','110cm 미만','',1),
(22,'스윙팡팡','어드벤처','1F','로티와 친구들과 함께 위,아래로 통통 튀기는 바구니','110cm 이상 어린이','110cm 미만','',1),
(23,'매직붕붕카','어드벤처','1F','좌충우돌 색색깔의 복어범퍼카','125cm ~ 140cm','100cm ~ 125cm 미만 어린이','',0),
(24,'어린이동화극장','어드벤처','1F','어린이 뮤지컬이 펼쳐지는 극장','','전체 이용 가능','',1),
(25,'카트라이더','어드벤처','1F','롯데월드에서 즐기는 카트라이더 레이싱','130cm ~ 180cm','','',0),
(26,'후렌치레볼루션','어드벤처','2F','어드벤처 실내를 질주하는 롤러코스터','120cm 이상','','',0),
(27,'범퍼카','어드벤처','2F','앞에서 쾅! 뒤에서 쾅! 좌충우돌 범퍼카','140cm 이상','','',0),
(28,'콩X고질라:더라이드','어드벤처','3F','히브 비행선을 타고 콩X고질라와 미지의 세계로!','110cm ~ 195cm','100cm ~ 110cm','',0),
(29,'월드모노레일','어드벤처','3F','로티,로리로 변신한 모노레일을 타고 어드벤처 한바퀴','전체 이용 가능','5세 이하','',0),
(30,'풍선비행','어드벤처','4F','열기구를 타고 하늘 위에서 바라보는 어드벤처','전체 이용 가능','6세 미만','',0),
(31,'파라오의분노','어드벤처','4F','파라오의 보물을 찾아 떠나는 스릴만점 다크 라이드!','110cm ~ 195cm','','',0),
(32,'어크로스다크','어드벤처','4F','잃어버린 유물을 찾아 우주로 떠나는 모험','110cm 이상','','',0),
(33,'아트란티스','매직아일랜드','야외','급발진하는 보트를 타고 미스터리 신전 속으로!','135cm ~ 190cm','','65세 이하',0),
(34,'자이로스윙','매직아일랜드','야외','석촌호수에 떨어질 듯 말 듯 아찔한 스윙','130cm ~ 190cm','','',0),
(35,'쁘띠빵빵','매직아일랜드','야외','호숫가를 드라이브 하는 귀여운 자동차','110cm 이상','110cm 미만','',1),
(36,'자이로드롭','매직아일랜드','야외','상공 70m 높이에서 100km/h 속도로 자유낙하하는 공포와 스릴','130cm ~ 190cm','','',0),
(37,'환타지드림','매직아일랜드','야외','꼬마 기차를 타고 떠나는 동화속 세상','110cm 이상','110cm 미만','',0),
(38,'혜성특급','매직아일랜드','야외','좌석이 회전하는 혜성특급열차를 타고 떠나는 어둠속 우주여행','120cm 이상','','',0),
(39,'자이로스핀','매직아일랜드','야외','거대한 나침반을 타고 돌고 도는 아찔한 서핑타임','125cm 이상','','',0),
(40,'스톤익스프레스','매직아일랜드','야외','돌의 정령을 따라 핑크빈을 찾아 떠나는 모험','110cm 이상','90cm ~ 110cm 미만','',1),
(41,'아르카나라이드','매직아일랜드','야외','정령의 나무를 치유하러 떠나는 마법여행','110cm 이상','110cm 미만','',1),
(42,'에오스타워','매직아일랜드','야외','타워 꼭대기를 열어 핑크빈을 찾아 떠나는 모험','120cm 이상','','',0),
]
PAGE={'B1F':1,'1F':2,'2F':3,'3F':3,'4F':3,'야외':4}
LEGX={1:740,2:None,3:None,4:None}
def words(p):
    s=open(f'/tmp/bb{p}.html').read()
    return [(x[4],float(x[0]),float(x[1]),float(x[2]),float(x[3])) for x in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>',s)]
imgs={p:Image.open(f'/tmp/c-{p}.png').convert('RGB') for p in (1,2,3,4)}
def top(p,w):
    im=imgs[p];x0,y0,x1,y1=w[1:];cs=[im.getpixel((int((x0+x1)/2+dx),int(y0-dy))) for dx in (-2,0,2) for dy in (1,2,3)]
    return max(cs,key=lambda c:max(c)-min(c))
def kind(c):
    r,g,b=c
    if max(c)-min(c)<40:return 'none'
    if b>=225 and r<200 and g<140 and r>120:return 'gift'
    if r>=190 and g<130 and 110<=b<=200:return 'food'
    return 'attr'
coords={}
for p in (1,2,3,4):
    for w in words(p):
        if re.fullmatch(r'\d{1,2}',w[0]) and w[2]<=850 and kind(top(p,w))=='attr':
            coords.setdefault((p,int(w[0])),[]).append((round(w[1]),round(w[2])))
BASE={6:55,26:67,27:66,30:78,31:81,33:87,34:60,36:45,38:81,39:48,8:74,25:60,11:54,12:42,3:44,4:40,10:30,23:30,22:30}
CLOSED1123={7:'2026-11-22 운행 종료(리뉴얼)'}  # 그 밖의 운휴는 실시간 운행 상태로 판단
ALIAS={'콩X고질라더라이드':28,'배틀그라운드 월드 에이전트':11,'카트라이더레이싱월드':25,'월드모노레일(실내운영)':29,'3D 황야의 무법자 Ⅱ':14,'범퍼카(어드벤처)':27,'4D슈팅시어터':2}
norm=lambda x:re.sub(r'[\s:]','',x)
byname={norm(a[1]):a for a in A}
out=[];seen=set()
for line in open('/tmp/official.txt'):
    oid,name,pos,minh,maxh,guard,resv,single,status,wait,op,cl=line.rstrip('\n').split('|')
    no=ALIAS.get(name) or (byname.get(norm(name)) or [None])[0]
    pdf=next((a for a in A if a[0]==no),None)
    if no:seen.add(no)
    xy=coords.get((PAGE[pdf[3]],no),[]) if pdf else []
    if no==10:xy=[(1034,543)]
    if no==21:xy=[(1137,153)]
    out.append({'official_id':oid,'name':name,'guide_no':no,'area':pos,'description':pdf[4] if pdf else None,
     'min_height_cm':int(minh) or None,'max_height_cm':int(maxh) or None,'guardian_ride_ok':guard=='Y','boarding_reservation':resv=='Y','single_rider':single=='Y',
     'guide_height_solo':pdf[5] or None if pdf else None,'guide_with_guardian':pdf[6] or None if pdf else None,'guide_age_limit':pdf[7] or None if pdf else None,'kids_ride':bool(pdf[8]) if pdf else None,
     'hours_1118':None if op=='00:00' else [op,cl],'status_1118_evening':status,
     'closed_1123':CLOSED1123.get(no),'map_page':PAGE[pdf[3]] if pdf else None,'map_xy':list(xy[0]) if len(xy)==1 else None,
     'avg_wait_2025_min':BASE.get(no),'magic_pass':False if no==28 else None,
     'note':{28:'2026-07-24 오픈, 매직패스 대상(42종) 아님',6360:None}.get(no)})
print(len(out),'official;',sum(1 for o in out if o['guide_no']),'matched to guide map; unmatched:',[o['name'] for o in out if not o['guide_no']],'; guide-only:',[a[1] for a in A if a[0] not in seen])
PERF=[('12:30','로티스 페어리테일 매지컬 타임','키디존 어린이 동화극장','스테이지'),('12:30','Smile, with Friends (캐릭터 포토타임)','어드벤처 1층 만남의 광장','포토타임'),
('14:00','해피 크리스마스 퍼레이드','어드벤처 1층 퍼레이드 코스','퍼레이드'),('15:30','로티스 페어리테일 매지컬 타임','키디존 어린이 동화극장','스테이지'),
('15:30','쿠키런 Smile with Friend','어드벤처 1층 만남의 광장','포토타임'),('16:30','Smile, with Friends (연기자 포토타임)','키즈토리아','포토타임'),
('17:00','쿠키런 Smile with Friend','어드벤처 1층 만남의 광장','포토타임'),('17:30','Smile, with Friends (연기자 포토타임)','키즈토리아','포토타임'),
('18:30','마법 성냥과 꿈꾸는 밤','가든스테이지','스테이지'),('20:00','해피 크리스마스 퍼레이드','어드벤처 1층 퍼레이드 코스','퍼레이드'),('20:40','매직캐슬 라이츠업','매직아일랜드 매직캐슬','기타')]
D='/home/claude/lotte/data/'
meta={'captured':'2026-11-18 저녁','sources':{'official':'adventure.lotteworld.com 어트랙션 목록(이름·위치·키 제한·동반·예약·싱글라이더·운영시간·상태)','guide_map':'2026 가이드맵 PDF(guide_* 항목, description, map_xy: 1920x1080pt 페이지 좌표)','avg_wait_2025_min':'queue-times.com 2025 평균, 30/60/90분 묶음 값이라 참고용','closed_1123':'사용자 확인 운휴 + 스페인해적선 리뉴얼 보도'},
 'caveats':['hours_1118·status_1118_evening은 11/18 하루의 값이며 날마다 달라짐','실시간 대기·운휴는 공식 사이트/앱이 기준','이미지와 안내문 전문은 담지 않음']}
json.dump({'meta':meta,'attractions':out},open(D+'attractions.json','w'),ensure_ascii=False,indent=1)
json.dump({'meta':{'captured':'2026-11-18','source':'adventure.lotteworld.com 공연 타임테이블(11/23 선택 화면)','caveat':'공연 사정에 따라 변경·취소될 수 있음. 소요시간은 공식 표기 없음'},'date':'2026-11-23','timetable':[{'time':t,'name':n,'place':p,'category':c} for t,n,p,c in PERF]},open(D+'performances.json','w'),ensure_ascii=False,indent=1)
with open(D+'attractions.csv','w',newline='',encoding='utf-8-sig') as f:
    ks=[k for k in out[0] if k not in('map_xy','hours_1118')]+['open_1118','close_1118','map_x','map_y']
    w=csv.DictWriter(f,fieldnames=ks);w.writeheader()
    for o in out:
        r={k:o[k] for k in ks if k in o};h=o['hours_1118'] or ['',''];m=o['map_xy'] or ['',''];r.update(open_1118=h[0],close_1118=h[1],map_x=m[0],map_y=m[1]);w.writerow(r)
