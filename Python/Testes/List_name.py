namelist = []

print('\n')
namelist.append(input('Cadastre_1: '))
print('\n')
namelist.append(input('Cadastre_2: '))
print('\n')
namelist.append(input('Cadastre_3: '))

print('\n')
print(namelist)




for i in range (3):
    print('ola!')



on = True
while True:
  try:
    num = int(input('Digite um número entre 0 e 20: '))
    break
  except ValueError:
    print("Digite somente números!")