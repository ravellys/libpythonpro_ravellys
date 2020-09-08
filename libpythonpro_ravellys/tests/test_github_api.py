from unittest.mock import Mock

import pytest

from libpythonpro_ravellys import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars3.githubusercontent.com/u/3457115?v=4"
    resp_mock.json.return_value = {"login": "renzon",
                                   "id": 3457115,
                                   "avatar_url": url}
    get_mock = mocker.patch('libpythonpro_ravellys.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_github_api(avatar_url):
    url = github_api.buscar_avatar('renzon')
    assert url == avatar_url


def test_github_api_integracao():
    url = github_api.buscar_avatar('renzo')
    assert url == 'https://avatars3.githubusercontent.com/u/402714?v=4'
