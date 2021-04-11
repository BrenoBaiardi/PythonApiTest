import requests
import pytest
from hamcrest import assert_that, equal_to, has_key, contains_exactly, contains

USERS_PATH = 'https://reqres.in/api/users'


@pytest.fixture
def get_users():
    """ Returns a response to a get request with the users endpoint
    :return: the response"""
    return requests.get(USERS_PATH)


def test_get_users_is_sucess(get_users):
    response = get_users
    users_list = response.json()["data"]
    users_list_not_empty = len(users_list) > 0
    expected = (True, requests.codes["ok"])
    actual = (users_list_not_empty, response.status_code)
    assert_that(actual, equal_to(expected), "Expected results not found in get \"/users\" endpoint")


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
