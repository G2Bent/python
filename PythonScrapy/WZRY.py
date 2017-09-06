import requests
import re
from bs4 import BeautifulSoup
import os

url = "https://pvp.qq.com/web201605/js/herolist.json"
#print(url)
#def get_hero_name(url):
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/59.0.3071.115 Safari/537.36'}
html = requests.get(url,headers = head)
html.encoding = 'utf-8'
#print(html.text)
#html = requests.get(url)
html_json = html.json()
    # hero_name = html_json['data'].keys()
    # list_of_nameMax = list(hero_name)

    # list_of_nameMin = []
    # for ii in list_of_nameMax:
    #     name = ii.lower()
    #     list_of_nameMin.append(name)
    # return list_of_nameMin
#print(html_json)

#提取英雄名字和数字
hero_name = list(map(lambda x:x['cname'],html_json))#名字
hero_number = list(map(lambda x:x['ename'],html_json))#数字

#用于下载并保存图片
def main():
    #list_name = list_of_name
    #for i in range(0,100):
    i= 0
    for v in hero_number:
        os.mkdir("E:/learning/pyDjango/myweb/blog/demo/img/"+hero_name[i])
        os.chdir("E:/learning/pyDjango/myweb/blog/demo/img/"+hero_name[i])
        i =i+1
        for u in range(12):
            onehero_links = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"+str(v)+'/'+str(v)\
                                +'-bigskin-'+str(u)+'.jpg'
            im = requests.get(onehero_links)
            if im.status_code == 200:
                iv = re.split('-',onehero_links)
                open(iv[-1],'wb').write(im.content)

if __name__ == '__main__':
    main()