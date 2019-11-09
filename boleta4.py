# input
cliente=input("ingrese el nombre del cliente:")
cantidad_de_pernos=int(input("ingrese Nro de pernos que va a comprar:"))
cantidad_de_clavos=int(input("ingrese Nro de clavos que va a comprar:"))
cantidad_de_calaminas=int(input("ingrese Nro de calaminas que va a comprar:"))
pu_perno=float(input("ingrese el precio unitario de perno:"))
pu_clavos=float(input("ingrese el precio unitario de clavo:"))
pu_calaminas=float(input("ingrese el precio unitario de la calamina"))

#processing
total1=(pu_perno*cantidad_de_pernos)
total2=(pu_clavos*cantidad_de_clavos)
total3=(pu_calaminas*cantidad_de_calaminas)
consumo=(total1+total2+total3)
#verificador
comprador_complusivo=(consumo>2000)

#output
print("##############################")
print("#FERRETARIA EL CLAVITO")
print("cliente:",cliente)
print("##############################")
print("producto       cantidad   P.U     Total")
print("PERNOS",   cantidad_de_pernos  ,"     "    ,pu_perno  ,"   "   ,total1)
print("CLAVOS         ",   cantidad_de_clavos        ,"     "    ,pu_clavos,"   "   ,total2)
print("CALAMINAS         ",   cantidad_de_calaminas ,"     "    ,pu_calaminas,"   "   ,total3)
print("CONSUMO:",consumo)
print("comprador compulsivo:",comprador_complusivo)
print("###############################")
