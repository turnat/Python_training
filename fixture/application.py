# -*- coding: utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)


    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Группы").click()

    def create_group(self, group):
        wd = self.wd
        # init group creation
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Группы").click()


    def open_home_page(self):
        wd = self.wd
        # развернуть браузер на весь экран
        wd.maximize_window()
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
        driver.quit()


