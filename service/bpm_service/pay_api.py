import datetime
import json
import os
import time
from get_root_path import root_dir
import requests
from service.bpm_service.bpm_data import apply_data, agree_data, refuse_data, gql_url, ri_data
from config import ip, common_header, user_id
from service import login
from service.logger import Log

bpm_log_dir = os.path.join(root_dir, 'logs\\bpm_logs')
log = Log(bpm_log_dir)


def BA_stand_bpm(cookie):
    """事前申请单发起、撤回、复制、驳回、复制、作废"""
    apply_url = "http://" + ip + '/nky/service/BudgetApplication'
    common_header['Cookie'] = cookie
    print(gql_bill_status(cookie,"BudgetApplication","10506"))
    bill_id = requests.request('POST', apply_url, headers=common_header, data=json.dumps(apply_data))
    assert "200" in str(bill_id), str(bill_id)
    bill_id = bill_id.text
    log.info("【测试用例名称：事前申请单发起、撤回、复制、驳回、复制、作废】")
    log.info("新增事前申请单据，单据号：" + bill_id)

    """撤销该单据"""
    cancel_url = apply_url + '/' + bill_id
    cancel_data = {
        'id': bill_id,
        'statusId': 5,
    }
    cancel_response = requests.request('PUT', cancel_url, headers=common_header, data=json.dumps(cancel_data))
    assert "200" in str(cancel_response), str(cancel_response)
    log.info("撤销事前申请单据，单据号：" + bill_id)

    """复制该单据"""
    apply_data['description'] = "事前申请单发起、撤回、复制"
    bill_id1 = requests.request('POST', apply_url, headers=common_header, data=json.dumps(apply_data))
    assert "200" in str(bill_id1), str(bill_id1)
    bill_id1 = bill_id1.text
    log.info("复制事前申请单，原单据号：" + bill_id + '，新单据号：' + bill_id1)

    """删除原单据"""
    delete_bill = requests.request('DELETE', cancel_url, headers=common_header)
    assert "200" in str(delete_bill), str(delete_bill)
    log.info("删除已撤销的单据，单据号：" + bill_id)

    """GQL查询"""
    g_url = "http://" + ip + "/nky/service/graphql"
    g_data = {
        "query": '{↵  list: ApprovalLog(criteriaStr: "(billType =\'BudgetApplication\' and billId = ' + bill_id1 + ' )",'
                                                                                                                   ' sorts: [{name: "id", isAsc: false}], maxResult: 1) {↵    id↵  }↵}↵'
    }
    # 将<class 'requests.models.Response'> 属性换成json属性
    gql_result = requests.request('POST', g_url, headers=common_header, data=json.dumps(g_data)).json()
    approval_id = str(gql_result['data']['list'][0]['id'])
    log.info("通过gql查询到新单据号的审批id：" + approval_id)

    """驳回新单据"""
    approval_url = "http://" + ip + '/nky/service/ApprovalLog/' + approval_id
    refuse_data['id'] = bill_id1
    requests.request('PUT', approval_url, headers=common_header, data=json.dumps(refuse_data))
    log.info("驳回事前申请单，单据号：" + bill_id1)

    """复制被驳回的单据"""
    apply_data['description'] = "事前申请单发起、撤回、复制、驳回、复制"
    bill_id2 = requests.request('POST', apply_url, headers=common_header, data=json.dumps(apply_data))
    bill_id2 = bill_id2.text
    log.info("复制事前申请单，原单据号：" + bill_id1 + '，新单据号：' + bill_id2)

    """同意新单据"""
    g_data1 = {
        "query": '{↵  list: ApprovalLog(criteriaStr: "(billType =\'BudgetApplication\' and billId = ' + bill_id2 + ')",'
                                                                                                                   ' sorts: [{name: "id", isAsc: false}], maxResult: 1) {↵    id↵  }↵}↵'
    }
    gql_result = requests.request('POST', g_url, headers=common_header, data=json.dumps(g_data1)).json()
    approval_id1 = str(gql_result['data']['list'][0]['id'])
    log.info("通过gql查询到最新单据号的审批id：" + approval_id1)
    agree_url = "http://" + ip + '/nky/service/ApprovalLog/' + approval_id1
    agree_data['id'] = bill_id2
    agree1 = requests.request('PUT', agree_url, headers=common_header, data=json.dumps(agree_data))
    assert "200" in str(agree1), str(agree1)
    log.info("同意事前申请单，单据号：" + bill_id2)

    """作废上步操作同意的事前单"""
    stop_url = apply_url + '/' + bill_id2
    stop_data = {
        'id': bill_id2,
        'statusId': 9
    }
    requests.request('PUT', stop_url, headers=common_header, data=json.dumps(stop_data))
    log.info("作废事前申请单，单据号：" + bill_id2)

    """检查单据状态"""
    check_bill = {
        "query": "{↵  BudgetApplication(criteriaStr: \"(id =" + bill_id2 + ")\") {↵    statusId↵  }↵}↵"
    }
    gql_check_result = requests.request('POST', g_url, headers=common_header, data=json.dumps(check_bill)).json()
    bill_status = str(gql_check_result['data']['BudgetApplication'][0]['statusId'])
    if bill_status == "9":
        log.info("【检查事前单" + bill_id2 + "状态为" + bill_status + ",确认已作废，用例执行通过】")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + bill_id2 + "状态为" + bill_status + ",并非已作废，请检查脚本或复测】====")


