import random

numero = random.randint(1, 10)
tentativas = 3

print("Jogo da Advinhacao")
print("Voce tem 3 tentativas para acertar o numero entre 1 e 10.")

while tentativas > 0:
    palpite = int(input(f"Tentativa {4 - tentativas}: "))
    
    if palpite == numero:
        print("Acertou! Parabens!")
        break
    else:
        tentativas -= 1
        if palpite < numero:
            print("Errou! O numero e MAIOR.")
        else:
            print("Errou! O numero e MENOR.")

        if tentativas == 0:
            print(f"💀 Fim de jogo! O numero era {numero}")
