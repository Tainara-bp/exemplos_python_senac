import os
os.system("cls")

print("=== Cadastro de carros ===")

while True:
    carro = input("Digite o nome de um carro: ")

    continuar = input("Quer adicionar outro carro? (s/n): ").lower()

    if continuar != "s":
        print("Encerrando o programa...")
        break