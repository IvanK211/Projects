"""General-purpose low-voltage and dimensional calculations, not design certification."""
from __future__ import annotations
from .common import number

def fit_scale(source: list[float], target: list[float], clearance: float = 0) -> dict:
    if len(source) != 3 or len(target) != 3:
        raise ValueError("Provide three source and target dimensions")
    gap = number(clearance, "clearance")
    s = [number(x, "source", 0.000001) for x in source]
    t = [number(x, "target", 0.000001) - 2*gap for x in target]
    if min(t) <= 0:
        raise ValueError("Clearance leaves no usable interior")
    scale = min(b / a for a, b in zip(s, t))
    return {"uniformScale": scale, "percent": scale*100,
            "resultDimensions": [v*scale for v in s],
            "note": "Uniform bounding-box fit does not preserve functional holes or mating features."}

def energy_budget(voltage: float, amp_hours: float, watts: float, usable_fraction: float, efficiency: float) -> dict:
    v = number(voltage, "voltage", 0.000001)
    ah = number(amp_hours, "ampHours", 0.000001)
    w = number(watts, "loadWatts", 0.000001)
    usable = number(usable_fraction, "usableFraction", 0.000001)
    eff = number(efficiency, "efficiency", 0.000001)
    if usable > 1 or eff > 1:
        raise ValueError("Fractions must be in (0,1]")
    return {"nominalWh": v*ah, "estimatedUsableWh": v*ah*usable*eff,
            "estimatedHours": v*ah*usable*eff/w,
            "note": "Planning estimate only; does not validate cell matching, BMS, fusing or thermal safety."}

def flow_measurement(volume_liters: float, seconds: float, reservoir_liters: float) -> dict:
    volume = number(volume_liters, "collectedVolumeLiters", 0.000001)
    elapsed = number(seconds, "collectionSeconds", 0.000001)
    reservoir = number(reservoir_liters, "reservoirLiters", 0.000001)
    rate = volume/elapsed*60
    return {"measuredLitersPerMinute": rate,
            "idealVolumeTurnoverMinutes": reservoir/rate,
            "note": "An ideal mixing estimate is not an oxygenation measurement or irrigation recommendation."}
