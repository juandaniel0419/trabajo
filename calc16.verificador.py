# superficie total de un cilindro
perimetro_de_la_base=0
generatriz=0
area_de_base=0

# asignacion de valores
perimetro_de_la_base=30
generatriz=5
area_de_base=10

# calculo
superficie_total_de_un_cilindro=perimetro_de_la_base*generatriz+2*area_de_base

print("perimetro de la base es",perimetro_de_la_base)
print("generatriz es ",generatriz)
print("area de la base es",area_de_base)
print("superficie total de un cilindro es ",superficie_total_de_un_cilindro)

# verificador
capacidad=(superficie_total_de_un_cilindro>100000)
print("la superficie total de un cilindro es mayor que 10000",capacidad)

