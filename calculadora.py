print("=== Calculadora Simples ===")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+ - * /): ")

if op == "+":
    print(f"Resultado: {n1 + n2}")
elif op == "-":
    print(f"Resultado: {n1 - n2}")
elif op == "*":
    print(f"Resultado: {n1 * n2}")
elif op == "/":
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Erro: Divisão por zero!")
else:
    print("Operação inválida.")