def BA_bpm2(cookie):
    """事前申请单发起、通过、报销、核销、关闭"""
    log = Log(bpm_log_dir)
    apply_url = "http://" + ip + '/nky/service/BudgetApplication'
    common_header['Cookie'] = cookie
    bill_id = requests.request('POST', apply_url, headers=common_header, data=json.dumps(apply_data)).text
    log.info("【测试用例名称：事前申请单发起、通过、报销、核销、关闭】")
    log.info("新增事前申请单据，单据号：" + bill_id)
    # 通过
    g_data1 = {
        "query": '{↵  list: ApprovalLog(criteriaStr: "(billType =\'BudgetApplication\' and billId = ' + bill_id + ' )",'
                                                                                                                  ' sorts: [{name: "id", isAsc: false}], maxResult: 1) {↵    id↵  }↵}↵'
    }
    gql_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data1)).json()
    approval_id = str(gql_result['data']['list'][0]['id'])

    log.info("通过gql查询到最新单据号的审批id：" + approval_id)
    agree_url = "http://" + ip + '/nky/service/ApprovalLog/' + approval_id
    agree_data['id'] = bill_id
    requests.request('PUT', agree_url, headers=common_header, data=json.dumps(agree_data))

    # 检查单据状态
    check_bill = {
        "query": "{↵  BudgetApplication(criteriaStr: \"(id =" + bill_id + ")\") {↵    statusId↵  }↵}↵"
    }
    gql_check_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(check_bill)).json()
    bill_status = str(gql_check_result['data']['BudgetApplication'][0]['statusId'])
    if bill_status == "4":
        log.info("检查事前单" + bill_id + "状态为" + bill_status + ",确认已通过")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + bill_id + "状态为" + bill_status + ",并非已通过，请检查脚本或复测】====")

    ba_item_sql = {
        'query': "{↵  	BudgetApplicationItem(criteriaStr: \"parentId=" + bill_id + '"' + "){↵  	id↵     }↵}↵"
    }
    ba_item_id = requests.request('POST', gql_url, headers=common_header, data=json.dumps(ba_item_sql)).json()
    ba_item_id = ba_item_id['data']['BudgetApplicationItem'][0]['id']
    # 新增报销单'budgetApplicationItemId': 10021
    ba_ri_data = {
        'paySettingId': 303,
        'amount': 100,
        'createdUserId': user_id,
        'departmentId': 10008,
        'applyDate': str(datetime.datetime.utcnow().isoformat()),
        'billFlowDefineId': 10001,
        'description': "对事前单" + bill_id + "发起报销",
        'reimbursePayItems': [{'paySettingId': 303, 'amount': 100}],
        'fiscalYearId': 10000,
        'contractItemId': 'null',
        'srcBillId': bill_id,
        'srcBillType': "BudgetApplication",
        'budgetApplicationId': bill_id,
        'reimburseItems': [{'budgetApplicationItemId': ba_item_id, 'budgetItemId': 10000, 'amount': 100, 'actual': 0}],
    }
    ri_url = "http://" + ip + '/nky/service/Reimburse'
    ri_id = requests.request('POST', ri_url, headers=common_header, data=json.dumps(ba_ri_data)).text
    log.info("新增报销单据：" + ri_id + ",关联事前申请单" + bill_id)

    # 同意报销单
    g_data1 = {
        "query": '{↵  list: ApprovalLog(criteriaStr: "(billType =\'Reimburse\' and billId = ' + ri_id + ')",'
                                                                                                        ' sorts: [{name: "id", isAsc: false}], maxResult: 1) {↵    id↵  }↵}↵'
    }
    gql_result1 = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data1)).json()
    approval_id = str(gql_result1['data']['list'][0]['id'])
    log.info("通过gql查询到报销单的审批id：" + approval_id)
    agree_url = "http://" + ip + '/nky/service/ApprovalLog/' + approval_id
    agree_data['id'] = ri_id
    requests.request('PUT', agree_url, headers=common_header, data=json.dumps(agree_data))
    log.info("同意报销单单，单据号：" + ri_id)

    # 核销报销单
    g_data2 = {
        "query": "{↵ ReimburseItem(criteriaStr: \"(parentId =" + ri_id + ")\") {↵    id↵  }↵}↵"
    }
    gql_result2 = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data2)).json()
    ri_item_id = str(gql_result2['data']['ReimburseItem'][0]['id'])
    log.info("通过gql查询到报销单明细id为：" + ri_item_id)
    g_data3 = {
        "query": "{↵ ReimbursePayItem(criteriaStr: \"(parentId =" + ri_id + ")\") {↵    id↵  }↵}↵"
    }
    gql_result3 = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data3)).json()
    ri_pay_id = str(gql_result3['data']['ReimbursePayItem'][0]['id'])
    verify_url = ri_url + '/' + ri_id
    verify_data = {
        'id': ri_id,
        'verifyDate': str(datetime.datetime.utcnow().isoformat()),
        'actual': 100,
        'isVerified': 'true',
        'reimburseItems': [{'id': ri_item_id, 'quotaNumber': "", 'actual': 100, 'editFlag': "update"}],
        'reimbursePayItems': [{'id': ri_pay_id, 'actual': 100, 'editFlag': "update"}],
        'additionalValues': {'closeApply': 'true'}
    }
    requests.request('PUT', verify_url, headers=common_header, data=json.dumps(verify_data))

    close_url = "http://" + ip + "/nky/service/BudgetApplication/" + bill_id
    close_data = {
        "id": bill_id,
        "statusId": 6
    }
    requests.request('PUT', close_url, headers=common_header, data=json.dumps(close_data))

    gql_data3 = {
        "query": "{↵  Reimburse(criteriaStr: \"(id = " + ri_id + ")\") {↵    amount↵    isVerified↵    actual↵  }↵}↵"
    }
    ri_status = requests.request('POST', gql_url, headers=common_header, data=json.dumps(gql_data3)).json()
    ri_amount = str(ri_status['data']['Reimburse'][0]['amount'])
    ri_verify = str(ri_status['data']['Reimburse'][0]['isVerified'])
    ri_actual = str(ri_status['data']['Reimburse'][0]['actual'])
    gql_data4 = {
        "query": "{↵  BudgetApplication(criteriaStr: \"(id =" + bill_id + ")\") {↵    statusId↵  }↵}↵"
    }

    gql_check_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(gql_data4)).json()
    bill_status = str(gql_check_result['data']['BudgetApplication'][0]['statusId'])
    if ri_verify == "True" and bill_status == "6":
        log.info("【报销单" + ri_id + "报销金额" + ri_amount + ",核销金额" + ri_actual + "，关联事前单状态为已关闭】")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + ri_id + "核销失败，请检查脚本或复测】====")


