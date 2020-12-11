# -*- coding: UTF-8 -*-
import json
import xlwt
import xlrd
import urllib3
import os
import math
import sys
from urllib import parse
from urllib import request

http = urllib3.PoolManager()

# 原系统地址
baseUrl = "http://192.168.1.63:8090/"
# 原系统检测分组
# systemCheckGroupId ={'systemCheckGroupId':'3974947273142556373962','name':'系统默认分组运行'}
systemCheckGroupId = {
    'systemCheckGroupId': '825665511518132', 'name': '系统默认分组运行'}


# 目标系统地址
destbaseUrl = 'http://192.168.1.64:8090/'


# 目标系统检测分组
destSystemCheckGroupId = {'systemCheckGroupId': '1336611306897391618', 'name': '系统默认分组运行'}

# 登陆


def login(url, param):
    return json.loads(http.request('POST', url+"/v1/saferycom/n/login/encryptLogin", fields=param).data)['result']['token']

# 获取环境检测组文件列表


def getSystemCheckList(param, headers):
    return json.loads(http.request('GET', baseUrl+"/v1/saferycom/l/system/check/getSystemCheckList", headers=headers, fields=param).data)

# 下载文件


def downloadfile(fildid, index, worksheet, headers):
    response = http.request(
        'GET', baseUrl+"/v1/saferycom/download_file/"+fildid, headers=headers)
    filename = parse.unquote(response.headers['Content-Disposition'])
    filename = filename.split('=')[1]
    worksheet.write(index, 6, filename)
    with open(filename, 'wb') as f:
        f.write(response.data)


def CopySrcCheckListIntoExcel(userInfo):
    print('下载 检测项目')
    headers = {'token': login(baseUrl, userInfo)}
    r = getSystemCheckList({'curPage': '1', 'curPageCount': '300',
                            'systemCheckGroupId': systemCheckGroupId['systemCheckGroupId']}, headers)
    if r['isSuccess'] == False:
        print('getSystemCheckList Error')
        return
    # excel创建文件
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('test')
    index = 0
    # 循环遍历检测项目，将检测项目存入excel，如果有检测文件，则下载检测文件。
    for item in r['result']['checkList']:
        if item['switchFlg'] == '0':  # 如果检测项目被关闭则跳过
            continue
        print('当前检测项目名称:'+item['name']+',进度'+str(index)+"/" +
              str(len(r['result']['checkList'])))  # 打印名称，显示展示进度
        worksheet.write(index, 0, item['type'])
        worksheet.write(index, 1, item['name'])
        worksheet.write(index, 2, item['checkValue'])
        worksheet.write(index, 3, item['systemName'])
        worksheet.write(index, 4, item['allState'])
        worksheet.write(index, 5, item['fileId'])
        if item['fileId'] != '' and item['fileId'] != None:
            downloadfile(item['fileId'], index, worksheet, headers)
        index = index+1
        print('当前检测项目->'+item['name']+'下载完成!')
    print('完成')
    workbook.save(systemCheckGroupId['systemCheckGroupId']+'.xls')

# 更新系统配置文件


def UpdateDestSysconfig(userInfo):
    print("更新系统配置文件")
    headers = {'token': login(destbaseUrl, userInfo)}
    srcConfig = json.loads(http.request(
        'GET', baseUrl+"/v1/saferycom/n/client/SystemConfig").data)
    if srcConfig['isSuccess'] == False:
        print('当前获取配置文件错误:'+r['message'])
        return
    for item in srcConfig['result']:
        if item['id'] == '7' or item['id'] == '8' or item['id'] == '9' or item['id'] == '10' or item['id'] == '2' or \
                item['id'] == '3' or item['id'] == '4' or item['id'] == '6' or item['id'] == '13' or item['id'] == '14' \
                or item['id'] == '20' or item['id'] == '18' or item['id'] == '17' or item['id'] == '15' or \
                item['id'] == '22' or item['id'] == '21' or item['id'] == '23':
            continue
        rt = json.loads(http.request('POST', destbaseUrl+"/v1/saferycom/l/common/operateConfig",
                                     headers=headers, fields=item).data)
        if rt['isSuccess'] == False:
            print('当前检测项目->'+item['id']+'创建错误:'+rt['message'])
            # return
        else:
            print('当前检测项目->'+item['id']+',创建成功')


# 读取excel更新指定分组


def readExcelToDest(userInfo):
    print('拷贝检测项目')
    headers = {'token': login(destbaseUrl, userInfo)}
    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    book = xlrd.open_workbook(systemCheckGroupId['systemCheckGroupId']+'.xls')
    sheet1 = book.sheets()[0]
    index = 0
    for item in sheet1._cell_values:
        print('当前检测项目名称:'+item[1]+',进度'+str(index)+"/" +
              str(len(sheet1._cell_values)))  # 打印名称，显示展示进度
        files = {'switchFlg': '1', 'name': item[1], 'checkValue': item[2], 'systemName': item[3], 'allState': str(
            item[4]).split('.')[0], 'type': item[0], 'systemCheckGroupId': destSystemCheckGroupId['systemCheckGroupId']}
        if item[6] != '':
            with open(os.path.abspath(item[6]), 'rb') as fp:
                file_data = fp.read()
            filename = {'name': item[6]}
            filename = parse.urlencode(filename)
            files['file'] = (filename.split('=')[1],
                             file_data)
        r = json.loads(http.request('POST', destbaseUrl+'/v1/saferycom/l/system/check/operateSystemCheck',
                                    headers=headers, multipart_boundary=boundary, fields=files).data)
        if r['isSuccess'] == False:
            print('当前检测项目->'+item[1]+'创建错误:'+r['message'])
            return
        print('完成')
        index = index+1

# 下载拷贝


def main_prc():
#    UpdateDestSysconfig({'userID': 'admin', 'pwd': '312b248f2e48ff1e27dccc6a4552e3cb', 'dataSource': 'AZT_DEVICE'})
#    CopySrcCheckListIntoExcel({'userID': 'admin', 'pwd': '312b248f2e48ff1e27dccc6a4552e3cb', 'dataSource': 'AZT_DEVICE'})
    readExcelToDest({'userID': 'admin', 'pwd': '312b248f2e48ff1e27dccc6a4552e3cb', 'dataSource': 'AZT_DEVICE'})


if __name__ == '__main__':
    main_prc()
