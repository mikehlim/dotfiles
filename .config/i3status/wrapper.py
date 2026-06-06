#!/usr/bin/env python3
"""Pipe i3status JSON (i3bar) and insert a weather block before the clock."""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CONF = os.path.expanduser("~/.config/i3status/weather.conf")
CACHE_TTL = 600.0
GEO_URL = (
    "https://geocoding-api.open-meteo.com/v1/search"
    "?name={name}&countryCode={cc}&count=1"
)
FC_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude={lat}&longitude={lon}"
    "&current=temperature_2m,weather_code"
    "&temperature_unit={unit}"
)

_state = {"text": "…", "until": 0.0, "color": "#5E81AC"}


def _read_conf():
    postal, country = "94102", "US"
    try:
        with open(CONF, encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip() and not ln.lstrip().startswith("#")]
        if lines:
            postal = lines[0]
        if len(lines) > 1:
            country = lines[1].upper()
    except OSError:
        pass
    return postal, country


def _wmo_emoji_and_label(code: int) -> tuple[str, str]:
    if code == 0:
        return "☀️", "clear"
    if code in (1, 2, 3):
        return "☁️", "cloudy"
    if code in (45, 48):
        return "🌫️", "fog"
    if code in (51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82):
        return "🌧️", "rain"
    if code in (71, 73, 75, 77, 85, 86):
        return "❄️", "snow"
    if code in (95, 96, 99):
        return "⛈️", "storm"
    return "🌡️", "weather"


def _fetch_json(url: str, timeout: float = 8.0):
    req = urllib.request.Request(url, headers={"User-Agent": "i3status-weather/1"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _refresh_weather():
    postal, country = _read_conf()
    unit = "fahrenheit" if country == "US" else "celsius"
    deg = "°F" if unit == "fahrenheit" else "°C"
    geo = _fetch_json(
        GEO_URL.format(name=urllib.parse.quote(postal), cc=urllib.parse.quote(country))
    )
    results = geo.get("results") or []
    if not results:
        _state["text"] = "🌦️ Weather — unknown place"
        _state["color"] = "#BF616A"
        return
    lat = results[0]["latitude"]
    lon = results[0]["longitude"]
    fc = _fetch_json(FC_URL.format(lat=lat, lon=lon, unit=unit))
    cur = fc.get("current") or {}
    temp = cur.get("temperature_2m")
    wcode = int(cur.get("weather_code") or 0)
    if temp is None:
        _state["text"] = "🌡️ Weather — no data"
        _state["color"] = "#EBCB8B"
        return
    sym, label = _wmo_emoji_and_label(wcode)
    t = int(round(float(temp)))
    _state["text"] = f"{sym} {label} {t}{deg}"
    _state["color"] = "#88C0D0"


def weather_block():
    now = time.monotonic()
    if now >= _state["until"]:
        try:
            _refresh_weather()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError, ValueError, json.JSONDecodeError):
            _state["text"] = _state.get("text", "…")
            _state["color"] = "#EBCB8B"
        _state["until"] = now + CACHE_TTL
    return {
        "name": "weather",
        "instance": "openmeteo",
        "markup": "none",
        "full_text": _state["text"],
        "color": _state["color"],
        "separator": True,
        "separator_block_width": 9,
    }


def print_line(message: str) -> None:
    sys.stdout.write(message + "\n")
    sys.stdout.flush()


def read_line() -> str:
    line = sys.stdin.readline()
    if not line:
        sys.exit(3)
    return line.strip()


if __name__ == "__main__":
    print_line(read_line())
    print_line(read_line())
    while True:
        raw = read_line()
        prefix = ""
        if raw.startswith(","):
            prefix, raw = ",", raw[1:]
        blocks = json.loads(raw)
        if isinstance(blocks, list) and blocks:
            w = weather_block()
            blocks.insert(0, w)
        print_line(prefix + json.dumps(blocks, separators=(",", ":")))
