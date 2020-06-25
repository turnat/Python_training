# -*- coding: utf-8 -*-
import unittest
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="NameG", header="header", footer="bla bla bla"))
        self.app.logaut()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logaut()

    def tearDown(self):
       self.app.destroy()



if __name__ == "__main__":
   pytest.main()
















# После выполнения всех действий мы не должны забыть закрыть окно браузера
#driver.quit()
