import csv

with open(r'D:\curso_python\archivo\ventas.csv','r')as archivo:
    datos_csv=csv.DictReader(archivo)
    for fila in datos_csv:
        print(fila)


fila={}
print(fila)
fila