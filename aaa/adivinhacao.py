def jogar():
    import random

    print("1 - Nível fácil 1")
    print("2 - Nível médio 2")
    print("3 - Nível difícil 3")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada:"))
    if (opcao == 1):
        print("Vocẽ entrou no modo fácil")
        print("Acerte o número que estou pensando de 1 a 10")
        print("Vocẽ tem 5 tentativas")
        numero_max = 10
        limite_tentativas = 5
    elif (opcao == 2):
        print("Vocẽ entrou no modo médio")
        print("Acerte o número que estou pensando de 1 a 20")
        print("Vocẽ tem 5 tentativas")
        numero_max = 20
        limite_tentativas = 5
    elif (opcao == 3):
        print("Vocẽ entrou no modo difícil")
        print("Acerte o número que estou pensando de 1 a 50")
        print("Vocẽ tem 10 tentativas")
        numero_max = 50
        limite_tentativas = 10
    elif (opcao == 4):
        print("Vocẽ saiu")  
        exit()  
    else: 
        print("Opoção inválida. Selecionado modo fácil")
        numero_max = 10
        limite_tentativas = 5


    sorteio = random.randint(1, numero_max)
    #print(sorteio)
    print("### JOGO DA ADIVINHAÇÃO ###")
    print("Adivinhe o número que estou pensando!")
    tentativa = 1
    while (limite_tentativas >= tentativa):
        print("Tentativa", tentativa)
        chute = int(input("Digite o seu chute:"))
        if (chute == sorteio):
            print("AEEEEEEEEEE VOCẼ ACERTOUUUUU :D!")
            break
        elif (chute > sorteio):
            print("Chute um número menor!")
        elif (chute < sorteio):
            print("Chute um número maior!")
        tentativa = tentativa + 1
        # FINAL DO LAÇO WHILE
    print("Cabo ;n;   O número sorteado era: ##", sorteio, "##")
    print("### FIM DO JOGO ###")

if(__name__ == "__main__"):
    jogar()
