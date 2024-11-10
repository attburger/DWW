import requests, json
from time import *
def sendData(Day):
  url = "Discord Webhook URL"
  complete_url = "Weatherapi.com url"
  response = requests.get(complete_url)
  data = response.json()
  name = data['location']['name']
  country = data['location']['country']
  date = data['forecast']['forecastday'][Day]['date']
  img = data['forecast']['forecastday'][Day]['day']['condition']['icon']
  max_temp_c = data['forecast']['forecastday'][Day]['day']['maxtemp_c']
  min_temp_c = data['forecast']['forecastday'][Day]['day']['mintemp_c']
  avg_temp_c = data['forecast']['forecastday'][Day]['day']['avgtemp_c']
  maxwind_kph = data['forecast']['forecastday'][Day]['day']['maxwind_kph']
  avghumidity = data['forecast']['forecastday'][Day]['day']['avghumidity']
  daily_chance_of_rain = data['forecast']['forecastday'][Day]['day']['daily_chance_of_rain']
  sunrise = data['forecast']['forecastday'][Day]['astro']['sunrise']
  sunset = data['forecast']['forecastday'][Day]['astro']['sunset']
  dataJson2 = {
    "content": "",
      "embeds": [
      {
        "title": F"Das Wetter in {name},{country}\n für den {date}!",
        "description": F"Maximale Temperatur:**{max_temp_c}°C** \nMinimale Temperatur:**{min_temp_c}°C** \navg. Temperatur:**{avg_temp_c}°C** \nWindspeed:**{maxwind_kph} km/h** \nLuftfeuchtigkeit: **{avghumidity}%** \nRegenwahrscheinlichkeit: **{daily_chance_of_rain}%** \nSonnenaufgang: **{sunrise} Uhr** \nSonnenuntergang: **{sunset} Uhr**",
        "thumbnail": {
          "url": F"https:{img}"
        }
      }
    ],
    }
  result = requests.post(url, json = dataJson2)
  try:
    result.raise_for_status()
  except requests.exceptions.HTTPError as err:
    print(err)
  else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
while True:
    time1 = strftime("%H%M%S", localtime())
    sleep(1)
    if time1 == "070000":
        sendData(0)
    if time1 == "210000":
        sendData(1)
