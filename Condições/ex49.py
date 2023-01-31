# Definição do valor inicial da casa/salário do comprador/tempo para pagar
valor_casa = float(input("Insira o valor da casa: "))
salario = float(input("Insira o seu salário: "))
anos = int(input("Insira a quantidade de anos pagar a casa: "))

# Análises prévias das variáveis de cálculo
meses = anos * 12
prestaçao = valor_casa / meses
verificaçao = salario * 0.30  

# Verificação de aprovação/reprovação do empréstimo
if prestaçao < verificaçao:
    print("Empréstimo aprovado")
else:
    print("Empréstimo reprovado")

