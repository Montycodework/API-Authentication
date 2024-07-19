# website link -  https://openweathermap.org/forecast5#list


import requests
from twilio.rest import Client


# 30d033aecbe1173d70f95e36ec5f309e



own_endpoint ="https://api.openweathermap.org/data/2.5/forecast"
api_key = "Your api key"

account_sid = 'Your sid'
auth_token = 'Your auth token'

# lat = 28.6667
# lon = 77.2167

parameters = {
    "lat":17.314260,
    "lon":78.675774,
    "appid":api_key,
    "cnt":4,
}


# response  = requests.get(url=f"api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}")
response  = requests.get(own_endpoint, params=parameters)
# print(response.status_code)

response.raise_for_status()

weather_data = response.json()

# https://openweathermap.org/weather-conditions

# print(weather_data)

# weather_id = weather_data["list"][0]["weather"][0]["id"]
# print(weather_id)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an Umbrella") # Here you get multiple print if condition code is less than 700
        # but there is a other way to do this
        will_rain = True
if will_rain:
    # print("Bring an Umbrella")
    # Now we are going to use twilio api to send the mesg
    # recovery_code for twilio = NQU18YYCZV7XRG691FUKV8FV
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to be rain today",
        from_='Twilio virtual number',
        to='reciever contact number'
    )
    print(message.status)
# now search rain location on map and use lat long
# https://www.ventusky.com/?p=50.0;13.9;5&l=temperature-2m

