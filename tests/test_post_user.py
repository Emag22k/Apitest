import pytest
import requests
import allure
from models import CreatedUserResponse

BASE_URL = "https://reqres.in/api"

@allure.feature("POST User")
@pytest.mark.positive
def test_create_user(user_payload):
    """Позитивный тест: создание пользователя"""
    response = requests.post(f"{BASE_URL}/users", json=user_payload)
    assert response.status_code == 201, "Код ответа должен быть 201"

    parsed_response = CreatedUserResponse(**response.json())
    assert parsed_response.name == user_payload["name"]
    assert parsed_response.job == user_payload["job"]

@allure.feature("POST User")
@pytest.mark.negative
def test_create_user_invalid_data(invalid_user_payload):
    """Негативный тест: создание пользователя с пустыми данными"""
    response = requests.post(f"{BASE_URL}/users", json=invalid_user_payload)
    assert response.status_code == 201, "reqres.in все равно создает пользователя, ожидаем 201"
    data = response.json()
    assert "name" not in data or data["name"] == "", "Имя не должно быть установлено"
    assert "job" not in data or data ["job"] == "", "Работа не должно быть установлено"
