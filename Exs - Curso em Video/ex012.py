# Calculando desconto

v = float(input('Qual o preço do produto?'))
vf = v - round(v * 5 / 100, 2)
print('O produto que custava R${:.2f}, com 5% de deconto vai custar R${}'.format(v, vf))
