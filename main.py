import random

numero = random.randint(1, 10)
palpite = int(input("Adivinhe o numero de 1 a 10: "))
if palpite == numero:
    print("Acertou!")
else:
    print(f"Errou! O numero era {numero}")
