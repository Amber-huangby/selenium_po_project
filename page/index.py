from selenium.webdriver.common.by import By

from page.addmember import AddMember
from page.base_page import BasePage


class Index(BasePage):
    def goto_register(self):
        # self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        pass

    def goto_login(self):
        pass

    def goto_addmember(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(True)
