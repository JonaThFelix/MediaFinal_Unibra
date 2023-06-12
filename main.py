#Calculando média da Unibra para passar na final

def i():
  print('-'* 50)
  
def media(av1,av2,av3):
  return (av1+av2+av3) / 3

i()
print('Selecione: \n')
print('1: ------- FINAL\n')

escolha = int(input('MENU ....: '))
i()
if escolha == 1:
  av1 = float(input('Digite sua AV1: '))
  av2 = float(input('Digite sua AV2: '))
  av3 = float(input('Digite sua AV3: '))
  print('\n')
  i()

  if media(av1,av2,av3) >=7:
    print(f'Você já passou com média {media(av1,av2,av3):.2f}.')
    print('Parabéns ! ╰(*°▽°*)╯')
    i()

  elif media(av1,av2,av3) < 7:
    print(f'Você ficou abaixo da média com {media(av1,av2,av3):.2f}, que veregonha (￣﹃￣)')
    mediafn =  (media(av1,av2,av3) - 10) * -1
    print(f'Você tem que tirar no mínimo {mediafn:.2f} para passar na cadeira.')
    i()


"""
Você tem que somar 21 pontos nas três avaliações.
Exemplo:
1AV  4.0
2Av 10.0
3AV 4.0

Somando as 3 = 18/3 = 6
6.0  para 10.0 
4.0 é quanto precisa tirar na final"""
