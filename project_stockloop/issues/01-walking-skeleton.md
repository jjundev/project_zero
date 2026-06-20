# 01 · Walking skeleton — pykrx 1종목 end-to-end

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
스택 전체를 관통하는 최소 트레이서 불릿. 고정한 1종목에 대해 pykrx로 일봉을 받아 `raw_prices`에 저장하고, 임시(trivial) 모멘텀 점수를 계산해 `analysis_results`에 적재한 뒤, `GET /recommendations` API로 노출하고, React 대시보드가 그 1행을 렌더한다. 데이터 수집→저장→점수→API→UI가 한 줄로 연결되어 돌아가는 것을 증명한다.

## Acceptance criteria
- [ ] Python 백엔드 + PostgreSQL + React 프론트 스캐폴드가 로컬에서 기동된다
- [ ] pykrx로 1종목 일봉을 받아 `raw_prices`에 저장한다
- [ ] 임시 점수를 계산해 `analysis_results`에 저장한다(engine_version 컬럼 포함)
- [ ] `GET /recommendations`가 해당 종목 1건을 JSON으로 반환한다
- [ ] 대시보드가 추천 1행(종목명·총점)을 렌더한다
- [ ] end-to-end smoke 테스트 1개가 통과한다

## Blocked by
- None - can start immediately
