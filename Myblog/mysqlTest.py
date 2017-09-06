import pymysql
conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = 'root',
                       passwd = 'b158160w158160!@#',db = 'myweb')

cur = conn.cursor()

cur.execute("SELECT * FROM myweb.blog_file")
for i in cur:
    print(i)
cur.close()
conn.close()