def add_BA(cookie, case_name):
    log = Log(bpm_log_dir)
    apply_url = "http://" + ip + '/nky/service/BudgetApplication'
    common_header['Cookie'] = cookie
    apply_data['description'] = case_name
    bill_id = requests.request('POST', apply_url, headers=common_header, data=json.dumps(apply_data)).text
    log.info(case_name)
    log.info("新增事前申请单据，单据号：" + bill_id)
    # 通过
    g_data1 = {
        "query": '{↵  list: ApprovalLog(criteriaStr: "(billType =\'BudgetApplication\' and billId = ' + bill_id + ' )",'
                                                                                                                  ' sorts: [{name: "id", isAsc: false}], maxResult: 1) {↵    id↵  }↵}↵'
    }
    gql_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data1)).json()
    approval_id = str(gql_result['data']['list'][0]['id'])

    log.info("通过gql查询到最新单据号的审批id：" + approval_id)
    agree_url = "http://" + ip + '/nky/service/ApprovalLog/' + approval_id
    agree_data['id'] = bill_id
    requests.request('PUT', agree_url, headers=common_header, data=json.dumps(agree_data))

    # 检查单据状态
    check_bill = {
        "query": "{↵  BudgetApplication(criteriaStr: \"(id =" + bill_id + ")\") {↵    statusId↵  }↵}↵"
    }
    gql_check_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(check_bill)).json()
    bill_status = str(gql_check_result['data']['BudgetApplication'][0]['statusId'])
    if bill_status == "4":
        log.info("检查事前单" + bill_id + "状态为" + bill_status + ",确认已通过")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + bill_id + "状态为" + bill_status + ",并非已通过，请检查脚本或复测】====")
    return bill_id


