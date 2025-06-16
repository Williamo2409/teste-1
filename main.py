import random

vitórias = 0
derrotas = 0

jogar_novamente = "s"
while jogar_novamente == "s":
    numero = random.randint(1, 10)
    tentativas = 3

    print("Jogo da Advinhacao", flush=True)
    print("Voce tem 3 tentativas para acertar o numero entre 1 e 10.", flush=True)

    while tentativas > 0:
        palpite = int(input(f"Tentativa {4 - tentativas}: "))

        if palpite == numero:
            print("😎 Acertou! Parabéns!")
            vitórias += 1
            break
        else:
            tentativas -= 1
            if palpite < numero:
                print("Errou! O número e MAIOR.")
            else:
                print("Errou! O número e MENOR.")

        if tentativas == 0:
            print(f"Errouuu 😱😱😱! O número era {numero}")
            derrotas += 1

    print (f"placar -> vitórias: {vitórias} | derrotas: {derrotas} ")
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
