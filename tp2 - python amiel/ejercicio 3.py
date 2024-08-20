gasto = float(input("Ingresar gasto:\n"))
dinero_recibido = float(input("Dinero recibido\n"))

vuelto = dinero_recibido - gasto

pesos = float(vuelto)
centavos = int((vuelto - int(vuelto)) * 100)

print("\nVuelto\n")
print("Pesos:")
print(f"{int(pesos)}")
print("Centavos:")
print(f"{centavos}")