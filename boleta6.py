# input
cliente=input("ingrese el nombre del cliente:")
cantidad_de_polos=int(input("ingrese Nro de polos que va a comprar:"))
cantidad_de_pantalones=int(input("ingrese Nro de pantalones que va a comprar:"))
cantidad_de_zapatillas=int(input("ingrese Nro de zapitillas que va a comprar:"))
pu_polos=float(input("ingrese el precio unitario de polo:"))
pu_pantalones=float(input("ingrese el precio unitario de pantalones:"))
pu_zapatillas=float(input("ingrese el precio unitario de la zapatillas"))

#processing
total1=(pu_polos*cantidad_de_polos)
total2=(pu_pantalones*cantidad_de_pantalones)
total3=(pu_zapatillas*cantidad_de_zapatillas)
consumo=(total1+total2+total3)
#verificador
comprador_complusivo=(consumo>1000)

#output
print("##############################")
print("# SAGAFALABELLA")
print("cliente:",cliente)
print("##############################")
print("producto       cantidad   P.U     Total")
print("POLOS ",   cantidad_de_polos  ,"     "    ,pu_polos ,"   "   ,total1)
print("PANTALONES       ",   cantidad_de_pantalones        ,"     "    ,pu_pantalones,"   "   ,total2)
print("ZAPITILLAS        ",   cantidad_de_zapatillas ,"     "    ,pu_zapatillas,"   "   ,total3)
print("CONSUMO:",consumo)
print("comprador compulsivo:",comprador_complusivo)
print("###############################")
