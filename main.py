import random

jogar_novamente = "s"
while jogar_novamente == "s":
    numero = random.randint(1, 10)
    tentativas = 3

print("Jogo da Advinhacao", flush=True)
print("Voce tem 3 tentativas para acertar o numero entre 1 e 10.", flush=True)

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
            print(f"Fim de jogo! O numero era {numero}")
            
jogar_novamente = input("Deseja jogar novamente? (s/n):")
