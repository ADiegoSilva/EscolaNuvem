notas = []

while True:

    try:
        nota = float(input("Insira uma nota ou '99' para finalizar: "))
    except ValueError:
        print("O valor informado não é uma nota válida. \n")
        continue

    if nota == 99:
        print(f"\nNotas informadas: {notas}")
        print(f"Média das notas:  {sum(notas) / len(notas)}")
        break

    if 0 <= nota <= 10:
        notas.append(nota)
        #print(f"Notas informadas: {notas}")
        #print(f"Soma valores da lista: {sum(notas)}")
        #print(f"Tamanho lista: {len(notas)}\n")