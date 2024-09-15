# The-weather-forecast-app
This is an application for displaying the current weather in a selected city, written using Kivy. The application uses the [OpenWeatherMap] API(https://openweathermap.org /) to get weather data. Users can enter the name of the city and get information about the current temperature, humidity, pressure, wind speed and description of weather conditions.

Functional
- Enter the name of the city to get weather data.
- Displays temperature, pressure, humidity, wind speed and weather descriptions.
- Dynamically change the background image depending on weather conditions (clear, cloudy, rainy, etc.).

![image](https://github.com/user-attachments/assets/29007011-0d2c-4c13-aa52-ae96e3c023b8)     ![image](https://github.com/user-attachments/assets/585c1df4-b0dc-4dc2-82d89c3786cea223)   ![image](https://github.com/user-attachments/assets/ee9138ef-53d1-4855-a8ec-cd760d79b4b6)



- Tests

API Tests:
The test verifies that the get_weather_data function returns the correct response from the API with code 200.

Temperature test:
Checks that the temperature in Moscow is within reasonable limits (-50°C to 50°C)

Test for the presence of images:
Checks that all necessary images are present in the application directory.

![image](https://github.com/user-attachments/assets/164aefd5-aa8f-4873-ab06-1353e61a8825)


Hung up:
Python 3.x
Kivy
requests
pytest
unittest.mock

Why This Project is Useful:
1) Learning Kivy Framework: This project serves as a great introduction to building graphical user interfaces (GUI) with the Kivy framework. It demonstrates key Kivy features such as layouts, buttons, text inputs, and dynamic background changes.

2) Real-time API Integration: It teaches how to interact with external APIs (in this case, OpenWeatherMap) to fetch real-time data, process it, and display it in a user-friendly format.

3) Dynamic User Experience: By changing the background based on weather conditions, this project showcases how to make an interactive and visually engaging user experience that reacts to real-world data.

4) Practical Application: Weather forecasting is a practical and widely used feature in many applications, making this project applicable to real-world scenarios.

5) Testing Integration: The project includes unit tests that demonstrate how to mock API responses and verify different aspects of the application. This helps in learning testing best practices, which are essential for reliable and maintainable software.

Overall, the project offers a hands-on approach to developing a functional, interactive application that integrates with external data sources, providing value for both learners and developers looking to implement weather-based features.
