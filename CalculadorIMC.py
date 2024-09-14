print("Calculadora IMC")
name = input("Ingrese su nombre: ")
print(f"Hola {name}, Bienvenido al sistema")
rango_personas = int(input("¿A cuántas personas desea realizar la medición?: "))
for i in range(rango_personas):
    name = input("Ingrese el nombre para hacer la medicion: ")
    estatura = float(input("Por favor ingrese la estatura en metros: "))
    peso = float(input("Ingrese su peso en Kilogramos: "))
    IMC = peso/estatura**2
    if IMC < 18.5:
        print(f"El usuario {name} esta en bajo peso")
    elif IMC >= 18.5 and IMC <= 24.9:
        print(f"El usuario {name}  esta en el rango normal ")
    elif IMC >= 25 and IMC <= 29.9:
        print(f"El usuario {name}  esta en sobrepeso")
    else:
        print(f"El usuario {name} esta en obesidad")


print(f"Gracias por usar nuestro sistema {name}, hemos terminado")