print("#--------------------------#")
print("#--| calculadora de imc |--#")
print("#--------------------------#")
peso = float(input("ingrese su peso en kilogramos: "))
altura = float(input("ingrese su altura en metros: "))
if peso <= 0 or altura <= 0:
    print("error: el peso y la altura deben ser valores positivos")
else:
    imc = peso / (altura ** 2)
    print("imc:", round(imc, 2))
    if imc < 18.5:
        print("clasificacion: bajo peso")
    elif imc < 25:
        print("clasificacion: peso normal")
    elif imc < 30:
        print("clasificación: sobrepeso")
    else:
        print("clasificación: obesidad")