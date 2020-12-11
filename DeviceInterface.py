import requests
import xlwt
import xlrd
import json
import DMAutoTestReport.deviceFunction as function
import time


class DeviceInterface:

    def __init__(self):
        # self.baseUrl = "http://140.249.154.2:9005/"
        self.baseUrl = 'http://192.168.1.64:8090/'
        # self.param = {'userID': 'admin', 'pwd': 'Safery001com!'}
        self.param = {'userID': 'admin', 'pwd': '312b248f2e48ff1e27dccc6a4552e3cb', 'dataSource': 'AZT_DEVICE'}
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))
        self.token = function.DeviceFunction().getToken()

    # 新增设备类型检测
    def deviceTypeAdd(self):
        headers = {'token': self.token}
        print(headers)
        url = self.baseUrl + "/v1/saferycom/l/supplier/check/operateDevicesCheck"
        f = open('测试用文件.zip', 'rb')     # 打开文件
        files = {'file': f}
        r = requests.post(url, {'name': '测试test' + self.date, 'type': '22', 'systemName': '''[
            # "Professional (64)",
            # "Windows 10 R2 (64)",
            # "Windows XP",
            # "Windows Vista",
            # "Windows 7 (32)",
            # "Windows 7 (64)",
            # "Windows 8 (32)",
            # "Windows 8 (64)",
            # "Windows 10 (32)",
            # "Windows 10 (64)",
            # "Windows XP (32)",
            # "Windows Server 2016 (64)"
        ]''',
                                'switchFlg': '0', 'allState': '1', 'devicesTypeId': '1', 'checkValue': '测试test',
                                "validate": "26dc569828a7ed1f0f008d13c94929a5"},
                          headers=headers, files=files)
        f.close()   # 关闭文件
        result = json.loads(r.text)
        print(result)
        checkItemId = json.loads(r.text).get('result').get('checkItemId')
        print('设备类型检测项的Id值为' + checkItemId)
        return checkItemId

    # 修改设备类型检测
    def deviceTypeCheckUpdate(self, checkItemId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/check/operateDevicesCheck"
        requests.post(url, {'checkItemId': checkItemId, 'name': '测试test修改' + self.date, 'type': '22', 'systemName': '''[
            "Professional (64)",
            "Windows 10 R2 (64)",
            "Windows XP",
            "Windows Vista",
            "Windows 7 (32)",
            "Windows 7 (64)",
            "Windows 8 (32)",
            "Windows 8 (64)",
            "Windows 10 (32)",
            "Windows 10 (64)",
            "Windows XP (32)",
            "Windows Server 2016 (64)"
        ]''',
                            'switchFlg': '0', 'allState': '1', 'devicesTypeId': '1', 'checkValue': '测试test修改'},
                      headers=headers)

    # 新增系统环境组
    def systemGroupAdd(self):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/system/group/operateSystemGroup"
        r = requests.post(url, {'systemCheckGroupId': None, 'name': 'auto测试' + self.date}, headers=headers)
        systemCheckGroupId = json.loads(r.text).get('result').get('systemCheckGroupId')
        print('系统环境组的Id值为' + systemCheckGroupId)
        return systemCheckGroupId

    # 修改系统环境组
    def systemGroupUpdate(self, systemCheckGroupId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/system/group/operateSystemGroup"
        requests.post(url, {'systemCheckGroupId': systemCheckGroupId, 'name': 'auto测试修改' + self.date}, headers=headers)

    # 新增系统环境检测
    def systemGroupCheckAdd(self, systemCheckGroupId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/system/check/operateSystemCheck"
        f = open('测试用文件.zip', 'rb')     # 打开文件
        files = {'file': f}
        r = requests.post(url, {'name': 'auto测试' + self.date, 'type': '22', 'systemName': '''[
            "Professional (64)",
            "Windows 10 R2 (64)",
            "Windows XP",
            "Windows Vista",
            "Windows 7 (32)",
            "Windows 7 (64)",
            "Windows 8 (32)",
            "Windows 8 (64)",
            "Windows 10 (32)",
            "Windows 10 (64)",
            "Windows XP (32)",
            "Windows Server 2016 (64)"
        ]''',
                                'switchFlg': '0', 'allState': '1', 'systemCheckGroupId': systemCheckGroupId,
                                'checkValue': '测试test'}, headers=headers, files=files)
        f.close()   # 关闭文件
        checkItemId = json.loads(r.text).get('result').get('checkItemId')
        print("系统环境组检测项的Id值为" + checkItemId)
        return checkItemId

    # 修改系统环境检测
    def systemGroupCheckUpdate(self, checkItemId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/system/check/operateSystemCheck"
        requests.post(url, {'checkItemId': checkItemId, 'name': '测试test修改' + self.date, 'type': '22', 'systemName': '''[
            "Professional (64)",
            "Windows 10 R2 (64)",
            "Windows XP",
            "Windows Vista",
            "Windows 7 (32)",
            "Windows 7 (64)",
            "Windows 8 (32)",
            "Windows 8 (64)",
            "Windows 10 (32)",
            "Windows 10 (64)",
            "Windows XP (32)",
            "Windows Server 2016 (64)"
        ]''',
                            'switchFlg': '0', 'allState': '1', 'devicesTypeId': '1', 'checkValue': '测试test修改'},
                      headers=headers)

    # 删除系统环境检测
    def systemGroupCheckDelete(self, checkItemId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/check/deleteDevicesCheck"
        requests.post(url, {'checkItemId': checkItemId}, headers=headers)

    # 删除系统环境组
    def systemGroupDelete(self, systemCheckGroupId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/system/group/deleteSystemGroup"
        requests.post(url, {'systemCheckGroupId': systemCheckGroupId}, headers=headers)

    # 新增供应商
    def supplierAdd(self):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/operateSupplier"
        r = requests.post(url, {'supplierId': None, 'name': 'auto测试' + self.date, 'supplierAddr': 'auto测试',
                                'saleAfterName': 'auto测试', 'saleAfterPhone': '123123123',
                                'saleAfterMail': 'autotest@autotest.com'}, headers=headers)
        supplierId = json.loads(r.text).get('result').get('supplierId')
        print('供应商的Id值为：' + supplierId)
        return supplierId

    # 修改供应商
    def supplierUpdate(self, supplierId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/operateSupplier"
        requests.post(url, {'supplierId': supplierId, 'name': 'auto测试修改' + self.date, 'supplierAddr': 'auto测试修改',
                            'saleAfterName': 'auto测试修改', 'saleAfterPhone': '123123123000',
                            'saleAfterMail': 'autotestupdate@autotestupdate.com'}, headers=headers)

    # 删除供应商
    def supplierDelete(self, supplierId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/deleteSupplier"
        requests.post(url, {'supplierId': supplierId}, headers=headers)

    # 新增供应商设备
    def deviceAdd(self, supplierId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/operateDevices"
        f = open('测试用文件.zip', 'rb')     # 打开文件
        files = {'file': f}
        r = requests.post(url, {'name': 'auto测试' + self.date, 'displayName': 'vid_1111&pid_1111', 'deviceProgramName': 'auto测试',
                                'configJson': '''{"width": 1600, "height": 1200, "rotate": 0, "isYuv": 1, "cameraindex": 0,
                                               "type": 11, "isseccreen": 1, "orgmode": 0, "maxpre": 0}''',
                                'devicesTypeId': '1', 'supplierId': supplierId}, headers=headers, files=files)
        f.close()   # 关闭文件
        supplierDevicesId = json.loads(r.text).get('result').get('supplierDevicesId')
        return supplierDevicesId

    # 修改供应商设备
    def deviceUpdate(self, supplierDevicesId, supplierId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/operateDevices"
        requests.post(url, {'supplierDevicesId': supplierDevicesId, 'name': 'auto测试修改' + self.date, 'displayName': 'vid_1111&pid_1111',
                            'deviceProgramName': 'auto测试修改', 'configJson': '''{"width": 1600, "height": 1200, "rotate": 0,
                                                                           "isYuv": 1, "cameraindex": 0, "type": 11,
                                                                           "isseccreen": 1, "orgmode": 0, "maxpre": 0}''',
                            'devicesTypeId': '1', 'supplierId': supplierId}, headers=headers)

    # 删除供应商设备
    def deviceDelete(self, supplierDevicesId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/deleteDevices"
        requests.post(url, {'supplierDevicesId': supplierDevicesId}, headers=headers)

    # 新增供应商设备检测
    def deviceCheckAdd(self, supplierId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/check/operateDevicesCheck"
        f = open('测试用文件.zip', 'rb')  # 打开文件
        files = {'file': f}
        r = requests.post(url, {'name': 'auto测试' + self.date, 'type': '22', 'systemName': '''["Professional (64)", "Windows 10 R2 (64)",
                                                                           "Windows XP", "Windows Vista",
                                                                           "Windows 7 (32)", "Windows 7 (64)",
                                                                           "Windows 8 (32)", "Windows 8 (64)",
                                                                           "Windows 10 (32)", "Windows 10 (64)",
                                                                           "Windows XP (32)",
                                                                           "Windows Server 2016 (64)"]''',
                                'switchFlg': '0', 'allState': '1', 'devicesTypeId': '0', 'supplierId': supplierId, 'checkValue': './',
                                "validate": "26dc569828a7ed1f0f008d13c94929a5"},
                          headers=headers, files=files)
        f.close()  # 关闭文件
        checkItemId = json.loads(r.text).get('result').get('checkItemId')
        print("供应商设备检测项的Id值为" + checkItemId)
        return checkItemId

    # 修改供应商设备检测
    def deviceCheckUpdate(self, supplierId, checkItemId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/check/operateDevicesCheck"
        requests.post(url, {'checkItemId': checkItemId, 'name': 'auto测试修改' + self.date, 'type': '22', 'systemName': '''[
                                                                                   "Professional (64)", "Windows 10 R2 (64)",
                                                                                   "Windows XP", "Windows Vista",
                                                                                   "Windows 7 (32)", "Windows 7 (64)",
                                                                                   "Windows 8 (32)", "Windows 8 (64)",
                                                                                   "Windows 10 (32)", "Windows 10 (64)",
                                                                                   "Windows XP (32)",
                                                                                   "Windows Server 2016 (64)"]''',
                            'switchFlg': '0', 'allState': '1', 'devicesTypeId': '0', 'supplierId': supplierId,
                            'checkValue': './'},
                      headers=headers)

    # 删除供应商设备检测
    def deviceCheckDelete(self, checkItemId):
        headers = {'token': self.token}
        url = self.baseUrl + "/v1/saferycom/l/supplier/check/deleteDevicesCheck"
        requests.post(url, {'checkItemId': checkItemId}, headers=headers)

    # 


if __name__ == '__main__':
    DeviceInterface().deviceTypeAdd()
    # DeviceInterface().deviceTypeAdd()
    # DeviceInterface().deviceTypeUpdate()
    # DeviceInterface().systemGroupAdd()
    # DeviceInterface().systemGroupUpdate()
