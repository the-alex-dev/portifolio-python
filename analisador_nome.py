print("=== Analisador de Nome ===")
nome = input("Digite seu nome completo: ").strip()
print(f"Nome em maiúsculas: {nome.upper()}")
print(f"Nome em minúsculas: {nome.lower()}")
print(f"Quantidade de letras (sem espaços): {len(nome.replace(' ', ''))}")
print(f"Primeiro nome tem {len(nome.split()[0])} letras")