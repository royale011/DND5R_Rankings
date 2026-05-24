from __future__ import annotations

from dataclasses import dataclass

from .model import DprCategory


RANK_ORDER = ("EX", "S+", "S", "S-", "A+", "A", "A-", "B+", "B", "C", "D", "E", "E-", "F")


@dataclass(frozen=True)
class CrStats:
    cr: str
    sample_count: int
    median_hp: float
    average_hp: float
    median_ac: float
    median_saves: dict[str, float]


@dataclass(frozen=True)
class LevelReference:
    level: int
    close_burst_cr: str
    close_sustained_cr: str
    close_aoe_cr: str
    ranged_burst_cr: str
    ranged_sustained_cr: str
    ranged_aoe_cr: str
    close_aoe_targets: int = 2
    ranged_aoe_targets: int = 3

    def cr_for_category(self, category: DprCategory) -> str:
        return {
            "close_burst": self.close_burst_cr,
            "close_sustained": self.close_sustained_cr,
            "close_aoe": self.close_aoe_cr,
            "ranged_burst": self.ranged_burst_cr,
            "ranged_sustained": self.ranged_sustained_cr,
            "ranged_aoe": self.ranged_aoe_cr,
        }[category]

    def targets_for_category(self, category: DprCategory) -> int:
        if category == "close_aoe":
            return self.close_aoe_targets
        if category == "ranged_aoe":
            return self.ranged_aoe_targets
        return 1


LEVEL_REFERENCES: dict[int, LevelReference] = {
    1: LevelReference(1, "1", "1", "1/2", "1", "1", "1/2"),
    2: LevelReference(2, "3", "2", "1", "3", "2", "1"),
    3: LevelReference(3, "4", "3", "2", "4", "3", "1"),
    4: LevelReference(4, "5", "4", "3", "5", "4", "2"),
    5: LevelReference(5, "8", "7", "4", "8", "7", "3"),
    6: LevelReference(6, "9", "8", "5", "9", "8", "4"),
    7: LevelReference(7, "10", "9", "6", "10", "9", "4"),
    8: LevelReference(8, "12", "10", "7", "12", "10", "5"),
    9: LevelReference(9, "13", "11", "8", "13", "11", "6"),
    10: LevelReference(10, "14", "12", "8", "14", "12", "7"),
    11: LevelReference(11, "16", "14", "9", "16", "14", "7"),
    12: LevelReference(12, "17", "15", "11", "17", "15", "8"),
    13: LevelReference(13, "18", "16", "12", "18", "16", "9"),
    14: LevelReference(14, "19", "17", "12", "19", "17", "10"),
    15: LevelReference(15, "20", "18", "13", "20", "18", "11"),
    16: LevelReference(16, "21", "19", "14", "21", "19", "11"),
    17: LevelReference(17, "22", "20", "15", "22", "20", "12"),
    18: LevelReference(18, "23", "21", "16", "23", "21", "14"),
    19: LevelReference(19, "24", "22", "18", "24", "22", "15"),
    20: LevelReference(20, "25", "23", "20", "25", "23", "16"),
}


def _saves(str_: float, dex: float, con: float, int_: float, wis: float, cha: float) -> dict[str, float]:
    return {"str": str_, "dex": dex, "con": con, "int": int_, "wis": wis, "cha": cha}


