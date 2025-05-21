# Radar eletrônico

vel = int(input('Qual a velocidade do seu carro: '))

if vel > 80:
    print(f"\033[31mVocê ultrapassou a velocidade média permitida!\n\033[1;33mDeverá pagar uma multa de R${(vel-80) * 7}")
else:
    print("\033[32mVelocidade dentro do limite, tenha um bom dia!")