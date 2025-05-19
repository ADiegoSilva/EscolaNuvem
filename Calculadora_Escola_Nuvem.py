while True:

    try:
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))
    except ValueError:
        print("Entrada inválida. Reiniciando a operação...\n")
        continue

    operacao = input("Informe a operação desejada (soma[+], subtração[-], "
                     "multiplicação[*], divisão[/]): ")

    if operacao not in ('+', '-', '*', '/'):
        print("Operação informada inválida [%s]. "
              "Operações permitidas: +, -, *, /. Reiniciando a operação...\n" % (operacao))
        continue

    #if operacao == '/' and num2 == 0:
    #    print("Divisão por zero não é permitida. Tente novamente.")

    try:
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2

        print(f"Resultado: {resultado}")
        break  # Saída do loop ao encontrar uma operação válida

    except ZeroDivisionError:
        print("Divisão por zero não é permitida. Reiniciando a operação... \n")