def add_ri(cookie, ri_name, bill_id="null", ba_item_id="null", ct_item_id="null"):
    common_header['cookie'] = cookie
    ba_ri_data = {
        'paySettingId': 303,
        'amount': 100,
        'createdUserId': user_id,
        'departmentId': 10008,
        'applyDate': str(datetime.datetime.utcnow().isoformat()),
        'billFlowDefineId': 10001,
        'description': ri_name,
        'reimbursePayItems': [{'paySettingId': 303, 'amount': 100}],
        'fiscalYearId': 10000,
        'contractItemId': ct_item_id,
        'srcBillId': bill_id,
        'srcBillType': "BudgetApplication",
        'budgetApplicationId': bill_id,
        'reimburseItems': [{'budgetApplicationItemId': ba_item_id, 'budgetItemId': 10000, 'amount': 100, 'actual': 0}],
    }
    ri_url = "http://" + ip + '/nky/service/Reimburse'
    ri_id = requests.request('POST', ri_url, headers=common_header, data=json.dumps(ba_ri_data)).text
    return ri_id


def cancel(cookie, bill_type, bill_id):
    common_header['cookie'] = cookie
    cancel_url = "http://" + ip + "/nky/service" + "/" + bill_type + '/' + bill_id
    cancel_data = {
        'id': bill_id,
        'statusId': 5,
    }
    requests.request('PUT', cancel_url, headers=common_header, data=json.dumps(cancel_data))


