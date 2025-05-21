#Conversor de medidas

x = int(input('Digite uma distância em metros: '))
km = x/1000
hm = x/100
dam = x/10
dm = x*10
cm = x*100
mm = x*1000
print(f'A medida de {x}m corresponde a: \n'
      f'{km}km \n'
      f'{hm}hm \n'
      f'{dam}dam \n'
      f'{dm}dm \n'
      f'{cm}cm \n'
      f'{mm}mm')