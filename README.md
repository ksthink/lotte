# 롯데월드 11/23 동선 판단기

https://ksthink.github.io/lotte/

- `index.html` — 판단기 페이지
- `data/attractions.json`, `data/attractions.csv` — 어트랙션 46종 (공식 사이트 11/18 기준 + 가이드맵 좌표·소개)
- `data/performances.json` — 11/23 공연 타임테이블 (공식 사이트 11/18 조회)
- `data/lotteworld-graph.json`, `data/travel-minutes.csv` — 가이드맵 좌표로 만든 이동 그래프와 이동시간(분)
- `data/build_graph.py`, `data/build_attractions.py` — 생성 스크립트(가이드맵 PDF와 조회 결과가 있어야 다시 돌릴 수 있음)

운영시간·상태는 조회한 날의 값입니다. 실시간 대기와 운휴는 공식 사이트/앱이 기준입니다.
이동시간과 예상 대기는 근사값입니다.
