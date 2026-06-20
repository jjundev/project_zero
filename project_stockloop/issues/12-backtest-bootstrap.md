# 12 · 과거 백테스트 부트스트랩

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
가상매수는 전향적이라 1년 수익률·성공률 KPI·진화가 누적 데이터를 기다려야 한다. 이를 해소하기 위해 pykrx 과거 일봉으로 과거 N개월 구간을 시뮬레이션해(현 엔진 버전 기준) 성과 지표(총수익률·MDD·승률 등)를 산출하는 백테스트 경로를 제공한다. look-ahead bias를 회피한다.

## Acceptance criteria
- [ ] 과거 N개월 일봉으로 추천·가상매수를 재현하는 백테스트 러너가 동작한다
- [ ] look-ahead bias 회피(분석 시점 이후 데이터 미사용)가 보장된다
- [ ] 총수익률·MDD·승률 등 성과 지표가 산출된다
- [ ] 백테스트 결과를 엔진 버전과 연결해 저장한다
- [ ] 재현성 테스트(동일 입력 → 동일 결과)가 통과한다

## Blocked by
- [10 · 일배치 오케스트레이션 + 자동 가상매수](10-batch-virtual-buy.md)
