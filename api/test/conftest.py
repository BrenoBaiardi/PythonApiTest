import shutil

import pytest
import requests
from py.path import local

pytest_plugins = [
    "test",
]

BASE_PATH = 'https://reqres.in/api'
USERS_ENDPOINT = '/users'
REGISTER_ENDPOINT = "/register"


@pytest.fixture()
def base_url():
    """ :return: the API base url"""
    return BASE_PATH


@pytest.fixture()
def base_url():
    """ :return: the API base url"""
    return BASE_PATH


@pytest.fixture
def users_url(base_url):
    """ Adds the users endpoint to the base url
    :return: the API base url with the users endpoint
    :rtype: String"""
    return base_url + USERS_ENDPOINT


@pytest.fixture
def register_url(base_url):
    """ Adds the users endpoint to the base url
    :return: the API base url with the users endpoint
    :rtype: String"""
    return base_url + REGISTER_ENDPOINT


@pytest.fixture()
def new_user_body():
    return {
        "email": "eve.holt@reqres.in",
        "password": "password"
    }


@pytest.fixture()
def non_compliant_user_body():
    return {
        "email": "eve.holt@reqres.in",
    }


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


@pytest.fixture()
def csv_cores():
    return "cores.csv"


@pytest.fixture()
def popular_csv_cores(csv_cores):
    # setUp
    cores_file = open(csv_cores, mode='w')
    cores_file.writelines("Azul,1")
    cores_file.close()
    yield cores_file.name
    # tearDown
    open(csv_cores, mode='w').close()


@pytest.fixture()
def criar_arquivo_customizado_com_tmpdir(tmpdir) -> local:
    print(tmpdir.dirname)
    path_arquivo = tmpdir.join('foo.txt')
    path_arquivo.write("texto escrito")
    yield path_arquivo
    shutil.rmtree(path_arquivo.dirname)
