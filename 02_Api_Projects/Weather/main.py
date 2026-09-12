# ============================================================
#  Weather App — fetches current weather for any city
#  Uses: OpenWeatherMap Geocoding API + Current Weather API
# ============================================================

import requests
import json

# ------------------------------------------------------------
# STEP 1: Load the API key from a text file
# ------------------------------------------------------------
API_KEY_PATH = "/home/aadarsh/Desktop/Github/AI_ML_Learning_Roadmap/02_Api_Projects/Weather/api_openweathermap.txt"

try:
    with open(API_KEY_PATH, "r", encoding="utf-8-sig") as f:
        YOUR_API_KEY = f.read().strip()
except FileNotFoundError:
    print(f"❌ API key file not found: {API_KEY_PATH}")
    print("   Create the file and paste your OpenWeatherMap key inside.")
    exit()

# Safety check: an empty key will always return 401 from the API
if not YOUR_API_KEY:
    print("❌ The API key file is empty.")
    print("   Paste your OpenWeatherMap key into:", API_KEY_PATH)
    exit()

# ------------------------------------------------------------
# STEP 2: Ask the user for a city name
# ------------------------------------------------------------
Your_location = input("Enter your location: ").strip()

if not Your_location:
    print("❌ No location entered. Exiting.")
    exit()

# ------------------------------------------------------------
# STEP 3: Geocode the city name → get latitude & longitude
# The Geocoding API converts a place name like "Kathmandu"
# into coordinates like lat=28.65, lon=77.22
# ------------------------------------------------------------
geo_url = (
    f"http://api.openweathermap.org/geo/1.0/direct"
    f"?q={Your_location}&limit=5&appid={YOUR_API_KEY}"
)

try:
    geo_response = requests.get(geo_url, timeout=10)
    geo_data = geo_response.json()
except requests.RequestException as e:
    # Network errors: no internet, DNS failure, timeout, etc.
    print(f"❌ Network error while geocoding: {e}")
    exit()
except requests.JSONDecodeError:
    # The server didn't return valid JSON (rare, but possible)
    print("❌ Geocoding API did not return valid JSON.")
    exit()

# The Geocoding API returns a LIST of matches.
# An empty list means the city wasn't found.
# A dict (with "cod" key) means there was an error.
if isinstance(geo_data, dict):
    print(f"❌ Geocoding API error: {geo_data.get('message', geo_data)}")
    exit()

if not geo_data:
    print(f"❌ Could not find '{Your_location}'. Check the spelling.")
    exit()

# We take the first (best) match. If you want to see all matches,
# uncomment the next line:
# print(json.dumps(geo_data, indent=4))

lat = geo_data[0]["lat"]
lon = geo_data[0]["lon"]
found_name = geo_data[0].get("name", Your_location)
found_country = geo_data[0].get("country", "??")

print(f"📍 Found: {found_name}, {found_country} ({lat}, {lon})")

# ------------------------------------------------------------
# STEP 4: Get the current weather for those coordinates
# The Current Weather API takes lat & lon (or a city name).
# units=metric → Celsius, m/s.  units=imperial → °F, mph.
# ------------------------------------------------------------
weather_url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?lat={lat}&lon={lon}&units=metric&appid={YOUR_API_KEY}"
)

try:
    weather_response = requests.get(weather_url, timeout=10)
    weather_data = weather_response.json()
except requests.RequestException as e:
    print(f"❌ Network error while fetching weather: {e}")
    exit()
except requests.JSONDecodeError:
    print("❌ Weather API did not return valid JSON.")
    exit()

# The API returns a "cod" field. 200 = success, anything else = error.
if weather_data.get("cod") != 200:
    print(
        f"❌ Weather API error: {weather_data.get('message', 'Unknown error')}")
    exit()

# ------------------------------------------------------------
# STEP 5: Extract the fields we care about and print them
# The response is a dict with nested dicts/lists.
# We use .get() with defaults so a missing field won't crash us.
# ------------------------------------------------------------
main_info = weather_data.get("main", {})
weather_info = weather_data.get("weather", [{}])[0]
wind_info = weather_data.get("wind", {})
sys_info = weather_data.get("sys", {})

temperature = main_info.get("temp")
feels_like = main_info.get("feels_like")
humidity = main_info.get("humidity")
pressure = main_info.get("pressure")
condition = weather_info.get("main", "Unknown")
description = weather_info.get("description", "no description")
wind_speed = wind_info.get("speed")
country = sys_info.get("country", "")

print()
print("=" * 40)
print(f"🌤️  Weather in {found_name}, {country}")
print("=" * 40)
print(f"  Condition   : {condition} ({description})")
print(f"  Temperature : {temperature}°C")
print(f"  Feels like  : {feels_like}°C")
print(f"  Humidity    : {humidity}%")
print(f"  Pressure    : {pressure} hPa")
print(f"  Wind speed  : {wind_speed} m/s")
print("=" * 40)
