# input
cliente=input("ingrese el nombre del cliente:")
cantidad_de_llantas=int(input("ingrese Nro de llantas que va a comprar:"))
cantidad_de_aros=int(input("ingrese Nro de aros que va a comprar:"))
cantidad_de_chasis=int(input("ingrese Nro de chasis que va a comprar:"))
pu_llantas=float(input("ingrese el precio unitario de llantas:"))
pu_aros=float(input("ingrese el precio unitario de aros:"))
pu_chasis=float(input("ingrese el precio unitario de la chasis"))

#processing
total1=(pu_llantas*cantidad_de_llantas)
total2=(pu_aros*cantidad_de_chasis)
total3=(pu_chasis*cantidad_de_chasis)
consumo=(total1+total2+total3)
#verificador
comprador_complusivo=(consumo>4000)

#output
print("##############################")
print("# RESTAURANTE - TIA JULIA")
print("cliente:",cliente)
print("##############################")
print("producto       cantidad   P.U     Total")
print("llantas ",   cantidad_de_llantas  ,"     "    ,pu_llantas  ,"   "   ,total1)
print("aros        ",   cantidad_de_aros        ,"     "    ,pu_aros,"   "   ,total2)
print("chasis        ",   cantidad_de_chasis ,"     "    ,pu_chasis,"   "   ,total3)
print("consumo:",consumo)
print("comprador compulsivo:",comprador_complusivo)
print("###############################")
