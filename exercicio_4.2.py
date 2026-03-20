
LIMITE_VELOCIDADE=80
TAXA_MULTA= 5.0

velocidade_usuario=int(input("Digite a velocidade do carro em km/h?"))

if velocidade_usuario>LIMITE_VELOCIDADE:
    diferenca_velocidade=velocidade_usuario-LIMITE_VELOCIDADE
    multa=diferenca_velocidade*TAXA_MULTA
    print(f"O usuário deve pagar uma taxa de R${multa} por excesso de velocidade")
else:
    print("O usuário está dentro do limite de velocidade")