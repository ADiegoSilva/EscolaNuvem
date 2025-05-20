notas = []

while True:

    try:
        nota = float(input("Insira uma nota ou '99' para finalizar: "))
    except ValueError:
        print("O valor informado não é uma nota válida. \n")
        continue

    if nota == 99:
        print(f"\nNotas informadas: {notas}")
        print(f"%.2Média das notas:  {sum(notas) / len(notas):.2f}")
        break

    if nota > 10:
        print("O valor informado não é uma nota válida. \n")
        continue

    if 0 <= nota <= 10:
        notas.append(nota)
