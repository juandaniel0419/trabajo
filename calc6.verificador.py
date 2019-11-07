# descuento total de unas compras
producto_1=0.0
producto_2=0.0
producto_3=0.0
descuento=0.0
precio_con_descuento=0.0
# asignacion de valores
producto_1=59
producto_2=20
producto_3=60
descuento=0.3

# calculo
precio_con_descuento=producto_1+producto_2+producto_3*0.3

print("producto 1 es",producto_1)
print("producto 2 es",producto_2)
print("producto 3 es",producto_3)
print("descuento es",descuento)
print("precio total con descuento es",precio_con_descuento)

# verificador
capacidad=(precio_con_descuento<100)
print("supera la cantidad de precio ,",capacidad)