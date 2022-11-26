import math
import pandas

#Importa a tabel normal
tabela_normal = pandas.read_csv("tabelaNormal.csv", sep="\t")
#Tranformas os valores da tabela em numeros
for colum in tabela_normal.columns.values:
  tabela_normal[colum] = tabela_normal[colum].str.replace(',', '.').astype(float)
#Tranforma a primeira coluna em index
tabela_normal = tabela_normal.set_index('Z')

def achaNormal(valor):
  cabe = tabela_normal.columns.values
  index = tabela_normal.index

  normal = 0.0
  
  for num1 in index:
    for num2 in cabe:
      #Valor igual
      if float(tabela_normal[num2][num1] == valor):
        normal = num1+float(str(num2).replace(',','.'))
      
      #O proximo ser maior
      next_num = float(str(num2).replace(',','.')) + 0.01
      next_num = str(next_num)
      if float(tabela_normal[num2][num1] < valor):
        normal = num1+float(str(num2).replace(',','.'))
  
  return normal


def EPM(dp_pop, num_elementos):
  return dp_pop / math.sqrt(num_elementos)

def Bicaudal(med_pop, valor_alvo, porcent, num_elementos, dp):
  normal = achaNormal(0.5 - (porcent/2))
  z = (med_pop - valor_alvo)/EPM(dp, num_elementos)
  print(f"Z critico = {normal} \n Z = {z}")
  if z >= float(normal)*-1 and z <= float(normal):
    print('Aceitar a hipotese base.')
  else:
    print('Rejetiar a hipotese base.')

def Monocaudal(med_pop, valor_alvo, porcent, num_elementos, dp):
  normal = achaNormal(0.5 - porcent)
  z = (med_pop - valor_alvo)/EPM(dp, num_elementos)
  print(f"Z critico = {normal} \n Z = {z}")
  if z <= float(normal):
    print('Aceitar a hipotese base.')
  else:
    print('Rejetiar a hipotese base.')


op = 1
while op != 0:
  print("\n----Teste de Hipotese: Uma Amostra-----\n")
  print("1. Entre com os dados do sua hipotese")
  print("0. Sair")
  op = int(input())

  if(op == 1):
    valor_alvo = float(input("Valor alvo: ").replace(',', '.'))
    med_pop = float(input("Media: ").replace(',','.'))
    porcent = float(input("Nivel de significancia: ").replace(',','.'))
    num_elementos = int(input("Num elementos: "))
    dp = float(input("Desvio padrao: ").replace(',','.'))

    print("Qual o tipo:")
    print("1. Monocaudal")
    print("2. Bicaudal")
    tipo = input()
    if(1):
      Monocaudal(med_pop, valor_alvo, porcent, num_elementos, dp)
    elif(2):
      Bicaudal(med_pop, valor_alvo, porcent, num_elementos, dp)
  