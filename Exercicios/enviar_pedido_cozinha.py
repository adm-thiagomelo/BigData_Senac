# import listar_pedidos_da_mesa.py

# vars a considerar: prato, quantidade, observações
# variável 'status': recebido ou entregue
# FALTA CONSIDERAR A MESA DO PEDIDO <<<<<<<<<<<<<<<<<<<<<<<<<<<
# PRATO = ITEM; nomenclatura
# mesa; atendente; item = {"nome": "preço"}; cardapio = {item: "descr"}; pedido = {item: qtd}; pedidos_mesa = [dicio1,dicio2...]
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

fila_de_preparacao = []

pedidos_da_mesa = [{'Prato': 'Peixe Frito',
                  'Quantidade': 1,
                  'Observação': 'N/A',
                  'Preço': 60},
                  {'Prato': 'Frango Grelhado',
                   'Quantidade': 2,
                   'Observação': 'Azeite, não óleo.',
                   'Preço': 45}]

def enviar_pedido_cozinha():
    '''
    Envia itens confirmados para a fila de preparação.
    '''

    for i in range(0, len(pedidos_da_mesa)):
        prato = pedidos_da_mesa[i].get('Prato')
        quantidade = pedidos_da_mesa[i].get('Quantidade')
        observacao = pedidos_da_mesa[i].get('Observação')
        status = 'Recebido'

        fila_de_preparacao.append({'Prato': prato, 'Quantidade': quantidade, 'Observação': observacao, 'Status': status})

enviar_pedido_cozinha()

print(fila_de_preparacao)