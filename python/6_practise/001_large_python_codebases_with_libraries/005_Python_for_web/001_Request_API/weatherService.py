# weatherService 

import requests

class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5'
    appId = 'c63eddfc3e9836238a7bc178f99c8366'

    @classmethod
    def getForecast(cls, city="new york", country="us"):
        url = f'{cls.baseUrl}/forecast'

        response = requests.get(url, params=[
            ('q', f'{city},{country}'),
            ('mode', 'json'),
            ('APPID', cls.appId)
            ])

        data = response.json()

        return data['list']

if __name__ == "__main__":
    print(WeatherService.getForecast())