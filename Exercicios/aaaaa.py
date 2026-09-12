# WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP

import pandas as pd

planilha_transacoes = pd.read_excel('base_invest.xlsx', sheet_name= 'Transacoes')
planilha_ativo = pd.read_excel('base_invest.xlsx', sheet_name = 'Ativo')

planilha_compra = planilha_transacoes[planilha_transacoes['operacao'] == 'compra']
planilha_venda = planilha_transacoes[planilha_transacoes['operacao'] == 'venda']

preco_max_compra = planilha_compra['preco'].max()
preco_min_compra = planilha_compra['preco'].min()
preco_max_venda = planilha_venda['preco'].max()
preco_min_venda = planilha_venda['preco'].min()
print(preco_max_compra)

print()
planilha_transacoes['valor_total'] = planilha_transacoes['quantidade'] * planilha_transacoes['preco']
valor_por_ativo = planilha_transacoes.groupby('id_ativo')['valor_total'].sum()
id_ativo_maior_valor = valor_por_ativo.idxmax()
cnpj_maior_valor = planilha_ativo[planilha_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]
print(cnpj_maior_valor)

print()
valor_por_participante = planilha_transacoes.groupby('id_participante')['valor_total'].sum()
print(valor_por_participante)