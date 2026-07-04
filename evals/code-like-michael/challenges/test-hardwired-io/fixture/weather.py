"""Weather fetcher — hard-wired IO, needs better tests."""

from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class WeatherReading:
    city: str
    temperature_c: float
    observed_at: datetime


def fetch_weather(city: str) -> WeatherReading:
    """Fetch current weather. Uses live HTTP — hard to test."""
    url = f"https://wttr.in/{city}?format=j1"
    with urllib.request.urlopen(url, timeout=10) as resp:
        payload = json.loads(resp.read().decode())
    current = payload["current_condition"][0]
    temp = float(current["temp_C"])
    return WeatherReading(
        city=city,
        temperature_c=temp,
        observed_at=datetime.now(timezone.utc),
    )


def classify_comfort(reading: WeatherReading) -> str:
    if reading.temperature_c < 10:
        return "cold"
    if reading.temperature_c > 28:
        return "hot"
    return "comfortable"
