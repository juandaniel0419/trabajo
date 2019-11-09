# input
cliente=input("ingrese el nombre del cliente:")
cantidad_producto=int(input("ingrese la cantidad comprada:"))
Pu=float(input("ingrese precio unitario:"))

#processing
total=(Pu*cantidad_producto)

#verificador
comprador_complusivo=(total>500)

#output
print("##############################")
print("# Boleta de ventas")
print("##############################")
print("#")
print("# cliente: ",  cliente)
print("# item   :",   cantidad_producto,"cajas de chocolate")
print("# P.u    :    $", Pu,)
print("# total  :    $", total)
print("###############################")
print("comprador compulsivo",comprador_complusivo)
