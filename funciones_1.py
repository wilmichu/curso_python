'''
def                           name                      (n)                  :
definiciòn         mnombre de la funciòn             parametros           delimitador
NOta: La funciòn puede o no devolver valores
'''
#funciòn
def suma (a,b):
    c=a+b
    return(c)
resultado=suma(7,5)
print(resultado)
print(suma(7,5))
#metodo
def sum (a,b):
    c=a+b
    print(c)
sum(8,6)
print("=====================================")
def fibonaci(x):
    a,b=0,1
    limite=x
    c=0
    while c< limite:
        print(a, end=', ')
        a,b=b,a+b
        c+=1
def fibonaci_1(x):
    serie=[]
    a,b=0,1
    limite=x
    c=0
    while c< limite:
        serie.append(a)
        a,b=b,a+b
        c+=1
    return(serie)

dato = input('escribe tu valor: ')
print('tu valor es:' + dato)
dato=int(dato)
fibonaci(dato)
serie_fibonacci=fibonaci_1(dato)
print(" ")
print(serie_fibonacci)