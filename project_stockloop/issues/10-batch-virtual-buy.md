# 10 · 일배치 오케스트레이션 + 자동 가상매수

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
장 마감 후 일배치를 스케줄러(APScheduler/cron)로 실행한다 — 스캔→필터→점수→사유→상위 N(=20) 추천 확정. 추천 종목 전부를 당일 종가 기준으로 자동 가상매수해 `virtual_trades`에 진입가·당시 점수·engine_version과 함께 기록한다(선택 편향 제거).

## Acceptance criteria
- [ ] 스케줄러가 장 마감 후 전체 파이프라인을 순서대로 실행한다
- [ ] 상위 N=20 추천이 확정된다
- [ ] 추천 종목 전부가 당일 종가로 가상매수되어 `virtual_trades`에 기록된다
- [ ] 진입 시점에 당시 점수·engine_version이 함께 저장된다(재현성)
- [ ] 배치 실패 시 재실행 가능하고 멱등성이 보장된다
- [ ] 파이프라인 통합 테스트가 통과한다

## Blocked by
- [04 · 추가 상승 여력 점수 + 리스크 등급](04-upside-score-risk-grade.md)
- [09 · 추천 사유 생성 (Claude)](09-recommendation-rationale.md)
