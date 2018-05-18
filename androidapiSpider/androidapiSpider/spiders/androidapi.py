# -*- coding: utf-8 -*-
import re
import scrapy
import json
import time
import datetime
from scrapy.http import Request
from urllib import parse

import MySQLdb
import MySQLdb.cursors
from scrapy.loader import ItemLoader
from androidapiSpider.items import ClassItem,OverviewItem,get_insert_sql





class AndroidapiSpider(scrapy.Spider):
    name = 'androidapi'
    allowed_domains = ['https://developer.android.com/reference/']
    start_urls = ['https://developer.android.com/reference/']
    #start_urls = ['https://developer.android.com/reference/index.html']
    base_url = 'https://developer.android.com/'

    def parse(self, response):

        #获取207条链接数据
        # urls =response.css('#devdoc-nav  a').extract()
        # post_urls = []
        # reg = '.*href="(.*)".*'
        # for i in range(len):
        #     matobj = re.match(reg, urls[i])
        #     if matobj:
        #        post_urls.append(matobj.group(1))


        # item = {}
        # item['id'] = "22"
        # item['url'] = "reference/android/accessibilityservice/AccessibilityService.GestureResultCallback"
        # item['package'] = "android.accessibilityservice"
        # item['package_url'] = "reference/android/text/package-summary.html"
        # item['class_name'] = "AccessibilityService.GestureResultCallback"
        # request_url = self.base_url + "reference/android/accessibilityservice/AccessibilityService.GestureResultCallback"
        # yield scrapy.Request(request_url, meta={"item": item}, callback=self.parse_class, dont_filter=True)


        item = {}
        with open("urls.txt", "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i]
                print(i)
                elements = line.split(",")
                item['id'] = elements[0]
                item['url'] = elements[1].replace(".html",'')
                item['package'] = elements[2]
                item['package_url'] = elements[3]
                item['class_name'] = elements[4]
                request_url = self.base_url + item['url']
                yield scrapy.Request(request_url,meta={"item":item},callback=self.parse_class,dont_filter=True)
                time.sleep(1)



        #result = json.load(open("navtree_data.json", encoding='utf-8'))
        #item = {}
        # for package_info in result:
        #     item['package'] = package_info[0]
        #     item['package_url'] = package_info[1]
        #     yield self.parse_overview(response=response,item=item)                    #解析描述
        #     package_children = package_info[2]
        #     for family in package_children:
        #         category = family[0]
        #         namesandurls = family[2]
        #         for single in namesandurls:
        #             item['class_name'] = single[0]
        #             item['url'] = single[1]
        #             yield self.parse_class(response=response,item=item)                #解析各个类别，包括class,interface,annotation,exception
        #             print(item['url'])
        #             #time.sleep(1000)


    def parse_class(self,response):

        #print("-----------------------------------------")

        #xpath css没有数据返回空列表
        item = response.meta["item"]
        item_loader = ItemLoader(item=ClassItem(), response=response)
        item_loader.add_value("package",item['package'])
        item_loader.add_value("package_url", item['package_url'])
        item_loader.add_value("class_name",item['class_name'])
        item_loader.add_value("url",item['url'])
        item_loader.add_value("id", item['id'])
        html = str(response.body, 'utf-8').replace('\n','')

       # print(html)
        item_loader.add_value("html", html)

        #继承常量
        item_loader.add_css("inhconstants_n","#inhconstants table")
        item_loader.add_css("lfields_n", "#lfields")
        item_loader.add_css("pubmethods_n", "#pubmethods")
        item_loader.add_css("inhmethods_n", "#inhmethods")
        item_loader.add_css("pubconstructors_n", "#pubctors")
        item_loader.add_css("lattrs_n", "#lattrs")
        item_loader.add_css("constants_n", "#constants")
        item_loader.add_css("enumconstants_n", "#enumconstants")
        item_loader.add_css("promethods_n", "#promethods")
        item_loader.add_css("proctors_n", "#proctors")

        if int(item["id"]) == 25:
            print(html)


        classitem = item_loader.load_item()

        print(classitem)

        insert_sql, params = get_insert_sql(classitem)

        #print(params[10])


        return classitem


    def parse_overview(self,response,item):
        item_loader = ItemLoader(item=OverviewItem(), response=response)
        pass


