import random

#lista de usuarios

usuarios = ["Juan", "Sofia", "Constanza", "Pedro", "Ramon",
            "Carolina", "Timon", "Eduardo", "Catalina", "Jose"]

#funcion para asignar contraseña aleatoria
def crear_cuenta(usuario):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    contraseña = "".join(random.choice(caracteres) for _ in range(8))
    return usuario, contraseña

#funcion para solicitar numero de contacto por cada cuenta
def solicitar_numero_contacto(usuario):
    while True:
        numero = input(f"Por favor, ingresa el número telefónico de contacto para {usuario} (8 dígitos): ")
        if len(numero) == 8 and numero.isdigit():
            return numero
        else:
            print("El número telefónico debe tener 8 dígitos numéricos.")

# Crear cuentas y asignar contraseñas
cuentas = {}
for usuario in usuarios:
    cuenta, contraseña = crear_cuenta(usuario)
    cuentas[cuenta] = contraseña

# Solicitar números de contacto
numeros_contacto = {}
for usuario in usuarios:
    numero = solicitar_numero_contacto(usuario)
    numeros_contacto[usuario] = numero

# Imprimir resultados
print("Cuentas creadas:")
for cuenta, contraseña in cuentas.items():
    numero = numeros_contacto[cuenta]
    print(f"Cuenta: {cuenta} - Contraseña: {contraseña} - Número de contacto: {numero}")