# input
cliente=input("ingrese el nombre del cliente:")
residencia=input("ingrese tipo de recidencia :")
direccion=input("ingrese direccion :")
costo_casaca=float(input("ingrese el precio de la prenda (casaca):"))
costo_polo=float(input("ingrese el precio de la prenda(polo):"))
cantidad_casacas=int(input("ingresar la cantidad de casacas compradas:"))
cantidad_polos=int(input("ingresar la canitdad de polos compradas:"))

#processing
total1=(cantidad_casacas*costo_casaca)
total2=(cantidad_polos*costo_polo)
total_final=(total1+total2)
#verificador
comprador_complusivo=(total_final>1000)

#output
print("##############################")
print("# Boleta de ventas")
print("##############################")
print("NOVEDADADES YULI")
print("# cliente: ",  cliente)
print("# recidencia  :",residencia)
print("# direcion de la tienda:",direccion)
print("# precio de casaca:$",costo_casaca)
print("# cantidad de casacas:",cantidad_casacas)
print("# precio de polo:$",costo_polo)
print("# cantidad de polos:",cantidad_polos)
print("# comprador compulsivo",comprador_complusivo)
print("# total a cancelar:$",total_final)
print("###############################")
print("comprador compulsivo ",comprador_complusivo)
