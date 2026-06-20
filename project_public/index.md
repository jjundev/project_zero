# 문서 인덱스

> **버전:** v0.2 — 2026-05-29
> **단일 진실 소스:** [product_overview_4th.md](product_overview_4th.md) (v2.3)
> **목적:** 4th가 인용·함의한 부속서·명세서·후보 실험 design doc의 작성 상태와 우선순위 추적.

---

## §0 단일 진실 소스

본 인덱스는 `product_overview_4th.md`를 위성 메타 추적용으로 보조한다. 4th는 인용 대상이며 인덱스의 작성 후보가 아니다. 인덱스 → 4th 단방향 인용만 유지하며, 4th 본문에 인덱스를 인용하지 않는다.

| 문서 | 버전 | 역할 |
|---|---|---|
| [product_overview_4th.md](product_overview_4th.md) | v2.3 | 제품 방향 PRD. 모든 부속서·명세서가 본 문서를 인용한다. |

---

## §1 작성 순서

작성 트리거 4단계로 묶어 한 묶음씩 진행한다. 묶음 내 파일은 동시 작성 가능. 각 트리거는 4th §16 Phase 전략과 연동된다.

1. **빌드 시작 전**: A(4건) + C 핵심 2건(`analytics_event_schema.md`, `copy_inventory.md`)
2. **Phase 1-A Gate 통과 전**: B(3건)
3. **Phase 1-B 출시 전**: C 나머지 2건(`data_source_spec.md`, `phase1b_universe_spec.md`)
4. **Candidate Experiment 1-C 진입 시**: D 해당 후보의 design doc

---

## §2 상태 enum 정의

| 상태 | 의미 |
|---|---|
| `existing` | 파일이 존재하고 내용이 확정된 상태 |
| `planned` | 파일 미존재. 작성 트리거가 미도달이거나, 도달 후 아직 작성 시작 전 |
| `draft` | 파일은 존재하나 내용 미완. 검토·보강 진행 중 |
| `blocked` | 외부 의존(게이트 통과·데이터 확보 등) 충족 대기 중. 후보 실험에서 주로 발생 |
| `dropped` | 4th §16 후보 표에서 해당 항목이 제거되었거나 폐기로 결정됨 |

상태 전이는 §7 갱신 정책 트리거 2번에 따른다.

---

## §3 카테고리 A — 4th가 파일명을 박은 부속서

작성 트리거: **빌드 시작 전**. `legal_release_checklist.md`와 `forbidden_phrase_lint.md`는 `copy_inventory.md`를 입력으로 받는다.

| 파일 | 역할 | 상태 | 4th 인용 | 비고 |
|---|---|---|---|---|
| `critical_data_gate_decision_table.md` | 약한 주의 신호와 critical 시장조치 매핑·enumeration·Gate 0 판정표 | planned | §9.1, §16 Gate 0 보강 | 판정 데드라인 2026-06-30 |
| `operations_runbook.md` | 데이터 갱신 지연 알람, 정보 오류 신고 SLA, 비상 운영 흐름 | planned | §9.2, §11.2 | — |
| `legal_release_checklist.md` | §15.3 법무 검토 패키지 sign-off 양식, LLM fallback 3자 검증 문서 | planned | §13.4, §15.3 | `copy_inventory.md` 후행 |
| `forbidden_phrase_lint.md` | §18 금지/허용 표현 자동 lint 규칙·검사 흐름 | planned | §16 Gate 1, Decision #57 | `copy_inventory.md` 후행 |

---

## §4 카테고리 B — 4th가 함의한 부속서

작성 트리거: **Phase 1-A Gate 통과 전**. 4th §16 마지막 단락("외부 출시 가능한 PRD로 전환하기 전에는 …")을 근거로 한다.

| 파일 | 역할 | 상태 | 4th 인용 | 비고 |
|---|---|---|---|---|
| `screen_state_spec.md` | 화면 상태 명세서. Gate 1 통과 조건 "화면 상태 명세서 초안 존재" | planned | §16 Gate 1 보강 | — |
| `dart_disclaimer.md` | DART 정확성·완전성·최신성 비보장 문구 + 사용자 노출 위치 매핑 | planned | §17 금지 목록, §15.3 | — |
| `rule_quality_audit.md` | 내부 룰 audit 샘플 기준 — §13.1 "사용자 이벤트와 분리된 내부 배치 리포트" 정의 | planned | §13.1, §16 | — |

---

## §5 카테고리 C — 빌드 진입 전 명세

C는 작성 트리거가 2종으로 갈리므로 트리거 컬럼을 추가로 둔다.

