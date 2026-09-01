def enviar_pedido_cozinha(pedido: dict, fila_cozinha: list[dict]) -> list[dict]:
    '''
    Envia os itens de um pedido confirmado para a fila da cozinha.

    Args:
        pedido: Dicionário contendo os dados do pedido.
        fila_cozinha: Lista que representa a fila de preparação.

    Returns:
        A fila da cozinha atualizada.

    Raises:
        TypeError: Se os parâmetros tiverem tipos inadequados.
        ValueError: Se o pedido não possuir itens ou número de pedido inválido.
    '''

    # Validações
    if not isinstance(pedido, dict):
        raise TypeError(
            "Parâmetro inválido: o pedido deve ser fornecido em um dicionário."
        )

    if not isinstance(fila_cozinha, list):
        raise TypeError(
            "Parâmetro inválido: a fila da cozinha deve ser fornecida em uma lista."
        )

    if "numero_pedido" not in pedido:
        raise ValueError(
            "Pedido inválido: o número do pedido não foi informado."
        )

    if "numero_mesa" not in pedido:
        raise ValueError(
            "Pedido inválido: o número da mesa não foi informado."
        )

    if "itens" not in pedido or not pedido["itens"]:
        raise ValueError(
            "Pedido inválido: não existem itens para enviar à cozinha."
        )

    # Verifica se o pedido já foi enviado para evitar duplicidade
    for item in fila_cozinha:
        if item["numero_pedido"] == pedido["numero_pedido"]:
            return fila_cozinha

    # Monta o registro que será enviado para a cozinha
    pedido_cozinha = {
        "numero_pedido": pedido["numero_pedido"],
        "numero_mesa": pedido["numero_mesa"],
        "itens": []
    }

    for item in pedido["itens"]:

        item_cozinha = {
            "codigo_prato": item["codigo_prato"],
            "nome_prato": item["nome_prato"],
            "quantidade": item["quantidade"],
            "observacoes": item["observacoes"]
        }

        pedido_cozinha["itens"].append(item_cozinha)

    # Adiciona o pedido ao final da fila
    fila_cozinha.append(pedido_cozinha)

    return fila_cozinha
