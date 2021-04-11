import requests
import pytest
from hamcrest import assert_that, equal_to, has_key, contains_exactly, contains

BASE_PATH = 'https://reqres.in/api'
USERS_ENDPOINT = '/users'


@pytest.fixture
def base_url():
    """ Returns a response to a get request with the users endpoint
    :return: the response"""
    return BASE_PATH

@pytest.fixture
def users_url(base_url):
    """ Returns a response to a get request with the users endpoint
    :return: the response"""
    return base_url + USERS_ENDPOINT


@pytest.fixture
def get_users_list(users_url):
    """ Returns a response to a get request with the users endpoint
    :return: the response"""
    return requests.get(users_url)


@pytest.fixture
def post_user(users_url):
    sample_user = {
        "name": "morpheus",
        "job": "leader"
    }
    """ Returns a response to a post request with the users endpoint
    :return: the response"""
    return requests.post(users_url, sample_user)


def test_get_users_is_sucess(get_users_list):
    response = get_users_list
    users_list = response.json()["data"]
    users_list_not_empty = len(users_list) > 0
    expected = (True, requests.codes["ok"])
    actual = (users_list_not_empty, response.status_code)
    assert_that(actual, equal_to(expected), "Expected results not found in GET \"/users\" endpoint")


def test_get_single_user(users_url):
    response = requests.get(users_url + "/2")
    user_data = response.json()["data"]
    expected = (True, "Janet", requests.codes["ok"])
    actual = (user_data["id"] == 2,
              user_data["first_name"],
              response.status_code)
    assert_that(actual, equal_to(expected), "Expected results not found in GET \"/users\" endpoint")


def test_create_user_returns_success(post_user):
    response = post_user
    response_json = response.json()

    expected = (
        "morpheus",
        "leader",
        True,
        requests.codes["created"]
    )
    actual = (
        response_json["name"],
        response_json["job"],
        "createdAt" in response_json.keys(),
        response.status_code
    )

    assert_that(actual, equal_to(expected), "Expected results not found in POST \"/users\" endpoint")
