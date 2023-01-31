# Inserção dos valores da operação
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"Primeiro número = {a}")
print(f"Segundo número = {b}\n")

# Criação de menu básico para escolha da operação matemática
print("1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n")

tipo = int(input("Escolha a opção que você deseja: "))


# Conta matemática mediante a escolha realizada no menu de operações
if tipo == 1:
    resultado = a + b
elif tipo == 2:
    resultado = a - b
elif tipo == 3:
    resultado = a * b
elif tipo == 4:
    resultado = a // b
else: 
    print("Opção inválida!")

print(f"\nResultado igual a: {resultado}")

