#!/usr/bin/env python
# coding=utf-8
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.keys import Keys
import pytest


class Testselenumdemo:
    chromepath = '/Users/chenxue/project/chromedriver/chromedriver'
    driver: webdriver

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path=cls.chromepath)
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_demo(self):
        self.driver.get("https://xueqiu.com")
        self.driver.find_element_by_name("q").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[text()[contains(.,'01688')]]").click()

        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

        # self.driver.find_element_by_xpath("//*[text()[contains(.,'自选')]]").click()
        self.driver.find_element_by_css_selector(".follow").click()
        self.driver.find_element_by_name("username").send_keys("15300000000")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_css_selector(".modal__login__btn").click()
        time.sleep(5)



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
