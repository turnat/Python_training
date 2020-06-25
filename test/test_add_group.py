# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="NameG", header="header", footer="bla bla bla"))
    app.session.logaut()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logaut()

if __name__ == "__main__":
  pytest.main()
















# После выполнения всех действий мы не должны забыть закрыть окно браузера
#driver.quit()
