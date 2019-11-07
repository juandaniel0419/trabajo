# calcular la pendiente de dos puntos en el plano
x1=0.0
y1=0.0
x2=0.0
y2=0.0

# asignacion de valores
x1=5
y1=9
x2=3
y2=4

# calculo
pendiente=(y2-y1)/(x2-x1)

print("x1 es",x1)
print("x2 es",x2)
print("y1 es",y1)
print("y2 es",y2)
print("pendiente es ",pendiente)

# verificador
capacidad=(pendiente<1)
print("la pendiente es menor que 1,",capacidad)


