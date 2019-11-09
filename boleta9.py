# input
cliente=input("ingrese el nombre del cliente:")
cantidad_de_celulares=int(input("ingrese Nro de celulares que va a comprar:"))
cantidad_de_cargadores=int(input("ingrese Nro de cargadores que va a comprar:"))
cantidad_de_protectores=int(input("ingrese Nro de protectores que va a comprar:"))
pu_celulares=float(input("ingrese el precio unitario de celular:"))
pu_cargadores=float(input("ingrese el precio unitario de cargadores:"))
pu_protectores=float(input("ingrese el precio unitario de la protectores"))

#processing
total1=(pu_celulares*cantidad_de_celulares)
total2=(pu_cargadores*cantidad_de_cargadores)
total3=(pu_protectores*cantidad_de_protectores)
consumo=(total1+total2+total3)
#verificador
comprador_complusivo=(consumo>1000)

#output
print("##############################")
print("# COLVOX ")
print("cliente:",cliente)
print("##############################")
print("producto       cantidad   P.U     Total")
print("celulares",   cantidad_de_celulares  ,"     "    ,pu_celulares  ,"   "   ,total1)
print("cargadores         ",   cantidad_de_cargadores       ,"     "    ,pu_cargadores,"   "   ,total2)
print("protectores        ",   cantidad_de_protectores ,"     "    ,pu_protectores,"   "   ,total3)
print("consumo:",consumo)
print("comprador compulsivo:",comprador_complusivo)
print("###############################")
