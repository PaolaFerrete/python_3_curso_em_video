frase = ('Curso em vídeo Python')
print(frase)
#Fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print('curso' in frase)

#Transformações
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = ('  aprendendo python  ')
print(frase2)
print(frase2.strip())
print(frase.split())
print('-'.join(frase))