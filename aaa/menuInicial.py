import adivinhacao
import forca
print("Escolha o jogo desejado:")
print("1 - Adivinhação")
print("2 - Forca")
print("3 - Sair")
opcao = int(input("Digite a opção desejada:"))
if (opcao == 1):
    print("Executando adivinhação...")
    adivinhacao.jogar()
elif (opcao == 2):
    print("Executando forca...")
    forca.jogar()
elif (opcao == 3):
    print("Vocẽ saiu")  
    exit()  
else:
    print("Opção inválida")
    print("Executando forca...")
    forca.jogar()