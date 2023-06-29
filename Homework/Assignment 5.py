import requests

def get_weather(api_key, city):
    url = f" http://www.google.com/ig/api?weather=Mumbai"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant weather information from the API response
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"Weather in {city}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Failed to retrieve weather data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    city = input("Enter the city name: ")
    get_weather(api_key, city)
