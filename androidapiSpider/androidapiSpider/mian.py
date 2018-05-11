# # -*- coding : utf-8 -*-
# __author__ = 'cyh'
#
# import re
#
#
# lines = [
#           "https://developer.android.com/reference/android/app/admin/package-summary.html",
#           "https://developer.android.com/reference/android/package-summary.html",
#           ""
#          ]
# regex_str=".*reference/(.*)/package-summary\\.html$"   #括号括起来代表一组
#
# for line in lines:
#     match_obj = re.match(regex_str, line)
#     if match_obj:
#         print(match_obj.group(1))
#     else:
#         print('null')


__author__ = 'cyh'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "androidapi"])

