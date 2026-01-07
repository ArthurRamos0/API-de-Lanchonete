from utils.file_utils import carregar_json

ARQUIVO_VENDAS = "data/vendas.json"


def faturamento_total():
    vendas = carregar_json(ARQUIVO_VENDAS)
    return sum(v["total"] for v in vendas)


def vendas_por_produto():
    vendas = carregar_json(ARQUIVO_VENDAS)
    relatorio = {}

    for v in vendas:
        nome = v["produto_nome"]
        relatorio[nome] = relatorio.get(nome, 0) + v["quantidade"]

    return relatorio
