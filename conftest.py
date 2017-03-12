import pytest
from fixture.application import App


@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture