import os
os.system("cls")
idade = int(input('Digite sua idade: '))

if idade >= 18:
    os.system("cls")
    print('Você é maior de idade. ')
else:
    os.system("cls")
    print('Você é menor de idade. ')