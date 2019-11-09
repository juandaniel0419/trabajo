# input
cliente=input("ingrese el nombre del cliente:")
cantidad_de_platos_arroz=int(input("ingrese Nro de platos de arroz con pollo:"))
cantidad_de_gaseosa=int(input("ingrese Nro de gaseosas:"))
cantidad_de_platos_ceviche=int(input("ingrese Nro de platos de ceviche"))
pu_arroz=float(input("ingrese el precio unitario de arroz"))
pu_ceviche=float(input("ingrese el precio unitario de ceviche"))
pu_gaseosa=float(input("ingrese el precio unitario de gaseosa"))

#processing
total1=(pu_arroz*cantidad_de_platos_arroz)
total2=(pu_ceviche*cantidad_de_platos_ceviche)
total3=(pu_gaseosa*cantidad_de_gaseosa)
consumo=(total1+total2+total3)
#verificador
comprador_complusivo=(consumo>200)

#output
print("##############################")
print("# RESTAURANTE - TIA JULIA")
print("cliente:",cliente)
print("##############################")
print("producto       cantidad   P.U     Total")
print("arroz con pollo ",   cantidad_de_platos_arroz   ,"     "    ,pu_arroz  ,"   "   ,total1)
print("gaseosa         ",   cantidad_de_gaseosa        ,"     "    ,pu_gaseosa,"   "   ,total2)
print("ceviche         ",   cantidad_de_platos_ceviche ,"     "    ,pu_ceviche,"   "   ,total3)
print("consumo:",consumo)
print("###############################")