def check_ri(cookie, ri_id):
    common_header['cookie'] = cookie
    g_data2 = {
        "query": "{↵ ReimburseItem(criteriaStr: \"(parentId =" + ri_id + ")\") {↵    id↵  }↵}↵"
    }
    gql_result2 = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data2)).json()
    ri_item_id = str(gql_result2['data']['ReimburseItem'][0]['id'])
    g_data3 = {
        "query": "{↵ ReimbursePayItem(criteriaStr: \"(parentId =" + ri_id + ")\") {↵    id↵  }↵}↵"
    }
    gql_result3 = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data3)).json()
    ri_pay_id = str(gql_result3['data']['ReimbursePayItem'][0]['id'])
    verify_url = "http://" + ip + '/nky/service/Reimburse/' + ri_id
    verify_data = {
        'id': ri_id,
        'verifyDate': str(datetime.datetime.utcnow().isoformat()),
        'actual': 100,
        'isVerified': 'true',
        'reimburseItems': [{'id': ri_item_id, 'quotaNumber': "", 'actual': 100, 'editFlag': "update"}],
        'reimbursePayItems': [{'id': ri_pay_id, 'actual': 100, 'editFlag': "update"}],
        'additionalValues': {'closeApply': 'true'}
    }
    requests.request('PUT', verify_url, headers=common_header, data=json.dumps(verify_data))
    # 检验报销单是否核销
    gql_data4 = {
        "query": "{↵  Reimburse(criteriaStr: \"(id = " + ri_id + ")\") {↵    amount↵    isVerified↵    actual↵  }↵}↵"
    }
    ri_status = requests.request('POST', gql_url, headers=common_header, data=json.dumps(gql_data4)).json()
    ri_amount = str(ri_status['data']['Reimburse'][0]['amount'])
    ri_verify = str(ri_status['data']['Reimburse'][0]['isVerified'])
    ri_actual = str(ri_status['data']['Reimburse'][0]['actual'])
    if ri_verify == "True" :
        log.info("【报销单" + ri_id + "报销金额" + ri_amount + ",核销金额" + ri_actual + "】")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + ri_id + "核销失败，请检查脚本或复测】====")


def void(cookie, bill_type, bill_id):
    # 作废单据
    common_header['cookie'] = cookie
    void_url = "http://" + ip + "/nky/service/"+bill_type+"/" + bill_id
    void_data = {
        'id': bill_id,
        'statusId': 9,
    }
    requests.request('PUT',void_url, headers=common_header, data=json.dumps(void_data))


def delete_bill(cookie, bill_type, bill_id):
    common_header['cookie'] = cookie
    delete_url =  "http://" + ip + "/nky/service/"+bill_type+"/" + bill_id
    requests.request('DELETE', delete_url, headers=common_header)


def close_ba(cookie, bill_id):
    common_header['cookie'] = cookie
    close_url = "http://" + ip + "/nky/service/BudgetApplication/" + bill_id
    close_data = {
        "id": bill_id,
        "statusId": 6
    }
    requests.request('PUT', close_url, headers=common_header, data=json.dumps(close_data))


def add_BA_RI(cookie, bill_id, ba_item_id, ct_item_id="null"):
    ri_id = add_ri(cookie, "事前报销", bill_id, ba_item_id, ct_item_id)
    log.info("新增报销单据：" + ri_id + ",关联事前申请单" + bill_id)
    agree_bill(cookie, 'Reimburse',ri_id)

    # 核销报销单
    check_ri(cookie, ri_id)
    # 关闭申请单
    close_ba(cookie, bill_id)
    gql_data3 = {
        "query": "{↵  Reimburse(criteriaStr: \"(id = " + ri_id + ")\") {↵    amount↵    isVerified↵    actual↵  }↵}↵"
    }
    ri_status = requests.request('POST', gql_url, headers=common_header, data=json.dumps(gql_data3)).json()
    ri_amount = str(ri_status['data']['Reimburse'][0]['amount'])
    ri_verify = str(ri_status['data']['Reimburse'][0]['isVerified'])
    ri_actual = str(ri_status['data']['Reimburse'][0]['actual'])
    gql_data4 = {
        "query": "{↵  BudgetApplication(criteriaStr: \"(id =" + bill_id + ")\") {↵    statusId↵  }↵}↵"
    }

    gql_check_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(gql_data4)).json()
    bill_status = str(gql_check_result['data']['BudgetApplication'][0]['statusId'])
    if ri_verify == "True" and bill_status == "6":
        log.info("【报销单" + ri_id + "报销金额" + ri_amount + ",核销金额" + ri_actual + "，关联事前单状态为已关闭】")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + ri_id + "核销/关闭失败，请检查脚本或复测】====")


