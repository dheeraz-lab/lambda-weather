import json
import requests

def lambda_handler(event, context):
    api_key = "your_api_key_here"  # 🔁 Replace with your actual OpenWeatherMap API key
    city = "New York"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data["main"]["temp"]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "city": city,
                "temperature_fahrenheit": temperature
            })
        }

    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
