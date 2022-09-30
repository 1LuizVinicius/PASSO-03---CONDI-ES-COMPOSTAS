'''Desenvolva um programa que leia o nome de um funcionário, seu salário, 
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado 
de acordo com a tabela a seguir: 
- Até 3 anos de empresa: aumento de 3% 
- entre 3 e 10 anos: aumento de 12.5% 
- 10 anos ou mais: aumento de 20% '''

nome = input('Nome do funcionario: ')
salario = float(input('Digite seu salário: '))
ano = float(input('Ta a quanto tempo na empresa?: '))

if ano >= 10:
    print(nome,'seu salário agora é de',salario+(salario*20/100))

elif ano >= 3:
    print(nome,'seu salário agora é de',salario+(salario*12.5/100))

else:
    print('{} seu salário agora é de {:.2f}'.format(nome,salario+(salario*3/100)))