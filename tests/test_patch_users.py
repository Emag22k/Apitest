import pytest
import requests
import allure
from models import UpdatedUserResponse

BASE_URL = "https://reqres.in/api"

@allure.feature("PATCH User")
@pytest.mark.positive
def test_update_user(user_payload):
    """Позитивный тест: обновление данных пользователя"""
    response = requests.patch(f"{BASE_URL}/users/2", json=user_payload)
    assert response.status_code == 200, "Код ответа должен быть 200"

    parsed_response = UpdatedUserResponse(**response.json())
    assert parsed_response.name == user_payload["name"]
    assert parsed_response.job == user_payload["job"]

@allure.feature("PATCH User")
@pytest.mark.negative
def test_update_nonexistent_user(user_payload):
    """Негативный тест: обновление несуществующего пользователя"""
    response = requests.patch(f"{BASE_URL}/users/9999", json=user_payload)
    assert response.status_code in [404, 200], "Код ответа может быть 404 или 200"
