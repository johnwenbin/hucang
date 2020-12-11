import requests
import xlwt
import xlrd
import json
import DMAutoTestReport.deviceFunction as function
import time


class deptnew:

    def __init__(self):
        # self.baseUrl = "http://140.249.154.2:9005/"
        self.baseUrl = 'http://58.215.200.58:19668/'
        # self.param = {'userID': 'admin', 'pwd': 'Safery001com!'}
        self.param = {'userID': 'admin', 'pwd': '1111QQqq'}
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))
        self.token = function.DeviceFunction().getToken()
        self.num = 201

    # 一级部门
    def yijidept(self):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/dept/operateDept"
        while self.num <= 400:
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num), 'deptCode': 'CSBM' + str(self.num),
                                'orderIndex': '0', 'deptFatherId': ''}, headers=headers)
            deptId1 = json.loads(r.text).get('result').get('deptId')
            print('一级部门Id值为' + deptId1)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '儿子部门', 'deptCode': 'CSBM'
                                + str(self.num) + 'son', 'orderIndex': '0', 'deptFatherId': deptId1}, headers=headers)
            deptId2 = json.loads(r.text).get('result').get('deptId')
            print('二级部门Id值为' + deptId2)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonson', 'orderIndex': '0', 'deptFatherId': deptId2}, headers=headers)
            deptId3 = json.loads(r.text).get('result').get('deptId')
            print('三级部门Id值为' + deptId3)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '曾孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonsonson', 'orderIndex': '0', 'deptFatherId': deptId3}, headers=headers)
            deptId4 = json.loads(r.text).get('result').get('deptId')
            print('四级部门Id值为' + deptId4)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '曾曾孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonsonsonson', 'orderIndex': '0', 'deptFatherId': deptId4}, headers=headers)
            deptId5 = json.loads(r.text).get('result').get('deptId')
            print('五级部门Id值为' + deptId5)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '曾曾曾孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonsonsonsonson', 'orderIndex': '0', 'deptFatherId': deptId5}, headers=headers)
            deptId6 = json.loads(r.text).get('result').get('deptId')
            print('六级部门Id值为' + deptId6)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '曾曾曾曾孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonsonsonsonsonson', 'orderIndex': '0', 'deptFatherId': deptId6}, headers=headers)
            deptId7 = json.loads(r.text).get('result').get('deptId')
            print('七级部门Id值为' + deptId7)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '曾曾曾曾曾孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonsonsonsonsonsonson', 'orderIndex': '0', 'deptFatherId': deptId7}, headers=headers)
            deptId8 = json.loads(r.text).get('result').get('deptId')
            print('八级部门Id值为' + deptId8)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '曾曾曾曾曾曾孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonsonsonsonsonsonsonson', 'orderIndex': '0', 'deptFatherId': deptId8}, headers=headers)
            deptId9 = json.loads(r.text).get('result').get('deptId')
            print('九级部门Id值为' + deptId9)
            r = requests.post(url, {'deptId': '', 'deptName': '测试部门' + str(self.num) + '曾曾曾曾曾曾曾孙子部门', 'deptCode': 'CSBM'
                                   + str(self.num) + 'sonsonsonsonsonsonsonsonson', 'orderIndex': '0', 'deptFatherId': deptId9}, headers=headers)
            deptId10 = json.loads(r.text).get('result').get('deptId')
            print('十级部门Id值为' + deptId10)
            print('-------------------' + str(self.num) + '-------------------')
            self.num += 1
        else:
            print('新增完成')


if __name__ == '__main__':
    deptnew().yijidept()