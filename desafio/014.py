c = float(input('Digite a temperatura em Celsius: '))
k = c + 273
f = 1.8 * c + 32
print('A temperatura de {:.0f} ºCelsius equivale {:.0f} Kelvin e {:.0f}º em Fahrenheit'.format(c, k, f))