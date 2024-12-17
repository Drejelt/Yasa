import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

try:
    user_city_input = input('Введите название города: ').lower()
    url = f"https://sinoptik.ua/погода-{user_city_input}"

    # A dictionary to map the class names of elements we need to scrape
    class_dict = {
        "temperature": "_6fYCPKSx",
        "day": "BzO81ZRx",
        "city_date_time": "fqWbgkcF"
    }

    # Setting the headers to simulate a request from a browser (to avoid being blocked by the website)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    # Sending a GET request to the specified URL with the headers
    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.text, 'html.parser')


    # Extracting the day of the week, temperature, and city/date/time using the class names from the dictionary
    day_element = html.find(class_=class_dict["day"])
    temp_element = html.find(class_=class_dict["temperature"])
    city_date_time_element = html.find(class_=class_dict["city_date_time"])

    # Printing the extracted information in a readable format (with title case for the day)
    print(f"Сегодня: {day_element.text.title()}, Температура: {temp_element.text}, Информация актуальная для г.{city_date_time_element.text}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при подключении к серверу: {e}")

except AttributeError:
    print("Оу, видимо ничего нет. Проверьте введённое название города.")
