from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self, name, phone):
        sleep(3)
        self.find(By.CSS_SELECTOR, '#username').send_keys(name)
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(name)
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
        # 点击保存
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def member_lists(self):
        els = self.finds(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        member_lists = []
        for el in els:
            member_lists.append(el.get_attribute('title'))
        return member_lists
