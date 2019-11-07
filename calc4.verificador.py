# calcular la altura en caida libre
altura=0.0
tiempo=0.0
gravedad=0.0
velocidad=0.0

# asignacion de valores
tiempo=5
gravedad=10
velocidad=30

# calculo
altura=(velocidad*tiempo)+(gravedad/2)*tiempo*tiempo

print("tiempo es",tiempo)
print("gravedad es",gravedad)
print("velocidad es",velocidad)
print("altura es ",altura)

# verificador
capacidad=(altura>100)
print("supera la altura,",capacidad)

