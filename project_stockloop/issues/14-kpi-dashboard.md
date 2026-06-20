# 14 · KPI 대시보드 6카드

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
요약 대시보드 상단에 6개 KPI 카드를 집계·노출한다 — 오늘 감지 후보 수 · 신규 가상매수 수 · 평균 예상 점수 · 오늘 공시 이벤트 수 · 실패 경고 수 · 최근 7일 성공률. "요약 → 상세 → 근거" 흐름의 진입점.

## Acceptance criteria
- [ ] 6개 KPI가 백엔드에서 집계되어 API로 제공된다
- [ ] 대시보드가 6개 KPI 카드를 렌더한다
- [ ] 최근 7일 성공률이 `virtual_trades` 판정에서 계산된다
- [ ] 데이터 없음(초기) 상태가 graceful하게 표시된다
- [ ] 집계 로직 단위 테스트가 통과한다

## Blocked by
- [11 · 성과 추적 + 성공/실패 판정](11-performance-verdict.md)
