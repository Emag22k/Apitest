import pytest
import requests
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature("DELETE User")
@pytest.mark.positive
def test_delete_user():
    """Позитивный тест: удаление пользователя"""
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204, "Код ответа должен быть 204"

@allure.feature("DELETE User")
@pytest.mark.negative
def test_delete_nonexistent_user():
    """Негативный тест: удаление несуществующего пользователя"""
    response = requests.delete(f"{BASE_URL}/users/998855")
    assert response.status_code in [204, 404], "Может вернуть 204 или 404"
