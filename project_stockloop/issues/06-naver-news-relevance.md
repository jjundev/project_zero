# 06 · 네이버 뉴스 수집 + 뉴스 연관성 점수

**Labels**: needs-triage
**Type**: HITL (네이버 검색 API 키 발급 필요)

## Parent
[prd.md](../prd.md)

## What to build
네이버 **공식 검색 API(뉴스)**로 종목 뉴스(제목·요약·시각·출처·키워드)를 수집해 `raw_news`에 저장하고(일반 페이지 크롤링 금지), 종목·키워드 매칭 빈도 기반 "뉴스 연관성" 하위 점수를 산출해 total_force_score에 통합한다.

## Acceptance criteria
- [ ] 네이버 검색 API 키가 시크릿으로 주입된다
- [ ] 뉴스를 수집해 `raw_news`에 저장한다(제목·요약·시각·출처·키워드)
- [ ] 종목·키워드 매칭 빈도 기반 연관성 점수가 산출된다
- [ ] 연관성 점수가 total_force_score 가중합에 반영된다
- [ ] API 일 한도/에러 처리(재시도·백오프)가 있다
- [ ] 점수 산출 단위 테스트가 통과한다

## Blocked by
- [03 · 가격 모멘텀 + 거래량 검증 점수](03-momentum-volume-score.md)