def agree_bill(cookie, bill_type, bill_id):
    common_header['Cookie'] = cookie
    g_data1 = {
        "query": "{↵  list: ApprovalLog(criteriaStr: \"billType = '"+bill_type+ "' and billId = "+bill_id+"\", "
        "sorts: [{name: \"id\", isAsc: false}], maxResult: 1) {↵    id↵  }↵}↵"
    }
    gql_result1 = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data1)).json()
    approval_id = str(gql_result1['data']['list'][0]['id'])
    agree_url = "http://" + ip + '/nky/service/ApprovalLog/' + approval_id
    requests.request('PUT', agree_url, headers=common_header, data=json.dumps(agree_data))


def gql_bill_status(cookie, bill_type, bill_id):
    # 检查单据状态
    common_header['Cookie'] = cookie
    gql_data = {
        "query": "{↵  " + bill_type + "(criteriaStr: \"(id =" + bill_id + ")\") {↵    statusId↵  }↵}↵"
    }
    bill_status = requests.request('POST', gql_url, headers=common_header, data=json.dumps(gql_data)).json()
    bill_status = str(bill_status['data'][bill_type][0]['statusId'])
    return bill_status


def gql_delete(cookie, bill_type, bill_id):
    common_header['Cookie'] = cookie
    gql_data = {
        "query": "{↵  " + bill_type + "(criteriaStr: \"(id =" + bill_id + ")\") {↵    statusId↵  }↵}↵"
    }
    bill_status = requests.request('POST', gql_url, headers=common_header, data=json.dumps(gql_data)).json()
    bill_status = str(bill_status['data'][bill_type])
    if bill_status == "[]":
        log.info("【删除单据" + bill_id + "成功】")
    else:
        log.info("==="*10+"删除单据" + bill_id + "失败===")

def add_PR(cookie, ba_id):
    pr_url = "http://" + ip + '/nky/service/PurchaseRequest'
    pr_data = {
        'amount': 100,
        'createdUserId': user_id,
        'departmentId': 10008,
        'registrationDate': str(datetime.datetime.utcnow().isoformat()),
        'purchaseCatalogId': 1500,
        'billFlowDefineId': 10003,
        'description': "事前申请单发起",
        'procurement': "test",
        'purType': "1301",
        'purMethod': "1406",
        'budgetApplicationId': ba_id,
        'purchaseRequestDetail': [
            {'name': "电脑(台式机)",
             'unitName': "台",
             'unitId': 7,
             'productId': 10001,
             'price': 10,
             'quantity': 10,
             'specification': "test",
             'assetPropertyId': 2200,
             'governmentPurchaseCatalogueId': 1,
             'amount': 100}],
        'fiscalYearId': 10000,
        'schoolYearId': 'null',
        'purchaseSupplierItem': [{'inquirer': "陈东雪", 'isSelect': 'true', 'supplierId': 10001, 'description': 'null'}]
    }
    common_header['Cookie'] = cookie
    pr_id = requests.request('POST', pr_url, headers=common_header, data=json.dumps(pr_data)).text
    log.info("新增采购单单据号：" + pr_id)
    agree_bill(cookie, 'PurchaseRequest', pr_id)
    # 检查单据状态
    check_bill = {
        "query": "{↵  PurchaseRequest(criteriaStr: \"(id =" + pr_id + ")\") {↵    statusId↵  }↵}↵"
    }
    gql_check_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(check_bill)).json()
    bill_status = str(gql_check_result['data']['PurchaseRequest'][0]['statusId'])
    if bill_status == "4":
        log.info("检查采购单" + pr_id + "状态为" + bill_status + ",确认已通过")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + pr_id + "状态为" + bill_status + ",并非已通过，请检查脚本或复测】====")
    return pr_id


