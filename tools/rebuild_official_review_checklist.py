from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKLIST = ROOT / "official-review-checklist.md"
EXTERNAL_HOMEBREW_CHECKLIST = ROOT / "homebrews" / "Rankings External" / "external-homebrew-review-checklist.md"


@dataclass(frozen=True)
class Row:
    checked: str
    name_en: str
    name_cn: str
    source: str
    note: str = ""


@dataclass(frozen=True)
class BuildRow:
    checked: str
    file_name: str
    chassis: str
    note: str = ""


@dataclass(frozen=True)
class ExternalCandidate:
    row: Row
    publisher: str
    path: str
    edition: int
    date: str
    existing: bool = False


MANUAL_SOURCE_DATES = {
    # First-party 2024 / current books.
    "XPHB": "2024-09-17",
    "XDMG": "2024-11-12",
    "XMM": "2025-02-18",
    "EFA": "2025-12-09",
    "FRHoF": "2025-11-11",
    "RHW": "2026-06-16",
    # Common first-party 5e books used by the current checklist.
    "PHB": "2014-08-19",
    "DMG": "2014-12-09",
    "MM": "2014-09-30",
    "SCAG": "2015-11-03",
    "XGE": "2017-11-21",
    "EGW": "2020-03-17",
    "TCE": "2020-11-17",
    "VRGR": "2021-05-18",
    "FTD": "2021-10-26",
    "SCC": "2021-12-07",
    "BMT": "2024-01-05",
    "BGG": "2023-08-15",
    "DSotDQ": "2022-12-06",
}


MANUAL_UA_DATES = {
    # UATheMysticClass is referenced by 5etools class-feature-variant data, but
    # the original Mystic class file is not present in the local UA repository.
    # Public UA mirrors and community archives list the article date as 2017-03-13.
    "UATheMysticClass": "2017-03-13",
}


SOURCE_CATEGORY_OVERRIDES = {
    "EFA": "official",
    "XPHB": "official",
    "XDMG": "official",
    "XMM": "official",
    "FRHoF": "official",
    "RHW": "official",
    "PHB": "official",
    "DMG": "official",
    "MM": "official",
    "SCAG": "official",
    "XGE": "official",
    "EGW": "official",
    "TCE": "official",
    "VRGR": "official",
    "FTD": "official",
    "SCC": "official",
    "BMT": "official",
    "BGG": "official",
    "DSotDQ": "official",
}


ARTIFICER_EFA_ROWS = [
    Row("- [x]", "Artificer", "奇械师", "EFA"),
    Row("- [x]", "Artificer - Alchemist", "奇械师 - 炼金师", "EFA"),
    Row("- [x]", "Artificer - Armorer", "奇械师 - 装甲师", "EFA"),
    Row("- [x]", "Artificer - Artillerist", "奇械师 - 魔炮师", "EFA"),
    Row("- [x]", "Artificer - Battle Smith", "奇械师 - 战地匠师", "EFA"),
    Row("- [x]", "Artificer - Cartographer", "奇械师 - 制图师", "EFA"),
]


WIZARD_PHB2014_ROWS = [
    Row("- [ ]", "Wizard - School of Conjuration", "法师 - 咒法学派", "PHB"),
    Row("- [ ]", "Wizard - School of Enchantment", "法师 - 附魔学派", "PHB"),
    Row("- [ ]", "Wizard - School of Necromancy", "法师 - 死灵学派", "PHB"),
    Row("- [ ]", "Wizard - School of Transmutation", "法师 - 变化学派", "PHB"),
]


CN_ONLY_EXTERNAL_ROWS = [
    Row("- [ ]", "Bard - College of Cavalry", "吟游诗人 - 骁骑学院", "DragonHorse2026", "CN 5etools raw-only source: `homebrew.kiwee.top/class/AluStar; 龙马迎春.json`"),
    Row("- [ ]", "Monk - Way of Iron Heel", "武僧 - 铁蹄宗", "DragonHorse2026", "CN 5etools raw-only source: `homebrew.kiwee.top/class/AluStar; 龙马迎春.json`"),
    Row("- [ ]", "Paladin - Oath of Iron Cavalry", "圣武士 - 铁骑之誓", "DragonHorse2026", "CN 5etools raw-only source: `homebrew.kiwee.top/class/AluStar; 龙马迎春.json`"),
]


