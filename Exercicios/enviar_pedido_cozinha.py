from listar_pedidos_da_mesa import listar_pedidos_da_mesa

def enviar_pedido_cozinha(numero_mesa, numero_pedido, pedidos, fila_cozinha):
    """
    Envia um pedido para a fila de preparação da cozinha.
    """

    # Validações
    if not isinstance(numero_mesa, int):
        raise TypeError("O número da mesa deve ser um número inteiro.")

    if numero_mesa <= 0:
        raise ValueError("O número da mesa deve ser maior que zero.")

    if not isinstance(numero_pedido, int):
        raise TypeError("O número do pedido deve ser um número inteiro.")

    if numero_pedido <= 0:
        raise ValueError("O número do pedido deve ser maior que zero.")

    if not isinstance(pedidos, list):
        raise TypeError("Os pedidos devem ser fornecidos em uma lista.")

    if not isinstance(fila_cozinha, list):
        raise TypeError("A fila da cozinha deve ser uma lista.")

    # Pega os pedidos da mesa sem imprimir no terminal
    pedidos_da_mesa = listar_pedidos_da_mesa(
        numero_mesa,
        pedidos,
        exibir=False
    )

    # Procura o pedido informado
    pedido_encontrado = None

    for pedido in pedidos_da_mesa:
        if pedido["numero_pedido"] == numero_pedido:
            pedido_encontrado = pedido
            break

    if pedido_encontrado is None:
        raise ValueError("Pedido não encontrado.")

    # Monta o pedido que será enviado para a cozinha
    pedido_cozinha = {
        "numero_pedido": pedido_encontrado["numero_pedido"],
        "numero_mesa": pedido_encontrado["numero_mesa"],
        "itens": []
    }

    # Coloca os itens do pedido na fila
    for item in pedido_encontrado["itens"]:

        item_cozinha = {
            "codigo_prato": item["codigo_prato"],
            "nome_prato": item["nome_prato"],
            "quantidade": item["quantidade"],
            "observacoes": item["observacoes"]
        }

        pedido_cozinha["itens"].append(item_cozinha)

    # Adiciona o pedido à fila
    fila_cozinha.append(pedido_cozinha)

    return fila_cozinha
