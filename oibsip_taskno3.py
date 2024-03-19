# QZBF2ZGWEQMLDE6QJTNSAT6Z3
import requests 
 
def get_weather_data(city, api_key): 
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Pune?unitGroup=metric&key=QZBF2ZGWEQMLDE6QJTNSAT6Z3&contentType=json'
     
    try: 
        response = requests.get(url) 
        data = response.json() 
        return data 
    except Exception as e: 
        print("Error fetching weather data:", e) 
        return None 
 
api_key = 'QZBF2ZGWEQMLDE6QJTNSAT6Z3' 
city = 'pune' 
 
weather_data = get_weather_data(city, api_key) 
if weather_data: 
    for day in weather_data['days']: 
        print("Date:", day['datetime']) 
        print("Temperature (Max):", day['tempmax'], "°C") 
        print("Temperature (Min):", day['tempmin'], "°C") 
        print("Feels Like:", day['feelslike'], "°C") 
        print("Humidity:", day['humidity'], "%") 
        print("Precipitation Probability:", day['precipprob']) 
        print("Wind Speed:", day['windspeed'], "km/h") 
        print("Wind Direction:", day['winddir'], "°") 
        print("Pressure:", day['pressure'], "hPa") 
        print("Cloud Cover:", day['cloudcover'], "%") 
        print("Visibility:", day['visibility'], "km") 
        print("Sunrise:", day['sunrise']) 
        print("Sunset:", day['sunset']) 
else: 
        print("Failed to fetch weather data.")
