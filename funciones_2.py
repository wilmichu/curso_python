def porcentaje (numero,porcentaje):
    c=numero*(porcentaje/100)
    return(c)
dato = input('escribe el primer valor: ')
dato_2=input('escribe el primer valor: ')
dato=int(dato)
dato_2=int(dato_2)
resultado=porcentaje(dato,dato_2)
print(resultado)

def porcentaje2 (numero,porcentaje=10):
    resultado=numero*(porcentaje/100)
    return(resultado)
dato = input('escribe el primer valor: ')
dato_2=input('escribe el primer valor: ')
dato=int(dato)
dato_2=int(dato_2)
resultado=porcentaje(dato,dato_2)
print(resultado)
resultado=porcentaje2(numero=80,porcentaje=25)
print(resultado)

lista=[20,80,100]
def aplicacion_porcentaje(lista):
    resultado_porcentaje=[]
    for numero in lista:
        resultado=porcentaje2(numero)
        resultado_porcentaje.appendÇ(resultado)
    return resultado_porcentaje
lista

