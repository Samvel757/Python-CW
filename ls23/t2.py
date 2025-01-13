import requests
from bs4 import BeautifulSoup


url = "https://wttr.in/Astana"


response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    weather_data = soup.get_text()
    
    print("Погода в Астане:\n")
    print(weather_data)
else:
    print(f"Ошибка при запросе: {response.status_code}")