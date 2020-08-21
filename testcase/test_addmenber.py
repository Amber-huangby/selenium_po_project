import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.index import Index


class Test_AddMember:
    def setup_class(self):
        self.index = Index(True)

    @pytest.mark.parametrize('name,phone', [('a1', '13425444679'), ('a2', '12345678999')])
    def test_addmember(self, name, phone):
        addmember = self.index.goto_addmember()
        addmember.add_member(name, phone)
        print(addmember.member_lists())
        assert name in addmember.member_lists()

    def test1(self):
        # option = webdriver.ChromeOptions()
        # option.debugger_address = "127.0.0.1:9222"  # 本地地址的9222端口的进程
        # self.driver = webdriver.Chrome(options=option)
        # self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # assert 1 == 1
        pass
