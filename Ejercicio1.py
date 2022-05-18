'''
EJERCICIO #15
'''
#Calcular la temperatura en grados Celsius y convertirla en grados Fahrenheit y viceversa.
print('Calcular temperatura en grados Celsius a Fahrenheit y viceversa.')
#Ingreso de valores por consola
celsius = float(input('Ingrese en la temperatura en Celsius: '))
fahrenheit = float(input('Ingrese en la temperatura en Fahrenheit: '))
#Fórmula para convertir Fahrenheit a Celsius
cal_celsius = (fahrenheit - 32) / 1.8
#Fórmula para convertir Celsius a Fahrenheit
cal_fahrenheit = (celsius * 1.8) + 32 
#Resultado de las conversiones
print('La temperatura en grados Celsius a Fahrenheit es:', cal_celsius)
print('La temperatura en grados Fahrenheit a Celsius es:', cal_fahrenheit)