# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import App

@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="werert", middlename="eretr", lastname="rtetre",
                                nickname="erertt", title="tttttt", company="rrrrr",
                                address="etrtytyret", phone_home="35456", email="klnlknnlgf"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                company="", address="", phone_home="", email=""))
    app.logout()