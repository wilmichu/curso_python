#Diccionario
telefono ={
    "Liz":79797979,
    "marco":34343434,
    "laura":12121212,
    "guido":44454647,
    "mabel":90909090,
}
print(type(telefono))
print(telefono["marco"])
print("guido" in telefono)
print("pedro"  not in telefono)
print("liz"  in telefono)
'''
"liz":78787878
CLAVE VALOR
'''
for clave, valor in telefono.items():
    print(f'{clave}  valor:{valor}')