import pytest
import requests
import allure
from models import UsersListResponse

BASE_URL = "https://reqres.in/api"

@allure.feature("GET Users")
@pytest.mark.positive
def test_get_users():
    """Позитивный тест: получение списка пользователей"""
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200, "Код ответа должен быть 200"

    parsed_response = UsersListResponse(**response.json())
    assert len(parsed_response.data) > 0, "Список пользователей не должен быть пуст"

@allure.feature("GET Users")
@pytest.mark.negative
def test_get_users_invalid_page():
    """Негативный тест: получение пользователей с несуществующей страницей"""
    response = requests.get(f"{BASE_URL}/users?page=228")
    assert response.status_code == 200, "Код ответа должен быть 200 даже для пустых данных"
    assert response.json()["data"] == [], "Должен вернуться пустой список"
