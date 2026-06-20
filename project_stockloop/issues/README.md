# StockLoop 이슈 (트레이서 불릿 분해)

출처: [prd.md](../prd.md) · 전부 `needs-triage` 라벨. 각 슬라이스는 수집→저장→점수→API→UI를 관통하는 수직 슬라이스.

## 의존 순서

```
01 Walking skeleton
├─ 02 유니버스 + 유동성 필터
│  └─ 03 모멘텀 + 거래량 점수
│     ├─ 04 상승여력 점수 + 리스크 등급
│     │  ├─ 10 일배치 + 자동 가상매수 ──┐ (also needs 09)
│     │  └─ 13 급등주 스캐너            │
│     └─ 06 네이버 뉴스 + 연관성 [HITL] │
│        └─ 07 뉴스 감성 (Claude) [HITL]│
│           └─ 09 추천 사유 (Claude) ───┘
│                                       └─ 10 ─ 11 성과/판정 ─ 14 KPI 대시보드
│                                              └─ 12 백테스트 부트스트랩
├─ 05 OpenDART 공시 [HITL]
├─ 08 pytrends 관심도
└─ 15 법적 면책 문구
```

## 목록

| # | 제목 | 타입 | Blocked by |
|---|---|---|---|
| 01 | [Walking skeleton](01-walking-skeleton.md) | AFK | — |
| 02 | [유니버스 + 유동성 필터](02-universe-liquidity-filter.md) | AFK | 01 |
| 03 | [모멘텀 + 거래량 점수](03-momentum-volume-score.md) | AFK | 02 |
| 04 | [상승여력 점수 + 리스크 등급](04-upside-score-risk-grade.md) | AFK | 03 |
| 05 | [OpenDART 공시](05-opendart-disclosures.md) | HITL | 01 |
| 06 | [네이버 뉴스 + 연관성](06-naver-news-relevance.md) | HITL | 03 |
| 07 | [뉴스 감성 (Claude)](07-news-sentiment-claude.md) | HITL | 06 |
| 08 | [pytrends 관심도](08-pytrends-interest.md) | AFK | 01 |
| 09 | [추천 사유 (Claude)](09-recommendation-rationale.md) | AFK | 07 |
| 10 | [일배치 + 자동 가상매수](10-batch-virtual-buy.md) | AFK | 04, 09 |
| 11 | [성과 추적 + 성공/실패 판정](11-performance-verdict.md) | AFK | 10 |
| 12 | [백테스트 부트스트랩](12-backtest-bootstrap.md) | AFK | 10 |
| 13 | [급등주 스캐너](13-surge-scanner.md) | AFK | 04 |
| 14 | [KPI 대시보드 6카드](14-kpi-dashboard.md) | AFK | 11 |
| 15 | [법적 면책 문구](15-legal-disclaimer.md) | AFK | 01 |

## 권장 착수 순서

1. **01** (스택 증명) → **02 → 03 → 04** (점수 코어, AFK 연속)
2. 병렬 HITL 트랙: **05**(공시 키), **06→07**(뉴스 키), **08**(트렌드)
3. **09 → 10 → 11 → 14** (추천·검증·KPI)
4. **12**(백테스트), **13**(스캐너), **15**(면책) — 의존 충족 시 병렬
