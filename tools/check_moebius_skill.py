#!/usr/bin/env python3
"""moebius-loop 스킬의 구조 불변식 검사.

사용: python3 tools/check_moebius_skill.py
종료코드: 0 = 전부 통과, 1 = 실패 있음
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SK = ROOT / ".claude" / "skills" / "moebius-loop"

results = []


def check(cid, desc, ok, detail=""):
    results.append((cid, desc, bool(ok), detail))


def main():
    skill = (SK / "SKILL.md").read_text(encoding="utf-8")
    fw = (SK / "references" / "framework.md").read_text(encoding="utf-8")
    out = (SK / "references" / "outputs.md").read_text(encoding="utf-8")
    grd = (SK / "references" / "guardrails.md").read_text(encoding="utf-8")

    # --- frontmatter ---
    m = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    check("FM1", "frontmatter 블록 존재", m is not None)
    if m:
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        check("FM2", "name == moebius-loop", name and name.group(1).strip() == "moebius-loop")
        check("FM3", "name 문자셋 [a-z0-9-]", name and re.fullmatch(r"[a-z0-9-]+", name.group(1).strip()))
        check("FM4", "name 예약어 없음", name and not re.search(r"anthropic|claude", name.group(1)))
        check("FM5", "description 1~1024자", desc and 0 < len(desc.group(1).strip()) <= 1024,
              f"len={len(desc.group(1).strip())}" if desc else "")
        check("FM6", "description XML 태그 없음", desc and not re.search(r"<[^>]+>", desc.group(1)))

    # --- 참조 경로 ---
    refs = sorted(set(re.findall(r"references/[a-z_]+\.md", skill)))
    missing = [r for r in refs if not (SK / r).exists()]
    check("REF1", "SKILL.md가 가리키는 references 전부 실재", not missing, f"없음: {missing}")

    # --- 종료 정의 (Task 2) ---
    check("T2a", "종료를 설계 변화로 잰다", "설계가 2라운드 연속 안 바뀌" in skill)
    check("T2b", "옛 종료 정의(새 번호 2라운드 연속) 제거됨",
          "새 번호가 **2라운드 연속** 하나도 안 붙는 것" not in skill)
    check("T2c", "사문 규칙(3라운드 전 수렴 선언 금지) 제거됨",
          "3라운드를 돌기 전에는 수렴을 선언하지 않는다" not in skill)
    check("T2d", "대장 상태에 재개 있음", "재개" in skill and "재개" in out)
    check("T2e", "대장 상태에 사장님몫 있음", "사장님몫" in skill)
    check("T2f", "자기채점 한계를 규칙이 아니라 사장님 눈으로 푼다고 명시",
          "자기채점을 이기는 건 규칙이 아니라 사장님 눈이다" in skill)
    check("T2g", "렌즈 미충족은 지적이 아니라고 명시", "렌즈 미충족은 지적이 아니다" in skill)
    check("T2h", "라운드별 설계 변화 기록 지시", "설계 변화:" in skill)
    check("T2i", "outputs.md 대장에 등급 열", "등급" in out)
    check("T2j", "지적을 안 고칠 셋째 문이 있음",
          "고쳐도 쓰는 사람에게 이득이 없다고 판단해 안 고치거나" in skill)
    check("T2k", "종료하려면 실제 설계 변화가 최소 1회 필요",
          "적어도 한 번은 실제로 바뀌어야 한다" in skill)
    check("T2l", "대장 상태에 안고침 있음", "안고침" in skill and "안고침" in out)
    check("T2m", "1차 기획 라운드는 계수에서 제외",
          "1차 기획을 만든 라운드는 계산에서 뺀다" in skill)
    check("T2n", "안고침·사장님몫이 생긴 라운드는 조용한 라운드가 아님",
          '그 라운드는 "없음"으로 세지 않는다' in skill)
    check("T2o", "사장님몫도 사유 기록을 요구", "왜 사장님 몫인지 한 줄을 반드시 적고" in skill)
    check("T2p", "outputs.md 종료 조건이 브레이크 반영본",
          "종료 조건은 셋을 다 만족해야 한다" in out)

    # --- 반론·전사·카드 (Task 3) ---
    check("T3a", "제약 공격 규칙이 렌즈뿐 아니라 사장님 관점까지",
          "사장님이 정한 것을 공격하는 반증" in skill)
    check("T3b", "없음 명시도 전사에 남긴다",
          '"없습니다"도 전사에 남긴다' in skill or "없습니다\"도 전사에 남긴다" in skill)
    check("T3c", "다른 눈 카드가 수렴 게이트에서 풀림",
          "미해결이 3라운드 연속 안 줄면" in skill)

    # --- guardrails (Task 4) ---
    check("T4a", "판별 문장이 SKILL.md에 있음",
          "값이 오르내리는 무언가에 돈을 넣거나 뺄지" in skill)
    check("T4b", "guardrails.md에 발동 판정이 남아있지 않음",
          "발동 조건" not in grd and "돈을 넣거나 뺄지" not in grd)
    check("T4f", "4단계 대조 결과를 통과 시에도 기록", "투자 대조:" in skill and "투자 대조:" in out)
    check("T4g", "아티팩트 템플릿에 투자 판정 칸", "투자 판정:" in out)
    check("T4h", "렌즈 건너뛰기와 투자 판정을 구분", "렌즈를 건너뛰는 것과 투자 판정은 다른 문제다" in fw)
    check("T4c", "투자 판정 결과를 기록", "투자 판정:" in skill)
    check("T4d", "4단계는 체크리스트 0번 고정 항목", "0번 고정 항목" in skill)
    check("T4e", "뒤집기는 한 방향만", "안 걸림 → 걸림" in skill)

    # --- 복원 (Task 5) ---
    check("T5a", "복원 점검 절 존재", "## 복원 점검" in skill)
    check("T5b", "복원 점검이 0단계보다 앞", 
          ("## 복원 점검" in skill and "### 0. 입력" in skill
           and skill.index("## 복원 점검") < skill.index("### 0. 입력")))
    _bstart = skill.find("━━━ 이어하기 ━━━")
    _warn = skill.find("⚠️ 새 대화창이면 이 블록만으로는 복원")
    _topic = skill.find("\n주제: ")
    check("T5c", "경고가 이어하기 블록 안, 주제 줄보다 앞에 있음",
          -1 < _bstart < _warn < _topic,
          f"block={_bstart} warn={_warn} topic={_topic}")
    check("T5d", "위조 금지 경계선 명시", "지어내지 않는다" in skill)
    check("T5e", "framework §13에 단서", "전달만 안 된 것" in fw)
    check("T5f", "outputs.md 트립와이어", "인용할 원문이 손에 없으면" in out)

    # --- framework (Task 6) ---
    check("T6a", "§11 두 경고의 우선순위 명시", "⚠B가 이긴다" in fw)
    check("T6b", "범위표 아래 예시 문장 보존(감량 금지)",
          "오프라인 매장 운영, 조직 관리, 화면 UX" in fw)

    # --- 금지 패턴 ---
    for label, text in (("SKILL.md", skill), ("framework.md", fw),
                        ("outputs.md", out), ("guardrails.md", grd)):
        check(f"X-{label}", f"{label}에 미정의 용어 '박스' 없음", "박스" not in text)

    failed = [r for r in results if not r[2]]
    for cid, desc, ok, detail in results:
        mark = "ok  " if ok else "FAIL"
        line = f"{mark} {cid:8} {desc}"
        if detail and not ok:
            line += f"  [{detail}]"
        print(line)
    print(f"\n{len(results) - len(failed)}/{len(results)} 통과")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
