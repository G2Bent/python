from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import *
import os
import urllib.request


#文件保存路径
file_path = r"F:\taqu"

def mkdir_for_girl(path,name):
    """
    创建以标题命令的目录
    :param path: 目录路径
    :param name: 目录名称
    :return: 返回创建的目录路径
    """
    path = os.path.join(path,name)
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def save_pictures(path,url_list):
    """
    保存图片到本地的指定文件夹
    :param path:保存图片的文件夹，有mkdir_for_girl返回
    :param url_list:待保存图片的url列表
    :return:none
    """
    for (index,url) in enumerate(url_list):
        try:
            print("%s 正在保存第%d图片" % (ctime(),index))
            pic_name = str(index) + '.jpg'
            file_name = os.path.join(path,pic_name)
            #如果存在该图片则不保存
            if os.path.exists(file_name):
                print("%s 该图片已经存在"%ctime())
                continue
            req = urllib.request.Request(url,headers={'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'})
            data = urllib.request.urlopen(req,timeout=30).read()
            f = open(file_name,'wb')
            f.write(data)
            f.close()
        except Exception as e:
            print("%s 第%d张图片保存失败，不处理，跳过继续处理下一张"%(ctime(),index))

def write_text(path,info):
        """
        在path目录中创建txt文件，将info信息（girl的文本描述和对话）写入txt文件中
        :param path: 保存txt文件的目录，由mkdir_for_girl返回
        :param info: 要写入txt的文本内容
        :return:none
        """
        #创建/打开info.txt文件，并写入内容
        filename = os.path.join(path,'info.txt')

        with open(filename,'a+') as fp:
            fp.write(info.encode('utf-8'))
            fp.write('\n'.encode('utf-8'))
            fp.write('\n'.encode('utf-8'))

#打开页面，设置超时时间，窗口最大化
driver = webdriver.Firefox()
#driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.taqu.cn/community/")

#切换到"他趣Girl"页面
driver.find_element_by_partial_link_text("他趣Girl").click()

#-----------------------滑动到窗口最底部，以将所有的girl都刷新出来-----------------------
# 由于页面很长，并且需要不断下拉才会刷新，因此通过javascript来控制器滚动条向下滑动
# 但是一次滑动并不能到达底部，需要多次，那么需要多少次呢？这里采用的方式是不停的向下
# 滑动，每滑动一次，都查询下是否到达底部，怎么查询呢？这是通过查到底部的一个标志图片来判断，
# 如果没找到标志，就说明还没到达底部，需要继续滑动，如果找到就跳出循环

# 为了快速滑动，先设置超时时间为1秒
driver.implicitly_wait(1)

# 不停的滑啊滑
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        # 定位页面底部的一个图片
        driver.find_element_by_xpath(".//*[@id='waterfall-loading']/img[@src='/img/no-more.png']")
        # 如果没抛出异常就说明找到了底部标志，跳出循环
        break
    except NoSuchElementException as e:
        # 抛出异常说明没找到底部标志，继续向下滑动
        pass

# 将超时时间改回10秒
driver.implicitly_wait(10)

# -----------------------找到所有girl的封面图片-----------------------
# 这些封面图片是可点击的，单击都会弹出该girl的所有图片和文字描述
girls = driver.find_elements_by_css_selector("div#container img")
num = len(girls)
print ("girl总数为：%d" % num)


# -----------------------依次点击每张封面，提取每个girl的信息-----------------------
for girl in girls:
    # 依次点击每一个girl的封面
    girl.click()

    # 每点击一个girl后，都再点击一下弹出框，以更新driver，不然driver中的缓存还是上一个girl的
    # 一定要注意这一步啊，撸主当时没有做这一步，折腾了好久
    driver.find_element_by_xpath("html/body/div[3]/div[2]").click()

    # 提取标题，由于标题中的字符:和|不能作为文件名，将他们替换了
    title = driver.find_element_by_css_selector("p.waterfall-detail-header-title").text
    title = title.encode('utf-8')
    title = title.replace(":", "：")
    title = title.replace("|", "丨")
    title = title.decode('utf-8')

    # 在file_path目录下，为该girl创建以标题命名的目录
    path = mkdir_for_girl(file_path, title)

    # 提取该girl所有图片的URL
    pics = driver.find_elements_by_css_selector("div.water-detail-content img")
    pic_url = [x.get_attribute('src') for x in pics]
    print ('该girl的图片总数为：%d' % len(pic_url))

    # 保存图片到本地以该girl标题命名的目录中
    save_pictures(path, pic_url)

    # 提取girl的基本介绍，并写入info.txt文件
    info = driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div[2]").text
    write_text(path, info)

    # 提取所有对话，写入info.txt文件
    talks = driver.find_elements_by_css_selector("div.water-detail-content p")
    for t in talks:
        write_text(path, t.text)

    # 关闭该girl的图片
    driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div/img").click()
    print ('该girl信息提取完成，继续处理下一个')
    sleep(1)

# -----------------------所有girl信息提取完成-----------------------
driver.close()
print ('恭喜，所有girl信息提取完成！')
