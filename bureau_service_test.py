"""测试bureau项目服务端压力测试"""

import json
import threading
import time
import requests
service=[
    {"service":"dev3.neikongyi.com","round":"14571","password":"CzcpZlKIbFG3WwuoHiTMpeA2V4bl9Q0GfIlBIvy6cxo=,1Ra9onAYTYlkrjjt2Acm54fw6LJwmNkX,yWZjztv5McncLqZbKcViIThw9p0uvPFGunzBMkvX+QplW3BANOnMTb1HZ9y3XVpBTnaFUGMitwHI5mLjG9HnpAa6qpYb64iTUvG3bplwhB8="},
    {"service":"58.118.2.63","round":"14201","password":"7FtAhUOPzKj/4R4zkn4z4kvUP0km71yFZ9LTYmxkW0c=,UeStnq9Cc1HXkzupml2z6q4feui1QdTP,djxuw9Duqz9Ll/eOv2dJVeuD8RlI+s5+WBOyYdxMp26QiBBhFY+cymp6Zh655d1nNrZj9BaoJR3HxMZWbHlWfjhk4ud7YTlQ4fGfDq4yKSE="}
]


class workSpace():
    def __init__(self):
        self.user = "admin1"
        useService=service[0]
        self.ip = useService['service']
        self.cookie = self.need_Verify_Code()
        self.password = useService['password']
        self.round = useService["round"]
        self.userId = '1'
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            'content-length': "240",
            'content-type': "application/json; charset=utf-8",
            'Cookie': self.cookie,
            "Host": self.ip,
            'origin': "http://" + self.ip,
            "Referer": "http://" + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
            "x-Current-User-Id": self.userId,
        }

    def need_Verify_Code(self):  # 获取cookie
        url = "http://" + self.ip + "/bureau/service/session/needVerifyCode"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": self.ip,
            "Referer": "http://" + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
        }
        response = requests.request("GET", url, headers=headers)
        header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
        set_cookie = header['Set-Cookie']
        cookie = set_cookie[0:43]
        # print("cookie：" + str(cookie))
        return cookie

    def login(self):
        url = "http://" + self.ip + "/bureau/service/session/login"
        payload = {
            "userName": self.user,
            "password": self.password,
            "round": self.round,
        }
        headers = self.headers
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        has_time = response.elapsed.microseconds
        return has_time

    def gql(self, gqljson):
        url = "http://" + self.ip + "/bureau/service/graphql"
        response = requests.request("POST", url, data=json.dumps(gqljson), headers=self.headers)
        has_time = response.elapsed.microseconds
        return has_time

    def allGql(self):
        GqlTime = 0
        gqlData = [
            {"query": "{↵    CacheDataVersion {↵      tableName↵      version↵    }↵  }", "variables": "null"},
            {"query": '{↵    BudgetaryYearDefine(sorts: [{name:"createdTime", isAsc: false}]) {↵      id↵      name↵  '
                      '    startDate↵      endDate↵      budgetaryTypeId↵      budgetaryStatusId↵      description↵   '
                      ' }↵  }', "variables": "null"},
            {"query": '{↵    Entities {↵      name↵      title↵      fields{↵        name↵        title↵        type↵ '
                      '       enumType↵        isSystemField↵        referInfo {↵          referEntityFieldName↵      '
                      '    referEntities{↵            referEntityName↵          }↵        }↵        sourceInfo {↵     '
                      '     sourceEntityName↵          sourceFieldName↵        }↵        fieldUiOpts {↵          '
                      'required↵          length↵          scale↵          precision↵        }↵      }↵      '
                      'entityUiOpts{↵        mainFields↵        selectMethod↵      }↵    }↵    EnumValue(sorts: [{'
                      'name: "ordinal", isAsc: true},{name: "id", isAsc: true}]) {↵      id↵      name↵      value↵   '
                      '   title↵      ordinal↵    }↵  }', "variables": "null"},
            {"query": '{↵    MenuRole(sorts:[{name:"roleId", isAsc: true},{name:"menuCode",isAsc:true}]) {↵      id↵  '
                      '    roleId↵      menuCode↵    }↵  }', "variables": "null"},
            {"query": '{↵	UserSetting(criteriaStr: "userId = 1"){↵    id,↵    name,↵    title,↵    value,↵  }↵}', "variables": "null"},
            {"query": '{↵    list: User(sorts: [{name: "name", isAsc: true},{name: "id", isAsc: true}]) {↵      id↵   '
                      '   name↵      avatar↵      mobile↵      userName↵      position↵      email↵      '
                      'entWechatAccount↵      idNo↵      accounts {↵        stopFlag↵      }↵      roles {↵        '
                      'roleId↵      }↵      orgnizationId↵      orgnizationName: exprField(expr: "orgnization.name")↵ '
                      '     relDepartments {↵        isDefault↵        departmentId↵        departmentName: '
                      'exprField(expr: "department.name")↵        stopFlag: exprField(expr: "department.stopFlag")↵   '
                      '   }↵    }↵  }', "variables": "null"},
            {"query": '{↵    list: Department(sorts:[{name:"ordinal", isAsc: true}, {name:"id", isAsc: true}]) {↵     '
                      ' ↵    id↵    orgnizationId↵    code↵    name↵    managerId↵    managerName: exprField(expr: '
                      '"manager.name")↵    executiveId↵    executiveName: exprField(expr: "executive.name")↵    '
                      'supervisorDepartmentId↵    description↵    stopFlag↵    idPath↵    isLeaf↵    parentId↵    '
                      'name↵    disabled: stopFlag↵    relUsers {↵      userId↵      userName: exprField(expr: '
                      '"user.name")↵    }↵  ↵      children(sorts:[{name:"ordinal", isAsc: true}, {name:"id", '
                      'isAsc: true}]) {↵        ↵    id↵    orgnizationId↵    code↵    name↵    managerId↵    '
                      'managerName: exprField(expr: "manager.name")↵    executiveId↵    executiveName: exprField('
                      'expr: "executive.name")↵    supervisorDepartmentId↵    description↵    stopFlag↵    idPath↵    '
                      'isLeaf↵    parentId↵    name↵    disabled: stopFlag↵    relUsers {↵      userId↵      '
                      'userName: exprField(expr: "user.name")↵    }↵  ↵        children(sorts:[{name:"ordinal", '
                      'isAsc: true}, {name:"id", isAsc: true}]) {↵          ↵    id↵    orgnizationId↵    code↵    '
                      'name↵    managerId↵    managerName: exprField(expr: "manager.name")↵    executiveId↵    '
                      'executiveName: exprField(expr: "executive.name")↵    supervisorDepartmentId↵    description↵   '
                      ' stopFlag↵    idPath↵    isLeaf↵    parentId↵    name↵    disabled: stopFlag↵    relUsers {↵   '
                      '   userId↵      userName: exprField(expr: "user.name")↵    }↵  ↵          children(sorts:[{'
                      'name:"ordinal", isAsc: true}, {name:"id", isAsc: true}]) {↵            ↵    id↵    '
                      'orgnizationId↵    code↵    name↵    managerId↵    managerName: exprField(expr: '
                      '"manager.name")↵    executiveId↵    executiveName: exprField(expr: "executive.name")↵    '
                      'supervisorDepartmentId↵    description↵    stopFlag↵    idPath↵    isLeaf↵    parentId↵    '
                      'name↵    disabled: stopFlag↵    relUsers {↵      userId↵      userName: exprField(expr: '
                      '"user.name")↵    }↵  ↵            children(sorts:[{name:"ordinal", isAsc: true}, {name:"id", '
                      'isAsc: true}]) {↵              ↵    id↵    orgnizationId↵    code↵    name↵    managerId↵    '
                      'managerName: exprField(expr: "manager.name")↵    executiveId↵    executiveName: exprField('
                      'expr: "executive.name")↵    supervisorDepartmentId↵    description↵    stopFlag↵    idPath↵    '
                      'isLeaf↵    parentId↵    name↵    disabled: stopFlag↵    relUsers {↵      userId↵      '
                      'userName: exprField(expr: "user.name")↵    }↵  ↵              children(sorts:[{name:"ordinal", '
                      'isAsc: true}, {name:"id", isAsc: true}]) {↵                ↵    id↵    orgnizationId↵    code↵ '
                      '   name↵    managerId↵    managerName: exprField(expr: "manager.name")↵    executiveId↵    '
                      'executiveName: exprField(expr: "executive.name")↵    supervisorDepartmentId↵    description↵   '
                      ' stopFlag↵    idPath↵    isLeaf↵    parentId↵    name↵    disabled: stopFlag↵    relUsers {↵   '
                      '   userId↵      userName: exprField(expr: "user.name")↵    }↵  ↵              }↵            }↵ '
                      '         }↵        }↵      }↵    }↵  }', "variables": "null"},
            {"query": '{↵    BillFlowDefine {↵      id↵      billTypeId↵      billType {↵        value↵        title↵ '
                      '     }↵      isDefault↵      name↵      flowCode↵      description↵      processDefinitionId↵ '
                      '   }↵  }', "variables": "null"},
        ]
        for gql_data in gqlData:
            has_time = self.gql(gql_data)
            # print("has_time"+str(has_time))
            GqlTime = GqlTime + has_time
        return GqlTime

    def main(self, counter):
        loginTime = self.login()
        gqlTime = self.allGql()
        msg = "：登录时间" + str(loginTime / 1000) + "ms，gql时间" + str(gqlTime / 1000) + "ms，总耗时" + str((loginTime + gqlTime) / 1000000) + "秒\n"
        with open('bureau_service.txt', 'a') as f:
            f.write(str(time.strftime("%Y-%m-%d %H:%M:%S"))+"线程数"+str(counter)+msg,)
        print(msg)


class myThread1(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        # print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        # threadLock.acquire()
        # # 释放锁，开启下一个线程
        # threadLock.release()
        w = workSpace()
        w.main(self.counter)


if __name__ == "__main__":
    threadLock = threading.Lock()
    threads = []
    for i in range(1, 51):
        t1 = myThread1(i, "thread" + str(i), str(i))
        t1.start()
        threads.append(t1)
    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")
    with open('bureau_service.txt', 'a') as f:
        f.write('————————————————————分割线———————————————————\n')
