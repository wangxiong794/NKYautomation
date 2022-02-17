# coding=utf-8
import os.path
import time

from selenium.webdriver import Keys

from get_root_path import root_dir

from .conPage import page


class asset_FASI(page):
    # 固定资产入库
    _filename = os.path.join(root_dir, 'service//po_elements//asset.ini')

    def addFASI(self,billRemark='测试单据',_section='assetFASI'):
        self.element(self._filename,_section,'assetGL').click()
        self.element(self._filename, _section, 'assetRK').click()
        self.element(self._filename, _section, 'assetRKD').click()
        self.element(self._filename, _section, 'assetAddButton').click()
        self.element(self._filename, _section, 'assetFlowInput').click()
        # 选择第一个流程
        self.element(self._filename, _section, 'assetFlowChoose2').click()
        self.element(self._filename, _section, 'assetRemarkInput').send_keys(billRemark)
        time.sleep(0.1)
        self.element(self._filename, _section, 'assetDetailName').click()
        self.element(self._filename, _section, 'assetDetailNameInput').send_keys('资产名称')
        self.element(self._filename, _section, 'assetDetailModel').click()
        self.element(self._filename, _section, 'assetDetailModel').click()
        self.element(self._filename, _section, 'assetDetailModelInput').send_keys('型号')
        self.element(self._filename, _section, 'assetDetailUnit').click()
        self.element(self._filename, _section, 'assetDetailUnit').click()
        self.element(self._filename, _section, 'assetDetailUnitChoose').click()
        self.element(self._filename, _section, 'assetDetailCount').click()
        self.element(self._filename, _section, 'assetDetailCount').click()
        self.element(self._filename, _section, 'assetDetailCountInput').send_keys('1')
        self.element(self._filename, _section, 'assetDetailPrice').click()
        self.element(self._filename, _section, 'assetDetailPrice').click()
        self.element(self._filename, _section, 'assetDetailPriceInput').send_keys('1')
        # self.element(self._filename, _section, 'assetDetailRemark').click()
        # self.element(self._filename, _section, 'assetDetailRemark').click()
        # self.element(self._filename, _section, 'assetDetailRemarkInput').send_keys('备注')
        self.element(self._filename, _section, 'assetSubmitButton').click()
        time.sleep(5)


