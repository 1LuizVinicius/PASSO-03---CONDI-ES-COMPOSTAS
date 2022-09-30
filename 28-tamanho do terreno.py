'''
Faça um programa que leia a largura e o comprimento de um terreno 
retangular, calculando e mostrando a sua área em m². O programa também 
devemostrar a classificação desse terreno, de acordo com a lista abaixo: 
- Abaixo de 100m² = TERRENO POPULAR 
- Entre 100m² e 500m² = TERRENO MASTER 
- Acima de 500m² = TERRENO VIP
'''

print('Qual largura e lagura você deja saber de um terreno retângular?')

largu = float(input('Digite uma largura em metros: '))
comprim = float(input('Digite uma comprimento em metros: '))

area = largu + comprim

if area >= 500:
    print('{}m² é um terreno VIP.'.format(area))

elif area >= 100:
    print('{}m² é um terreno MASTER.'.format(area))

else:
    print('{}m² é um terreno POPULAR.'.format(area))