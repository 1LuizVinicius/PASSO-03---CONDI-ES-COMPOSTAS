'''
Crie um programa que leia duas notas de um aluno e calcule a sua média, 
mostrando uma mensagem no final, de acordo com a média atingida: 
- Média até 4.9: REPROVADO 
- Média entre 5.0 e 6.9: RECUPERAÇÃO 
- Média 7.0 ou superior: APROVADO 
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

soma = (nota1 + nota2) / 2

if soma >= 7.0:
    print('Sua nota é',soma,'você esta aprovado')
elif soma >= 5.0:
    print('Sua nota é',soma,'você esta de recuperação')
else:
    print('Sua nota é',soma,'você esta reprovado')