# Verificação do consumo de energia elétrica
consumo = float(input("Digite o consumo mensal em kWh: "))

# Criação de um menu com os tipos de instalações
print("R - Residêncial\nC - Comercial\nI - Industrial\n")
tipo = str(input("Digite o tipo de instalação: "))

# Verificação do valor a se pagar
if tipo == "R" and consumo <= 500:
    pagar = consumo * 0.40
elif tipo == "R" and consumo > 500:
    pagar = consumo * 0.65
elif tipo == "C" and consumo <= 1000:
    pagar = consumo * 0.55
elif tipo == "C" and consumo > 1000:
    pagar = consumo * 0.60
elif tipo == "I" and consumo <= 5000:
    pagar = consumo * 0.55
elif tipo == "I" and consumo > 5000:
    pagar = consumo * 0.60
else:
    print("Opção inválida, tente novamente!")

print(f"Total a pagar: R$ {pagar}")

