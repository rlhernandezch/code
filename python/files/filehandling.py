#!/user/bin/python

fo = open("/home/tr011/github/code/code/python/files/foo.txt","a")
print("Filename: ", fo.name)
print("Open/Closed status: ", fo.closed)
print("Opening Mode: ", fo.mode)
fo.write("This is a new line!\n")
fo.close()
print("Open/Closed status: ", fo.closed)


fo = open("/home/tr011/github/code/code/python/files/foo.txt","r+")
print("Filename: ", fo.name)
print("Open/Closed status: ", fo.closed)
print("Opening Mode: ", fo.mode)
linea = fo.read(30)
print(linea)
position = fo.tell()
print("Current file position", position)
#Moverse a una posicion del archivo
position = fo.seek(0,0)
str = fo.read(10)
print("line new positon:", str)
fo.close()

print("Open/Closed status: ", fo.closed)