'''
Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
na tela uma das mensagens abaixo: - O primeiro valor é o maior 
- O segundo valor é o maior 
- Não existe valor maior, os dois são iguais
'''

pergunta = int(input('Digite um valor: '))
print('O primeiro número é',pergunta)

pergunta2 = int(input('Digite outo valor: '))
print('O segundo número é',pergunta)

if pergunta >= pergunta2:
    print(pergunta,'é maior que',pergunta2)
else:
    print(pergunta,'nao é maior que',pergunta2)