from urllib import request
import time
import MySQLdb
import MySQLdb.cursors
from items import get_insert_sql
from bs4 import BeautifulSoup
import json
from settings import MY_USER_AGENT


header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "scrapy"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
TIMEOUT = 1

base_url = 'https://developer.android.com/'



def dbpa():
    dbparms = dict(
                host = MYSQL_HOST,
                db = MYSQL_DBNAME,
                user = MYSQL_USER,
                passwd = MYSQL_PASSWORD,
                charset='utf8',
                cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=True,
    )
    return dbparms

def insert_db(sql,params):
    db = MySQLdb.connect(**dbpa())
    cursor = db.cursor()
    cursor.execute(sql,params)
    db.commit()
    cursor.close()
    db.close()

def tostr(arr):
    dest = []
    for i in range(len(arr)):
        dest.append(str(arr[i]))
    return dest

def get_html(url):
    try:
        res = request.urlopen(request.Request(url, headers=header),timeout=TIMEOUT)
        html = res.read()
        code = res.getcode()

        if code != 200:
           raise BaseException("code:"+ str(code))
        return str(html, 'utf-8')
    except BaseException as e:
        raise

    #print(str(html,'utf-8'))


def parse_class(url,item):

    classitem = {}
    classitem["id"] = [item["id"]]
    try:
        html = get_html(url)
        soup_html = BeautifulSoup(html, "lxml")

        classitem["package"] = [item["package"]]
        classitem["package_url"] = [item["package_url"]]
        classitem["class_name"] = [item["class_name"]]
        classitem["url"] = [item["url"]]
        classitem["html"] = [html]

        classitem["inhconstants_n"] = tostr(soup_html.select("#inhconstants"))
        classitem["lfields_n"] = tostr(soup_html.select("#lfields"))
        classitem["pubmethods_n"] = tostr(soup_html.select("#pubmethods"))
        classitem["inhmethods_n"] = tostr(soup_html.select("#inhmethods"))
        classitem["pubconstructors_n"] = tostr(soup_html.select("#pubconstructors"))
        classitem["lattrs_n"] = tostr(soup_html.select("#lattrs"))
        classitem["constants_n"] = tostr(soup_html.select("#constants"))
        classitem["enumconstants_n"] = tostr(soup_html.select("#enumconstants"))
        classitem["promethods_n"] = tostr(soup_html.select("#promethods"))
        classitem["proctors_n"] = tostr(soup_html.select("#proctors"))

        # if len(classitem["constants_n"]) > 1:
        #     print(type(classitem["constants_n"][0]))

        #print(json.dumps(classitem))

        insert_sql, params =  get_insert_sql(classitem)

        insert_db(insert_sql, params)
    except BaseException as e:
        print(e)
        with open("numserror.txt", "a") as f:
            f.write(classitem["id"][0]+ "," + str(e) + "\n")


item = {}
with open("urls.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        print(str(i)+" "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
        elements = line.split(",")
        item['id'] = elements[0].replace("\n","")
        item['url'] = elements[1].replace(".html", '').replace("\n","")
        item['package'] = elements[2].replace("\n","")
        item['package_url'] = elements[3].replace("\n","")
        item['class_name'] = elements[4].replace("\n","")
        request_url = base_url + item['url']
        parse_class(request_url, item)
        time.sleep(1)



