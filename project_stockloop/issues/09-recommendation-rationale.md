# 09 · 추천 사유 생성 (Claude)

**Labels**: needs-triage
**Type**: AFK

## Parent
[prd.md](../prd.md)

## What to build
완성된 구조화 신호(5개 하위 점수·공시·리스크 등급 등)를 입력으로 Claude API가 추천 사유를 자연어 문장으로 생성한다. 메인 화면 문구는 짧고 즉시 이해 가능하게, 상세는 깊게. 생성된 사유는 `analysis_results`에 저장된다.

## Acceptance criteria
- [ ] 구조화 신호 → 자연어 사유 생성 프롬프트가 구현된다
- [ ] 짧은 요약 + 상세 사유 두 형태가 생성된다
- [ ] 사유가 `analysis_results`에 저장된다
- [ ] 신호 누락/LLM 장애 시 폴백(템플릿 문구)이 있다
- [ ] 생성 결과 스냅샷 테스트가 통과한다

## Blocked by
- [07 · 뉴스 감성 점수 (Claude 분류)](07-news-sentiment-claude.md)