CR_STATS: dict[str, CrStats] = {
    "1/2": CrStats("1/2", 34, 19, 20.4, 12, _saves(0, 0, 0, 0, 0, 0)),
    "1": CrStats("1", 41, 26, 28.9, 13, _saves(2, 2, 1, -2, 1, -1)),
    "2": CrStats("2", 59, 45, 46.2, 13, _saves(3, 2, 2, -1, 1, -1)),
    "3": CrStats("3", 41, 65, 62.7, 14, _saves(3, 2, 2, 0, 1, 0)),
    "4": CrStats("4", 27, 71, 70.9, 15, _saves(3, 2, 3, 0, 1, 2)),
    "5": CrStats("5", 36, 93.5, 98.9, 15, _saves(4, 1, 3, -2, 1, -1.5)),
    "6": CrStats("6", 23, 112, 109, 16, _saves(4, 2, 4, -1, 3, 0)),
    "7": CrStats("7", 16, 126.5, 128.4, 16, _saves(4, 2.5, 4, -0.5, 3.5, 0)),
    "8": CrStats("8", 23, 136, 135, 16, _saves(4, 2, 5, 1, 4, 2)),
    "9": CrStats("9", 12, 156.5, 157.8, 17.5, _saves(5, 4, 5, 2, 5, 3)),
    "10": CrStats("10", 16, 161.5, 170.7, 18, _saves(5, 5, 5, 3, 7, 4.5)),
    "11": CrStats("11", 12, 197, 194.1, 17, _saves(6, 4.5, 5, 1.5, 4.5, 4)),
    "12": CrStats("12", 7, 182, 188, 18, _saves(6, 5, 6, 3, 6, 4)),
    "13": CrStats("13", 9, 195, 200.2, 18, _saves(6, 5, 6, 3, 6, 4)),
    "14": CrStats("14", 4, 195, 200.5, 18.5, _saves(5.5, 6.5, 6, 4, 7, 4)),
    "15": CrStats("15", 6, 209.5, 216, 18, _saves(7, 5, 7, 4, 7, 5)),
    "16": CrStats("16", 7, 255, 240.1, 19, _saves(8, 5, 9, 4, 8, 6)),
    "17": CrStats("17", 7, 256, 255.4, 20, _saves(8, 6, 8, 4, 8, 6)),
    "18": CrStats("18", 1, 180, 180, 20, _saves(8, 6, 8, 4, 8, 6)),
    "19": CrStats("19", 1, 287, 287, 19, _saves(8, 6, 8, 4, 8, 6)),
    "20": CrStats("20", 4, 332.5, 331.2, 20, _saves(8, 6.5, 7.5, 3.5, 9, 6)),
    "21": CrStats("21", 5, 333, 335.8, 21, _saves(9, 7, 9, 4, 9, 6)),
    "22": CrStats("22", 3, 444, 405.3, 22, _saves(9, 7, 9, 4, 9, 7)),
    "23": CrStats("23", 5, 468, 444.8, 22, _saves(10, 7, 10, 4, 10, 7)),
    "24": CrStats("24", 2, 526.5, 526.5, 22, _saves(10, 8, 10, 4, 10, 7)),
    "25": CrStats("25", 1, 553, 553, 23, _saves(10, 8, 10, -4, 8, -1)),
    "30": CrStats("30", 1, 697, 697, 25, _saves(10, 9, 10, 5, 9, 9)),
}


SUSTAINED_THRESHOLDS = (
    ("EX", 45.0),
    ("S+", 33.0),
    ("S", 25.0),
    ("S-", 20.0),
    ("A+", 16.7),
    ("A", 12.5),
    ("A-", 10.0),
    ("B+", 8.3),
    ("B", 6.5),
    ("C", 4.5),
    ("D", 3.0),
    ("E", 1.0),
    ("E-", 0.01),
)

BURST_THRESHOLDS = (
    ("EX", 100.0),
    ("S+", 75.0),
    ("S", 55.0),
    ("S-", 40.0),
    ("A+", 30.0),
    ("A", 22.0),
    ("A-", 16.7),
    ("B+", 12.5),
    ("B", 8.3),
    ("C", 5.0),
    ("D", 3.0),
    ("E", 1.0),
    ("E-", 0.01),
)


def rank_for_percent(category: DprCategory, percent: float) -> str:
    thresholds = SUSTAINED_THRESHOLDS if category.endswith("sustained") else BURST_THRESHOLDS
    for rank, minimum in thresholds:
        if percent >= minimum:
            return rank
    return "F"


def reference_for(level: int, category: DprCategory) -> tuple[LevelReference, CrStats, int]:
    level_ref = LEVEL_REFERENCES[level]
    cr = level_ref.cr_for_category(category)
    return level_ref, CR_STATS[cr], level_ref.targets_for_category(category)
