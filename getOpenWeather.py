#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

from config import APPID

# # Compute location from command line arguments.
# if len(sys.argv) < 2:
# 	print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
# 	sys.exit()
# location = ' '.join(sys.argv[1:])

# # Download the JSON data from OpenWeatherMap.org's API
# url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID%s ' % (location, APPID)
# response = requests.get(url)
# response.raise_for_status()

# Compute location from command line arguments.
if len(sys.argv) < 2:
	print('Usage: getOpenWeather.py <lattitude> <longitude>')
	sys.exit()
lat = sys.argv[1]
lon = sys.argv[2]

# Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely,hourly&appid=%s' % (lat, lon, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# print(response.text)

# Load JSON data into a python variable.
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData # ['list']

print('Current weather at %s, %s:' % (lat, lon))
print(w['current']['weather'][0]['main'], '-', w['current']['weather'][0]['description'])
print()
print('Tomorrow:')
print(w['daily'][0]['weather'][0]['main'], '-', w['daily'][0]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w['daily'][1]['weather'][0]['main'], '-', w['daily'][0]['weather'][0]['description'])

# EXAMPLE RETURN DATA
# {
# 	'lat': 43.66, 'lon': -79.38, 'timezone': 'America/Toronto', 'timezone_offset': -14400,
# 	'current': {
# 		'dt': 1599522589, 'sunrise': 1599475716, 'sunset': 1599522150, 'temp': 293.07, 'feels_like': 292.76, 'pressure': 1012, 'humidity': 72, 'dew_point': 287.88, 'uvi': 6.36, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 80, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'rain': {}
# 	},
# 	'daily': [
# 		{'dt': 1599498000, 'sunrise': 1599475716, 'sunset': 1599522150, 'temp': {'day': 293.07, 'min': 290.17, 'max': 293.2, 'night': 290.17, 'eve': 293.2, 'morn': 293.07}, 'feels_like': {'day': 292.2, 'night': 287.17, 'eve': 292.59, 'morn': 292.2}, 'pressure': 1012, 'humidity': 72, 'dew_point': 287.88, 'wind_speed': 3.41, 'wind_deg': 292, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': 90, 'pop': 0.63, 'rain': 0.57, 'uvi': 6.36
# 		},
# 		{'dt': 1599584400, 'sunrise': 1599562183, 'sunset': 1599608441, 'temp': {'day': 287.59, 'min': 287.59, 'max': 289.06, 'night': 288.62, 'eve': 289.03, 'morn': 289.06}, 'feels_like': {'day': 282.93, 'night': 286.27, 'eve': 285.72, 'morn': 285.35}, 'pressure': 1022, 'humidity': 61, 'dew_point': 280.33, 'wind_speed': 5.67, 'wind_deg': 41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': 100, 'pop': 1, 'rain': 1.46, 'uvi': 6.43
# 		},
# 		{'dt': 1599670800, 'sunrise': 1599648649, 'sunset': 1599694731, 'temp': {'day': 292.5, 'min': 288.3, 'max': 293.33, 'night': 288.5, 'eve': 291.06, 'morn': 288.3}, 'feels_like': {'day': 290.69, 'night': 284.95, 'eve': 288.75, 'morn': 285.39}, 'pressure': 1026, 'humidity': 58, 'dew_point': 284.15, 'wind_speed': 2.99, 'wind_deg': 65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': 98, 'pop': 0, 'uvi': 6.3
# 		},
# 		{'dt': 1599757200, 'sunrise': 1599735116, 'sunset': 1599781022, 'temp': {'day': 292.03, 'min': 287.35, 'max': 292.03, 'night': 287.57, 'eve': 289.49, 'morn': 287.35}, 'feels_like': {'day': 290.4, 'night': 284.98, 'eve': 286.23, 'morn': 284.75}, 'pressure': 1029, 'humidity': 55, 'dew_point': 282.97, 'wind_speed': 2.25, 'wind_deg': 13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': 95, 'pop': 0, 'uvi': 6.34
# 		},
# 		{'dt': 1599843600, 'sunrise': 1599821582, 'sunset': 1599867312, 'temp': {'day': 291.25, 'min': 286.22, 'max': 291.31, 'night': 289.6, 'eve': 290.16, 'morn': 286.22}, 'feels_like': {'day': 287.62, 'night': 286.78, 'eve': 287.2, 'morn': 283.22}, 'pressure': 1027, 'humidity': 46, 'dew_point': 279.5, 'wind_speed': 3.97, 'wind_deg': 103, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': 0, 'pop': 0, 'uvi': 6.77
# 		},
# 		{'dt': 1599930000, 'sunrise': 1599908049, 'sunset': 1599953602, 'temp': {'day': 293.21, 'min': 289.77, 'max': 293.86, 'night': 293.08, 'eve': 293.86, 'morn': 289.77}, 'feels_like': {'day': 292.18, 'night': 291.75, 'eve': 293.72, 'morn': 286.5}, 'pressure': 1016, 'humidity': 67, 'dew_point': 287.01, 'wind_speed': 3.15, 'wind_deg': 114, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'clouds': 100, 'pop': 1, 'rain': 30.87, 'uvi': 6.07
# 		},
# 		{'dt': 1600016400, 'sunrise': 1599994515, 'sunset': 1600039891, 'temp': {'day': 296.77, 'min': 287.18, 'max': 296.77, 'night': 287.18, 'eve': 290.98, 'morn': 293.41}, 'feels_like': {'day': 294.29, 'night': 282.96, 'eve': 287.06, 'morn': 293.23}, 'pressure': 1012, 'humidity': 57, 'dew_point': 288.01, 'wind_speed': 5.64, 'wind_deg': 306, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'clouds': 26, 'pop': 1, 'rain': 9.67, 'uvi': 5.79
# 		},
# 		{
# 			'dt': 1600102800, 'sunrise': 1600080982, 'sunset': 1600126181, 'temp': {'day': 290.5, 'min': 285.43, 'max': 290.66, 'night': 287.88, 'eve': 289.22, 'morn': 285.43}, 'feels_like': {'day': 287.55, 'night': 286.08, 'eve': 286.61, 'morn': 281.99}, 'pressure': 1024, 'humidity': 39, 'dew_point': 276.67, 'wind_speed': 2.14, 'wind_deg': 103, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': 0, 'pop': 0,
# 			'uvi': 5.69
# 		}
# 	]
# }