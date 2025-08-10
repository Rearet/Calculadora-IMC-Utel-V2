# Calculadora de IMC

def pedir_texto(mensaje):
    """Pide un texto y se asegura que no esté vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        else:
            print("⚠ Este campo no puede quedar vacío.")

def pedir_numero(mensaje, tipo=float):
    """Pide un número y valida que sea positivo."""
    while True:
        valor = input(mensaje).strip()
        if valor.replace('.', '', 1).isdigit():
            numero = tipo(valor)
            if numero > 0:
                return numero
            else:
                print("⚠ El valor debe ser mayor a 0.")
        else:
            print("⚠ Debes ingresar un número válido.")

# Solicitar datos personales para el calculo de IMC
nombre = pedir_texto("Nombre: ")
apellido_paterno = pedir_texto("Apellido paterno: ")
apellido_materno = pedir_texto("Apellido materno: ")
edad = pedir_numero("Edad (años): ", int)
peso = pedir_numero("Peso (kg): ")
estatura = pedir_numero("Estatura (metros, ej. 1.70): ")

# Proceso de calcular IMC
imc = peso / (estatura ** 2)

# Mostrar resultados completos
print("\n=== Datos ingresados ===")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")
