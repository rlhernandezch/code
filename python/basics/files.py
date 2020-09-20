import struct
MyString="my|comma|separated|values|file"+"\n"
file = open('myoutputfile.log', 'a')
file.write(MyString)
file.close()
