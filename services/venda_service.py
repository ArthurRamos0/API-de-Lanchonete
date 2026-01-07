from utils.file_utils import carregar_json, salvar_json
from datetime import datetime

ARQUIVO_PRODUTOS = "data/produtos.json"
ARQUIVO_VENDAS = "data/vendas.json"


def registrar_venda(produto_id: int, quantidade: int):
    produtos = carregar_json(ARQUIVO_PRODUTOS)
    vendas = carregar_json(ARQUIVO_VENDAS)

    for produto in produtos:
        if produto["id"] == produto_id:
            if quantidade > produto["estoque"]:
                raise ValueError("Estoque insuficiente")

            total = produto["preco"] * quantidade
            produto["estoque"] -= quantidade

            venda = {
                "produto_id": produto_id,
                "produto_nome": produto["nome"],
                "quantidade": quantidade,
                "preco_unitario": produto["preco"],
                "total": total,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }

            vendas.append(venda)

            salvar_json(ARQUIVO_PRODUTOS, produtos)
            salvar_json(ARQUIVO_VENDAS, vendas)

            return venda

    raise ValueError("Produto não encontrado")
