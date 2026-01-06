from datetime import datetime
import csv
from utils.file_utils import carregar_json, salvar_json
from services.produto_service import listar_produtos

ARQUIVO_VENDAS = "data/vendas.json"


def registrar_venda(produto_id, quantidade, arquivo_produtos, arquivo_vendas):
    produtos = carregar_json(arquivo_produtos)
    vendas = carregar_json(arquivo_vendas)

    for produto in produtos:
        if produto["id"] == produto_id:
            if quantidade > produto["estoque"]:
                raise ValueError("Estoque insuficiente")

            produto["estoque"] -= quantidade
            total = produto["preco"] * quantidade

            venda = {
                "produto_id": produto["id"],
                "produto_nome": produto["nome"],
                "quantidade": quantidade,
                "preco_unitario": produto["preco"],
                "total": total,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }

            vendas.append(venda)
            salvar_json(arquivo_produtos, produtos)
            salvar_json(arquivo_vendas, vendas)

            return venda

    raise ValueError("Produto não encontrado")