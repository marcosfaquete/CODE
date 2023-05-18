

palavra_secreta = ["H", "A", "C", "E", "I", "O"]

letras_descobertas = []

print("\n*** Jogo da Forca ***\n")

for i in range(0, len(palavra_secreta)) :
    letras_descobertas.append("-")

acertou = False

while acertou == False :
    letra = str(input("Digite a letra: "))

    for i in range(0, len(palavra_secreta)) :
        if letra == palavra_secreta[i] :
           letras_descobertas[i] = letra

        print(letras_descobertas[i])
