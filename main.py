appid = os.environ['APPID']
url = "https://api.openweathermap.org/data/2.5/onecall"
lat = 48.464718
lon = 35.046185
import requests
from twilio.rest import Client
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": appid,
    "exclude": "current,minutely,daily"
}
response = requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour in weather_slice:
    if hour['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+18643875952',
        to='+380664110994'
    )
print(message.status)







