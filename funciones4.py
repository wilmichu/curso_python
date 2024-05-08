productos={
    "arroz":58,
    "gaseosas":50,
    "trigo":25,
    "harina":100
}
def porcentaje (numero,porcentaje=13):
    c=numero*(porcentaje/100)
    return(c)
# si el precio es mayor a 100 entonces el descuento es de 15%
# si no entonces 5%
def descuento(precio):
    total=0
    if precio> 100:
        total =porcentaje(precio,15)
        total =precio-total 
    else:
        total =porcentaje(precio,5)
        total =precio-total
    return total
mi_variable = input('escribe tu valor: ')
mi_variable=int(mi_variable)
resultado=descuento(mi_variable)
#print (resultado)
def calcular(lista,funcion):
    total=0
    for producto,precio in lista.itmes():
        total +=funcion(precio)
    return total
iva=calcular(productos,porcentaje)
print(f' Iva Total: {iva}')
total=calcular(productos,descuento)
print(f' Desc Total: {total}')

