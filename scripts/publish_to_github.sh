#!/usr/bin/env bash
# 潮驿 Agent · 一键发布到 GitHub
# 在 Git Bash 中运行：bash scripts/publish_to_github.sh
# 前置：安装 GitHub CLI (https://cli.github.com/) 并先执行 `gh auth login`
set -uo pipefail

# 解析 gh 路径：优先 PATH，未写入 PATH 时回退到常见安装位置
if ! command -v gh >/dev/null 2>&1; then
  for cand in "C:/tools/gh_2.99.0_windows_amd64/bin/gh.exe" "$LOCALAPPDATA/Microsoft/WinGet/Packages"/*/gh.exe; do
    if [ -x "$cand" ]; then export PATH="$(dirname "$cand"):$PATH"; echo "    使用 gh: $cand"; break; fi
  done
fi

REPO_NAME="chaoyi_agent"
REPO_DESC="让每一个小社群都拥有数字社工 · 跨宿主开源 Skill 库（Skills 1.0 + MCP 0.4）· MIT"
TOPICS="ai-agents skills mcp open-source community developer-tools llm automation chinese agent-framework self-hosted"

echo "== 1/6 前置检查 =="
command -v git >/dev/null 2>&1 || { echo "  x 未安装 git"; exit 1; }
command -v gh  >/dev/null 2>&1 || { echo "  x 未安装 gh (GitHub CLI)，请先安装并 gh auth login"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "  x gh 未登录，请先运行 gh auth login"; exit 1; }

GH_USER=$(gh api user --jq .login)
echo "    已登录为 @$GH_USER"

# 确保 git 身份已配置——否则 commit 会失败，仓库变空壳（最常见卡点）
if [ -z "$(git config user.name)" ]; then
  git config user.name "$GH_USER"
  echo "    已设置 git user.name=$GH_USER"
fi
if [ -z "$(git config user.email)" ]; then
  GHE=$(gh api user --jq .email 2>/dev/null)
  [ -z "$GHE" ] && GHE="$GH_USER@users.noreply.github.com"
  git config user.email "$GHE"
  echo "    已设置 git user.email=$GHE"
fi

echo "== 2/6 初始化本地 git（若尚未） =="
if [ ! -d .git ]; then
  git init -b main
  git add -A
  git commit -q -m "chore: initial release v0.1.0 - Chaoyi Agent skill library"
  echo "    已 git init + 首次提交"
else
  echo "    已是 git 仓库，跳过 init"
  git add -A
  if git diff --cached --quiet; then
    echo "    无新改动，跳过提交"
  else
    git commit -q -m "chore: initial release v0.1.0 - Chaoyi Agent skill library"
    echo "    已提交暂存改动"
  fi
fi

echo "== 3/6 创建 GitHub 仓库（公开）并推送 =="
if gh repo view "$REPO_NAME" >/dev/null 2>&1; then
  echo "    仓库 $REPO_NAME 已存在，仅推送"
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$GH_USER/$REPO_NAME.git"
    echo "    已添加 origin -> https://github.com/$GH_USER/$REPO_NAME.git"
  fi
  git push -u origin main
else
  gh repo create "$REPO_NAME" --public --description "$REPO_DESC" --push --source . --remote origin
fi

echo "== 4/6 设置 Topics =="
for t in $TOPICS; do gh repo edit "$REPO_NAME" --add-topic "$t" >/dev/null 2>&1 || true; done
echo "    已设置 Topics: $TOPICS"

echo "== 5/6 打 tag + 创建 Release v0.1.0 =="
git tag -a v0.1.0 -m "Chaoyi Agent v0.1.0: 5 community skills + template" 2>/dev/null || true
git push origin v0.1.0 2>/dev/null || true
gh release create v0.1.0 --title "v0.1.0" \
  --notes "首发：5 个社群 Skill（入驻/议题/发布/翻译/致谢）+ 模板 + 索引。兼容 Skills 1.0 + MCP 0.4，跨宿主，MIT。" >/dev/null 2>&1 \
  || echo "    Release 已存在或创建失败（可稍后手动补）"

echo "== 6/6 完成 =="
echo "  [OK] 仓库已发布: https://github.com/$GH_USER/$REPO_NAME"
echo "       下一步：按 chaoyi_agent/潮驿Agent一周千星战术战略书.md 执行 D-1 与七日作战"
