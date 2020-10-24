#!/user/bin/python

from PIL import Image
import time
import psutil
im = Image.open("/home/tr011/Imágenes/tr011.png")


total_breaks=3
break_count=0
print("Este programa empezo a las "+time.ctime())

while(break_count < total_breaks):    
    im.show()
    time.sleep(10)
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
    break_count=break_count+1
    time.sleep(10)

