# calcular velocidad final de caida libre
velocidad_final=0.0
velocidad_inicial=0.0
tiempo=0.0
gravedad=0.0

#asignacion de valores
velocidad_final=40
velocidad_inicial=100
tiempo=6
gravedad=10

# calculo
velocidad_final=velocidad_inicial+(gravedad*tiempo)

print("gravedad es ",gravedad)
print("velocidad inicial es",velocidad_inicial)
print("tiempo es ",tiempo)
print("velocidad final es",velocidad_final)

# verificador
capacidad=(velocidad_final<20)
print("es correcto,",capacidad)

