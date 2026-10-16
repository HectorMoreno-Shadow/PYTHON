servidor = {
    "nombre": "Web",
    "ip": "192.168.10.10",
    "puerto": 80
}

clave = input("Clave a buscar")

if clave in servidor:
    print(servidor[clave])
else:
    print (f"clave {clave} no existe")