| 파일 | 역할 | 상태 | 4th 인용 | 작성 트리거 | 비고 |
|---|---|---|---|---|---|
| `analytics_event_schema.md` | §13 이벤트 이름·속성·집계·90일 보존 정책의 엔지니어링 스키마 | planned | §13.1~§13.4 | 빌드 시작 전 | A의 `legal_release_checklist.md`와 짝 |
| `copy_inventory.md` | 탐색 관점·조건·결과·상세·관찰·금지/허용 표현의 전수 카피 모음 | planned | §8, §10, §11, §12, §18 | 빌드 시작 전 | A의 `legal_release_checklist.md`·`forbidden_phrase_lint.md`와 짝 |
| `data_source_spec.md` | DART/OpenDART 데이터 모델, 산식 임시 기본값, 갱신 파이프라인, fallback 규칙 | planned | §9.2 | Phase 1-B 출시 전 | critical 시장조치 데이터 세트 확정 후 보강 |
| `phase1b_universe_spec.md` | Phase 1 유니버스(코스피·코스닥 − 거래정지·관리·상폐사유) 운영 룰 | planned | §9.2 | Phase 1-B 출시 전 | `data_source_spec.md`와 짝 |

---

## §6 카테고리 D — Candidate Experiment design doc

작성 트리거: **해당 1-C 후보 진입 시**. 기존 2건은 게이트 진입 가능 상태.

| 파일 | 역할 | 상태 | 4th 인용 | 비고 |
|---|---|---|---|---|
| [saju_exploration_question_design.md](saju_exploration_question_design.md) | 1-C-Saju 후보 실험 상세 설계 | existing | §8.5 | 게이트 진입 시 `saju_legal_gate.md` 신설 후보 |
| [natural_language_condition_input_design.md](natural_language_condition_input_design.md) | 1-C-NL 후보 실험 상세 설계 | existing | §8.6 | LLM fallback 사용 시 `llm_fallback_signoff.md` 신설 후보 |
| `1c_price_design.md` | 1-C-Price 가격 변동 조건 검토 | blocked | §16 후보 표 | KRX 데이터 이용 조건 통과 후 |
| `1c_observe_design.md` | 1-C-Observe 관찰 루프 강화 | blocked | §16 후보 표 | 다시 보기 재방문 수요 확인 후 |
| `1c_account_design.md` | 1-C-Account 계정·동기화 검토 | blocked | §16 후보 표 | 로컬 저장 한계가 병목으로 확인 후 |

---

## §7 참고 자료(외부)

4th와 별도로 루트에 존재하는 디렉터리. 인덱스의 의무 관리 범위 밖이지만 위치 추적용으로 표기한다.

| 디렉터리 | 용도 | 4th 관련성 |
|---|---|---|
| `STT/` | 용도 미확인, 인덱스 관리 범위 밖 | — |
| `docs/` | 사주명리학 외부 연구 자료 | 1-C-Saju 후보 실험 진입 시 참조 가능 |
| `study_stock/` | 용도 미확인, 인덱스 관리 범위 밖 | — |
| `reports/` | 격주 미팅 진행 보고서·발표 자료 누적 위치, 인덱스 관리 범위 밖 | 4th를 인용하나 부속서·명세서 아님 |
| `wireframes/` | 화면 wireframe 초안 누적 위치, 인덱스 관리 범위 밖 | §3 카테고리 B `screen_state_spec.md` 작성 시 입력 자료 |
| `presentations/` | stakeholder onboarding deck 누적 위치, 인덱스 관리 범위 밖 | 4th 정수 소개, 시간 무관 |

`prd_archive/`는 인덱스에서 제외한다.

---

## §8 갱신 정책

- **갱신 주체**: PM 책임자(신현준). 4th §16 Gate 0 보강과 동일 owner.
- **갱신 트리거**:
  1. 새 파일이 4th에서 신규 인용될 때
  2. 기존 파일의 상태 전이(`planned` → `draft` → `existing`, 또는 `blocked` → `planned`)
  3. 4th의 §16 Phase 전략 표 변경 시
  4. 4th v2.x bump 시 §0의 4th 버전 라인 동기화
  5. 후보 실험이 영구 dropped되는 경우(4th §16 후보 표에서 해당 항목 제거 또는 dropped 표기) 해당 D 카테고리 entry를 인덱스에서 제거하거나 `dropped` 상태로 표기
- **bump 단위**: 위 트리거 1건 이상 발생 시 minor bump(`v0.x` → `v0.(x+1)`). 카테고리 신설·구조 변경 시 major bump.

---

## §9 변경 이력

- **v0.2 — 2026-05-29**: §7 참고 자료(외부)에 `reports/`·`wireframes/`·`presentations/` 3개 디렉터리 추가. 인덱스 관리 범위는 그대로 유지하되 위치 추적성 확보.
- **v0.1 — 2026-05-28**: 신설. 4th v2.3 기준 A(4)/B(3)/C(4)/D(5) 카테고리 16개 파일 등록.
