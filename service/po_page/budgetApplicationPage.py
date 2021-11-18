# coding=utf-8
import os.path
import time

from selenium.webdriver import Keys

from get_root_path import root_dir

from .conPage import page


class budgetApplication(page):
    _filename = os.path.join(root_dir, 'service//po_elements//pay.ini')

    def menu(self, _section='payMenu'):
        self.element(self._filename,_section,'payout').click()
        self.element(self._filename, _section, 'budgetApplication').click()

    def add_budget(self, _section='budgetApplication'):
        self.element(self._filename,_section,'startBill').click()
        time.sleep(1)
        self.choiceBudget()

    def edit_2(self,_section='applyEdit'):
        self.element(self._filename, _section, 'amount').send_keys(100)
        self.element(self._filename, _section, 'nextButton').click()

    def edit_3(self,_description='test',_section='applyEdit'):
        self.element(self._filename, _section, 'departmentInput').click()
        self.element(self._filename, _section, 'departmentInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'descriptionInput').send_keys(_description)


