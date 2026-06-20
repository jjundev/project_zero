# 03 · 가격 모멘텀 + 거래량 검증 점수

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
규칙 기반 정량식으로 두 개의 하위 점수를 산출한다 — 가격 모멘텀(N일 수익률·이평 이격·신고가 근접도)과 거래량 검증(거래대금 급증 배수, 평소 대비 z-score). 두 점수를 `total_force_score`의 부분 가중합으로 결합하고 `analysis_results`에 하위 점수와 함께 저장한다.

## Acceptance criteria
- [ ] 가격 모멘텀 점수 산출식이 구현된다
- [ ] 거래량 검증 점수 산출식이 구현된다
- [ ] 두 하위 점수가 가중치로 결합되어 부분 total_force_score가 계산된다
- [ ] 하위 점수가 `analysis_results`에 개별 컬럼으로 저장된다
- [ ] 사용된 가중치가 `engine_versions` 스냅샷에서 읽힌다
- [ ] 각 산출식의 단위 테스트가 통과한다

## Blocked by
- [02 · 전체 유니버스 수집 + 유동성 필터](02-universe-liquidity-filter.md)
