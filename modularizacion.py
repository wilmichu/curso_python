import operaciones
productos={
'cereales':58,
'carne':150,
'gaseosas':84,
'arroz':259,
'papel':78,
'maletas': 567,
}
iva=operaciones.calcular(productos, operaciones.porcentaje)
des=operaciones.calcular(productos, operaciones.descuento)
print(f'Iva:{iva}')
print(f'Descuento:{des}')