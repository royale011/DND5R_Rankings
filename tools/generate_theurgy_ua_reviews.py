from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_SCRIPT = ROOT / "tools" / "generate_theurgy_official_reviews.py"
PARTNER_SCRIPT = ROOT / "tools" / "generate_theurgy_partner_reviews.py"
OUT = ROOT / "Rankings" / "法师" / "神圣奇术"
CHANGELOG = ROOT / "Rankings" / "changelog.md"

official_spec = importlib.util.spec_from_file_location("theurgy_official", OFFICIAL_SCRIPT)
gen = importlib.util.module_from_spec(official_spec)
official_spec.loader.exec_module(gen)

partner_spec = importlib.util.spec_from_file_location("theurgy_partner", PARTNER_SCRIPT)
partner = importlib.util.module_from_spec(partner_spec)
partner_spec.loader.exec_module(partner)


UA_DOMAINS = [
    {
        "name": "奥秘领域（UA）",
        "ranks": ["S-", "S", "S+", "S+"],
        "summary": "UA奥秘领域比正式奥秘更适合神圣奇术法师：它给反魔法、法术调校和高环法师法术选择。真正危险点仍是14级提前取得领域17级能力后，可能通过多职业法术位规则提前持有并最终施放高环法师法术。",
        "details": [
            "3级阶段主要是奥秘熟练、法师戏法/法术入口和`神圣奥能`；低级强度仍由法师底盘与少量奥术工具支撑。",
            "6级取得UA奥秘3级非引导收益后，法师的奥术辨识和施法调校能力更稳定，但与法师本身生态有重叠。",
            "10级若取得驱散复原或类似反魔法/治疗串联，神圣奇术法师可把救援、解除和反制做成更高效回合。",
            "14级提前取得UA奥秘17级高环法师法术选择，是全表警戒点。即使14级纯法师不能施放8/9环，后续多职业法术位仍可能兑现，故T3/T4按S+风险处理。",
        ],
        "reasons": [
            "低级主要是法师底盘、`神圣奥能`和奥术工具，强但未破界，评S-。",
            "中期`法术反制`/`解除魔法`生态、施法调校和法师底盘叠加，达到S。",
            "14级提前取得高环法师法术选择并产生多职业法术位滥用风险，升S+。",
            "终局继续保有反魔法、调校和高环法术选择优势，保持S+。",
        ],
    },
    {
        "name": "坟墓领域（UA）",
        "ranks": ["A+", "S", "S", "S"],
        "summary": "UA坟墓领域把正式版的单次易伤窗口改成更泛用的附赠动作压制。接到神圣奇术法师后，它能让法师主动作继续施法，同时用引导奥秘让敌人攻击和豁免处于劣势，动作经济非常优秀。",
        "details": [
            "3级获得UA版`往墓之途`后，附赠动作压低目标攻击和豁免，可直接服务法师控制法术；1-2级仍是普通法师，所以T1不按全程S。",
            "6级取得生死轮回等非引导收益后，法师获得少量暗蚀收割和濒死治疗强化，补出牧师式救援。",
            "10级反重击类能力接入后，法师不仅能让敌人豁免变差，还能抹掉首领暴击峰值，团队容错很高。",
            "14级死灵扩展/死亡主题终局提升上限；它强在关键轮压制，不是常驻全队数学，因此不升S+。",
        ],
        "reasons": [
            "3级后附赠动作压制很强，但T1含1-2级普通法师，综合A+。",
            "中期附赠动作劣势让法师主动作继续施放控制，成品强度达到S。",
            "高环法师控制叠反重击和豁免压制，继续S。",
            "终局仍是强关键轮引擎，但资源和目标限制阻止S+。",
        ],
    },
    {
        "name": "保护领域（5E UA）",
        "ranks": ["A+", "S-", "S-", "S-"],
        "summary": "保护领域给神圣奇术法师贴身护卫、反应施加劣势和防护法术。问题是法师不想长期站在队友5尺内当护卫，且它的保护多处理攻击命中，不处理高Tier最危险的豁免、控制和现实改写。",
        "details": [
            "3级按兼容补丁取得旧1级防护包和引导奥秘；`信仰之盾`类反应保护可用，但要求站位靠近被保护者。",
            "6级取得保护领域3级非引导收益后，法师可以用反应帮队友挡一次攻击；这和`护盾术`、`法术反制`等反应竞争明显。",
            "10级治疗回流或防护串联能补续航，但治疗动作仍会挤压法师控制回合。",
            "14级可变抗性/转移抗性是好终局防御，但转移吃动作，且不解决控制、豁免失败或反魔法。",
        ],
        "reasons": [
            "低级防护包有用，但站位和反应竞争明显，评A+。",
            "中期领域法术与反应保护接到法师底盘，达到S-；不是全队数学破界。",
            "高环仍能保护关键队友，但主要危险常来自豁免/控制/法术，保持S-。",
            "终局抗性转移好用但动作慢、范围有限，维持S-。",
        ],
    },
    {
        "name": "城市领域（5E UA）",
        "ranks": ["A", "S-", "S-", "S-"],
        "summary": "城市领域是战役标签极强的神圣奇术映射。默认启用城市规则、现代风格法术和科技魔法后，它能给法师城市设施、交通和科技法术入口；但神圣奇术不会取得领域中的武器熟练，所以枪械熟练不能转入法师。离开现代城市环境时，大量子职增量会消失。",
        "details": [
            "3级才取得旧1级/2级城市包：`开关术`、载具/城市社交和`城市之魂`等内容。这些都强烈依赖城市设施；其中枪械熟练属于武器熟练，按神圣奇术规则不转入法师。",
            "6级城市察觉/洞悉专精能让法师成为都市调查核心，但这不是地城、荒野或异界通用能力。",
            "10级科技法术和设施互动继续扩宽解题面，若战役有网络、公共交通、电子设备、安防系统和现代基础设施，这些法术作为法师法术写入法术书后，实际更像都市奥术黑客工具。",
            "14级后若取得城市传送/公共交通调度，终局能改写都市行动半径；但这是场景S-，不是所有战役S。",
        ],
        "reasons": [
            "1-2级无子职，3级城市工具上线后仍吃环境，评A。",
            "中期现代城市战役中科技法术、设施控制和法师法术书结合很强；枪械熟练不转入法师，且通用性不足，所以是S-而非S。",
            "高环继续作为都市调查/设施解题者，现代法术作为法师法术的价值很高；非城市环境掉档明显，保持S-。",
            "终局城市交通/设施调度可改变战役节奏，都市桌为S-；离开城市会下滑。",
        ],
    },
]

