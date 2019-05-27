from xlsxwriter import Workbook

book = Workbook('conta.xlsx')
pla = book.add_worksheet()

conta = (
    ['Luz', 80],
    ['Água', 60],
    ['Gás', 70],
    ['Comida', 500],
)

linha = 0
coluna = 0

for item, custo in conta:
    pla.write(linha, coluna, item)
    pla.write(linha, coluna+1, custo)
    linha +=1

pla.write(linha, coluna, 'Total')
pla.write(linha, coluna+1, '=SUM(B1:B4)')

book.close()
