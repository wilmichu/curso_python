'''precios=[50,75,46,22,80,65,8]
tamaño=len(precios)
print(tamaño)
a=0
max=precios[a]
while a<tamaño:
    
    if max>=precios[a]:
        max=precios[a]
    a+=1
print(max)
a=0
men=precios[a]
while a<tamaño:
    
    if men<=precios[a]:
        men=precios[a]
    a+=1
print(men)
#555555555555555555555555555555555555555


y=input('Dime una palabra: ')
x=list(y)
z=len(x)
i=z/2
if z%2==0:
  m=x[0:int(i)]
  m.reverse()
  q=x[int(i):int(z)]
  if m==q:
    print('Es un Palíndromo')
  else:
    print('No es un Palíndromo')
else:
  h=(z/2)-0.5
  m=x[0:int(h)]
  m.reverse()
  q=x[int(h+1):int(z)]
  if m==q:
    print('Es un Palíndromo')
  else:
    print('No es un Palíndromo')
'''
mi_variable = input('escribe tu valor mayor a cero: ')
mi_variable=int(mi_variable)
if mi_variable>0:
    contador=mi_variable
    for i in range(0,mi_variable):
        contador-=1
        print(contador, end=' ')
else:
    mi_variable = input('escribe tu valor mayor a cero: ')
