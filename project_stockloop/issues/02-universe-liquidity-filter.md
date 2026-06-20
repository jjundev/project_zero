# 02 · 전체 유니버스 수집 + 유동성 필터

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
KOSPI+KOSDAQ 전체 종목 메타데이터(`stocks`: 코드·종목명·업종·섹터·시장구분·시총)와 일봉을 수집하고, 직전 20거래일 평균 거래대금 하위 30%를 제외하는 유동성 필터를 적용한다. 필터를 통과한 유니버스가 후속 점수 단계의 입력이 된다.

## Acceptance criteria
- [ ] pykrx로 KOSPI+KOSDAQ 전체 종목 메타데이터를 `stocks`에 적재한다
- [ ] 전체 유니버스의 일봉을 `raw_prices`에 저장한다
- [ ] 직전 20거래일 평균 거래대금 하위 30% 제외 필터가 동작한다
- [ ] 필터링된 유니버스 목록을 조회할 수 있다
- [ ] 필터 경계값(하위 30%) 단위 테스트가 통과한다

## Blocked by
- [01 · Walking skeleton](01-walking-skeleton.md)