FORCE_EN_NAME_ROWS = {
    ("Apothecary - Exorcist", "GuideDrakkenheim"),
    ("Messenger", "TLotRR"),
    ("Messenger - Counsellor", "TLotRR"),
    ("Messenger - Herald", "TLotRR"),
    ("Tamer - Leader", "HelianasGuidetoMonsterHunting"),
    ("Treasure Hunter", "TLotRR"),
    ("Treasure Hunter - Burglar", "TLotRR"),
    ("Treasure Hunter - Spy", "TLotRR"),
}


SOURCE_PUBLISHER_HINTS = {
    "BH2022": "Matthew Mercer",
    "BH2020": "Matthew Mercer",
    "BloodHunter": "Matthew Mercer",
    "Pugilist2024": "Benjamin Huffman",
    "SterlingVermin": "Benjamin Huffman",
    "SterlingVermin:Patreon": "Benjamin Huffman",
}


SOURCE_EDITION_HINTS = {
    "Pugilist2024": 1,
}


SOURCE_DATE_HINTS = {
    "BH2022": "2022-02-14",
    "BH2020": "2020-01-27",
    "Pugilist2024": "2024-01-01",
}


OFFICIAL_PUBLISHED_BASE_CLASSES = {
    "Artificer",
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard",
}


DISCOVER_EXTERNAL_HOMEBREW_DIRS = [
    ROOT / "5etools-homebrew" / "class",
    ROOT / "5etools-homebrew" / "subclass",
]


ARTIFICER_REMOVE_SOURCES = {
    "TCE",
    "UA2020SubclassesPt3",
    "UAArtificer",
    "UAArtificerRevisited",
    "XUA2025EberronUpdates",
}


UA_TO_OFFICIAL_ALIASES = {
    "barbarian - path of the wild soul": "barbarian - path of wild magic",
    "cleric - love domain": "cleric - peace domain",
    "cleric - unity domain": "cleric - peace domain",
    "fighter - psi knight": "fighter - psi warrior",
    "fighter - psychic warrior": "fighter - psi warrior",
    "fighter - knight": "fighter - cavalier",
    "monk - way of mercy": "monk - warrior of mercy",
    "barbarian - battlerager": "barbarian - path of the battlerager",
    "barbarian - berserker": "barbarian - path of the berserker",
    "paladin - oath of heroism": "paladin - oath of glory",
    "ranger (ambuscade)": "ranger",
    "ranger (spell-less)": "ranger",
    "ranger - deep stalker": "ranger - gloom stalker",
    "ranger - deep stalker conclave": "ranger - gloom stalker",
    "rogue - the revived": "rogue - phantom",
    "sorcerer - clockwork soul": "sorcerer - clockwork sorcery",
    "sorcerer - psionic soul": "sorcerer - aberrant sorcery",
    "sorcerer - aberrant mind": "sorcerer - aberrant sorcery",
    "sorcerer - draconic bloodline": "sorcerer - draconic sorcery",
    "sorcerer - divine soul sorcery": "sorcerer - divine soul",
    "sorcerer - favored soul": "sorcerer - divine soul",
    "sorcerer - lunar magic": "sorcerer - lunar sorcery",
    "sorcerer - shadow": "sorcerer - shadow sorcery",
    "sorcerer - shadow magic": "sorcerer - shadow sorcery",
    "sorcerer - storm": "sorcerer - storm sorcery",
    "sorcerer - wild magic": "sorcerer - wild magic sorcery",
    "blood hunter - profane soul": "blood hunter - order of the profane soul",
    "warlock - great old one": "warlock - great old one patron",
    "warlock - the great old one": "warlock - great old one patron",
    "warlock - archfey": "warlock - archfey patron",
    "warlock - the archfey": "warlock - archfey patron",
    "warlock - alternate great old one": "warlock - great old one patron",
    "warlock - revised great old one": "warlock - great old one patron",
    "warlock - the great old one, tweaked": "warlock - great old one patron",
    "warlock - the genie": "warlock - genie patron",
    "warlock - the noble genie": "warlock - genie patron",
    "warlock - the celestial": "warlock - celestial patron",
    "warlock - the undying light": "warlock - celestial patron",
    "warlock - the lurker in the deep": "warlock - fathomless patron",
    "warlock - the hexblade": "warlock - hexblade patron",
    "warlock - the undead": "warlock - undead patron",
}


def load_source_dates_from_json() -> dict[str, str]:
    dates: dict[str, str] = {}
    roots = [
        ROOT / "5etools-src" / "data",
        ROOT / "5etools-homebrew",
        ROOT / "5etools-unearthed-arcana",
    ]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.json"):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            meta = data.get("_meta")
            if not isinstance(meta, dict):
                continue
            for source in meta.get("sources", []) or []:
                if not isinstance(source, dict):
                    continue
                date = source.get("dateReleased")
                if not date:
                    continue
                for key in (source.get("json"), source.get("abbreviation")):
                    if key:
                        dates[str(key)] = str(date)
    return dates


