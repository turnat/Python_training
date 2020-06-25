# -*- coding: utf-8 -*-
import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import geckodriver_autoinstaller
driver = webdriver.Chrome()
import unittest, time, re
from group import Group
from application import Application
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#time.sleep(5)
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
#driver.get("http://localhost/addressbook/")
#time.sleep(5)

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
        driver.quit()


if __name__ == "__main__":
    unittest.main()






















































# После выполнения всех действий мы не должны забыть закрыть окно браузера
#driver.quit()
