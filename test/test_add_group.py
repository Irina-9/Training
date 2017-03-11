# -*- coding: utf-8 -*-
import pytest

from fixture.application import App
from model.group import Group


@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="111111", header="2222", footer="333"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()