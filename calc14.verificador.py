# area de la superficie lateral de un tronco de piramide
p1=0.0
p2=0.0
area=0.0
ap=0.0

# asignacion de valores
p1=12
p2=30
ap=40

# calculo
area=(p1+p2)*ap

print("perimetro 1 es",p1)
print("periemtro 2 es",p2)
print("area lateral es",area)

# verificador
capacidad=(area>3007)
print("el area supera a 3007,",capacidad)
