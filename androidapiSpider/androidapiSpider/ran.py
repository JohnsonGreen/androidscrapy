# -*- coding: utf-8 -*-
__author__ = 'cyh'

import random

nums = []
while True and len(nums) != 100:
    num = random.randint(1, 4419)
    if num not in nums:
        nums.append(num)

with open("urls.txt", "r") as f:
   lines = f.readlines()
   for line in lines:
       elements = line.split(",")
       if int(elements[0]) in nums:
           with open("test.txt", "a") as f:
               f.write("https://developer.android.com/" +elements[1]+"\n")

       #for element in elements:
        #   print(element)