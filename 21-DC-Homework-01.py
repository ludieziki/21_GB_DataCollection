import requests

# Запрос на ввод категории
category = input("Введите интересующую вас категорию поиска (кофейни, кафе, музеи, парки, стадионы, магазины и т.д.): ")

#Получение географических координат устройства
#Для примера будем использовать фиксированные координаты центра Москвы
latitude = 55.7558
longitude = 37.6176

#Отправка запроса к API Foursquare
client_id = "YOUR_CLIENT_ID"  # Вставьте свой Client ID
client_secret = "YOUR_CLIENT_SECRET"  # Вставьте свой Client Secret
url = f"https://api.foursquare.com/v2/venues/search?client_id={client_id}&client_secret={client_secret}&ll={latitude},{longitude}&query={category}&v=20220101&radius=1000"

response = requests.get(url)
data = response.json()

#Обработка результатов запроса
venues = data["response"]["venues"]
for venue in venues:
name = venue["name"]
address = venue["location"]["formattedAddress"]
rating = venue["rating"] if "rating" in venue else "Рейтинг не указан"
print(f"Название: {name}, Адрес: {address}, Рейтинг: {rating}")