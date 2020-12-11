import requests
import json
import os
from PIL import Image
import pandas
import xlsxwriter
import openpyxl
from openpyxl.drawing.image import Image
import DMAutoTestReport.deviceFunction as dF
import time


class ExcelReport:

    def __init__(self):
        self.path = 'ScreenShot'
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))

    def excel_image(self, filein):
        # 获取截图文件夹目录
        path = dF.DeviceFunction().currentDir(self.path)
        print('获取截图文件夹路径：' + path)
        # 获取截图图片名前缀
        png_name = dF.DeviceFunction().png_name(path)
        # 定义变量
        row = 0
        E = []
        # openpyxl打开excel
        wb = openpyxl.load_workbook(filein)
        sheet = wb.active
        # 获取excel行数
        num = sheet.max_row - 1
        # 定义图片尺寸
        new_size = (160, 90)
        # pandas读取excel
        df = pandas.read_excel(filein)
        # 遍历第一列内容并写入E数组
        while row < num:
            data = df.iloc[row, 0]
            E.append(str(data).split('-')[0])
            # print(E)
            # print(data)
            # 判断E数组中的第row个字符串是否在png_name中，是就将图片写入excel
            if E[row] in png_name:
                # 图片路径
                img = Image(path + "\\" + str(data) + '.png')
                # 设备图片尺寸
                img.width, img.height = new_size
                # 将图片写入‘I’列的第（row+2）行
                sheet.add_image(img, 'I' + str(row+2))
                print('写入图片：' + data)
            row = row + 1
        # 保存到excel
        wb.save('设备管理程序后台' + self.date + '内测测试报告.xlsx')


if __name__ == '__main__':
    ExcelReport().excel_image('设备管理程序上线测试报告.xlsx')