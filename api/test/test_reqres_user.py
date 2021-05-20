import requests
import pytest
from hamcrest import assert_that, equal_to, has_key, contains_exactly, contains

EXPECTED_NOT_FOUND_IN_GET = "Expected results not found in GET \"/users\" endpoint"


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
