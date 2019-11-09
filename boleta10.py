# input
cliente=input("ingrese el nombre del cliente:")
cantidad_de_relojes=int(input("ingrese Nro de relojes que va a comprar:"))
cantidad_de_cadenas_oro=int(input("ingrese Nro de cadenas de oro que va a comprar:"))
cantidad_de_cadenas_plata=int(input("ingrese Nro de cadenas de plata que va a comprar:"))
pu_relojes=float(input("ingrese el precio unitario de relojes:"))
pu_cadena_de_oro=float(input("ingrese el precio unitario de de la cadena de oro:"))
pu_cadena_de_plata=float(input("ingrese el precio unitario de la cadena de plata"))

#processing
total1=(pu_relojes*cantidad_de_relojes)
total2=(pu_cadena_de_oro*cantidad_de_cadenas_oro)
total3=(pu_cadena_de_plata*cantidad_de_cadenas_plata)
consumo=(total1+total2+total3)
#verificador
comprador_complusivo=(consumo>5000)

#output
print("##############################")
print("# RELOJERIA RAMOS")
print("cliente:",cliente)
print("##############################")
print("producto       cantidad   P.U     Total")
print("relojes            " ,   cantidad_de_relojes ,"     "    ,pu_relojes  ,"   "   ,total1)
print("cadena de oro       ",   cantidad_de_cadenas_oro      ,"     "    ,pu_cadena_de_oro,"   "   ,total2)
print("cadena de plata     ",   cantidad_de_cadenas_plata,"     "    ,pu_cadena_de_plata,"   "   ,total3)
print("consumo:",consumo)
print("comprador compulsivo:",comprador_complusivo)
print("###############################")
