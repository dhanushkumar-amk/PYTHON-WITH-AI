import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    db='test',
    charset='utf8'
)
