'''
Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
de triângulo será formado: 
- EQUILÁTERO: todos os lados iguais 
- ISÓSCELES: dois lados iguais 
- ESCALENO: todos os lados diferentes 
'''

('Imforme os lados A,B e C.')
valor1 = int(input('Digite o lado A: '))
valor2 = int(input('Digite o lado B: '))
valor3 = int(input('Digite o lado C: '))

if ((valor1 < (valor2+valor3)) and (valor2 < (valor1+valor3)) and (valor3 < (valor1+valor2))):
    print("os segmentos acima pode formar triangulo")

    if valor1 == valor2 and valor2 == valor3:
        print("EQUILÁTERO: todos os lados iguais")

    elif valor1!= valor2!= valor3!= valor1:
        print("ESCALENO: todos os lados diferentes")
        print("Não pode formar um triângulo")
        
    else:
       print("ISÓSCELES: dois lados iguais")

'''valor1=float(input('digite o primeiro valor: '))
valor2=float(input('digite o segundo valor: '))
valor3=float(input('digite o terceiro valor: '))
if valor1< valor2 + valor3 and valor2< valor1 + valor3 and valor3< valor1 + valor2:
    print('os segmentos acima pode formar triangulo')

    if valor1 == valor2 and valor2 == valor3:
        print('EQUILÁTERO: todos os lados iguais')

    elif valor1!= valor2!= valor3 != valor1:
        print('ESCALENO: todos os lados diferentes')
        print("Não pode formar um triângulo")

    else :
        print('ISÓSCELES: dois lados iguais')'''