
import MySQLdb
import MySQLdb.cursors
import json
import random

MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "scrapyspider"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""

dbparms = dict(
            host = MYSQL_HOST,
            db = MYSQL_DBNAME,
            user = MYSQL_USER,
            passwd = MYSQL_PASSWORD,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
)

key_words = [
    #位置
    "location",
    "Location",
    "ACCESS_COARSE_LOCATION",
    "ACCESS_FINE_LOCATION",
    "ACCESS_LOCATION_EXTRA_COMMANDS",
    "GPS",
    "gps",

    #短信
    #"Message",
    #"message",
    "SMS",      #Short Message Service 手机短信服务
    "SmsManager",
    "MMS",      #MS为Multimedia Messaging Service的缩写，中文译为多媒体短信服务

    #"content",
    #"information",
    #"Send",
    # "TextMessage",
    # "textmessage",
    # "textMessage",


     #通信录
     "contacts",
     "CONTACTS",
     "PHONE_NUMBER",
     "phone number",
     "phone state",      #允许只读访问手机状态,包括设备的电话号码, 当前手机网络信息,任何正在进行的调用的状态,任何的列表 PhoneAccount 注册在设备上
     "CALL_PRIVILEGED",  #
     "READ_CALL_LOG",   #通话记录
     "call log",
     "READ_CONTACTS",


     #应用列表
     "AppList",  #获取应用列表，包括应用得相关信息
     "applist",
     "appList",


     #浏览器
     #"Browser",
     #"browser",
     "BOOKMARKS",  #书签及浏览记录
     "bookmark",
     "history",
     "HISTORY",


     #设备
      "IMEI",   #设备唯一识别码
      "imei",
      "IMSI",   #国际移动用户识别码
      "imsi",
      "ICCID",  #手机卡识别码
      "iccid",
      "ICC-ID",
      "fingerprint", #指纹
      "Fingerprint",
      "FINGERPRINT",
      "READ_EXTERNAL_STORAGE"  #外部存储
      "BATTERY_STATS",  #电池状态
      "Camera",
      "camera",
      "MIC",
      #"mic",

      #"",       #陀螺仪，指南针，计步
      #"BODY_SENSORS",  #身体传感器 心率


     #连接
      "WIFI",
      "wifi",
      "Wifi",
      "WiFi",
      "Bluetooth",
      "bluetooth",
      "NFC",
      "nfc",
      "VPN",
      "vpn",

]



def finddescri(methods,class_):
    keymethods = []
    for method in methods:
        method["class"] = class_
        flag = False
        # if method['parameters']:
        #     for p in method['parameters']:
        #         if not flag and findkey(p["scri"]):
        #             keymethods.append(method)
        #             flag = True
        if not flag and method['descri']:
            if findkey(method['descri']):
                keymethods.append(method)
                flag = True
        # if not flag and method['returns']:
        #     for r in method['returns']:
        #         if findkey(r['scri']):
        #             keymethods.append(method)
        #             flag = True
    return keymethods

def findkey(descri):
    if descri is not None and descri != "":
        for key in key_words:
            if descri.find(key) != -1 and descri.find("was deprecated") == -1 :  #论文点
                # descri = descri.replace(key, "***********" + key + "**********")
                print(key)
                print(descri)

                return True
    return False


db = MySQLdb.connect(**dbparms)
cursor = db.cursor()
# sql = """
#       SELECT * FROM scrapy_class WHERE package = '%s'
#       """ % (package)

sql = """
      SELECT * FROM scrapy_class
      """
cursor.execute(sql)
results = cursor.fetchall()


total_methods = 0
keymethods = []
for row in results:
    id = row['id']
    package_url = row['package_url']
    class_name = row['class_name']
    package = row['package']
    url = row['url']
    crawl_time = row['crawl_time']
    summary_inhconstants = row['summary_inhconstants']
    summary_lfields = row['summary_lfields'],
    summary_pubmethods = row['summary_pubmethods']
    summary_inhmethods = row['summary_inhmethods']
    class_info = row['class_info']
    summary_pubconstructors = row['summary_pubconstructors']
    summary_lattrs = row['summary_lattrs']
    summary_constants = row['summary_constants']
    summary_enumconstants = row['summary_enumconstants']
    summary_promethods = row['summary_promethods']
    summary_proctors = row['summary_proctors']


    methods = []
    #print("------------" +str(id) + "-----------")
    if summary_pubmethods != "null":
        for elem in json.loads(summary_pubmethods):
            methods.append(elem)
    if summary_pubconstructors != "null":
        for elem in json.loads(summary_pubconstructors):
            methods.append(elem)
    if summary_proctors != "null":
        for elem in json.loads(summary_proctors):
            methods.append(elem)
    if summary_promethods != "null":
        for elem in json.loads(summary_promethods):
            methods.append(elem)

    total_methods += len(methods)
    kmethods = finddescri(methods, package +"."+ class_name)
    for m in kmethods:
        keymethods.append(m)

    # print(id)
    # print(package)
    # print(summary_lfields)
    # print(summary_pubmethods)
    # print(class_info)
    # print(summary_pubconstructors)
    # print(summary_lattrs)
    # print(summary_constants)
    # print(summary_enumconstants)
    # print(summary_promethods)
    # print(summary_proctors)
    # print(summary_lfields[0])
    # print(len(summary_lfields))
    # if summary_lfields[0] == 'null' or summary_lfields[0] =='[]':
    #   print(True)
    # else:
    #   print(False)

# 关闭游标连接
cursor.close()
# 关闭数据库连接
db.close()

#print(keymethods)
print(total_methods)
print(len(keymethods))

nums = []
while True and len(nums) != 100:
    num = random.randint(1, len(keymethods))
    if num not in nums:
        nums.append(num)

print(nums)


with open("keymethods2.md", "a") as f:
    for j in range(100):
        for i in range(len(keymethods)):
            if i == nums[j]:
                f.write(#keymethods[i]["class"].replace("\n","").strip() + "---"+
                      keymethods[i]["name"].replace("\n","").strip() + ":  \n"
                      + keymethods[i]["descri"].replace("\n","").strip() + "\n\n")
    # f.write(json.dumps(keymethods))



#
# print("------------------------------------------------------------------------------------")
#
#
# for m in keymethods:
#     print(m["descri"])