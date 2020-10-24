#!/user/bin/python
asistentes=["A","B","C","D","E","F"]

def fn_presentes(x):  
    presente=0  
    for i in range(len(asistentes)):
        if (x == asistentes[i]):
            presente=1
            break
    return (presente)

vlX=str(input("Introducir Nombre:" ))

if (fn_presentes(vlX) == 1 ):
    print("Presente")
else:
    print("Ausente")

##############################################


