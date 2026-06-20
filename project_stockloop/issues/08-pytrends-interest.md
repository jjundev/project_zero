# 08 · pytrends 검색 관심도 + graceful degradation

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
pytrends로 종목명·테마 키워드 검색 관심도를 일배치 수집해 `raw_trends`에 저장한다. 비공식 소스의 차단·rate-limit에 대비해 캐싱·재시도를 두고, 결손 시 해당 신호 가중치를 0으로 처리한다(graceful degradation). 대시보드의 Google Trends 모듈에서 관심도를 표시한다.

## Acceptance criteria
- [ ] pytrends로 검색 관심도를 수집해 `raw_trends`에 저장한다
- [ ] 일배치 캐싱 + 재시도/백오프가 동작한다
- [ ] 수집 실패 시 해당 신호 가중치 0 처리(graceful degradation)가 검증된다
- [ ] 대시보드 Google Trends 모듈이 관심도를 렌더한다
- [ ] 결손 시나리오 테스트가 통과한다

## Blocked by
- [01 · Walking skeleton](01-walking-skeleton.md)
