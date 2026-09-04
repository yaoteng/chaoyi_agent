#!/usr/bin/env python3
"""校验 skills/ 下所有 SKILL.md 是否符合 Skills 1.0 frontmatter 规范。

用法:
    python scripts/validate_skills.py
退出码:
    0 = 全部通过
    1 = 存在缺失字段 / 解析失败的 Skill
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")

# 必填 frontmatter 字段；模板目录不参与校验
REQUIRED_FIELDS = ["name", "description", "version", "license", "compatible_hosts", "standards"]
SKIP_DIRS = {"_template"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str):
    """极简 YAML frontmatter 解析（仅支持本项目用到的 key: value / key: [a, b]）。"""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    body = m.group(1)
    data = {}
    for line in body.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        val = raw.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            items = [i.strip().strip('"').strip("'") for i in inner.split(",") if i.strip()]
            data[key] = items
        else:
            data[key] = val.strip().strip('"').strip("'")
    return data


def main():
    if not os.path.isdir(SKILLS_DIR):
        print(f"[x] 找不到 skills 目录: {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, d)) and d not in SKIP_DIRS
    )

    if not skill_dirs:
        print("[!] 没有发现可校验的 Skill（已跳过 _template）")
        return 0

    total = len(skill_dirs)
    failed = 0
    print(f"== 校验 {total} 个 Skill ==")

    for d in skill_dirs:
        path = os.path.join(SKILLS_DIR, d, "SKILL.md")
        if not os.path.isfile(path):
            print(f"  [x] {d}: 缺少 SKILL.md")
            failed += 1
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        fm = parse_frontmatter(text)
        if fm is None:
            print(f"  [x] {d}: 未找到合法的 YAML frontmatter（需以 --- 包裹）")
            failed += 1
            continue
        missing = [k for k in REQUIRED_FIELDS if not fm.get(k)]
        if missing:
            print(f"  [x] {d}: 缺字段 {missing}")
            failed += 1
            continue
        print(f"  [OK] {d}  (name={fm['name']}, v={fm['version']}, hosts={len(fm['compatible_hosts'])}种, standards={fm['standards']})")

    print("-" * 40)
    if failed:
        print(f"[FAIL] {failed}/{total} 个 Skill 未通过校验")
        return 1
    print(f"[PASS] 全部 {total} 个 Skill 通过 Skills 1.0 规范校验")
    return 0


if __name__ == "__main__":
    sys.exit(main())
