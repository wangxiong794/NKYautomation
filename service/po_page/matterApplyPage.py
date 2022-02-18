
# coding=utf-8
import os.path
import time

from selenium.webdriver import Keys


from get_root_path import root_dir

from .conPage import page




class matterApply(page):
    # 重要事项
    _filename = os.path.join(root_dir, 'service//po_elements//matter.ini')

    def countersign(self, billRemark='测试单据Countersign', _section='countersign'):
        self.element(self._filename, 'con', 'matter').click()
        self.element(self._filename, _section, 'menuCountersign').click()
        self.element(self._filename, _section, 'assetAddButton').click()
        # TODO
        self.element(self._filename, _section, 'countersignTime').click()
        self.element(self._filename, _section, 'countersignTimeInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'countersignLocation').send_keys('会签地点')
        self.element(self._filename, _section, 'countersignHostUser').click()
        self.element(self._filename, _section, 'countersignHostUserInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'countersignRecordUser').click()
        self.element(self._filename, _section, 'countersignRecordUserInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'countersignType').click()
        self.element(self._filename, _section, 'countersignTypeInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'countersignDescription').send_keys(billRemark)
        self.element(self._filename, _section, 'countersignPeopleButton').click()
        self.element(self._filename, _section, 'countersignPeopleChoose').click()
        self.element(self._filename, _section, 'countersignPeopleAdd').click()
        self.element(self._filename, 'con', 'sureButton').click()
        time.sleep(0.5)
        self.element(self._filename, _section, 'nextButton').click()
        self.element(self._filename, _section, 'countersignContent').send_keys(billRemark)
        self.element(self._filename, 'con', 'assetSubmitButton').click()
        self.element(self._filename, 'con', 'lookViewButton').click()
        time.sleep(1)
        self.screenShot(billRemark)