SPELL_FOCUS = {
    "奥秘领域（UA）": "领域法术与反魔法工具非常适合神圣奇术法师，尤其是`法术反制`、`解除魔法`和施法调校；与法师本表有重叠，但重叠换来更强的反魔法稳定性。",
    "坟墓领域（UA）": "领域法术包偏死亡、反重击、濒死救援和死灵扩展。真正价值不是伤害，而是附赠动作压低敌方攻击/豁免，让法师控制更容易兑现。",
    "保护领域（5E UA）": "领域法术包含`援助术`、`缓慢术`、`欧提路克弹力法球`、`力场墙`等强防护/分隔工具；对法师而言部分与本表重叠，但仍提供牧师化防线和保护主题。",
    "城市领域（5E UA）": "领域法术包依赖城市规则、现代风格法术和科技魔法：都市设施、电子设备、交通与现代防护很强，传统奇幻环境会明显缩水。枪械资源环境照常启用，但枪械熟练属于武器熟练，不会通过神圣奇术映射转给法师。",
}

DESIGN_FOCUS = {
    "奥秘领域（UA）": ("C", "UA奥秘与神圣奇术的高环法师法术提前取得交互风险很高；机制现代但边界需要强约束。"),
    "坟墓领域（UA）": ("B+", "附赠动作压低攻击和豁免很强，短持续和引导奥秘成本让设计仍可控。"),
    "保护领域（5E UA）": ("B", "保护主题清楚，但贴身护卫逻辑和法师后排底盘适配一般，反应竞争明显。"),
    "城市领域（5E UA）": ("B", "现代城市主题非常集中，问题是强度由战役场景资产决定，而不是单纯角色资源。"),
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def update_focus() -> None:
    gen.SPELL_FOCUS.update(partner.SPELL_FOCUS)
    gen.DESIGN_FOCUS.update(partner.DESIGN_FOCUS)
    gen.SPELL_FOCUS.update(SPELL_FOCUS)
    gen.DESIGN_FOCUS.update(DESIGN_FOCUS)


def combined_nonofficial_domains() -> list[dict]:
    return partner.PARTNER_DOMAINS + UA_DOMAINS


def update_theurgy_readme() -> None:
    readme = OUT / "README.md"
    text = readme.read_text(encoding="utf-8")
    marker = "## UA/合作方/第三方子职分阶段排行榜"
    start = text.find(marker)
    if start < 0:
        raise RuntimeError("神圣奇术 README missing UA/partner leaderboard marker")
    official_part = text[:start].rstrip()
    board = gen.render_leaderboard(marker[3:], gen.row_entries(combined_nonofficial_domains()))
    write(readme, official_part + "\n\n" + board)


def update_changelog() -> None:
    text = CHANGELOG.read_text(encoding="utf-8")
    entry = """## 神圣奇术UA牧师领域映射评审与全体校准（2026-05-09）
- 新增4个 `神圣奇术（5E UA） - UA牧师领域` 组合评审：保护领域（5E UA）、城市领域（5E UA）、坟墓领域（UA）、奥秘领域（UA）。
- 完成神圣奇术现有33个牧师领域映射的横向校准：官方、5E/5.5e UA、合作方、第三方均按同一标准比较，综合评分继续以法师底盘、神圣奇术底包、领域法术锁定、映射特性增量和限制器共同判断。
- 校准重点：`奥秘领域（UA）`因14级提前取得高环法师法术选择而进入T3/T4 `S+`警戒；`坟墓领域（UA）`因附赠动作压低攻击/豁免进入T2-T4 `S`；`保护领域（5E UA）`因站位和反应竞争维持`S-`；`城市领域（5E UA）`因现代风格法术/科技魔法可作为法师法术写入法术书，T2-T4校准为`S-`，但明确枪械熟练不转入法师且强环境依赖。
- 重新生成神圣奇术目录、法师 README 与根 README 的分阶段排行榜，确保所有神圣奇术组合从文件级 `综合评分` 回读。

"""
    if entry.strip() not in text:
        CHANGELOG.write_text(entry + text, encoding="utf-8", newline="\n")


def main() -> None:
    update_focus()
    for domain in UA_DOMAINS:
        write(OUT / f"{domain['name']}.md", gen.review_file(domain))
    update_theurgy_readme()
    update_changelog()


if __name__ == "__main__":
    main()
