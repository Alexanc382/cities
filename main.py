from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key): # передадим в функцию аргументы из city и key
    try:
        geocoder = OpenCageGeocode(key) # создаёт объект geocoder для работы с API OpenCage Geocoding на основе переданного API-ключа 'key'
        results = geocoder.geocode(city, language='ru') # запрос к сервису с передачей 'city', получение данных (координат) с сервера, результат — в results.
        if results: # если всё нормально координаты вернутся в переменную results и запустится if/else
            return results[0]['geometry']['lat'], results[0]['geometry']['lng'] # функция get_... возвращает нам координаты (55.625578, 37.6063916) по 'пути',
            # который мы прописали (см. путь и индексы в файле json с сайта OpenCage)
            # lat - широта, lng - долгота
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка: {e}'

key = 'b129484e1f8f49dc8c1625f078a65dc2'
city = 'London' # указываем город, координаты которого хотим запросить
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')