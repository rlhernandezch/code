#!/user/bin/python

import os
#os.execl("touch foo.txt")
#os.rename("foo.txt","foo2.txt")
#os.remove("foo2.txt")


import os
curr_path = os.path.abspath(os.getcwd())

print (curr_path)
os.rmdir("NuevoDir" )

os.mkdir("NuevoDir")
vlNuevoDir = curr_path+'/'+'NuevoDir'
os.chdir(vlNuevoDir)

newFile = open("MyDummyFile.txt","a")
newFile.write("Pum!\n")

newFile.close
