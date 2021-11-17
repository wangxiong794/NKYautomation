# coding=utf-8
from .conPage import page


class budgetApplication(page):
    def ele(self,_section='test', _option='test'):
        return self.element(_filename='../po_elements/pay.ini',section=_section,option=_section)

    def menu(self, _section='menu'):
        self.ele(_section, 'payout').click()
        self.ele(_section, 'budgetApplication').click()

