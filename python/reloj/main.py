#!/usr/bin/python
from classes.reloj import reloj
catalogo= [ {"marca":"rolex","modelo":"rol01","precio":100000},
            {"marca":"casio","modelo":"cas33","precio":600},
            {"marca":"patito","modelo":"pat50","precio":50},
            ]


MiReloj=reloj(12,10,30,catalogo[1])
SegReloj=reloj(23,00,00,catalogo[0])


print(MiReloj.getMinuto())
print(MiReloj.getHora())
print(MiReloj.getSegundo())

print(MiReloj.getHoraCompleta() )


print(SegReloj.getHoraCompleta() )


print("Tipo MiReloj:", MiReloj.getTipo() )
print("Tipo SegReloj:", SegReloj.getTipo() )


print("Tipo MiReloj:", MiReloj.getPrecio("precio") )