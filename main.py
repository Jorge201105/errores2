
"""
file = open("archivo.txt", "r", encoding="utf-8")
for linea in file:
    print(linea)


file.close()


file = open("archivo.txt", "r", encoding="utf-8")
lineas = file.readlines()
print(lineas)

file.close()


file = open("archivo.txt", "a", encoding="utf-8")
file.write("holamundo\n")

file.close()

lista =["pera","manzana"]

file = open("archivo.txt", "a",encoding = "utf-8")
for fruta in lista:
    file.write(fruta + "\n")

file.close




with open("logs/archivo.txt","r", encoding="utf-8") as a:
    lineas = a.readlines()
    print(lineas)
"""

import time
import datetime
import pytz

tz_CL = pytz.timezone("America/Santiago")
datetime_CL = datetime.datetime.now(tz_CL)

try:
    edad = int(input(" ingrese la edad "))

except Exception as e:
    #with open(f"error.log", "a", encoding="utf-8") as log:
    #    log.write(f"el error es  {datetime.datetime.now()}, {e}\n")

    with open(f"error.log", "a", encoding="utf-8") as log:
        log.write(f"el error es  {datetime_CL.strftime("%d/%m/%y, %H:%M:%S")}, {e}\n")



        




