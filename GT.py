import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

def get_weather_data(city):
    api_key = "c75f410829ff4eecded6044061b1396f"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={api_key}"
    response = requests.get(url)
    return response.json()

def convert_pressure_to_mm_hg(pressure_hpa):
    return int(pressure_hpa * 0.750063755419211)

class WeatherApp(App):
    def build(self):
        Window.size = (360, 640)

        self.layout = RelativeLayout()

        self.background = Image(source='clear.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.background)

        self.city_input = TextInput(
            hint_text="Введите название города",
            font_size=20,
            size_hint=(0.8, None),
            height=40,
            pos_hint={'center_x': 0.5, 'y': 0.8},
            background_color=(0, 0, 0, 0.5),
            foreground_color=(1, 1, 1, 1)
        )
        self.layout.add_widget(self.city_input)

        self.update_button = Button(
            text="Обновить погоду",
            font_size=20,
            size_hint=(0.5, None),
            height=50,
            pos_hint={'center_x': 0.5, 'y': 0.7},
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1)
        )
        self.update_button.bind(on_press=self.update_weather)
        self.layout.add_widget(self.update_button)

        self.weather_label = Label(
            text="Введите название города и нажмите 'Обновить погоду'",
            size_hint=(1, 0.7),
            color=(1, 1, 1, 1),
            font_size='20sp',
            width=300,
            halign='center',
            valign='middle',
            text_size=(300, None)
        )
        self.weather_label.bind(
            size=self.weather_label.setter('text_size'))
        self.layout.add_widget(self.weather_label)

        return self.layout

    def update_weather(self, instance=None):
        city = self.city_input.text.strip()
        data = get_weather_data(city)
        if data["cod"] == 200:
            temp = int(data["main"]["temp"])
            pressure_hpa = data["main"]["pressure"]
            pressure_mm_hg = convert_pressure_to_mm_hg(pressure_hpa)
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            city_name = data["name"]
            weather_main = data["weather"][0]["main"].lower()

            if "clear" in weather_main:
                self.background.source = 'clear.jpg'
            elif "clouds" in weather_main:
                self.background.source = 'cloudy.jpg'
            elif "rain" in weather_main or "drizzle" in weather_main:
                self.background.source = 'rainy.jpg'
            elif "sunny" in weather_main:
                self.background.source = 'sunny.jpg'
            else:
                self.background.source = 'default_weather.jpg'

            weather_info = (
                f"Город: {city_name}\n"
                f"Температура: {temp}°C\n"
                f"Давление: {pressure_mm_hg} мм рт. ст.\n"
                f"Описание: {description}\n"
                f"Влажность: {humidity}%\n"
                f"Скорость ветра: {wind_speed} м/с"
            )
            print(weather_info)
            self.weather_label.text = weather_info
        else:
            self.weather_label.text = "Не удалось получить данные о погоде."

if __name__ == '__main__':
    WeatherApp().run()
