#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/11/18 6:28 下午
# @Author :
# @File : inner_function.py
# @desc:

class InnerFunc():

    #获取绝对值
    def func_abs(self):
        a = -10
        # a.__abs__()
        # return abs(a)
        return abs(a)

    #参数可迭代对象，迭代对象为空时，返回True，如果迭代对象的所有元素都为真，那么返回True，否则返回False
    def func_all(self):
        a = all(['python',123])
        b = all([])
        c = all([0])
        d = all("")
        e = all(1,' ',2,None)
        return e

    #any() 参数为可迭代对象，参数为空时返回True
    def func_any(self):
        a = any([None,0,'',(),1])
        b = any('')
        return a

    #sum() 求和
    def func_sum(self):
        res = sum(i for i in range(5))
        return res

    #bin() 将参数转化为二进制
    def func_bin(self):
        a = bin(3)
        return a

    #bool()布尔函数，返回bool值，False或True
    def func_bool(self):
        a = bool(3)
        b = bool(0)
        return a,b

    #ascli()调用对象的__repr__()方法，获得该方法的返回值

    #bytes()将一个字符串转化为字节类型
    def func_bytes(self):
        a = bytes('python',encoding="UTF-8")
        return a

    #str()将字符类型/数值转化为字符串类型
    def func_str(self):
        a = str(1)
        return a

    #chr()查看十进制数对应的ASCLI字符
    def func_chr(self):
        a = chr(65)
        return a

    #ord()查看某个ASCLI对应的十进制
    def func_ord(self):
        a = ord('a')
        return a

    #callabe()判断对象是否可以被调用，能被调用的对象就是一个callables对象，比如函数和带有__call__()的实例

    # complie() 将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译
    '''
    compile(source ,filename ,mode ,flags=0 ,dont_inherit=False ,optimize=-1)
    说明：
        1.将 source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
        2.参数 source：字符串或者AST（Abstract Syntax Trees）对象。即需要动态执行的代码段。
        3.参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。当传入了source参数时，filename参数传入空字符即可。
        4.参数mode：指定编译代码的种类，可以指定为 ‘exec’ ,’eval’ ,’single’。当source中包含流程语句时，mode应指定为‘exec’；当source中只包含一个简单的求值表达式，mode应指定为‘eval’；当source中包含了交互式命令语句，mode应指定为'single'。
    '''

    def func_exec(self):
        # 流程语句使用exec
        code1 = 'for i in range(10):print(i)'
        aa = compile(code1,'','exec')
        return exec(aa)

    def func_eval(self):
        #简单求值表达式用eval
        code2 = "1+2+3+4"
        bb = compile(code2,'','eval')
        return eval(bb)

    def func_single(self):
        #交互语句用single
        code3 = "name = input('please input your name:')"
        cc = compile(code3,'','single')
        return exec(cc)

    #complex()
    def func_complex(self):
        # 1 创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数是字符串，则不需要指定第二个参数。
        # 2 参数real：int，long，float或字符串。
        # 3 参数imag：int，long，float
        x = complex(1-2j)
        return x.real,x.imag

    #delattr()删除对象属性



    #classmethod() 用来置顶一个方法为类的方法，由类直接调用执行，只有一个cls参数，执行类的方法时，自动将调用该方法的类赋值给cls，没有此参数指定的方法为实例方法
class Province:
    country = "中国"

    def __init__(self,name):
        self.name = name

    @classmethod
    def show(cls):
        print(cls)




if __name__ == '__main__':
    r = InnerFunc()
    print(r.func_complex())
    # print(Province.show())