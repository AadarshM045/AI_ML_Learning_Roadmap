# 01 — Weather App

> Fetches real-time weather for any city in the world — your first project using an API that requires a key.

---

## 📂 Files

| File | Purpose |
|------|---------|
| [`main.py`](./main.py) | Main program |
| `api_openweathermap.txt` | Your API key — stored locally, never commit this to GitHub |

---

## 🌐 APIs Used

| | |
|---|---|
| **Provider** | [OpenWeatherMap](https://openweathermap.org/api) |
| **API 1** | Geocoding API — converts a city name → latitude & longitude |
| **API 2** | Current Weather API — fetches live weather for those coordinates |
| **Auth** | API key required (free tier available) |
| **Endpoint 1** | `http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}` |
| **Endpoint 2** | `https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}` |

---

## ✨ Features

- Converts any city name to coordinates using the Geocoding API
- Fetches live weather using those coordinates
- Displays temperature, feels like, humidity, pressure, wind speed, and condition
- Handles all errors gracefully — wrong city, empty key, no internet, bad JSON

---

## 🧠 What You'll Learn

- Reading an API key from a local `.txt` file instead of hardcoding it
- Two-step API workflow — geocode first, then fetch weather with the coordinates
- Chained API calls — output of API 1 feeds into API 2
- `isinstance()` — checking whether the API returned a list or a dict to detect errors
- `.get(key, default)` — safely extracting fields from nested dicts without crashing
- `weather_data.get("weather", [{}])[0]` — safely unpacking a nested list
- `requests.RequestException` — one catch for all network errors
- `exit()` — stopping the program cleanly at any failure point
- Checking `weather_data.get("cod") != 200` for API-level errors
- `encoding="utf-8-sig"` — handles the invisible BOM character some text editors add

---

## 💡 Key Concepts in Practice

```python
import requests

# ── Load API key from file (never hardcode secrets) ───
with open("api_openweathermap.txt", "r", encoding="utf-8-sig") as f:
    YOUR_API_KEY = f.read().strip()

# ── Step 1: Geocode city name → lat/lon ──────────────
geo_url = (
    f"http://api.openweathermap.org/geo/1.0/direct"
    f"?q={Your_location}&limit=5&appid={YOUR_API_KEY}"
)
geo_data = requests.get(geo_url, timeout=10).json()

# API returns a list on success, dict on error — check which one came back
if isinstance(geo_data, dict):
    print(f"API error: {geo_data.get('message')}")
    exit()

lat = geo_data[0]["lat"]      # take the first (best) match
lon = geo_data[0]["lon"]

# ── Step 2: Fetch weather using coordinates ───────────
weather_url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?lat={lat}&lon={lon}&units=metric&appid={YOUR_API_KEY}"
)
weather_data = requests.get(weather_url, timeout=10).json()

# cod=200 means success, anything else is an error
if weather_data.get("cod") != 200:
    print(f"Error: {weather_data.get('message')}")
    exit()

# ── Safely unpack nested response ────────────────────
main_info    = weather_data.get("main", {})
weather_info = weather_data.get("weather", [{}])[0]  # list → first item
wind_info    = weather_data.get("wind", {})

temperature = main_info.get("temp")        # .get() won't crash if key missing
humidity    = main_info.get("humidity")
condition   = weather_info.get("main", "Unknown")

# ── Catch all network errors in one block ────────────
try:
    response = requests.get(url, timeout=10)
except requests.RequestException as e:
    print(f"Network error: {e}")
    exit()
```

---

## ▶️ How to Set Up & Run

**1. Get a free API key**
- Sign up at [openweathermap.org](https://openweathermap.org/api)
- Go to your profile → API Keys → copy the key

**2. Save the key to a file**
```bash
# Create the key file (do NOT commit this to GitHub)
echo "your_api_key_here" > api_openweathermap.txt
```

**3. Add the key file to `.gitignore`**
```
api_openweathermap.txt
```

**4. Install dependencies**
```bash
pip install requests
```

**5. Run the app**
```bash
python3 main.py
```

---

## 🖥️ Sample Output

```
Enter your location: Kathmandu
📍 Found: Kathmandu, NP (27.708317, 85.3205817)

========================================
🌤️  Weather in Kathmandu, NP
========================================
  Condition   : Clouds (broken clouds)
  Temperature : 22°C
  Feels like  : 21°C
  Humidity    : 74%
  Pressure    : 1012 hPa
  Wind speed  : 1.8 m/s
========================================
```

---

## ⚠️ Keep Your API Key Safe

- **Never commit `api_openweathermap.txt` to GitHub** — add it to `.gitignore`
- If you accidentally push it, regenerate your key immediately on OpenWeatherMap

---

## 🔗 How This Project Uses Previous Skills

| Skill | Where it appears |
|-------|-----------------|
| File I/O | Reading the API key from a `.txt` file |
| Dictionaries | Unpacking the entire API response |
| `try/except` | Network errors, file not found, empty key |
| f-strings | Building API URLs and formatting output |
| Functions (next step) | Currently all inline — good refactor exercise |

---

*Part of the [AI/ML Learning Roadmap](../../../README.md)*