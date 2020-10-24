#!/usr/bin/python
import random
asistentes=["A","B","C","D","E","F"]


def novino(x):
    print("No vino", asistentes[x-1])

x=random.randint(0, len(asistentes)-1)
print("Se enviara:",x, " a la función")
novino(x)