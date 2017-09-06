# -*- coding:utf-8 -*-
import unittest,time,json,urllib.request,os,urllib.parse,requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from copy import copy
from Heygears.Selenium import hg_selenium
from Heygears.hg_exception import OpenUrlException,\
    PictureScrollTopException,TextNoneException,OperationNoFind,\
    MobileCodeNoeException,AssertFailException,AttributeNotFindException


class handing_data(hg_selenium,unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []  # 记录脚本运行错误信息
        self.accept_next_alert = True  # 是否接受弹窗警告，默认为True

    #Checkpoint
    #每个一秒就扫描一次attribute_value是否与 Checkpoint 相同
    def hg_attribute_Checkpoint(self,element,attribute,Checkpoint):
        result = False
        for i in range(0,20):
            attribute_value = self.hg_get_attribute(element, attribute)
            if Checkpoint == attribute_value:
                result = True
                break
            time.sleep(0.5)
        return result
    #每个一秒就扫描一次获取的文本 text 是否与 Checkpoint 相同
    def hg_text_Checkpoint(self,element,Checkpoint):
        result = False
        for i in range(0,20):
            text = self.hg_text(element).strip()
            if Checkpoint == text:
                result = True
                break
            time.sleep(0.5)
        return result

    #excel表格转化为字典
    def file_content_to_dict(self, file_content):
        dict_key,dict_a,dict_b,dict_c = ['index',
                                         'Operating_instructions',
                                         'wait_time',
                                         'element',
                                         'Operation',
                                         'Operation_value',
                                         'picture',
                                         'Output_element',
                                         'Output_value'], {}, {}, {}

        for (index, content) in enumerate(file_content):
            for i in range(len(content)):
                dict_b[dict_key[i]] = content[i]
            #copy，如果没有复制，那么地址变量是一致的
            dict_c = copy(dict_b)
            dict_a[index] = dict_c
        return dict_a

    #获取售后的验证码
    def after_sale_mobile_code(self,mobile):
        mobile_code= None
        try:
            TOKEN = json.loads(urllib.request.
                               urlopen('http://test.kong.business.heygears.com/common/token/get?api-key=58b5b2c732f0476582e66302b09f4796').read()
                               )
            TOKEN_Value = TOKEN['data']['token']
            url = 'http://test.kong.business.heygears.com/common/sms/code?token=' + str(
                TOKEN_Value) + '&mobile='+str(mobile)+'&type=104'
            mobile_code = json.loads(urllib.request.urlopen(url).read())
            # 售后点击提交的时候，会验证SID，所以要修改SID
            js = r"testChangeSid('" + str(mobile_code['data']['sid']) + "')"
            self.hg_run_js(js)
        except urllib.request.URLError as e:
            print(e.reason)
        return mobile_code['err_msg']

    #获取官网的验证码
    def www_mobile_code(self,mobile):
        mobile_code = None
        try:
            TOKEN = json.loads(
                requests.get('http://test.kong.business.heygears.com/common/token/get?api-key=47281ccb043e49a59aaa769881b7c285').text
            )
            TOKEN_Value = TOKEN['data']['token']
            url = 'http://test.kong.business.heygears.com/goods/book/mobile-code'
            headers = {"Content-Type":"application/json"}
            data_dict = {'token':TOKEN_Value,'mobile':mobile}
            data_str = json.dumps(data_dict)
            mobile_code = json.loads(requests.post(url=url, data=data_str, headers=headers).text)
            js = r"testChangeSid('" + str(mobile_code['data']['sid']) + "')"
            self.hg_run_js(js)
        except urllib.request.URLError as e:
            print(e.reason)
        return mobile_code['err_msg']

    #selenium操作判断
    def test_hg_selenium(self,content_file,Report_picture_url,report_sheet,index):
        Output = dict()
        for (key,dicts) in content_file.items():
            #先判断element是否为空，不为空之后，才可以执行以下操作
            if dicts['element'] != None:
                #单击
                if dicts['Operation'] == 'click':
                    self.hg_click(dicts['element'])

                #双击
                elif dicts['Operation'] == 'double_click':
                    self.hg_double_click(dicts['element'])

                #鼠标悬停
                elif dicts['Operation'] == 'move':
                    self.hg_move_to_element(dicts['element'])

                #鼠标拖放
                elif dicts['Operation'] == 'drag_drop':
                    #传入开始起始元素位置和结束元素位置
                    self.hg_drag_and_drop(dicts['element'],dicts['element'])

                #写入值
                elif dicts['Operation'] == 'send':
                    self.hg_clear(dicts['element'])
                    self.hg_send(dicts['element'],dicts['Operation_value'])

                #写入验证码
                elif dicts['Operation'] == 'send_code':
                    #判断当前是什么模块
                    current_url = self.hg_current_url()
                    if current_url.startswith('http://test.mall.heygears.com/aftersale'):
                        mobile_code = self.after_sale_mobile_code(dicts['Operation_value'])

                    elif current_url.startswith('http://test.www.heygears.com'):
                        mobile_code = self.www_mobile_code(dicts['Operation_value'])
                    else:
                        mobile_code = None

                    if mobile_code == None:
                        raise MobileCodeNoeException
                    else:
                        self.hg_send(dicts['element'],mobile_code)

                #清除文本
                elif dicts['Operation'] == 'clear':
                    self.hg_clear(dicts['element'])

                #键盘删除文本
                elif dicts['Operation'] == 'Back_Space':
                    self.hg_keys_delete(dicts['element'])

                #进入iframe
                elif dicts['Operation'] == 'iframe':
                    self.hg_iframe(dicts['element'])

                #获取属性的值
                elif dicts['Operation'] == 'get_attribute':
                    attribute_value = self.hg_get_attribute(dicts['element'],dicts['Operation_value'])
                    if attribute_value == None:
                        raise AttributeNotFindException
                    else:
                        Output[dicts['Operating_instructions']] = attribute_value

                #文本断言匹配
                elif dicts['Operation'] == 'assert_text':
                    #判断 --写入的值-- 和 --获取页面-- 的值是否相同\
                        #hg_text需要去除掉前后空格
                    if self.hg_text_Checkpoint(element=dicts['element'],Checkpoint=dicts['Operation_value']):
                        Output[dicts['Operating_instructions']] = '写入值与输出值匹配成功！'
                    else:
                        raise AssertFailException

                #属性断言匹配
                elif dicts['Operation'] == 'assert_attribute':
                    #断言需要传入attribute ，但是文本匹配也是需要传入值，所以这里用(attribute,text)格式写入值
                    Operation_value = dicts['Operation_value'].split(',')
                    attribute, text = Operation_value[0],Operation_value[1]
                    #element,fd,Checkpoint
                    if self.hg_attribute_Checkpoint(element=dicts['element'],attribute=attribute, Checkpoint=text):
                        Output[dicts['Operating_instructions']] = '写入值与输出值匹配成功！'
                    else:
                        raise AssertFailException

                #上传文件(需要事先写好Autolt脚本)
                elif dicts['Operation'] == 'upfile':
                    #注意 Antolt脚本里面的路径是写死的
                    self.hg_move_to_element(dicts['element'])
                    self.hg_click(dicts['element'])
                    os.system(dicts['Operation_value'])
                    #这里是设置等等是为了防止上传窗口还没有关闭，然后点击了其他地方，点击不了
                    time.sleep(2)

                #没有找到操作的话，直接报错
                else:
                    raise OperationNoFind

            #时间等待
            if dicts['wait_time'] != None:
                time.sleep(int(dicts['wait_time']))

            #文本框的输出
            if dicts['Output_element'] != None:
                if self.hg_text(dicts['Output_element']) == '' or self.hg_text(dicts['Output_element']) == None:
                    raise TextNoneException
                else:
                    Output[dicts['Operating_instructions']] = self.hg_text(dicts['Output_element'])

            #添加cookies
            if dicts['Operation'] == 'cookie':
                with open(r'F:\Web\Public\Cookie\get_cookie.py','r') as f:
                    cookies = f.readlines()
                    key,value = cookies[0].replace('\n',''),cookies[1].replace('\n','')
                    self.hg_add_cookie(key,value)

            # 获取当前页面的url
            if dicts['Operation'] == 'get_current_url':
                url = self.hg_current_url()
                if url == None:
                    raise OpenUrlException
                else:
                    Output[dicts['Operating_instructions']] = url

            # 文本断言匹配
            if dicts['Operation'] == 'assert_url':
                # 判断 --写入的值-- 和 --获取页面-- 的值是否相同\
                if dicts['Operation_value'] == self.hg_current_url():
                    Output[dicts['Operating_instructions']] = '写入值与输出值匹配成功！'
                else:
                    raise AssertFailException

            #浏览器前进操作
            if dicts['Operation'] == 'forward':
                self.hg_forward()

            #浏览器后退操作
            if dicts['Operation'] == 'back':
                self.hg_back()

            # 截图
            if dicts['picture'] != None:
                a_list = dicts['picture'].split(',')
                Whether_picture, scrollTop = a_list[0], a_list[1]
                picture_url = Report_picture_url + '\\' + dicts['Operating_instructions'] + '.jpg'
                # scrollTop等于0的话，就直接截取当前图片
                if int(scrollTop) == 0:
                    if Whether_picture == 'Yes' or Whether_picture == 'yes' or Whether_picture == '是':
                        self.hg_save_screenshot(picture_url)
                        if report_sheet['D%d' % (index)].value == None:
                            report_sheet['D%d' % (index)].hyperlink = picture_url
                        else:
                            index += 1
                            report_sheet['D%d' % (index)].hyperlink = picture_url
                elif int(scrollTop) > 0:
                    if Whether_picture == 'Yes' or Whether_picture == 'yes' or Whether_picture == '是':
                        js = 'var q = document.body.scrollTop=' + str(scrollTop)
                        self.hg_run_js(js)
                        self.hg_save_screenshot(picture_url)
                        if report_sheet['D%d' % (index)].value == None:
                            report_sheet['D%d' % (index)].hyperlink = picture_url
                        else:
                            index += 1
                            report_sheet['D%d' % (index)].hyperlink = picture_url
                else:
                    raise PictureScrollTopException
                    # 没有找到操作的话，直接报错
            '''注意！截图要放在最后面！因为涉及到excel报告算法的问题！'''

        return (Output,index)



    # 判断元素是否存在
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 处理弹出的警告框
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 关闭警告框并且获取警告框的信息
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # 收尾工作
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
