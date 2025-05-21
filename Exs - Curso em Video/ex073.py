# Tuplas com times de Vôlei

times = ('Vôlei Renata', 'Sesi Bauru', 'Cruzeiro', 'Praia Clube', 'Minas',
         'Vedacit Guarulhos', 'Joinville', 'Suzano', 'Neurologia Ativa', 'Goiás', 'Blumenau',
         'São José Vôlei')


print(f"5 primeiros colocados da Superliga Masculina de Vôlei: {times[0:5]}\n"
      f"Os 3 últimos colocados: {times[-1:-4:-1]}\n"
      f"Lista dos times em ordem alfabética: {sorted(times)}\n"
      f"Posição do Vedacit Guarulhos: {times.index('Vedacit Guarulhos') + 1} colocado")