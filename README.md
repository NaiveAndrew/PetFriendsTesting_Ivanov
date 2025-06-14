# PetFriendsTesting_Ivanov
# Проект автоматического тестирования сайта PetFriends

## Описание проекта

Этот проект предназначен для автоматизированного тестирования API сайта [PetFriends](https://petfriends.skillfactory.ru). Тесты написаны с использованием `pytest` и охватывают как позитивные, так и негативные сценарии. Документация API доступна на [Swagger](https://petfriends.skillfactory.ru/apidocs/#/).

## Структура проекта

### 1. `api.py`

Содержит библиотеку функций для работы с API.

### 2. `settings.py`

Импортирует переменные окружения `valid_email` и `valid_password` из `.env` с помощью `dotenv`.

### 3. `test_pet_friends.py`

Набор автоматических тестов:

- `test_get_api_key_for_valid_user` — **позитивный**
- `test_add_new_pet_simple_with_valid_data` — **позитивный**
- `test_get_list_of_my_pets` — **позитивный**
- `test_add_pet_photo_with_valid_data` — **позитивный**
- `test_add_new_pet_with_invalid_data` — **негативный** (выполняется, но ожидается ошибка — обнаружен баг)
- `test_get_api_key_for_invalid_user` — **негативный**
- `test_update_pet_with_invalid_pet_id` — **негативный**
- `test_get_all_pets_with_valid_key` — **позитивный**
- `test_successful_delete_self_pet` — **позитивный**
- `test_successful_update_self_pet_info` — **позитивный**

### 4. `tests/images/`

Папка с изображениями для тестов.

### 5. `.env`

Файл с переменными окружения:
- `valid_email`
- `valid_password`

---

# PetFriends Website Testing Project

## Project Description

This project is for automated testing of the [PetFriends](https://petfriends.skillfactory.ru) website API. The tests are written using `pytest` and cover both positive and negative scenarios. API documentation is available on [Swagger](https://petfriends.skillfactory.ru/apidocs/#/).

## Project Structure

### 1. `api.py`

Contains API interaction methods.

### 2. `settings.py`

Loads environment variables `valid_email` and `valid_password` from `.env` using `dotenv`.

### 3. `test_pet_friends.py`

Set of automated tests:

- `test_get_api_key_for_valid_user` — **positive**
- `test_add_new_pet_simple_with_valid_data` — **positive**
- `test_get_list_of_my_pets` — **positive**
- `test_add_pet_photo_with_valid_data` — **positive**
- `test_add_new_pet_with_invalid_data` — **negative** (test fails as it reveals a bug)
- `test_get_api_key_for_invalid_user` — **negative**
- `test_update_pet_with_invalid_pet_id` — **negative**
- `test_get_all_pets_with_valid_key` — **positive**
- `test_successful_delete_self_pet` — **positive**
- `test_successful_update_self_pet_info` — **positive**

### 4. `tests/images/`

Directory with test images.

### 5. `.env`

Contains login credentials:
- `valid_email`
- `valid_password` 
