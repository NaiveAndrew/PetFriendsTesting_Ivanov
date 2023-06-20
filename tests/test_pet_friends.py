from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

#1----------------------------------------------------------------------------------------------------------------------

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

#2----------------------------------------------------------------------------------------------------------------------

def test_add_new_pet_simple_with_valid_data(name='Чувак', animal_type='Пес', age='3'):
    """Проверяем, что можно создать питомца с корректными данными"""

    # Запрашиваем ключ API и сохраняем его в переменной auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Создаем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Проверяем полученный ответ и ожидаемый результат
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age

#3----------------------------------------------------------------------------------------------------------------------

def test_get_list_of_my_pets(filter="my_pets"):
    """Проверяем, что получаем список питомцев. После запуска предыдущего теста список питомцев обязан содержать
    хотя бы одного питомца"""

    # Запрашиваем ключ API и сохраняем его в переменной auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем список питомцев
    status, result = pf.get_list_of_pets(auth_key, filter)

    # Проверяем полученный ответ и ожидаемый результат
    assert status == 200
    assert len(result) > 0
    print(result)

#4----------------------------------------------------------------------------------------------------------------------

def test_add_pet_photo_with_valid_data(pet_photo='images/dog1.jpg'):
    """Проверяем, что можно установить фото для питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменной pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ API и сохраняем его в переменной auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем список своих питомцев и сохраняем его в переменной my_pets
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    # Устанавливаем фото для питомца
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)

    # Проверяем полученный ответ и ожидаемый результат
    assert status == 200
    assert result["id"] == pet_id
    assert len(result["pet_photo"])>0

#5----------------------------------------------------------------------------------------------------------------------
def test_add_new_pet_with_invalid_data(name='0', animal_type='0', age='0',pet_photo = "images/racoon1.pdf"):
    """Проверяем, что получаем ошибку при добавлении питомца с некорректными данными и некорректным по формату изображением"""

    # Запрашиваем ключ API и сохраняем его в переменной auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Проверяем полученный ответ и ожидаемый результат
    assert status == 400  # Ожидаемый статус код 400 - Неверный запрос
    """ Фактический статус == 200, питомец добавляется, хотя не должен. 
    Данный тест провалился, значит в приложении есть баги"""

#6----------------------------------------------------------------------------------------------------------------------

def test_get_api_key_for_invalid_user(email="invalid_email", password="invalid_pass"):
    """ Проверяем что запрос api ключа возвращает статус 403, если мы вводим неверные данные пользователя"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'Forbidden' in result
    print(result)

#7----------------------------------------------------------------------------------------------------------------------
def test_update_pet_with_invalid_pet_id(name='Корень', animal_type='Енот', age=5):
    """Проверяем, что получаем ошибку при попытке обновления данных питомца с некорректным id"""

    # Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pet_id = "invalid_id"  # Некорректный идентификатор питомца

    status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)

    # Проверяем полученный ответ и ожидаемый результат
    assert status == 400  # Ожидаемый статус код 400 - Неверный запрос
    assert 'Bad Request' in result
    print(result)

#8----------------------------------------------------------------------------------------------------------------------

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

#9----------------------------------------------------------------------------------------------------------------------

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Ракета", "Енот", "4", "images/racoon1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

#10----------------------------------------------------------------------------------------------------------------------

def test_successful_update_self_pet_info(name='Мох', animal_type='Лось', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")