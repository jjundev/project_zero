# 04 · 추가 상승 여력 점수 + 리스크 등급

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
규칙 기반으로 "추가 상승 여력" 하위 점수(52주 고점 대비 여력, 과열 차감)를 산출하고, 모든 추천에 병행 노출할 리스크 등급(High/Medium/Low)을 룰로 부여한다. High = 52주 고점 대비 +X% 이내 추격 AND 거래량 급증 동반, Medium = 둘 중 하나, Low = 해당 없음. 임계값은 부록 표로 관리한다.

## Acceptance criteria
- [ ] 추가 상승 여력 점수 산출식이 구현된다
- [ ] High/Medium/Low 리스크 룰이 구현된다
- [ ] 리스크 등급이 `analysis_results`에 저장된다
- [ ] 리스크 임계값이 설정값(부록 표)으로 외부화되어 있다
- [ ] 등급 경계 케이스 단위 테스트가 통과한다

## Blocked by
- [03 · 가격 모멘텀 + 거래량 검증 점수](03-momentum-volume-score.md)
