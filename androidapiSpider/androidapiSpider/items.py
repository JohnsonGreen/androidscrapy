# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re
import bs4
from bs4 import BeautifulSoup

import json
from androidapiSpider.settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class AndroidapispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass


def filterlabel(html):
     dr = re.compile(r'<[^>]+>', re.S)
     dd = dr.sub('', html).replace('\n','').strip()
     return dd


#单个方法
def single_method(pre):
    sibs = pre.next_siblings
    descri = ''   #方法描述
    method = {}
    method['parameters'] = None
    method['returns'] = None
    method['throws'] = None
    h3 = pre.find_previous_sibling('h3')
    method['name'] = h3.text.strip() if h3 is not None else None
    method['funcname']= pre.text.strip()
    for sib in sibs:
        tp = BeautifulSoup(str(sib),"lxml")
        ta = tp.find('table',class_='responsive')
        parameters = []
        returns = []
        throws = []
        if ta:
           classify  = ta.find("tr").text
           if classify == "Parameters":
              trs = ta.find_all("tr")
              for i in range(1,len(trs)):
                  td = trs[i].find("td")
                  name = td.text.strip() if td is not None else None
                  ntd = td.find_next("td") if td is not None else None
                  scri = ntd.text.strip() if ntd is not None else None
                  dict = {'name':name,'scri':scri}
                  parameters.append(dict)
              method['parameters'] = parameters
           elif classify == "Returns":
              ftd = ta.find("td")
              type = ftd.text.strip() if ftd is not None else None
              ntd = ftd.find_next("td") if ftd is not None else None
              scri = ntd.text.strip() if ntd is not None else None
              dict = {'type':type,'scri':scri}
              returns.append(dict)
              method['returns'] = returns
           elif classify == "Throws":
               trs = ta.find_all("tr")
               for i in range(1, len(trs)):
                   td = trs[i].find("td")
                   type = td.text.strip() if td is not None else None
                   ntd = td.find_next("td") if td is not None else None
                   scri = ntd.text.strip() if ntd is not None else None
                   dict = {'type': type, 'scri': scri}
                   throws.append(dict)
               method['throws'] = throws
        else:
           descri = descri +" "+ tp.text.strip()
    method['descri'] = descri
    return method

#fields
def single_field(pre):
    sibs = pre.next_siblings
    descri = ''  # 属性描述
    fields = {}
    for sib in sibs:
        tp = BeautifulSoup(str(sib),"lxml")
        try:
          descri = descri + " " + tp.text.strip()
        except:
            pass
    fields['scri'] = descri
    return fields

def single_attr(h):
    name = ''
    name = h.get_text()
    p = h.find_next_sibling("p")
    descri = p.get_text() if tmp is not None else None
    dict = {'name':name,'descri':descri}
    return json.dumps(dict)

