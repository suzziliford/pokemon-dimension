class WeatherAPI:
    base_url = 'http://api.weatherapi.com/v1'
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def _get(self, city, api_method, **params):
        request_url = f"{self.base_url}{api_method}?key={self.api_key}&q={city}"
        if params:
            for key, value in params.items():
                request_url += f"&{key}={value}"
        weather_response = requests.get(request_url)
        if weather_response.ok:
            return weather_response.json()
        else:
            print('There was an error')
        
    def get_current_weather(self, city):
        weather_data = self._get(city, '/current.json')
        city_name = weather_data['location']['name']
        region_name = weather_data['location']['region']
        current_temp = weather_data['current']['temp_f']
        feels_like = weather_data['current']['feelslike_f']
        current_condition = weather_data['current']['condition']['text']
        city_weather = CityWeather(current_temp, feels_like, current_condition, city_name, region_name)
        return city_weather
            
        
class CityWeather:
    def __init__(self, current, feels_like, condition, city_name, region_name):
        self.current = current
        self.feels_like = feels_like
        self.condition = condition
        self.city = city_name
        self.region = region_name
        
    def __str__(self):
        degree_sign = u'\N{DEGREE SIGN}'
        return f"It is currently {self.condition} and {self.current}{degree_sign}F in {self.city}, {self.region}. \
It feels like {self.feels_like}{degree_sign}F"
        
    
client = WeatherAPI('1ac9901266fa4ab48f9185441220510')
my_city = client.get_current_weather('Chicago')