from process import ModuloProcessamento
from json import dumps

#Desf = ModuloProcessamento.Desfazimentos('self')
#credit = ModuloProcessamento.Geral('self')

#ModuloProcessamento.salvaxml('self', 'interno-0100-logq2', l)
l = ModuloProcessamento.Geral('self', True)
for i in l:
    print(i)
#print(f'Total de Credito Mercado Pago: {credit}')
#print(f'Total de Desfazimentos Mercado Pago: {Desf}')
#oi