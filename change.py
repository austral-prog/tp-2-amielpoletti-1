def change():
    gasto = 23.75
    dinero_recibido = 100

    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)

    print("Ingresar gasto:")
    print(f"{gasto}")
    print("Dinero recibido")
    print(f"{dinero_recibido}")
    print("\nVuelto\n")
    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{centavos}")

