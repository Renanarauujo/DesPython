vel = int(input("Digite a velocidade do carro: "))
lim = 80

if vel > lim:
    multa = ( vel - lim ) * 5
    print(f"Você foi multado em {multa} reais")
else:
    print("Velocidade aceita na via!")
