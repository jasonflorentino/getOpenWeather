#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

from config import APPID

# FROM LESSON -- DOESN'T WORK?

# # Compute location from command line arguments.
# if len(sys.argv) < 2:
# 	print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
# 	sys.exit()
# location = ' '.join(sys.argv[1:])

# # Download the JSON data from OpenWeatherMap.org's API
# url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID%s ' % (location, APPID)
# response = requests.get(url)
# response.raise_for_status()

# REWORKING TO FIT CURRENT API USAGE:

# Get location from command line arguments.
# Toronto = 43.717899 -79.6582408
if len(sys.argv) < 2:
	print('Usage: getOpenWeather.py <lattitude> <longitude>')
	sys.exit()
lat = sys.argv[1]
lon = sys.argv[2]

# TODO make location input more human friendly...

# Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely,hourly&appid=%s' % (lat, lon, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to print raw JSON text:
# print(response.text)

# Load JSON data into a python variable.
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData
print('Current weather at %s, %s:' % (lat, lon))
print(w['current']['weather'][0]['main'], '-', w['current']['weather'][0]['description'])
print()
print('Tomorrow:')
print(w['daily'][0]['weather'][0]['main'], '-', w['daily'][0]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w['daily'][1]['weather'][0]['main'], '-', w['daily'][0]['weather'][0]['description'])