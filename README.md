# 롯데월드 11/23 동선 판단기

https://ksthink.github.io/lotte/

- `index.html` — 판단기 페이지
- `data/lotteworld-graph.json` — 2026 공식 가이드맵 PDF 마커 좌표로 만든 이동 그래프(노드·간선·이동시간)
- `data/travel-minutes.csv` — 장소 간 이동시간(분) 표
- `data/build_graph.py` — 그래프 생성 스크립트

이동시간은 근사값입니다. 가이드맵이 조감도라 축척이 일정하지 않고, 매직아일랜드 축척과 다리 이동시간은 가정값입니다.
