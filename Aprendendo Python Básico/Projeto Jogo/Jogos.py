print("\n*********************************")
print("      Escolha o seu Jogo!!")
print("*********************************")


print("\n(1)Adivinhação   (2)Forca")
jogo = input("Qual? ")

if jogo.isnumeric():
    jogo = int(jogo)
    if jogo == 1:
        print("\nCarregando Jogo da Adivinhação")
    elif jogo == 2:
        print("\nCarregando Jogo da Forca")
    else:
        print("\nOpção Inválida!")
else:
    print("\nOpção Inválida!")