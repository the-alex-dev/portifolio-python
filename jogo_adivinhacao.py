from random import randint

print("=== Jogo da Adivinhação ===")
numero_secreto = randint(1, 10)
tentativa = int(input("Adivinhe o número entre 1 e 10: "))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print(f"Errou! O número era {numero_secreto}.")