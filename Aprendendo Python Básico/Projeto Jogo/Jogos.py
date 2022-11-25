import Jogo_Foca
import Jogo_Adivinhacao

def escolha_jogo():
    print("\n*********************************")
    print("      Escolha o seu Jogo!!")
    print("*********************************")


    print("\n(1)Adivinhação   (2)Forca")
    jogo = input("Qual? ")

    if jogo.isnumeric():
        jogo = int(jogo)
        if jogo == 1:
            print("\nCarregando Jogo da Adivinhação")
            Jogo_Adivinhacao.start_adivinhacao()
        elif jogo == 2:
            print("\nCarregando Jogo da Forca")
            Jogo_Foca.start_foca()
        else:
            print("\nOpção Inválida!")
    else:
        print("\nOpção Inválida!")

if __name__ == "__main__":
    escolha_jogo()