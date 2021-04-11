import requests
import json
import pytest
from hamcrest import assert_that, equal_to, has_key


def test_get_users_is_sucess():
    response = requests.get("https://reqres.in/api/users")
    assert response.status_code == 200


def test_create_user_returns_success():
    sample_user = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post("https://reqres.in/api/users", sample_user)
    assert_that(response.status_code, equal_to(201))
    response_json = response.json()
    assert_that(response_json["name"], equal_to("morpheus"))
    assert_that(response_json["job"], equal_to("leader"))
    assert_that(response_json, has_key("createdAt"))
