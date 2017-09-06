"""
              ┏┓    ┏┓
            ┏━┛┻━━━━┛┻━┓
            ┃     ☃    ┃
            ┃   ┳┛ ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑 ┣┓
              ┃　永无BUG！┏┛
              ┗┓┓┏━━━━┳┓┏┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from web.models import File
import os
from django import forms
# Create your views here.

# #首页
# def index(request):
#     return render_to_response("web/index.html")

#上传文件
def index(request):
    files =File.objects.all()
    return render_to_response("web/upload.html",{"file_list":files})

def upload_save(request):
    files = File.objects.all()
    filename = request.POST.get("filename","")
    fileing = request.FILES.get("fileing","")
    if filename =="" or fileing =="":
        error = "文件和文件名不能为空"
        return render_to_response("web/upload.html",{'error':error,"file_list":files})
    else:
        upload = File()
        upload.filename = filename
        upload.fileway = fileing
        upload.save()
        return render_to_response("web/upload_s.html",{'upload_success':'上传文件成功',
                                                       'file_list':files})
def action(request):
    # test = request.GET.get("test")
    # os.system("testbaidu.py")
    files = File.objects.all().last()
    return render_to_response("web/action.html",{"file_list":files})

def report(request):
    os.listdir("F:\HgWeb\hey\Heygears\Report")
    return render_to_response("web/report.html")

def button(request):
    # python = 'D:\python3.6.2\python.exe'
    # file  = 'testbaidu.py'
    # cmd = '%s,%s'% python,file
    os.system('python hey/Heygears/tests.py')
    return render(request,"web/test.html")