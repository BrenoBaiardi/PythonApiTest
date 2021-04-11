import requests
import pytest
from hamcrest import assert_that, equal_to, has_key, contains_exactly, contains

EXPECTED_NOT_FOUND_IN_GET = "Expected results not found in GET \"/users\" endpoint"

BASE_PATH = 'https://reqres.in/api'
USERS_ENDPOINT = '/users'


@pytest.fixture
def base_url():
    """ :return: the API base url"""
    return BASE_PATH


@pytest.fixture
def users_url(base_url):
    """ Adds the users endpoint to the base url
    :return: the API base url with the users endpoint """
    return base_url + USERS_ENDPOINT


@pytest.fixture
def get_users_list(users_url):
    """ Sends get request to obtain the users list
    :return: the response containing the list"""
    return requests.get(users_url)


@pytest.fixture
def post_user(users_url):
    """ Sends post request to create a user to the users endpoint
    :return: the response concerning the creation"""
    sample_user = {
        "name": "morpheus",
        "job": "leader"
    }
    return requests.post(users_url, sample_user)


@pytest.fixture
def put_user(users_url):
    """ Sends put request to update a user to the users endpoint
    :return: the response concerning the update"""
    sample_user = {
        "name": "morpheus",
        "job": "another job"
    }
    return requests.put(users_url, sample_user)


def test_get_users_is_sucess(get_users_list):
    response = get_users_list
    users_list = response.json()["data"]
    users_list_not_empty = len(users_list) > 0
    expected = (True, requests.codes["ok"])
    actual = (users_list_not_empty, response.status_code)
    assert_that(actual, equal_to(expected), EXPECTED_NOT_FOUND_IN_GET)


def test_get_single_user(users_url):
    response = requests.get(users_url + "/2")
    user_data = response.json()["data"]
    expected = (True, "Janet", requests.codes["ok"])
    actual = (user_data["id"] == 2,
              user_data["first_name"],
              response.status_code)
    assert_that(actual, equal_to(expected), EXPECTED_NOT_FOUND_IN_GET)


def test_single_user_not_found(users_url):
    response = requests.get(users_url + "/23")
    assert_that(requests.codes["not_found"], equal_to(response.status_code), EXPECTED_NOT_FOUND_IN_GET)


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

def test_update_user_returns_success(put_user):
    response = put_user
    response_json = response.json()
    expected = (
        "morpheus",
        "another job",
        True,
        requests.codes["ok"]
    )
    actual = (
        response_json["name"],
        response_json["job"],
        "updatedAt" in response_json.keys(),
        response.status_code
    )

    assert_that(actual, equal_to(expected), "Expected results not found in POST \"/users\" endpoint")
