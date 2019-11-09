# input
cliente=input("ingrese el nombre del cliente:")
cantidad_de_fotos=int(input("ingrese Nro de fotos que va a comprar:"))
cantidad_de_cuadros=int(input("ingrese Nro de cuadros que va a comprar:"))
cantidad_de_almanaques=int(input("ingrese Nro de almanaques que va a comprar:"))
pu_foto=float(input("ingrese el precio unitario de foto:"))
pu_cuadros=float(input("ingrese el precio unitario de cuadro:"))
pu_almanaques=float(input("ingrese el precio unitario de la almanaques"))

#processing
total1=(pu_foto*cantidad_de_fotos)
total2=(pu_cuadros*cantidad_de_cuadros)
total3=(pu_almanaques*cantidad_de_almanaques)
consumo=(total1+total2+total3)
#verificador
comprador_complusivo=(consumo>200)

#output
print("##############################")
print("# FOTOHOUSE.S.A.C")
print("cliente:",cliente)
print("##############################")
print("producto       cantidad   P.U     Total")
print("fotos "                ,  cantidad_de_fotos ,"     "    ,pu_foto ,"   "   ,total1)
print("cuadros      ",    cantidad_de_cuadros      ,"     "    ,pu_cuadros,"   "   ,total2)
print("almanaques      ",   cantidad_de_almanaques ,"     "    ,pu_almanaques,"   "   ,total3)
print("consumo:",consumo)
print("comprador compulsivo:",comprador_complusivo)
print("###############################")
