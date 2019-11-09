# input
cliente=input("ingrese el nombre del cliente:")
kg=int(input("ingrese Nro kg de manzana:"))
Pu=float(input("ingrese precio unitario:"))

#processing
total=(Pu*kg)

#verificador
comprador_complusivo=(total>200)

#output
print("##############################")
print("# Boleta de ventas")
print("##############################")
print("#")
print("# cliente: ",  cliente)
print("# item   :",   kg,"kg manzana")
print("# P.u    :    $", Pu,)
print("# total  :    $", total)
print("###############################")
print("El comprador es complusivo",comprador_complusivo)