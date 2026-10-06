edad = int(input("Su edad:"))
saldo = int(input("Su saldo:"))

if edad >= 18 and saldo > 0:
    print("Acceso permitido")
else:
    print("Acceso no permitido")