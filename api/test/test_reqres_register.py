from hamcrest import equal_to, assert_that
from requests import post

from api.test.AssertFailedMessages import AssertFailedMessages as message


def test_register_new_user_is_sucess(new_user_body, register_url):
    response = post(register_url, new_user_body)
    assert_that(response.status_code, equal_to(200), message.EXPECTED_NOT_FOUND_IN_POST_REGISTER.value)


def test_register_new_user_missing_password_is_fail(non_compliant_user_body, register_url):
    response = post(register_url, non_compliant_user_body)
    assert_that(response.status_code, equal_to(400), message.EXPECTED_NOT_FOUND_IN_POST_REGISTER.value)
