'''
EJERCICIO #2
'''
#Teorema de Pitágoras
print('Cálculo del Teorema de Pitágoras')
#Ingreso de valores por consola
ca = float(input('Ingrese el valor de cateto adyacente: '))
co = float(input('Ingrese el valor de cateto opuesto: '))
#Fórmula del Teorema de Pitágoras c = ((ca**2)+(co**2))**0.5
p = ((ca**2) + (co**2))**0.5
#Resultado del Teorema de Pitágoras
print('El Teorema de Pitágoras con CA:',ca,'y CO:',co,'es de',p)