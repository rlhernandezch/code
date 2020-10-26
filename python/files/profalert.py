#!/user/bin/python
import os, sys
from  urllib import request, parse

curPath = os.getcwd()
fileName = "moviequote.txt"
fileFullPath = curPath+'/'+fileName

os.chdir(curPath)


def read_text ():
    quotes = open(fileFullPath)
    content=quotes.read()
    #print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(vlText):
    connection = request.urlopen('http://www.wdylike.appspot.com/?q='+parse.quote(vlText))
    output = connection.read()
#    print(output)
    connection.close()

    if b"true" in output:
        print("Profanity Alert")
    elif b"false" in output:
        print("No course")
    else:
        print("Default exit")

read_text()