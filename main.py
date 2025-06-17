import random
import time
import threading

def placar(vitórias, derrotas):
    print(f"📊 Placar -> Vitórias: {vitórias} | Derrotas: {derrotas}")
    print("=" * 40)
    
def input_com_timeout(prompt, timeout):
    resposta = [None]

    def receber_imput():
        resposta[0] = input(prompt)

    t = threading.Thread(target=receber_imput)
    t.start()
    t.join(timeout)

    if t.is_alive():
        return None
    return resposta[0]

vitórias = 0
derrotas = 0

while True:
    inicio = time.time()
    numero = random.randint(1, 10)
    tentativas = 3
    print("=" * 40)
    print("🎮 Jogo da Advinhação", flush=True)
    print("Voce tem 3 tentativas para acertar o numero entre 1 e 10.",
          flush=True)

    while tentativas > 0:
        if time.time() - inicio > 10:
            print("⏰ Muito lentooo!")
            derrotas += 1
            break
        entrada = input_com_timeout(f"Tentativa {4 - tentativas}: ", 10)
        if entrada is None:
            print("⏰ Muito lentooo!")
            derrotas += 1
            break

        if entrada.lower() == "placar":
            placar(vitórias, derrotas)
            continue

        try:
            palpite = int(entrada)
        except ValueError:
            print("⚠️ Digite apenas números válidos ou 'placar'.")
            continue

        if palpite == numero:

            print("😎 Acertou! Parabéns!")
            vitórias += 1
            break
        else:
            tentativas -= 1
            if palpite < numero:

                print("Errou! O número e MAIOR.")
                print("=" * 40)
            else:

                print("Errou! O número e MENOR.")
                print("=" * 40)

        if tentativas == 0:
            print(f"Errouuu 😱😱😱! O número era {numero}")
            derrotas += 1

    placar(vitórias, derrotas)

    while True:
        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        try:
            if jogar_novamente == "s":
                break
            elif jogar_novamente == "n":
                print("Obrigado por jogar! Até a próxima!")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("⚠️ Digite apenas 's' ou 'n'.")