#继承常量
def inhconstantsfunc(self):
    inhconstants = []
    try:
        for p in self['inhconstants_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr") #包含类型 属性名 描述信息的标签
            for tr in table:

                tmp = tr.find("code")
                type = tmp.get_text().strip() if tmp is not None else None

                tmp = tr.find("a")
                name = tmp.get_text().strip() if tmp is not None else None

                tmp = tr.find("p")
                description = tmp.get_text().replace('\n', '').strip() if tmp is not None else None
                inhconstants.append([type,name,description])
    except:
        inhconstants = None
        #print("inhconstants-----None")

    inhconstants = json.dumps(inhconstants)
    return inhconstants


#constants
def constantsfunc(self):
    constants = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:

        for p in self['constants_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr") #包含类型 属性名 描述信息的标签
            names = []
            for i in range(1,len(table)):
                tr = table[i]

                tmp = tr.select("td:nth-of-type(2) code")[0]

                name = tmp.get_text().strip() if tmp is not None else None
                if name not in names:
                    names.append(name)
                    tmp = tr.find("code")
                    type = tmp.get_text().strip() if tmp is not None else None
                    hs = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in hs:
                        sf = single_field(h.parent.find("pre"))
                        sf['type'] = type
                        sf['name'] = name
                        constants.append(sf)
    except:
        constants = None
        #print("constants-----None")

    constants = json.dumps(constants)
    return constants

#enumconstants
def enumconstantsfunc(self):
    enumconstants = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:
        for p in self['enumconstants_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr") #包含类型 属性名 描述信息的标签
            names = []
            for i in range(1,len(table)):
                tr = table[i]
                tmp = tr.select("td:nth-of-type(2) code")[0]
                name = tmp.get_text().strip() if tmp is not None else None
                if name not in names:
                    names.append(name)
                    tmp = tr.find("code")
                    type = tmp.get_text().strip() if tmp is not None else None
                    hs = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in hs:
                        sf = single_field(h.parent.find("pre"))
                        sf['type'] = type
                        sf['name'] = name
                        enumconstants.append(sf)
    except:
        enumconstants = None
        #print("enumconstants-----None")

    enumconstants = json.dumps(enumconstants)
    return enumconstants


#类属性
def lfieldsfunc(self):
    lfields = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:
        for p in self['lfields_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr") #包含类型 属性名 描述信息的标签
            names = []
            for i in range(1,len(table)):
                tr = table[i]
                tmp = tr.select("td:nth-of-type(2) code")[0]
                name = tmp.get_text().strip() if tmp is not None else None
                if name not in names:
                    names.append(name)
                    tmp = tr.find("code")
                    type = tmp.get_text().strip() if tmp is not None else None
                    hs = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in hs:
                        sf = single_field(h.parent.find("pre"))
                        sf['type'] = type
                        sf['name'] = name
                        lfields.append(sf)
    except:
        lfields = None
        #print("lfields-----None")

    lfields = json.dumps(lfields)
    return lfields




#pubmethod
def pubmethodsfunc(self):
    pubmethods = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:
        for p in self['pubmethods_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr") #包含类型 属性名 描述信息的标签
            names = []
            for i in range(1, len(table)):
                tr = table[i]
                tmp = tr.find("a")
                name = tmp.get_text().strip() if tmp is not None else None

                if name not in names:
                    names.append(name)
                    tmp = tr.find("code")
                    type = tmp.get_text().strip() if tmp is not None else None

                    #tmp = tr.find("p")
                    #description = tmp.get_text().replace('\n', '').strip() if tmp is not None else None

                    res = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in res:
                        sm = single_method(h.parent.find("pre"))
                        sm['type'] = type
                        pubmethods.append(sm)
    except:

        pubmethods = None
        #print("pubmethods-----None")

    pubmethods = json.dumps(pubmethods)
    return pubmethods

#promethods
def promethodsfunc(self):
    promethods = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:
        for p in self['promethods_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr")  # 包含类型 属性名 描述信息的标签
            names = []
            for i in range(1, len(table)):
                tr = table[i]
                tmp = tr.select("td:nth-of-type(2) code a")[0]
                name = tmp.get_text().strip() if tmp is not None else None

                if name not in names:
                    names.append(name)
                    tmp = tr.select("td:nth-of-type(1)")[0]
                    type = tmp.get_text().strip() if tmp is not None else None
                    res = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in res:
                        sm = single_method(h.parent.find("pre"))
                        sm['type'] = type
                        promethods.append(sm)
    except:

        promethods = None
        # print("promethods-----None")

    promethods = json.dumps(promethods)
    return promethods
    pass

#pubconstructors
def pubconstructorsfunc(self):
    pubconstructors = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:
        for p in self['pubconstructors_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr")  # 包含类型 属性名 描述信息的标签
            names = []
            for i in range(1, len(table)):
                tr = table[i]
                tmp = tr.find("a")
                name = tmp.get_text().strip() if tmp is not None else None

                if name not in names:
                    names.append(name)
                    res = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in res:
                        sm = single_method(h.parent.find("pre"))
                        pubconstructors.append(sm)
    except:
        pubconstructors = None
        # print("pubconstructors-----None")

    pubconstructors = json.dumps(pubconstructors)
    return pubconstructors

#proctors
def proctorsfunc(self):
    proctors = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:
        for p in self['proctors_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr")  # 包含类型 属性名 描述信息的标签
            names = []
            for i in range(1, len(table)):
                tr = table[i]
                tmp = tr.find("a")
                name = tmp.get_text().strip() if tmp is not None else None

                if name not in names:
                    names.append(name)
                    res = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in res:
                        sm = single_method(h.parent.find("pre"))
                        proctors.append(sm)
    except:
        proctors = None
        # print("proctors-----None")

    proctors = json.dumps(proctors)
    return proctors


#lattrs
def lattrsfunc(self):
    lattrs = []
    soup_html = BeautifulSoup(self['html'][0], "lxml")
    try:
        for p in self['lattrs_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("table tr")  # 包含类型 属性名 描述信息的标签
            names = []
            for i in range(1, len(table)):
                tr = table[i]
                tmp = tr.find("a")
                name = tmp.get_text().strip() if tmp is not None else None

                if name not in names:
                    names.append(name)
                    res = soup_html.find_all('h3', class_='api-name', text=name)
                    for h in res:
                        sm = single_attr(h)
                        lattrs.append(sm)
    except:
        lattrs = None
        # print("lattrs-----None")

    lattrs = json.dumps(lattrs)
    return lattrs

#类信息
def classinfofunc(self):
    classinfo = {}
    html = self['html'][0]
    class_name = self['class_name'][0]
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.find('h1',class_='api-title',text=class_name)
    desflag = False
    descri = ''
    extends = ''
    if h1:
        for sib in h1.next_siblings:
            if isinstance(sib, bs4.element.Tag):
                sibsoup = BeautifulSoup(str(sib), 'lxml')
                resu = sibsoup.find("h2", class_="api-section")
                if resu:
                    descri = descri.strip()
                    break
                # 继承信息
                table = sibsoup.find("table", class_="jd-inheritance-table")
                if table:
                    extends = table.get_text().strip()
                # 描述信息
                if desflag or sibsoup.find("hr"):
                    desflag = True
                    descri = descri + " " + sibsoup.get_text().strip()

    classinfo['class_name'] = class_name
    classinfo['extends'] = extends
    classinfo['descri'] = descri
    return json.dumps(classinfo)


#继承方法
def inhmethodsfunc(self):
    inhmethods = []
    try:
        for p in self['inhmethods_n']:
            soup = BeautifulSoup(p, "lxml")
            table = soup.select("#inhmethods tr table.responsive tr") #包含类型 属性名 描述信息的标签
            for tr in table:
                tmp = tr.find("code")
                type = tmp.get_text().strip() if tmp is not None else None
                tmp = tr.find("a")
                name = tmp.get_text().strip() if tmp is not None else None
                tmp = tr.find("p")
                description = tmp.get_text().replace('\n', '').strip() if tmp is not None else None
                inhmethods.append([type,name,description])
    except:
        inhmethods = None
        #print("inhmethods-----None")

    inhmethods = json.dumps(inhmethods)
    return inhmethods


class ClassItem(scrapy.Item):
    id = scrapy.Field()
    package = scrapy.Field()
    package_url = scrapy.Field()
    class_name = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()

    #class_description
    title_p = scrapy.Field()

    #summary
    inhconstants_n = scrapy.Field()
    lfields_n = scrapy.Field()
    pubmethods_n = scrapy.Field()
    inhmethods_n = scrapy.Field()
    pubconstructors_n = scrapy.Field()
    lattrs_n = scrapy.Field()
    constants_n = scrapy.Field()
    enumconstants_n = scrapy.Field()
    promethods_n = scrapy.Field()
    proctors_n = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
           insert into scrapy_class(id,package,package_url,class_name,url,crawl_time,summary_inhconstants,summary_lfields,
                  summary_pubmethods,summary_inhmethods,class_info,summary_pubconstructors,summary_lattrs,summary_constants,summary_enumconstants,
                  summary_promethods,summary_proctors)
           values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
           ON DUPLICATE KEY UPDATE crawl_time=values(crawl_time)
        """
        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)
        package = self["package"][0]
        package_url = self["package_url"][0]
        class_name = self["class_name"][0]
        url = self["url"][0]
        id = int(self["id"][0])

        summary_inhconstants = inhconstantsfunc(self)
        summary_lfields = lfieldsfunc(self)
        summary_pubmethods = pubmethodsfunc(self)
        summary_inhmethods = inhmethodsfunc(self)


        class_info = classinfofunc(self)

        summary_pubconstructors = pubconstructorsfunc(self)
        summary_lattrs = lattrsfunc(self)
        summary_constants = constantsfunc(self)
        summary_enumconstants = enumconstantsfunc(self)
        summary_promethods = promethodsfunc(self)
        summary_proctors = proctorsfunc(self)

        #print(summary_inhconstants)
        #print(inhconstants_descrs)
        params = (id,package,package_url,class_name,url,crawl_time,summary_inhconstants,summary_lfields,
                  summary_pubmethods,summary_inhmethods,class_info,summary_pubconstructors,summary_lattrs,summary_constants,summary_enumconstants,
                  summary_promethods,summary_proctors)
        return insert_sql,params





class OverviewItem(scrapy.Item):

    pass