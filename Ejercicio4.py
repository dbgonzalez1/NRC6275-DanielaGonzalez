'''
EJERCICIO #17
'''
#Calcular año, mes y días
print('Calcular los años, meses y días')
#Ingreso de valores por consola
dias = float(input('Ingrese los días a calcular: '))
semanas = float(input('Ingrese las semanas a calcular: '))
anios = float(input('Ingrese los años a calcular: '))
#Fórmula para calcular del año a mes, mes = anios * (12/1)
mes = anios * (12/1)
print('Su resultado de año a mes es:',mes)
#Fórmula para calcular de la semana a día, dia = semanas * (7/1)
dia = semanas * (7/1)
print('Su resultado de semana a día es:',dia)
#Fórmula para calcular de semana a mes, mes = semanas * 0.23
mes = semanas * 0.23
print('Su resultado de semana a mes es:',mes)
#Fórmula para calcular de años a semana, semana = anios * ((365/1)*(1/7))
semana = anios * ((365/1)*(1/7))
print('Su resultado de años a semana es:',semana)