def load_ua_source_dates_from_generated_indexes() -> dict[str, str]:
    generated = ROOT / "5etools-unearthed-arcana" / "_generated"
    sources_path = generated / "index-sources.json"
    timestamps_path = generated / "index-timestamps.json"
    if not sources_path.exists() or not timestamps_path.exists():
        return {}

    sources = json.loads(sources_path.read_text(encoding="utf-8"))
    timestamps = json.loads(timestamps_path.read_text(encoding="utf-8"))
    dates: dict[str, str] = {}

    for source, rel_path in sources.items():
        entry = timestamps.get(rel_path)
        if not isinstance(entry, dict) or "p" not in entry:
            continue
        try:
            date = datetime.fromtimestamp(int(entry["p"]), tz=timezone.utc).date().isoformat()
        except (TypeError, ValueError, OSError):
            continue
        dates[str(source)] = date
    return dates


def load_source_dates() -> dict[str, str]:
    dates = load_source_dates_from_json()
    # Only UA gets the generated timestamp fallback in this pass. Partner /
    # third-party unknown release dates intentionally remain unresolved.
    for source, date in load_ua_source_dates_from_generated_indexes().items():
        dates.setdefault(source, date)
    dates.update(MANUAL_SOURCE_DATES)
    dates.update(MANUAL_UA_DATES)
    return dates


