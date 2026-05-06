# DND5R 职业/子职节奏榜

这是一个面向 D&D 5.5e / 2024 / 5R 的职业、子职与构筑评分仓库。评分文本以简体中文为主，目标是把官方、UA、合作方、第三方公开内容放在同一套标准下进行横向比较。

## 仓库内容

- `.codex`：项目级 Codex skills。这里保存评分流程、资料核查规则、文件结构、命名规则和 changelog 规则。
- `tools`：批量生成、校准或整理评分文件的本地脚本。这些脚本主要服务于已有工作流，不保证都是通用 CLI。
- `Rankings`：官方、UA、合作方与第三方公开内容的评分与评审产物。
- `DND5e_chm`：资料 submodule，指向 `https://github.com/DND5eChm/DND5e_chm`。用于核查最新 5.5e / 2024 内容，应保持更新。
- `DND2014_legacy`：资料 submodule，同样指向 `https://github.com/DND5eChm/DND5e_chm.git`，但固定在当前 revision。用于保留纯 5e 时代资料，尤其是未来复核 5e UA 子职；不要为了 5e UA 评审而更新它。

`homebrews` 目录不纳入本仓库。该目录目前属于个人创作与迭代区，不作为公开评分产物发布；与 homebrew 评审相关的流程规则仍保留在 `.codex` skills 中，方便本地使用。

## 初始化

克隆仓库后拉取 submodule：

```powershell
git clone --recurse-submodules git@github.com:royale011/DND5R_Rankings.git
```

如果已经普通克隆：

```powershell
git submodule update --init --recursive
```

更新最新资料时，只更新 `DND5e_chm`：

```powershell
git -C DND5e_chm pull
git add DND5e_chm
git commit -m "Update DND5e_chm submodule"
```

不要随手更新 `DND2014_legacy`。它的用途是保留当前 5e 时代资料快照。

## 如何运行官方评分

官方、UA、合作方、第三方公开内容的评分输出写入 `Rankings`。

推荐流程：

1. 使用 `.codex/skills/official-dnd-ranking-review/SKILL.md` 作为工作规则。
2. 先读 `Rankings/changelog.md`，确认当前评分标准和最近校准。
3. 用 `DND5e_chm` 核查职业、子职、专长、法术、物品、规则原文和中文译名。
4. 如需社区意见，必须确认评论讨论的是同一版本规则；不匹配的旧版评论只能作为背景，不可直接套用。
5. 修改对应的 `Rankings/[职业]/README.md`、子职文件或 `Rankings/构筑/*.md`。
6. 如果更新了标准、校准逻辑或大范围结论，把记录添加到 `Rankings/changelog.md` 文件开头。

可用脚本在 `tools` 下。常用示例：

```powershell
python .\tools\update_root_summary.py
python .\tools\rebuild_class_leaderboards_from_reviews.py
```

其他 `rewrite_*` 脚本多数是针对历史某一轮重写或校准的专用脚本。运行前先读脚本内容，确认它的目标文件和假设。

## 如何添加 Homebrew 内容

本仓库不会提交 `homebrews`。如果本地需要评审 homebrew，目录建议保持为：

```text
homebrews/
  [原始 homebrew txt / md / pdf 等]
  Rankings/
    changelog.md
    [职业或类型]/
      [子职名].md
      Archive/
```

新增 homebrew 原文后，使用 `.codex/skills/homebrew-dnd-ranking-review/SKILL.md` 作为工作规则。评审时仍要参考：

- `Rankings/changelog.md`
- 已有 `Rankings` 官方/合作方/第三方评分文件
- `DND5e_chm` 中的官方规则文本
- `homebrews/Rankings/changelog.md` 中的 homebrew 专用标准

Homebrew 文件如果同时有英文和中文，以中文作为 `原文` 归档内容，除非明确说明相反。

## 如何运行 Homebrew 评分

Homebrew 评分输出写入 `homebrews/Rankings`，不写入根 `Rankings`。

推荐流程：

1. 读取 `homebrews/Rankings/changelog.md` 和根 `Rankings/changelog.md`。
2. 读取当前 homebrew 原文。
3. 如果已有评审文件，比较当前中文原文和评审文件中的 `## 原文`。
4. 如果原文改变，先归档旧评审，再生成新评审。
5. 如果只是评分标准或文字表达改变，原文未变，可以直接原地更新，不必归档。
6. 核查 homebrew 提到的所有官方内容，不用记忆判断法术、专长、职业能力或怪物数据。
7. 在评审文件内写清 `修改建议`；不要维护 `homebrews/Rankings/README.md` 作为总建议文件。

Homebrew 评审必须包含 `原文`，并在需要时包含：

- `设计相关评分 - 个人期望`
- `修改建议 - 公开发布`
- `修改建议 - 个人意图`
- 改编来源核查，例如 `基于...改编`

## Homebrew 归档规则

当 homebrew 原文发生变化时，先把当前评审文件复制到：

```text
homebrews/Rankings/[职业或类型]/Archive/[子职名] - [YYYYMMDD HHMMSS].md
```

然后再生成新的评审文件。归档判断以“当前 homebrew 文件中的中文原文”和“评审文件 `## 原文` 区块”比较为准。

`homebrews/Rankings/changelog.md` 采用倒序记录：最新记录写在文件开头。

## 贡献评分更新

评分更新应遵守以下原则：

- 必须使用 `DND5e_chm` 核查当前规则文本和中文译名。
- 不要用模型记忆替代规则核查。
- 不要把 2014 特性误写到 2024 职业或子职中。
- `综合评分` 必须来自该文件的实际分项分析，不要只改排行榜。
- 如果更新排行榜，排行榜的等级和理由必须取自对应子职/构筑文件的 `综合评分` 表。
- 构筑目录只收录真正的多职业或跨系统构筑，不收录纯职业优化包。
- 官方、UA、合作方、第三方内容可以各自获得真实强度评分；但排行榜收录规则要按 skill 执行。
- 如果改变评分标准或校准逻辑，在 `Rankings/changelog.md` 文件开头新增记录。

提交前建议检查：

```powershell
git status --short
git diff --check
```

确认没有提交本地私有内容：

```powershell
git check-ignore -v homebrews homebrews\Rankings
```

## 贡献 Skill 更新

Skill 是本仓库评分一致性的核心。修改 `.codex/skills/*/SKILL.md` 时：

- 写清触发场景、输出路径、命名规则和禁止事项。
- 同步更新根 `README.md` 中对应的使用说明。
- 如果变更会影响既有评分标准，在对应 changelog 文件开头记录。
- 官方评分规则改动记录到 `Rankings/changelog.md`。
- Homebrew 评分规则改动记录到 `homebrews/Rankings/changelog.md`，但该文件本身不提交到本仓库。
- 不要让官方与 homebrew 输出路径混用。

Skill 更新后，至少抽查一个已有评分文件，确认新规则不会和当前文件结构冲突。
