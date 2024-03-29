from page_object.page.App import App
import pytest


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage = App.main().gotoProfile()

    def setup_method(self):
        self.loginPage = self.profilePage.gotoLogin()

    # 首次在设备上登录，会触发图片验证码，可先手动登录一次，则后续不会影响case运行
    @pytest.mark.parametrize("user, pw, msg", [
        ("156005347600", "111111", "手机号码"),
        ("15302462430", "123456", "密码错误")
    ])
    def test_login_password(self, user, pw, msg):
        self.loginPage.loginByPassword(user, pw)
        assert msg in self.loginPage.getErrorMsg()

    def teardown_method(self):
        self.loginPage.back()