def add_AT(cookie, pr_id):
    common_header['Cookie'] = cookie
    # 查询子表id
    g_data1 = {
        'query': "{↵  PurchaseRequestDetail(criteriaStr:\"purchaseRequestId = " + pr_id + "\"){↵  id↵}↵}"
    }
    pr_detail = requests.request('POST', gql_url, headers=common_header, data=json.dumps(g_data1)).json()
    pr_detail_id = str(pr_detail['data']['PurchaseRequestDetail'][0]['id'])
    at_url = "http://" + ip + '/nky/service/CheckRequest'
    at_data = {
        'createdUserId': user_id,
        'checkDate': str(datetime.datetime.utcnow().isoformat()),
        'description': "test验收",
        'remark': "test",
        'additionalValues': {'userIds': [{'userId': user_id}]},
        'statusId': 2,
        'purchaseRequestId': pr_id,
        'checkRequestDetail': [
            {'purchaseRequestDetailId': pr_detail_id,
             'productId': 10001,
             'name': "电脑(台式机)",
             'specification': "test",
             'unitId': 7,
             'unitName': "台",
             'assetPropertyId': 2200,
             'price': 10,
             'supplierId': 10001,
             'quantity': 10,
             'amount': 100}],
        'fiscalYearId': 10000,
        'schoolYearId': 'null',
    }
    at_id = requests.request('POST', at_url, headers=common_header, data=json.dumps(at_data)).text
    log.info("新增验收单据号：" + at_id)
    agree_bill(cookie, 'CheckRequest', at_id)
    # 检查验收单单号
    check_bill = {
        "query": "{↵  CheckRequest(criteriaStr: \"(id =" + at_id + ")\") {↵    statusId↵  }↵}↵"
    }
    gql_check_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(check_bill)).json()
    bill_status = str(gql_check_result['data']['CheckRequest'][0]['statusId'])
    if bill_status == "4":
        log.info("检查验收单" + pr_id + "状态为" + bill_status + ",确认已通过")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + pr_id + "状态为" + bill_status + ",并非已通过，请检查脚本或复测】====")


def add_ba_ct(cookie, ba_id, pr_id):
    ct_url = "http://" + ip + '/nky/service/Contract'
    common_header["Cookie"] = cookie
    ct_data = {
        'createdUserId': user_id,
        'departmentId': 10008,
        'applyDate': str(datetime.datetime.utcnow().isoformat()),
        'amount': 200,
        'name': "test" + str(datetime.datetime.utcnow().isoformat()),
        'contractTypeId': 1600,
        'bSupplierId': 10001,
        'cSupplierId': 'null',
        'dSupplierId': 'null',
        'signUsers': user_id,
        'governmentContract': 2,
        'isArchived': 'false',
        'contractPurchaseCatalogId': 1500,
        'billFlowDefineId': 10004,
        'description': "事前申请单发起、通过、采购、验收、报销、核销、关闭",
        'changeIdPath': "",
        'signUserId': 10003,
        'fiscalYearId': 10000,
        'schoolYearId': 'null',
        'budgetApplicationId': ba_id,
        'purchaseRequestId': pr_id,
        'contractItems': [
            {'ratio': 0.5,
             'budgetYear': 2020,
             'budgetaryYearFlag': 1,
             'amount': 100,
             'paymentDate': 1593336124233}, {
                'ratio': 0.5,
                'budgetYear': 2021,
                'budgetaryYearFlag': 0,
                'amount': 100,
                'paymentDate': 1593336134698
            }
        ]
    }
    ct_id = requests.request('POST', ct_url, headers=common_header, data=json.dumps(ct_data)).text
    log.info("新增合同单据号：" + ct_id)
    agree_bill(cookie, "Contract",ct_id)
    # 检查单据状态
    check_bill = {
        "query": "{↵  Contract(criteriaStr: \"(id =" + ct_id + ")\") {↵    statusId↵  }↵}↵"
    }
    gql_check_result = requests.request('POST', gql_url, headers=common_header, data=json.dumps(check_bill)).json()
    bill_status = str(gql_check_result['data']['Contract'][0]['statusId'])
    if bill_status == "4":
        log.info("检查合同单" + ct_id + "状态为" + bill_status + ",确认已通过")
    else:
        log.info("====" * 10 + "【出问题了，该单据" + ct_id + "状态为" + bill_status + ",并非已通过，请检查脚本或复测】====")
    return ct_id


