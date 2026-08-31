'''
1. DETERMINAR O NÚMERO DE MESAS
2. CHECAR OS PEDIDOS DE CADA MESA
- COMO DETERMINAR A ORDEM? HÁ ALGUM ID DO PEDIDO?
3. EXTRAIR O PRATO, A QUANTIDADE, AS OBSERVAÇÕES E A MESA QUE FEZ O PEDIDO
4. JUNTAR ESSAS INFORMAÇÕES EM UM DICT
5. INSERIR OS PEDIDOS (DICTS) EM UMA LISTA EM ORDEM. A LISTA SERÁ CHAMADA DE FILA_DE_PREPARACAO
'''

# import listar_mesas()
# import listar_pedidos_da_mesa()

def enviar_pedido_cozinha():
    '''
    Envia itens confirmados para a fila de preparação.
    '''

    lista_de_mesas_ocupadas = []

    # DETERMINAR O NÚMERO DE MESAS OCUPADAS

    # lista_de_mesas = listar_mesas()
    lista_de_mesas = [{'Mesa': 1, 'Status': 'Ocupada'},
                      {'Mesa': 2, 'Status': 'Livre'},
                      {'Mesa': 3, 'Status': 'Ocupada'}]

    for cada_mesa in lista_de_mesas:
        if cada_mesa.get('Status') == 'Ocupada':
            lista_de_mesas_ocupadas.append(cada_mesa)

    # EXTRAIR OS PEDIDOS DE CADA MESA

    lista_de_pedidos = [{'Item': 1, 'Quantidade': 2, 'Observações': 'N/A', 'Mesa': 1}
                        ]

    for cada_mesa_ocupada in lista_de_mesas_ocupadas:

