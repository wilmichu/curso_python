def porcentaje(numero,porcentaje=13):
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

#print (resultado)
def calcular(lista,funcion):
    total=0
    for producto,precio in lista.itmes():
        total +=funcion(precio)
    return total