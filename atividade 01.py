import os
os.system("cls")
print("=== Bem-vindo ao sistema de Taxi ===")

nome = input("Qual é o seu nome? ")

print(f"Olá, {nome}!")

tipo = input("Você quer uma corrida de moto ou carro? (moto/carro): ").lower()

if tipo == "moto":
    print(f"{nome}, uma moto está a caminho! ")
elif tipo == "carro":
    print(f"{nome}, um carro está a caminho! ")
else:
    print("Opção inválida. Tente novamente escolhendo 'moto' ou 'carro'.")
