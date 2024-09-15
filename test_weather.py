import sys
import pytest
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch
import unittest
from GT import get_weather_data, WeatherApp

def test_api_response_200():
    api_response = {
        'cod': 200
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = api_response
        mock_get.return_value.status_code = 200
        mock_get.return_value.ok = True

        city = "Moscow"
        response = get_weather_data(city)

        assert response['cod'] == 200, "Ожидали 200"

class TestWeatherApp(unittest.TestCase):
    def test_temp(self):
        data = get_weather_data("Moscow")
        temp = data["main"]["temp"]
        self.assertGreaterEqual(temp, -50)
        self.assertLessEqual(temp, 50)

def test_image():
    @pytest.mark.parametrize("image_filename", [
        'clear.jpg',
        'cloudy.jpg',
        'rainy.jpg',
        'sunny.jpg',
        'default_weather.jpg'
    ])

    def test_image_exists(image_filename):
        image_directory = 'C:\PycharmProjects\kivi_app\weather_forecast_app_kivy'
        image_path = os.path.join(image_directory, image_filename)

        assert os.path.isfile(image_path), f"Файл {image_filename} не найден в директории {image_directory}"





