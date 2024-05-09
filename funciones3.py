# diccionario:
productos={
    "arroz":58,
    "gaseosas":50,
    "trigo":25,
    "harina":100
}
def porcentaje (numero,porcentaje):
    c=numero*(porcentaje/100)
    return(c)
# iterar mi lista y calcular el iva acumulado


def calculo_iva(lista):
    total=0
    for producto, precio in lista.items():
        total +=porcentaje(precio,13)
    return total
total_iva=calculo_iva(productos)
print(total_iva)