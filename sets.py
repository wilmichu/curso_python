lista=[1,1,2,3,3,1,4,8,3]
lista_unica=[]
for  numero in lista:
    print(numero)
    #por elemento
for  i in range(len(lista)):
    print(lista[i])
#por indice
for numero in lista:
    if numero not in lista_unica:
        lista_unica.append(numero)
print(lista_unica)
lista_unica_2=set(lista)
print(lista_unica_2)
print(type(lista_unica_2))
print("==========================")
grupo1=set("abracadabra")
grupo2=set("alacazam")
print(grupo1)
print(grupo2)
print(grupo1-grupo2)
print(grupo1 |grupo2)
print(grupo1 & grupo2)
print(grupo1 ^ grupo2)
print((grupo1 & grupo2)|(grupo1 &grupo2))
