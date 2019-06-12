import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from xlsxwriter import Workbook

# Escrevendo

'''book = Workbook('Tabela.xlsx')
pla = book.add_worksheet()

tab = (
    ['Número Missão', 'Pontos Missão', 'Pontos'],
    [1, 46, 0]
)

linha = 0
coluna = 0

# Escrevendo
for nm, pm, po in tab:
    pla.write(linha, coluna, nm)
    pla.write(linha, coluna+1, pm)
    pla.write(linha, coluna+2, po)
    linha +=1

book.close()'''

# Lendo

tabe = pd.read_excel('Tabela.xlsx')

# Coluna
# tabe['Número Missão']

# Linha
for i in tabe.index:
    con = tabe['Número Missão'][i]
    #print(tabe['Número Missão'][i])
    #print(i)
    print('{}: {}'.format(i, con))
