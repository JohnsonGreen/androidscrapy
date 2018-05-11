# -*- coding: utf-8 -*-
__author__ = 'cyh'

from scrapy.cmdline import execute

import sys
import os
import json
from bs4 import BeautifulSoup

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)
sys.path.append(cur_dir)

#result = json.load(open("navtree_data.json", encoding='utf-8'))
# i=0
# with open("urls.txt", "w") as f:
#   for package_info in result:
#      package = package_info[0]
#      package_url = package_info[1]
#      package_children = package_info[2]
#      for family in package_children:
#         category = family[0]
#         namesandurls = family[2]
#         for single in namesandurls:
#             name = single[0]
#             url = single[1]
#             i += 1
#             f.write(str(i)+","+url+","+package+","+package_url+","+name+"\n")
#             print(url)


# with open("urls.txt", "r") as f:
#    lines = f.readlines()
#    for line in lines:
#        print(line)
#        elements = line.split(",")
#        print(elements[1])
#        #for element in elements:
#         #   print(element)


#测试bs4


str = """
<table id="inhconstants" class="responsive constants inhtable">
<tbody><tr><th><h3>Inherited constants</h3></th></tr>

  <tr class="api apilevel-">
  <td>
    <div class="expandable jd-inherited-apis">
      <span class="expand-control exw-expanded">From interface
        <code><a href="https://developer.android.com/reference/android/os/Parcelable.html">android.os.Parcelable</a></code>
      </span>
      <table class="responsive exw-expanded-content">



    <tbody><tr class="api apilevel-1" data-version-added="1">
        <td><code>int</code></td>
        <td width="100%">
          <code><a href="https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR">CONTENTS_FILE_DESCRIPTOR</a></code>
          <p>Descriptor bit used with <code><a href="https://developer.android.com/reference/android/os/Parcelable.html#describeContents()">describeContents()</a></code>: indicates that
 the Parcelable object's flattened representation includes a file descriptor.


</p>
        </td>
    </tr>


    <tr class="api apilevel-1" data-version-added="1">
        <td><code>int</code></td>
        <td width="100%">
          <code><a href="https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE">PARCELABLE_WRITE_RETURN_VALUE</a></code>
          <p>Flag for use with <code><a href="https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)">writeToParcel(Parcel, int)</a></code>: the object being written
 is a return value, that is the result of a function such as
 "<code>Parcelable someFunction()</code>",
 "<code>void someFunction(out Parcelable)</code>", or
 "<code>void someFunction(inout Parcelable)</code>".

</p>
        </td>
    </tr>


      </tbody></table>
    </div>
  </td></tr>


</tbody></table>

"""
#soup = BeautifulSoup(str,"lxml")
#print(soup.prettify())
#a=None
#b = a['text'] if a == None else "hehe"
#print(b)

t = []
t.append('')
t.append('')
t.append('')
print(t)