#!/usr/bin/env python
# coding=utf-8
import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDanjuan(object):
    caps = {}
    caps["platformName"] = "android"
    caps["deviceName"] = "emulator-5554"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps["autoGrantPermissions"] = True
    caps["unicodeKeyboard"] = True
    caps["resetKeyboard"] = True

    driver: webdriver
    _jiaoyibutton = (
        By.XPATH,
        "//*[contains(@resource-id, 'tab_name') and @text='交易']")

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.caps)

        # 隐式等待
        cls.driver.implicitly_wait(10)

        # 显示等待
        WebDriverWait(cls.driver, 20).until(EC.presence_of_element_located(cls._jiaoyibutton))
        cls.driver.find_element(*cls._jiaoyibutton).click()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_logincase1(self):
        self.driver.find_element_by_accessibility_id("基金开户").click()
        self.driver.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()
        self.driver.find_element_by_accessibility_id("使用密码登录").click()

        # 切换上下文
        print(self.driver.contexts)
        print(self.driver.current_context)
        self.driver.switch_to.context(
            self.driver.contexts[-1])

        self.driver.find_element_by_id("telno").send_keys("15302462430")
        self.driver.find_element_by_id("pass").send_keys("123456")
        self.driver.find_element_by_accessibility_id("安全登录").click()
