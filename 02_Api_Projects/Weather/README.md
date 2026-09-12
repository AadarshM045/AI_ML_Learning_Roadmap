# 🌤️ Weather App

A beginner-friendly Python weather application that fetches **current weather information for any city** using the **OpenWeatherMap API**.

The project demonstrates how to work with **REST APIs, JSON data, API keys, query parameters, nested dictionaries, error handling, and user input** in Python.

## 🚀 Features

* 🌍 Search for weather by city name
* 📍 Converts the city name into latitude and longitude using the **Geocoding API**
* 🌤️ Fetches current weather using the **Current Weather API**
* 🌡️ Displays temperature and feels-like temperature
* 💧 Shows humidity
* 🧭 Shows atmospheric pressure
* 💨 Shows wind speed
* ⚠️ Handles network, JSON, API-key, and invalid-location errors
* 🔐 Keeps the API key in a separate file instead of hard-coding it

## 🛠️ Technologies Used

* **Python**
* **Requests** — for making HTTP requests
* **JSON** — for handling API responses
* **OpenWeatherMap API**

## 📁 Project Structure

```text
Weather/
├── weather_app.py
├── api_openweathermap.txt
└── README.md
```

> ⚠️ `api_openweathermap.txt` contains your private API key and should **never be uploaded to GitHub**.

## 🔑 API Key Setup

This project uses an API key from **OpenWeatherMap**.

Create a file named:

```text
api_openweathermap.txt
```

Put your API key inside the file:

```text
YOUR_API_KEY_HERE
```

The program reads the key from this file before making API requests.

### Important

Add the API key file to `.gitignore`:

```gitignore
api_openweathermap.txt
```

Never commit or publicly share your API key.

## 📦 Installation

Make sure Python is installed, then install the `requests` library:

```bash
pip install requests
```

Or, if you are using a virtual environment:

```bash
pip install requests
```

## ▶️ How to Run

Run the Python file:

```bash
python weather_app.py
```

Enter a city when prompted:

```text
Enter your location: Kathmandu
```

The program first searches for the location and then retrieves its current weather.

## 💻 Example Output

```text
Enter your location: Kathmandu

📍 Found: Kathmandu, NP (27.708317, 85.3205817)

========================================
🌤️  Weather in Kathmandu, NP
========================================
  Condition   : Clouds (broken clouds)
  Temperature : 24.5°C
  Feels like  : 25.1°C
  Humidity    : 72%
  Pressure    : 1012 hPa
  Wind speed  : 2.6 m/s
========================================
```

*The values will change depending on the current weather.*

## 🔄 How It Works

The application follows this workflow:

```text
User enters city
       ↓
Geocoding API
       ↓
City → Latitude & Longitude
       ↓
Current Weather API
       ↓
JSON Response
       ↓
Extract weather information
       ↓
Display results
```

### 1. Get the city name

The user enters a location:

```python
Your_location = input("Enter your location: ").strip()
```

### 2. Geocode the location

The OpenWeatherMap Geocoding API converts the city name into coordinates:

```text
Kathmandu → latitude + longitude
```

### 3. Fetch weather data

Those coordinates are sent to the Current Weather API.

The request uses:

```text
units=metric
```

so temperatures are displayed in **Celsius**.

### 4. Parse JSON

The API returns JSON containing nested data such as:

```text
main
weather
wind
sys
```

The program extracts the required values from these sections.

### 5. Display the weather

The extracted information is formatted and displayed in the terminal.

## 🧠 Concepts Learned

This project helped practice several important Python and API concepts:

* `requests.get()`
* REST APIs
* HTTP requests
* Query parameters
* API authentication
* JSON responses
* Lists and dictionaries
* Nested dictionaries
* `.get()` with default values
* Exception handling
* `try` / `except`
* `RequestException`
* `JSONDecodeError`
* Reading files with `open()`
* User input
* String formatting
* Working with external data

## 🛡️ Error Handling

The application handles several possible problems:

### Missing API key file

```text
❌ API key file not found
```

### Empty API key

```text
❌ The API key file is empty.
```

### Network problems

For example:

* No internet connection
* Timeout
* DNS failure

```text
❌ Network error while fetching weather
```

### Invalid city

```text
❌ Could not find 'UnknownCity'
```

### Invalid JSON response

```text
❌ Weather API did not return valid JSON.
```

### API errors

The program checks the API response code and displays the returned error message when necessary.

## 📚 APIs Used

### OpenWeatherMap Geocoding API

Used to convert a location name into geographic coordinates.

```text
City → Latitude + Longitude
```

### OpenWeatherMap Current Weather API

Used to retrieve current weather information based on latitude and longitude.

```text
Latitude + Longitude → Current Weather
```

## 🎯 Project Goal

The goal of this project is not only to create a weather application, but also to learn how Python programs can communicate with **real-world APIs** and process the JSON data they return.

This project is part of my **AI/ML learning journey**, where understanding APIs and external data sources is an important foundation for building future data and AI projects.

## 🔮 Future Improvements

Possible improvements for this project include:

* 🌅 Add sunrise and sunset times
* 🌧️ Add weather forecasts
* 📅 Show hourly and daily forecasts
* 🌎 Display more location information
* 🎨 Build a graphical user interface
* 📊 Store weather history
* 🔄 Add automatic weather updates
* 🗺️ Add weather information for multiple cities

---

### 📌 Project Status

**Completed ✅**

Built as part of my **Python → APIs & JSON** learning journey.
