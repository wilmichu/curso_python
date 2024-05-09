import operaciones
ruta=r'd:\curso_python\archivo\ventas.csv'
nueva_venta={
    'id':0,
    'codigo_cliente':10000,
    'cliente':'Wilmer Machaca',
    'producto':'papas fritas',
    'precio':68,
    'descuento': '',
    'iva': ''
}
#operaciones.registrar_csv(nueva_venta,ruta)
lectura=True
while lectura:
    accion = input('Accion:  ')
    if (accion == 'nuevo'):
        cliente = input('escribe el nombre: ')
        producto=input('escribe el producto')
        precio=input('escribe el precio')
        nueva_venta={
            'id':0,
            'codigo_cliente':10000,
            'cliente':cliente,
            'producto':producto,
            'precio':precio,
            'descuento': '',
            'iva': ''
        }
        operaciones.registrar_csv(nueva_venta,ruta)
        
        
    else:
        lectura=False
    
