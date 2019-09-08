#!/usr/bin/python
#import regexp
import re

vlString = "'I AM NOT YELLING', she said. Though we knew it to not be true"
print (vlString)
new = re.sub('[A-Z]','',vlString)
print (new)
new2 = re.sub('[a-z]','',vlString)
print (new2)
new3 = re.sub('[.,\'a-zA-Z+" "]','',vlString)
print (new3)
#remove everything except ( ^ )
vlString2 = "'I AM NOT YELLING', she said. Though we knew it to not be true"+ "6 88 a - 345"
new4 = re.sub('[^0-9]','_',vlString2)
print (new4)