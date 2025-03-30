import pytest
import requests

BASE_URL = "https://reqres.in/api"

@pytest.fixture
def user_payload():
    return {"name": "Barney Stinson", "job": "QA Engineer"}

@pytest.fixture
def invalid_user_payload():
    return {"name": "", "job": ""}  # invalid data
