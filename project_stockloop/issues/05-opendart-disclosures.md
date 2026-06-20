# 05 · OpenDART 공시 수집 + DART 이벤트 모듈

**Labels**: needs-triage
**Type**: HITL (OpenDART API 키 발급 필요)

## Parent
[prd.md](../prd.md)

## What to build
OpenDART API로 유증·자사주·실적·수주·주요 경영이슈 공시를 수집해 `raw_disclosures`에 저장하고, 대시보드의 "DART 이벤트" 모듈에서 오늘의 주요 공시를 호재/악재 방향과 함께 표시한다.

## Acceptance criteria
- [ ] OpenDART API 키가 환경변수/시크릿으로 안전하게 주입된다
- [ ] 공시를 수집해 `raw_disclosures`에 저장한다(유증·자사주·실적·수주·경영이슈 분류)
- [ ] 대시보드 DART 이벤트 카드가 오늘 공시를 렌더한다
- [ ] API rate limit/에러에 대한 재시도·로깅이 있다
- [ ] 수집·파싱 단위 테스트가 통과한다

## Blocked by
- [01 · Walking skeleton](01-walking-skeleton.md)
