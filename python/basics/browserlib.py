#!/user/bin/python

import webbrowser
import time

total_breaks=3
break_count=0
print("Este programa empezo a las "+time.ctime())


while(break_count < total_breaks):    
    time.sleep(10)
    x=input("Lanzar video?(y/n)")
    if (x == "y"):
        webbrowser.open("https://www.youtube.com/watch?v=KdWgysitPgU&list=RDKdWgysitPgU&start_radio=1")        
        break_count=break_count+1
    