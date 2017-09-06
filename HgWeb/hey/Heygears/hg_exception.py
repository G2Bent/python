#-*- coding:utf-8 -*-
class VerifyExcelException(Exception):
    def __init__(self, err='Excel表格数据填写不正确！'):
        Exception.__init__(self, err)

class OpenUrlException(Exception):
    def __init__(self,err='url为空！'):
        Exception.__init__(self,err)

class PictureScrollTopException(Exception):
    def __init__(self,err='ScrollTop的高度必须大于0！'):
        Exception.__init__(self,err)

class TextNoneException(Exception):
    def __init__(self,err='文本内容为空！'):
        Exception.__init__(self,err)

class OperationNoFind(Exception):
    def __init__(self,err='Operation No Find!'):
        Exception.__init__(self,err)

class MobileCodeNoeException(Exception):
    def __init__(self,err='获取验证码的接口异常'):
        Exception.__init__(self,err)

class AssertFailException(Exception):
    def __init__(self,err='匹配失败！'):
        Exception.__init__(self,err)

class AttributeNotFindException(Exception):
    def __init__(self,err='获取的属性为空！请检查是否写错！'):
        Exception.__init__(self,err)