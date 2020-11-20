# coding:utf-8
"""
事前申请单的data明细

"""
import datetime

from config import user_id, ip

gql_url = "http://"+ip+"/nky/service/graphql"
apply_data = {
    'modifiedUserId': user_id,
    'applyDate': str(datetime.datetime.utcnow().isoformat()),
    'description': "事前申请单发起",
    'departmentId': 10008,
    'amount': ' 100',
    'billFlowDefineId': 10000,
    'fiscalYearId': 10000,
    'schoolYearId': ' null',
    'budgetApplicationItems': [{"budgetItemId": 10000, "amount": 100}],
    'isPurchase': ' true',
    'isContract': ' true',
    'isReimburse': ' true'}

refuse_data = {
    'approvalStatusId': 503,
    'approvalDate': str(datetime.datetime.utcnow().isoformat()),
    'description': "test驳回。"
}

agree_data = {
    'approvalStatusId': 502,
    'approvalDate': str(datetime.datetime.utcnow().isoformat()),
    'description': "test同意。",
}

ri_data = {
    'createdUserId': user_id,
    'departmentId': 10008,
    'applyDate': str(datetime.datetime.utcnow().isoformat()),
    'amount': 10,
    'paySettingId': 303,
    'billFlowDefineId': 10001,
    'description': "报销单的发起了",
    'reimbursePayItems': [{'amount': 10, 'paySettingId': 303}],
    'fiscalYearId': 10000,
    'contractItemId': 'null',
    'srcBillType': "BudgetApplication",
    'budgetApplicationId': 'null',
    'reimburseItems': [{'budgetApplicationItemId': user_id, 'budgetItemId': 10000, 'amount': 10, 'actual': 0}]
}

