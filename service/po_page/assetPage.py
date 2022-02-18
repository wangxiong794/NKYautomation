# coding=utf-8
import os.path
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from get_root_path import root_dir

from .conPage import page


class asset(page):
    # 固定资产入库
    _filename = os.path.join(root_dir, 'service//po_elements//asset.ini')

    def addAssetWarehouse(self, billRemark='测试单据AssetWarehouse', _section='assetFASI'):
        self.element(self._filename, _section, 'assetGL').click()
        self.element(self._filename, _section, 'assetRK').click()
        self.element(self._filename, _section, 'assetRKD').click()
        self.element(self._filename, _section, 'assetAddButton').click()
        self.element(self._filename, _section, 'assetFlowInput').click()
        # 选择第一个流程
        try:
            time.sleep(0.1)
            self.element(self._filename, _section, 'assetFlowChoose2').click()
        except InterruptedError:
            self.element(self._filename, _section, 'assetFlowInput').click()
            time.sleep(0.5)
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
        time.sleep(1)
        self.element(self._filename, 'con', 'lookViewButton').click()
        time.sleep(2)
        self.screenShot(billRemark)

    def addAssetConsumer(self, billDescription='测试单据assetConsumer', _section='assetConsumer'):
        # 新增资产领用
        self.element(self._filename, 'con', 'assetGL').click()
        self.element(self._filename, _section, 'assetLY').click()
        self.element(self._filename, _section, 'assetAddButton').click()
        self.element(self._filename, _section, 'department').click()
        self.element(self._filename, _section, 'departmentInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'billFlowDefine').click()
        self.element(self._filename, _section, 'billFlowDefineInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'textDescription').send_keys(billDescription)
        self.element(self._filename, _section, 'detailAssetName').click()
        self.element(self._filename, _section, 'chooseAssetInput').click()
        time.sleep(1)
        self.element(self._filename, 'con', 'sureButton').click()
        time.sleep(0.5)
        js='document.querySelector("#globalLayoutContent > div > div.ant-spin-nested-loading > div > div > div > div ' \
           '> div > div.ant-table-wrapper.antd-pro-components-v2-table-edit-table-table.antd-pro-components-v2-table' \
           '-edit-table-borderRight > div > div > div > div > div").scrollTo(1000,0) '
        self.driver.execute_script(js)
        # self.element(self._filename, 'con', 'assetSubmitButton').click()
        time.sleep(1)
        self.element(self._filename, _section, 'assetLocation').click()
        time.sleep(0.5)
        self.element(self._filename, _section, 'assetLocationChoose').click()
        self.element(self._filename, 'con', 'assetSubmitButton').click()
        self.element(self._filename, 'con', 'lookViewButton').click()
        time.sleep(1)
        self.screenShot(billDescription)

    def addAssetHandBack(self, billDescription='测试单据assetHandBack', _section='assetHandBack'):
        # 新增资产领用
        self.element(self._filename, 'con', 'assetGL').click()
        self.element(self._filename, _section, 'assetTH').click()
        self.element(self._filename, _section, 'assetAddButton').click()
        self.element(self._filename, _section, 'department').click()
        self.element(self._filename, _section, 'departmentInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'billFlowDefine').click()
        self.element(self._filename, _section, 'billFlowDefineInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'textDescription').send_keys(billDescription)
        self.element(self._filename, _section, 'detailAssetName').click()
        self.element(self._filename, _section, 'chooseAssetInput').click()
        time.sleep(1)
        self.element(self._filename, 'con', 'sureButton').click()
        time.sleep(0.5)
        js='document.querySelector("#globalLayoutContent > div > div.ant-spin-nested-loading > div > div > div > div ' \
           '> div.ant-table-wrapper.antd-pro-components-v2-table-edit-table-table.antd-pro-components-v2-table-edit' \
           '-table-borderRight > div > div > div > div > div").scrollTo(1000,0) '
        self.driver.execute_script(js)
        # self.element(self._filename, 'con', 'assetSubmitButton').click()
        time.sleep(1)
        self.element(self._filename, _section, 'assetLocation').click()
        time.sleep(0.5)
        self.element(self._filename, _section, 'assetLocationChoose').click()
        self.element(self._filename, 'con', 'assetSubmitButton').click()
        self.element(self._filename, 'con', 'lookViewButton').click()
        time.sleep(1)
        self.screenShot(billDescription)

    def addInWarehouse(self, billDescription='测试单据inWarehouse', _section='inWarehouse'):
        # 新增资产领用
        self.element(self._filename, 'con', 'assetGL').click()
        self.element(self._filename, _section, 'inWarehouse').click()
        self.element(self._filename, _section, 'inWarehouseBill').click()
        self.element(self._filename, _section, 'AddButton').click()
        self.element(self._filename, _section, 'openUser').click()
        self.element(self._filename, _section, 'openUserInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'textRemark').send_keys(billDescription)
        self.element(self._filename, _section, 'detailWarehouseName').click()
        self.element(self._filename, _section, 'chooseWarehouseInput').click()
        time.sleep(1)
        self.element(self._filename, 'con', 'sureButton').click()
        time.sleep(0.5)
        js = 'document.querySelector("#globalLayoutContent > div > div:nth-child(3) > div:nth-child(2) > div > ' \
             'div.ant-table-wrapper.antd-pro-components-v2-table-edit-table-table.antd-pro-components-v2-table-edit' \
             '-table-borderRight > div > div > div > div > div").scrollTo(1000,0) '
        self.driver.execute_script(js)
        # self.element(self._filename, 'con', 'assetSubmitButton').click()
        time.sleep(1)
        self.element(self._filename, _section, 'detailWarehouseAmount').click()
        time.sleep(0.5)
        self.element(self._filename, _section, 'detailWarehouseAmountInput').send_keys('1')
        self.element(self._filename, 'con', 'assetSubmitButton').click()
        self.element(self._filename, 'con', 'lookViewButton').click()
        time.sleep(1)
        self.screenShot(billDescription)

    def addOutWarehouse(self, billDescription='测试单据outWarehouse', _section='outWarehouse'):
        # 新增资产领用
        self.element(self._filename, 'con', 'assetGL').click()
        self.element(self._filename, _section, 'outWarehouse').click()
        self.element(self._filename, _section, 'AddButton').click()

        self.element(self._filename, _section, 'department').click()
        self.element(self._filename, _section, 'departmentInput').send_keys(Keys.ENTER)
        self.element(self._filename, _section, 'textRemark').send_keys(billDescription)
        self.element(self._filename, _section, 'detailWarehouseName').click()
        self.element(self._filename, _section, 'chooseWarehouseInput').click()
        time.sleep(1)
        self.element(self._filename, 'con', 'sureButton').click()
        time.sleep(0.5)
        self.element(self._filename, _section, 'detailWarehouseAmount').click()
        time.sleep(0.5)
        self.element(self._filename, _section, 'detailWarehouseAmountInput').send_keys('1')
        self.element(self._filename, 'con', 'assetSubmitButton').click()
        self.element(self._filename, 'con', 'lookViewButton').click()
        time.sleep(1)
        self.screenShot(billDescription)