def BA_bpm3(cookie):
    """事前申请单发起、通过、采购、验收、报销、核销、关闭"""
    ba_id = add_BA(cookie, "【事前申请单发起、通过、采购、验收、报销、核销、关闭】")
    pr_id = add_PR(cookie, ba_id)
    add_AT(cookie, pr_id)
    ba_item_sql = {
        'query': "{↵  	BudgetApplicationItem(criteriaStr: \"parentId=" + ba_id + '"' + "){↵  	id↵     }↵}↵"
    }
    ba_item_id = requests.request('POST', gql_url, headers=common_header, data=json.dumps(ba_item_sql)).json()
    ba_item_id = ba_item_id['data']['BudgetApplicationItem'][0]['id']
    add_BA_RI(cookie, ba_id, ba_item_id)


def BA_bpm4(cookie):
    """事前申请单发起、通过、采购、合同、报销、核销"""
    ba_id = add_BA(cookie, "【事前申请单发起、通过、采购、合同、报销、核销、关闭】")
    pr_id = add_PR(cookie, ba_id)
    ct_id = add_ba_ct(cookie, ba_id, pr_id)
    ba_item_sql = {
        'query': "{↵  	BudgetApplicationItem(criteriaStr: \"parentId=" + ba_id + '"' + "){↵  	id↵     }↵}↵"
    }
    ba_item_id = requests.request('POST', gql_url, headers=common_header, data=json.dumps(ba_item_sql)).json()
    ba_item_id = ba_item_id['data']['BudgetApplicationItem'][0]['id']
    ct_item_sql = {
        'query': "{↵  	ContractItem(criteriaStr: \"parentId=" + ct_id + '"' + ",maxResult:1){↵  	id↵     }↵}↵"
    }
    ct_item_id = requests.request('POST', gql_url, headers=common_header, data=json.dumps(ct_item_sql)).json()
    ct_item_id = ct_item_id['data']['ContractItem'][0]['id']
    add_BA_RI(cookie, ba_id, ba_item_id, ct_item_id)


def ri_bpm1(cookie):
    """无申请报销单发起、撤销、复制、通过、核销"""
    log.info("【无申请报销单发起、撤销、复制、通过、核销】")
    ri_id = add_ri(cookie, "无申请报销单发起、撤销、复制、通过、核销")
    ri_status = gql_bill_status(cookie, "Reimburse", ri_id)
    log.info("新增无申请报销单" + ri_id + "，状态为" + ri_status)
    cancel(cookie, "Reimburse", ri_id)
    ri_status = gql_bill_status(cookie, "Reimburse", ri_id)
    log.info("撤销报销单" + ri_id + "，状态为" + ri_status)
    ri_id1 = add_ri(cookie, "无申请报销单发起、撤销、复制、通过、核销+复制")
    ri_status = gql_bill_status(cookie, "Reimburse", ri_id1)
    log.info("复制" + ri_id + "，新单据为" + ri_id1 + "，状态为" + ri_status)
    agree_bill(cookie, "Reimburse", ri_id1)
    check_ri(cookie, ri_id1)


def ri_bpm2(cookie):
    """无申请报销申请单发起、通过、作废、删除"""
    log.info("【无申请报销申请单发起、通过、作废、删除】")
    ri_id = add_ri(cookie, "无申请报销单发起、撤销、复制、通过、核销")
    ri_status = gql_bill_status(cookie, "Reimburse", ri_id)
    log.info("新增无申请报销单" + ri_id + "，状态为" + ri_status)
    agree_bill(cookie, "Reimburse", ri_id)
    void(cookie,"Reimburse",ri_id)
    ri_status = gql_bill_status(cookie, "Reimburse", ri_id)
    log.info("作废报销单" + ri_id + "，状态为" + ri_status)
    delete_bill(cookie,"Reimburse",ri_id)
    gql_delete(cookie,"Reimburse",ri_id)



if __name__ == "__main__":
    c = login.get_cookie_login()
    BA_stand_bpm(c)

