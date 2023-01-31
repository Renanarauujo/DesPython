# Criando os contadores para elaboração de tabuada inputada, com início e fim

tabuada = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

# Condição para evitar erro no código por falha de input do usuário
if inicio > fim:
    print("Erro de input!")
else:
    while inicio < fim:
        inicio = inicio + 1
        x = inicio * tabuada
        print(f"{tabuada} x {inicio} = {x}")
    
