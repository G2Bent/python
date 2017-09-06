from urllib import request
import warnings
from bs4 import BeautifulSoup as bs
import codecs


warnings.filterwarnings('ignore')

#分析网页函数
def getNowPlayingMovie_list():
    return nowplaying_list

#爬去评论函数
def getCommentsById(movieId,pageNum):
    if pageNum>0:
        start = (pageNum-1)*20
    else:
        return False
    requrl = 'https://movie.douban.com/subject/' + movieId + \
             '/comments' +'?' +'start=' + str(start) + '&limit=20'
    print(requrl)
    return eachCommentList
def main():
    commentList = []
    NowPlayingMovie_list = getNowPlayingMovie_list()
    for i in range(10):
        num = i+1
        commentList_temp = getCommentsById(NowPlayingMovie_list[0]['id'],num)
        commentList.append(commentList_temp)

        for k in range(len(commentList)):
            comments = comments + (str(commentList[k])).strip()

worldcloud = WordCloud()

resp = request.urlopen("https://movie.douban.com/nowplaying/guangzhou/")
html_data = resp.read().decode("utf-8")
# print(html_data)

soup = bs(html_data,'html.parser')
nowplaying_movie = soup.find_all('div',id= 'nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all('li',class_='list-item')
# print(nowplaying_movie_list[5])
nowplaying_list = []
for item in nowplaying_movie_list:
    nowplaying_dict = {}
    nowplaying_dict['id'] = item['data-subject']
    for tag_img_item in item.find_all('img'):
        nowplaying_dict['name'] = tag_img_item['alt']
        nowplaying_list.append(nowplaying_dict)
# print(nowplaying_list)


resp = request.urlopen(requrl)
# print(requrl)
# print(resp)
comment_div_list = soup.find_all('div',class_='comment')
# print(comment_div_list)
eachCommentList = [ ];
for item in comment_div_list:
    if item.find_all('p')[0].string is not None:
        eachCommentList.append(item.find_all('p')[0].string)
# print(eachCommentList)