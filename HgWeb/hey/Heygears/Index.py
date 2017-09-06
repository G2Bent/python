#-*- coding:utf-8 -*-
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles.colors import RED,BLUE
from Heygears.Excels import hg_excel
from pyecharts import Bar
from Heygears.hg_exception import VerifyExcelException
import xml.dom.minidom,time,os

if __name__ == '__main__':
    Excel_url = os.getcwd()+'\Excel'                                                #测试文档的路径
    file_list = os.listdir(Excel_url)                                               #测试文档下

    #读取配置文件（xml）
    dom = xml.dom.minidom.parse('config.xml')
    root = dom.documentElement
    url = root.getElementsByTagName('test_url')[0].getAttribute('url')              #测试的超链接
    like_file = root.getElementsByTagName('file')[0].getAttribute('filename')       #测试的匹配文件

    #判断excel表格是否符合规范
    excel_test_result = list()
    for file in file_list:
        if file.startswith(like_file):
            hg = hg_excel(url=url, file_url=Excel_url + '\\' + file)
            excel_test_result.append(hg.Verify_Excel(file.replace('.xlsx','')))
    for result in excel_test_result:
        if 'False' in result:
            raise VerifyExcelException



    Now_time = time.strftime('%Y-%m-%d %H-%M-%S')                                   #当前时间
    Report_file_url = os.getcwd()+'\Report\\'+Now_time                              #使用当前时间生成报告目录的文件路径
    Report_picture_url = Report_file_url + '\Picture'                               #测试图片的路径
    os.makedirs(Report_file_url)                                                    #根据路径创建文件夹
    os.makedirs(Report_picture_url)                                                 #图片路径

    fail_list, pass_list, attr = list(), list(), list()

    # 表格报告
    report_workbook ,first= openpyxl.Workbook(),True
    for file in file_list:
        if file.startswith(like_file):
            attr.append(file)
            file_name = file.replace('.xlsx', '')
            if first == True:
                rwk = report_workbook.active
                first = False
            else:
                rwk = report_workbook.create_sheet()
            rwk.title = file_name
            report_sheet = report_workbook.get_sheet_by_name(file_name)
            font_RED = Font(color=RED)
            report_sheet['A1'], report_sheet['B1'], report_sheet['C1'], report_sheet['D1'] = \
                '测试用例', '输出值', '测试结果', '图片链接'
            report_sheet['A1'].font, report_sheet['B1'].font, report_sheet['C1'].font, report_sheet['D1'].font = \
                font_RED, font_RED, font_RED, font_RED

            hg = hg_excel(url=url,file_url=Excel_url+'\\'+file)
            test_result = hg.Open_Excel(
                file_name=file_name,
                report_sheet = report_sheet,
                Report_picture_url=Report_picture_url
            )
            pass_count, fail_count = test_result[0],test_result[1]
            pass_list.append(pass_count)
            fail_list.append(fail_count)

    #可视化测试报告
    bar = Bar('测试报告')
    bar.add("Pass",attr,pass_list)
    bar.add("Fail",attr,fail_list)
    bar.render(Report_file_url + '\\report.html')
    report_workbook.save(Report_file_url + '\\report.xlsx')