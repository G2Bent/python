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

    def func_float(self):
        #字符串或整数转化为浮点数
        a = float(1)
        return a

    #list() 参数为可迭代列表对象

    #tuple()元组

    #dict()创建数据字典

    #set()创建集合

    #frozenset() 不可变集合

    #dir() 不带参数时返回当前范围的变量，方法和定义的类型列表，带参数时返回参数的属性，方法列表

    #divmod()分别取商和余数，二个参数x和y，输出元组(x//y,x%y)
    def func_divmod(self):
        res = divmod(100,3)
        return res

    #enumerate()返回一个可以枚举的对象，该对象的next()方法将返回一个元组
    def func_enumerate(self):
        for i in enumerate(['a','b','c','d']):
            print(i)
        return True

    #eval()将字符串str中的表达式提取出来并运行
    def func_evals(self):
        s = "1 + 2 * 3"
        return type(s),eval(s)

    #filter()　　过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，
    # 在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据


    #format()　　格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法
    def func_format(self):
        a = "I am {0}, I like {1}".format("derek","python")
        return a

    #getattr()　　获取对象的属性
    def func_getattr(self):
        # getattr(object ,name[ ,defalut ])
        # 获取对象object名为name的特性，如果object不包含名为name的特性，将会抛出AttributeError异常；如果不包含名为name的特性
        # 且提供default参数，将返回default。
        # 参数object：对象
        # 参数name：对象的特性名
        # 参数default：缺省返回值
        a = getattr(list,'append')
        mylist = [3,4,5]
        mylist.append(6)
        return mylist


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
    print(r.func_getattr())
    # print(Province.show())