'''print("iterador for")
for i in range(1,11):
    print(i, end=' ')

print('iterador while')
limite =10
i=1
while (i<=limite):
    print(i,end=' ')
    i +=1
    print('')
animales = ['perro', 'gato', 'alcon', 'caballo']
indice =0
while indice < len(animales):
    animal=animales[indice]
    print(f'{indice}.-{animal}')
    indice +=1'''
#fibonaci
a,b=0,1
c=0
limite=10
while c< limite:
    print(a, end=',')
    a,b=b,a+b
    c+=1
    #c=a
    #a=b
    #b=c+b