def parse_build_rows(text: str) -> list[BuildRow]:
    rows: list[BuildRow] = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("| Checkbox | Build file |"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        rows.append(BuildRow(cells[0], cells[1], cells[2], cells[3]))
    return rows


def parse_rows(text: str) -> list[Row]:
    rows: list[Row] = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("| Checkbox | Class / Subclass name"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            break
        if line.startswith("| Checkbox |"):
            break
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells and cells[0] == "---":
            continue
        if len(cells) < 4:
            continue
        rows.append(Row(cells[0], cells[1], cells[2], cells[3], cells[5] if len(cells) > 5 else ""))
    return rows


def discovered_external_note(existing_note: str = "") -> str:
    note = "5etools-homebrew class/subclass目录新增；未定位到DND5e_chm/5etools-cn可靠译名，CN名暂用英文"
    if existing_note:
        return existing_note
    return note


def is_discovered_external_row(row: Row) -> bool:
    return row.note.startswith("5etools-homebrew class/subclass目录新增")


def is_cn_only_external_row(row: Row) -> bool:
    return any(row.name_en == candidate.name_en and row.source == candidate.source for candidate in CN_ONLY_EXTERNAL_ROWS)


def is_private_external_homebrew_row(row: Row) -> bool:
    return is_discovered_external_row(row) or is_cn_only_external_row(row)


def is_theurgy_for_private_external_row(row: Row, private_sources: set[str]) -> bool:
    prefix = "UAWarlockAndWizard + "
    return (
        row.name_en.startswith("Wizard - Theurgy - ")
        and row.source.startswith(prefix)
        and row.source.removeprefix(prefix) in private_sources
    )


def external_overlap_canonical_name(row: Row) -> str:
    name = row.name_en
    name = re.sub(r"^Alternate\s+", "", name)
    name = re.sub(r"^Variant\s+", "", name)
    name = re.sub(r"^Adaptive\s+", "", name)
    name = re.sub(r"^Versatile\s+", "", name)
    name = re.sub(r"^Martial\s+", "", name)
    name = re.sub(r"\s+Reworks?(?=\s+-|$)", "", name)
    name = re.sub(r"\s+Reworked(?=\s+-|$)", "", name)
    name = re.sub(r"\s+\((?:Balanced|Tweaked|Revised|Revised Spell-less|Variant|Variant Magic)\)", "", name)
    name = re.sub(r" - (?:Alternate|Revised)\s+", " - ", name)
    name = re.sub(r", Tweaked$", "", name)
    return canonical_name(Row(row.checked, name, row.name_cn, row.source, row.note))


def external_overlap_class_name(row: Row) -> str:
    class_name = row.name_en.split(" - ", 1)[0]
    class_name = re.sub(r"^Alternate\s+", "", class_name)
    class_name = re.sub(r"^Variant\s+", "", class_name)
    class_name = re.sub(r"^Adaptive\s+", "", class_name)
    class_name = re.sub(r"^Versatile\s+", "", class_name)
    class_name = re.sub(r"^Martial\s+", "", class_name)
    class_name = re.sub(r"\s+Reworks?$", "", class_name)
    class_name = re.sub(r"\s+Reworked$", "", class_name)
    class_name = re.sub(r"\s+\((?:Balanced|Tweaked|Revised|Revised Spell-less|Variant|Variant Magic)\)", "", class_name)
    return canonical_name(Row(row.checked, class_name, row.name_cn, row.source, row.note))


def is_external_rewrite_chassis(row: Row) -> bool:
    class_name = row.name_en.split(" - ", 1)[0]
    return bool(
        class_name.startswith(("Alternate ", "Variant ", "Adaptive ", "Versatile ", "Martial "))
        or re.search(r"\s+Reworks?$", class_name)
        or re.search(r"\s+Reworked$", class_name)
        or re.search(r"\((?:Balanced|Tweaked|Revised|Revised Spell-less|Variant|Variant Magic)\)", class_name)
    )


def external_publisher_from_path(path: Path) -> str:
    stem = path.stem
    if ";" in stem:
        return stem.split(";", 1)[0].strip()
    return stem.strip()


def external_meta_by_file() -> dict[str, dict]:
    path = ROOT / "5etools-homebrew" / "_generated" / "index-meta.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {str(key): value for key, value in data.items() if isinstance(value, dict)}


def external_date_for_data(data: dict, source: str) -> str:
    meta = data.get("_meta")
    if not isinstance(meta, dict):
        return "未知"
    for source_entry in meta.get("sources", []) or []:
        if not isinstance(source_entry, dict):
            continue
        if source in {source_entry.get("json"), source_entry.get("abbreviation")}:
            return str(source_entry.get("dateReleased") or "未知")
    return "未知"


def candidate_sort_key(candidate: ExternalCandidate) -> tuple[int, str, str]:
    date = candidate.date if candidate.date != "未知" else "0000-00-00"
    return (candidate.edition, date, candidate.row.source)


def discover_external_homebrew_rows(existing_rows: list[Row]) -> list[Row]:
    """Add dedicated 5etools-homebrew class/subclass-directory entries.

    This intentionally scans only `class/` and `subclass/`, not adventure/book/
    collection embeds. The latter contains thousands of mixed appendices and is
    too noisy for the standing checklist unless the project explicitly opens a
    resource-specific pass.
    """

    existing_by_name_source = {(row.name_en, row.source): row for row in existing_rows}
    existing_canonical_names = {canonical_name(row) for row in existing_rows}
    existing_class_names = {canonical_name(Row(row.checked, row.name_en, row.name_cn, row.source, row.note)) for row in existing_rows if " - " not in row.name_en}
    candidates: list[ExternalCandidate] = []
    for row in existing_rows:
        publisher = SOURCE_PUBLISHER_HINTS.get(row.source)
        if not publisher:
            continue
        candidates.append(
            ExternalCandidate(
                row=row,
                publisher=publisher,
                path="official-review-checklist.md",
                edition=SOURCE_EDITION_HINTS.get(row.source, 0),
                date=SOURCE_DATE_HINTS.get(row.source, "未知"),
                existing=True,
            )
        )
    meta = external_meta_by_file()
    for root in DISCOVER_EXTERNAL_HOMEBREW_DIRS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8-sig"))
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            rel_key = str(path.relative_to(ROOT / "5etools-homebrew")).replace("\\", "/")
            file_key = str(path.relative_to(root)).replace("\\", "/")
            file_meta = meta.get(file_key) or meta.get(rel_key) or meta.get(path.name) or {}
            edition = int(file_meta.get("e") or 0)
            publisher = external_publisher_from_path(path)

            def add_candidate(name: str, source: str) -> None:
                row = existing_by_name_source.get((name, source))
                existing = row is not None
                if row is None:
                    row = Row("- [ ]", name, name, source, discovered_external_note())
                if external_overlap_canonical_name(row) in existing_canonical_names:
                    return
                if is_external_rewrite_chassis(row) and external_overlap_class_name(row) in existing_class_names:
                    return
                candidates.append(
                    ExternalCandidate(
                        row=row,
                        publisher=SOURCE_PUBLISHER_HINTS.get(source, publisher),
                        path=str(path),
                        edition=edition,
                        date=external_date_for_data(data, source),
                        existing=existing,
                    )
                )

            for cls in data.get("class", []) or []:
                # Broad checklist intentionally excludes external base classes.
                # Review them only through explicit, resource-scoped tasks.
                continue
            for subclass in data.get("subclass", []) or []:
                if (
                    not isinstance(subclass, dict)
                    or not subclass.get("name")
                    or not subclass.get("className")
                    or not subclass.get("source")
                ):
                    continue
                if str(subclass["className"]) not in OFFICIAL_PUBLISHED_BASE_CLASSES:
                    continue
                name = f"{subclass['className']} - {subclass['name']}"
                add_candidate(str(name), str(subclass["source"]))

    grouped: dict[tuple[str, str], list[ExternalCandidate]] = {}
    for candidate in candidates:
        key = (candidate.publisher.lower(), canonical_name(candidate.row))
        grouped.setdefault(key, []).append(candidate)

    rows: list[Row] = []
    emitted: set[tuple[str, str]] = set()
    for group in grouped.values():
        winner = sorted(group, key=candidate_sort_key)[-1]
        if winner.existing:
            continue
        key = (winner.row.name_en, winner.row.source)
        if key in emitted:
            continue
        emitted.add(key)
        rows.append(winner.row)
    return rows


def source_pieces(source: str) -> list[str]:
    return [piece.strip() for piece in re.split(r"\s*\+\s*", source)]


def date_for_source(source: str, dates: dict[str, str]) -> str:
    pieces = source_pieces(source)
    resolved = [dates.get(piece, "未知") for piece in pieces]
    if len(resolved) == 1:
        return resolved[0]
    return " + ".join(resolved)


def category_for_source(source: str) -> str:
    pieces = source_pieces(source)
    if any(piece.startswith("UA") or piece.startswith("XUA") for piece in pieces):
        return "ua"
    if all(SOURCE_CATEGORY_OVERRIDES.get(piece) == "official" for piece in pieces):
        return "official"
    return "partner"


def source_era(source: str) -> str:
    pieces = source_pieces(source)
    if any(piece.startswith("XUA") or piece in {"XPHB", "XDMG", "XMM", "EFA", "FRHoF", "RHW"} for piece in pieces):
        return "2024"
    return "2014"


def is_ua(row: Row) -> bool:
    return category_for_source(row.source) == "ua"


def is_official(row: Row) -> bool:
    return category_for_source(row.source) == "official"


def is_official_counterpart(row: Row) -> bool:
    if is_official(row):
        return True
    if row.name_en.startswith("Wizard - Theurgy - "):
        pieces = source_pieces(row.source)
        # Theurgy itself is UA, but its mapped domain can be official. For
        # Theurgy-domain dedupe, an official domain mapping should count as the
        # current counterpart for older UA versions of that same domain line.
        return any(SOURCE_CATEGORY_OVERRIDES.get(piece) == "official" for piece in pieces[1:])
    return False


def normalize_name(name: str) -> str:
    name = name.lower()
    name = name.replace("&", "and")
    name = name.replace(" - the ", " - ")
    name = re.sub(r"\s*\((?:ua|revised|revisited)\)", "", name)
    name = re.sub(r"\s+v\d+\b", "", name)
    name = re.sub(r"\s+", " ", name)
    name = name.replace("patron patron", "patron")
    return name.strip()


def canonical_name(row: Row) -> str:
    normalized = normalize_name(row.name_en)
    if normalized.startswith("wizard - theurgy - "):
        domain = normalized.removeprefix("wizard - theurgy - ")
        mapped_domain = UA_TO_OFFICIAL_ALIASES.get(f"cleric - {domain}")
        if mapped_domain and mapped_domain.startswith("cleric - "):
            return f"wizard - theurgy - {mapped_domain.removeprefix('cleric - ')}"
    return UA_TO_OFFICIAL_ALIASES.get(normalized, normalized)


def is_artificer_legacy_duplicate(row: Row) -> bool:
    if not row.name_en.startswith("Artificer"):
        return False
    if row.source not in ARTIFICER_REMOVE_SOURCES:
        return False
    if row.name_en == "Artificer - Reanimator":
        return False
    return True


def row_date(row: Row, dates: dict[str, str]) -> str:
    return date_for_source(row.source, dates)


def normalize_forced_english_name(row: Row) -> Row:
    if (row.name_en, row.source) not in FORCE_EN_NAME_ROWS:
        return row
    note = "未定位到DND5e_chm/5etools-cn可靠译名；CN名暂回退为英文名"
    if row.note and row.note != note:
        note = f"{row.note}；{note}"
    return Row(row.checked, row.name_en, row.name_en, row.source, note)


def is_nonofficial_base_class_row(row: Row) -> bool:
    if category_for_source(row.source) != "partner":
        return False
    if " - " not in row.name_en:
        return True
    parent_class = row.name_en.split(" - ", 1)[0]
    return parent_class not in OFFICIAL_PUBLISHED_BASE_CLASSES


def theurgy_row_for_cleric(row: Row) -> Row:
    domain_en = row.name_en.removeprefix("Cleric - ")
    domain_cn = row.name_cn
    if domain_cn.startswith("牧师 - "):
        domain_cn = domain_cn.removeprefix("牧师 - ")
    elif domain_cn.startswith("Cleric - "):
        domain_cn = domain_cn.removeprefix("Cleric - ")
    source = f"UAWarlockAndWizard + {row.source}"
    note = "由牧师领域清单自动补入神圣奇术映射；待独立重评"
    return Row("- [ ]", f"Wizard - Theurgy - {domain_en}", f"法师 - 神圣奇术 - {domain_cn}", source, note)


def add_missing_theurgy_rows(rows: list[Row]) -> tuple[list[Row], list[str]]:
    audit: list[str] = []
    by_key = {(row.name_en, row.source): row for row in rows}
    for row in list(rows):
        if not row.name_en.startswith("Cleric - "):
            continue
        if row.name_en.startswith("Cleric - Theurgy - "):
            continue
        theurgy_row = theurgy_row_for_cleric(row)
        key = (theurgy_row.name_en, theurgy_row.source)
        if key in by_key:
            continue
        by_key[key] = theurgy_row
        audit.append(f"added Theurgy counterpart: {theurgy_row.name_en} [{theurgy_row.source}]")
    return list(by_key.values()), audit


def cleanup_rows(rows: list[Row], dates: dict[str, str]) -> tuple[list[Row], list[str]]:
    audit: list[str] = []
    cleaned: list[Row] = []
    seen: set[tuple[str, str]] = set()

    for row in rows:
        row = normalize_forced_english_name(row)
        if is_nonofficial_base_class_row(row):
            audit.append(f"removed non-official-base partner/third-party row: {row.name_en} [{row.source}]")
            continue
        if is_artificer_legacy_duplicate(row):
            audit.append(f"removed Artificer legacy duplicate: {row.name_en} [{row.source}]")
            continue
        if row.name_en in {
            "Artificer - Alchemist",
            "Artificer - Armorer",
            "Artificer - Artillerist",
            "Artificer - Battle Smith",
            "Artificer - Cartographer",
        } and row.source != "EFA":
            audit.append(f"removed Artificer non-EFA duplicate: {row.name_en} [{row.source}]")
            continue
        if row.name_en == "Artificer" and row.source != "EFA":
            audit.append(f"removed Artificer non-EFA duplicate: {row.name_en} [{row.source}]")
            continue

        key = (row.name_en, row.source)
        if key in seen:
            audit.append(f"removed exact duplicate: {row.name_en} [{row.source}]")
            continue
        seen.add(key)
        cleaned.append(row)

    by_key = {(row.name_en, row.source): row for row in cleaned}
    for row in ARTIFICER_EFA_ROWS:
        existing = by_key.get((row.name_en, row.source))
        if existing is None:
            audit.append(f"added latest EFA Artificer row: {row.name_en}")
            by_key[(row.name_en, row.source)] = row
        elif existing.checked != row.checked:
            audit.append(f"rechecked completed EFA Artificer row: {row.name_en}")
            by_key[(row.name_en, row.source)] = Row(row.checked, existing.name_en, existing.name_cn, existing.source, existing.note)
    for row in WIZARD_PHB2014_ROWS:
        if (row.name_en, row.source) not in by_key:
            audit.append(f"added unreplaced PHB2014 Wizard row: {row.name_en}")
        by_key.setdefault((row.name_en, row.source), row)
    cleaned = list(by_key.values())

    official_by_name_era: dict[tuple[str, str], Row] = {}
    official_by_name_any: dict[str, list[Row]] = {}
    for row in cleaned:
        if not is_official_counterpart(row):
            continue
        key = canonical_name(row)
        official_by_name_era[(key, source_era(row.source))] = row
        official_by_name_any.setdefault(key, []).append(row)

    next_rows: list[Row] = []
    for row in cleaned:
        if not is_ua(row):
            next_rows.append(row)
            continue
        key = canonical_name(row)
        era = source_era(row.source)
        same_era = official_by_name_era.get((key, era))
        any_official = [candidate for candidate in official_by_name_any.get(key, []) if candidate != row]
        has_2024_ua_vs_2014_official = era == "2024" and any(source_era(candidate.source) == "2014" for candidate in any_official)
        if same_era and same_era != row:
            audit.append(f"removed same-era UA duplicate: {row.name_en} [{row.source}] -> {same_era.name_en} [{same_era.source}]")
            continue
        if any_official and not has_2024_ua_vs_2014_official:
            target = sorted(any_official, key=lambda candidate: row_date(candidate, dates))[-1]
            audit.append(f"removed UA duplicate with official counterpart: {row.name_en} [{row.source}] -> {target.name_en} [{target.source}]")
            continue
        next_rows.append(row)

    grouped_ua: dict[str, list[Row]] = {}
    for row in next_rows:
        if is_ua(row) and not row.name_en.startswith("Wizard - Theurgy - "):
            grouped_ua.setdefault(canonical_name(row), []).append(row)

    keep_ua: set[Row] = set()
    for key, group in grouped_ua.items():
        if len(group) == 1:
            keep_ua.add(group[0])
            continue
        newest = sorted(group, key=lambda row: row_date(row, dates))[-1]
        keep_ua.add(newest)
        for row in group:
            if row != newest:
                audit.append(f"removed older UA variant: {row.name_en} [{row.source}] -> {newest.name_en} [{newest.source}]")

    final_rows: list[Row] = []
    for row in next_rows:
        if is_ua(row) and not row.name_en.startswith("Wizard - Theurgy - ") and row not in keep_ua:
            continue
        final_rows.append(row)

    artificer_rows = [row for row in ARTIFICER_EFA_ROWS]
    remainder = [
        row
        for row in final_rows
        if not (row.name_en == "Artificer" or (row.name_en.startswith("Artificer - ") and row.source == "EFA"))
    ]

    out: list[Row] = []
    inserted = False
    for row in remainder:
        if not inserted and row.name_en > "Artificer":
            out.extend(artificer_rows)
            inserted = True
        out.append(row)
    if not inserted:
        out.extend(artificer_rows)
    return out, audit


def count_special(rows: list[Row]) -> tuple[int, int]:
    strixhaven = sum(1 for row in rows if "Strixhaven" in row.name_en or row.source == "UA2021MagesOfStrixhaven")
    theurgy = sum(1 for row in rows if "Theurgy" in row.name_en or "神圣奇术" in row.name_cn)
    return strixhaven, theurgy


def sort_rows(rows: list[Row], dates: dict[str, str]) -> list[Row]:
    return sorted(rows, key=lambda row: (row.name_en.split(" - ", 1)[0], row.name_en, row.source, row_date(row, dates)))


def render_build_rows(build_rows: list[BuildRow]) -> list[str]:
    if not build_rows:
        return []
    lines = [
        "## Existing Build Review Checklist",
        "",
        "| Checkbox | Build file | Primary chassis | 备注 |",
        "|---|---|---|---|",
    ]
    for row in build_rows:
        lines.append(f"| {row.checked} | {row.file_name} | {row.chassis} | {row.note} |")
    lines.append("")
    return lines


def render(rows: list[Row], build_rows: list[BuildRow], dates: dict[str, str]) -> str:
    counts = {"official": 0, "ua": 0, "partner": 0}
    for row in rows:
        counts[category_for_source(row.source)] += 1
    strixhaven, theurgy = count_special(rows)

    lines = [
        "# Official / UA / Partner / Third-Party Review Checklist",
        "",
        "> Generated from local 5etools JSON resources for the next full review pass. 规则：同世代优先最新官方；2014 官方 + 2024 UA 并列；无官方时取最新 UA；第三方/合作方纳入项目资源集。",
        "> External creator-homebrew rows discovered from raw `5etools-homebrew` class/subclass files are intentionally excluded from this public official checklist. They are written to `homebrews/Rankings External/external-homebrew-review-checklist.md` and should be reviewed with the homebrew workflow in a gitignored location.",
        "> `5etools-homebrew` 的 adventure/book/collection 内嵌职业/子职暂不整库纳入清单；这些文件噪声很高，除非项目后续打开具体资源批次，否则只作为按资源检索时的候选来源。",
        "> Explicitly excluded: `Rune Scribe | 符文抄录者`, because it is a 3.5e-style prestige class and cannot be reviewed on the normal 5e/5.5e class/subclass progression.",
        "> Redundant same-name or same-lineage entries are cleaned by the project version rules: latest official for same-era official/UA conflicts, separate 2014-official + 2024-UA rows where required, and 2024/5.5e partner or third-party versions over 2014/5e predecessors only when they are from the same author / publisher and use the same or a clearly similar name.",
        "> External homebrew base classes and subclasses under external base classes are omitted from this broad checklist, even if present in 5etools. Review them only through explicit, resource-scoped tasks.",
        "> CN-only 5etools raw class/subclass resources are added only when explicitly verified, because the local CN mirror does not currently store those raw files under `homebrew/` or `prerelease/`.",
        "> Release dates are resolved from 5etools `_meta.sources[].dateReleased` first; UA dates additionally fall back to `5etools-unearthed-arcana\\_generated\\index-sources.json` + `index-timestamps.json`, then narrow manual metadata when local files are incomplete. Partner / third-party `未知` dates are intentionally not resolved by generated timestamps in this pass.",
        "",
        f"- Total rows: {len(rows) + len(build_rows)}",
        f"- Build rows: {len(build_rows)}",
        f"- Official rows: {counts['official']}",
        f"- UA rows: {counts['ua']}",
        f"- Partner / third-party rows: {counts['partner']}",
        f"- Strixhaven mapped rows: {strixhaven}",
        f"- Theurgy mapped rows: {theurgy}",
        "",
    ]
    lines.extend(render_build_rows(build_rows))
    lines.extend([
        "| Checkbox | Class / Subclass name (EN) | CN name counterpart | Resource abbr. name | Resource release date | 备注 |",
        "|---|---|---|---|---|---|",
    ])
    for row in rows:
        lines.append(
            f"| {row.checked} | {row.name_en} | {row.name_cn} | {row.source} | {date_for_source(row.source, dates)} | {row.note} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_external_homebrew(rows: list[Row], dates: dict[str, str]) -> str:
    rows = sort_rows(rows, dates)
    lines = [
        "# External Creator-Homebrew Review Checklist",
        "",
        "> This checklist is generated from raw external `5etools-homebrew` class/subclass files and explicitly verified CN-only raw sources. It is kept under `homebrews/Rankings External/`, which is gitignored, so these reviews do not appear as public root official / UA / partner / third-party rankings.",
        "> Treat every row here with the `homebrew-dnd-ranking-review` workflow. Do not write its reviews under root `Rankings` unless the user explicitly promotes a specific source into the public published-resource scope.",
        "> Current generator scope intentionally remains narrow: dedicated external `class/` and `subclass/` directory entries that pass the existing discovery filters, plus explicitly verified CN-only external rows. Adventure/book/collection embedded options are not bulk-imported.",
        "",
        f"- Total rows: {len(rows)}",
        "",
        "| Checkbox | Class / Subclass name (EN) | CN name counterpart | Resource abbr. name | Resource release date | 备注 |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row.checked} | {row.name_en} | {row.name_cn} | {row.source} | {date_for_source(row.source, dates)} | {row.note} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    text = CHECKLIST.read_text(encoding="utf-8")
    build_rows = parse_build_rows(text)
    parsed_rows = parse_rows(text)
    private_existing_rows = [row for row in parsed_rows if is_private_external_homebrew_row(row)]
    rows = [row for row in parsed_rows if not is_private_external_homebrew_row(row)]
    external_seed_rows = rows + private_existing_rows
    for row in CN_ONLY_EXTERNAL_ROWS:
        if not any(existing.name_en == row.name_en and existing.source == row.source for existing in external_seed_rows):
            external_seed_rows.append(row)
            private_existing_rows.append(row)
    external_rows = discover_external_homebrew_rows(external_seed_rows)
    dates = load_source_dates()
    private_by_key = {(row.name_en, row.source): row for row in private_existing_rows}
    for row in external_rows:
        private_by_key[(row.name_en, row.source)] = row
    private_rows = list(private_by_key.values())
    private_sources = {row.source for row in private_rows}
    rows = [row for row in rows if not is_theurgy_for_private_external_row(row, private_sources)]
    rows, audit = cleanup_rows(rows, dates)
    rows, theurgy_audit = add_missing_theurgy_rows(rows)
    audit.extend(theurgy_audit)
    CHECKLIST.write_text(render(rows, build_rows, dates), encoding="utf-8", newline="\n")
    EXTERNAL_HOMEBREW_CHECKLIST.parent.mkdir(parents=True, exist_ok=True)
    EXTERNAL_HOMEBREW_CHECKLIST.write_text(render_external_homebrew(private_rows, dates), encoding="utf-8", newline="\n")
    print(f"wrote {CHECKLIST.relative_to(ROOT)} with {len(rows) + len(build_rows)} rows")
    print(f"wrote {EXTERNAL_HOMEBREW_CHECKLIST.relative_to(ROOT)} with {len(private_rows)} rows")
    print(f"build rows: {len(build_rows)}")
    print(f"private external homebrew rows: {len(private_rows)}")
    print(f"removed/added audit entries: {len(audit)}")
    for entry in audit[:80]:
        print(f"- {entry}")
    if len(audit) > 80:
        print(f"- ... {len(audit) - 80} more")


if __name__ == "__main__":
    main()
