from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class SmoothingCfg:
    kind: str = "ema"
    alpha: float = 0.2
    median_kernel: int = 5

@dataclass
class MajorMinorCfg:
    enabled: bool = True
    time_col: str = "time_utc"
    value_col: str = "phase_ratio"
    dt_hours: float = 3.0
    thr_major: float = 0.911
    thr_minor: float = 0.444
    min_pts_major: int = 2
    min_pts_minor: int = 3
    smoothing: SmoothingCfg = SmoothingCfg()

@dataclass
class DriftCfg:
    enabled: bool = True
    drift_threshold_8: float = 1.0
    drift_threshold_9: float = 1.125

@dataclass
class BundleCfg:
    major_minor_rule: MajorMinorCfg = MajorMinorCfg()
    drift_rule: DriftCfg = DriftCfg()

default_cfg = BundleCfg()
