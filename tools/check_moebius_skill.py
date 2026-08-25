#!/usr/bin/env python3
"""moebius-loop 스킬의 구조 불변식 검사.

사용: python3 tools/check_moebius_skill.py
종료코드: 0 = 전부 통과, 1 = 실패 있음
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / ".claude" / "skills" / "moebius-loop"
SK = PLUGIN / "skills" / "moebius-loop"

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
    check("T2a", "종료 정의가 세 조건을 한자리에서 말한다",
          "**종료 = 아래 셋을 다 만족하" in skill
          and "설계가 **2라운드 연속** 안 바뀐다" in skill
          and "적어도 한 번은 실제로 바뀌었다" in skill
          and "새로 생기지 않았다" in skill)
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
    check("T2p", "outputs.md가 종료 조건을 따로 말하지 않음(진실은 SKILL.md 한 곳)",
          '2라운드 연속 "없음"이면 끝난다' not in out
          and "종료 조건은 셋을 다 만족해야 한다" not in out)

    # --- 반론·전사·카드 (Task 3) ---
    check("T3a", "제약 공격 규칙이 렌즈뿐 아니라 사장님 관점까지",
          "사장님이 정한 것을 공격하는 반증" in skill)
    check("T3b", "없음 명시도 전사에 남긴다",
          '"없습니다"도 전사에 남긴다' in skill or "없습니다\"도 전사에 남긴다" in skill)
    check("T3c", "다른 눈 카드가 수렴 게이트에서 풀림",
          "미해결이 3라운드 연속 안 줄" in skill)

    # --- guardrails (Task 4) ---
    check("T4a", "판별 축이 원금 확정성",
          "돌려받는 금액이 미리 정해져 있지 않은 곳" in skill
          and "둘 다로 읽히면 걸리는 쪽으로 간다" in skill)
    check("E1", "라운드 경계 — 미루기 금지", "다음 라운드로 미루지 않는다" in skill)
    check("E2", "이미 처리되던 지적도 대장에", "현 설계가 이미 처리하고 있었다면 그것도 해결이다" in skill)
    check("E3", "사장님몫에 선택지 요구", "사장님이 실제로 고르실 선택지를 둘 이상" in skill)
    check("E4", "다른 눈 카드에 설계 변화 조건", "설계가 4라운드 연속 바뀌고 있으면" in skill)
    check("E5", "복원 게이트가 대조 가능성", "이 문서로 대장의 각 지적이 어디서 나왔는지" in skill)
    check("E6", "대장 번호 세기", "1번부터 최대 번호까지 빠짐없이" in skill)
    check("E7", "기록에 대한 추정도 금지", "안 온 것에 대해서는 원인도 내용도 추정하지 않는다" in skill)
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

    # --- 2026-08-25 사장님 요구사항 (Task 7) ---
    check("T7a", "outputs.md에 시각화 다이어그램(Mermaid) 섹션 존재",
          "## 시각화 다이어그램" in out and "mermaid" in out)
    check("T7b", "SKILL.md에 글과 그림 동시 산출 및 사전 보고(0.5단계) 명시",
          "글과 그림" in skill and ("사전" in skill or "0.5" in skill))
    check("T7c", "framework.md에 작전 기획 렌즈(CIA 208 / 국방부) 명시",
          "작전" in fw or "CIA" in fw or "국방부" in fw)
    check("T7d", "서브에이전트에 아부·동조 금지 지침 포함",
          (PLUGIN / "agents" / "red-team.md").exists()
          and ("아부" in (PLUGIN / "agents" / "red-team.md").read_text(encoding="utf-8")
               or "동조" in (PLUGIN / "agents" / "red-team.md").read_text(encoding="utf-8")
               or "거짓말" in (PLUGIN / "agents" / "red-team.md").read_text(encoding="utf-8")))

    # --- 금지 패턴 ---
    for label, text in (("SKILL.md", skill), ("framework.md", fw),
                        ("outputs.md", out), ("guardrails.md", grd)):
        check(f"X-{label}", f"{label}에 미정의 용어 '박스' 없음", "박스" not in text)

    # --- 전역 제약 ---
    n_lines = len(skill.splitlines())
    check("G1", "SKILL.md 500줄 이내", n_lines <= 500, f"{n_lines}줄")
    m = re.search(r"^description:\s*(.+)$", skill, re.M)
    check("G2", "description 254자 고정", m and len(m.group(1).strip()) == 254,
          f"{len(m.group(1).strip())}자" if m else "없음")

    import zipfile
    z = ROOT / "dist" / "moebius-loop.plugin"
    if not z.exists():
        check("G3", "배포 plugin 패키지가 라이브 파일과 동일", False, "plugin 없음(아직 재패키징 전이면 정상)")
    else:
        with zipfile.ZipFile(z) as zf:
            names = {n for n in zf.namelist() if not n.endswith("/")}
            expected = set()
            for f in PLUGIN.rglob("*"):
                if f.is_file() and ".DS_Store" not in f.name:
                    expected.add(f"moebius-loop/{f.relative_to(PLUGIN)}")
            same = names == expected and all(
                zf.read(n) == (PLUGIN.parent / n).read_bytes() for n in names)
        check("G3", "배포 plugin 패키지가 라이브 파일과 바이트 동일", same,
              f"zip 파일수={len(names)} 기대={len(expected)}")

    # --- 플러그인 구조 ---
    check("P1", ".claude-plugin/plugin.json 존재 및 name=moebius-loop",
          (PLUGIN / ".claude-plugin" / "plugin.json").exists()
          and json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text()).get("name") == "moebius-loop")

    agents_dir = PLUGIN / "agents"
    expected_agents = {"red-team.md", "user-advocate.md", "quality-reviewer.md",
                        "spec-compliance-reviewer.md", "fresh-eyes-reviewer.md"}
    found_agents = {f.name for f in agents_dir.glob("*.md")} if agents_dir.exists() else set()
    check("P2", "서브에이전트 5개 전부 존재", expected_agents <= found_agents,
          f"없음: {expected_agents - found_agents}")

    def agent_fm(name):
        fp = agents_dir / name
        if not fp.exists():
            return None
        s = fp.read_text(encoding="utf-8")
        m = re.match(r"\A---\n(.*?)\n---\n", s, re.S)
        return m.group(1) if m else None

    for fname in expected_agents:
        fm = agent_fm(fname)
        has_fields = fm is not None and all(f"\n{k}:" in ("\n" + fm) for k in ("name", "description", "model"))
        stem = fname[:-3]
        name_matches = fm is not None and re.search(rf"^name:\s*{re.escape(stem)}\s*$", fm, re.M) is not None
        referenced = f"@moebius-loop:{stem}" in skill
        check(f"P3-{fname}", f"{fname} frontmatter 완비 + name==파일명 + SKILL.md가 @참조함",
              has_fields and name_matches and referenced)

    check("P4", "red-team.md에 framework.md가 언급조차 되지 않음(격리가 문자열로도 안 새는지)",
          (agents_dir / "red-team.md").exists()
          and "framework.md" not in (agents_dir / "red-team.md").read_text(encoding="utf-8"))

    check("P5", "폴백 규칙이 호출 지점 4곳 전부에 있음(문자열 하나로는 안 셈)",
          skill.count("불러지지 않으면") >= 4)

    check("P6", "SKILL.md에 비용 인지 문구", "토큰" in skill and "비용" in skill)


    check("P8", "전사를 그대로 옮기라는 지시 유지",
          "요약하지 말고" in skill or "그대로 옮" in skill)

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
