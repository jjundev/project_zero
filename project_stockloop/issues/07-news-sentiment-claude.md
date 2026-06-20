# 07 · 뉴스 감성 점수 (Claude 분류) → 5축 점수 완성

**Labels**: needs-triage
**Type**: HITL (Claude API 키·비용 승인 필요)

## Parent
[prd.md](../prd.md)

## What to build
Claude API로 수집된 뉴스를 호재/악재/중립으로 분류해 "뉴스 감성" 하위 점수를 산출한다(폴백: 한국어 감성 사전). 이로써 total_force_score의 5개 하위 축(가격 모멘텀·거래량 검증·뉴스 연관성·뉴스 감성·추가 상승 여력)이 모두 완성된다.

## Acceptance criteria
- [ ] Claude API 키가 시크릿으로 주입되고 모델 ID가 설정값으로 외부화된다
- [ ] 뉴스가 호재/악재/중립으로 분류되어 감성 점수가 산출된다
- [ ] 한국어 감성 사전 폴백 경로가 존재한다(Claude 장애 시)
- [ ] 5개 하위 점수 전체가 가중합되어 완전한 total_force_score가 계산된다
- [ ] LLM 호출 비용/토큰이 로깅된다
- [ ] 분류·통합 테스트가 통과한다

## Blocked by
- [06 · 네이버 뉴스 수집 + 뉴스 연관성 점수](06-naver-news-relevance.md)
