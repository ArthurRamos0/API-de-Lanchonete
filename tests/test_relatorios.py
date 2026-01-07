import json
from services.relatorio_service import faturamento_total, vendas_por_produto

ARQUIVO_VENDAS = "data/vendas.json"


def setup_function():
    vendas_mock = [
        {
            "produto_id": 1,
            "produto_nome": "Coxinha",
            "quantidade": 2,
            "preco_unitario": 5.0,
            "total": 10.0,
            "data": "01/01/2025 10:00"
        },
        {
            "produto_id": 2,
            "produto_nome": "Pastel",
            "quantidade": 1,
            "preco_unitario": 7.0,
            "total": 7.0,
            "data": "01/01/2025 11:00"
        },
        {
            "produto_id": 1,
            "produto_nome": "Coxinha",
            "quantidade": 3,
            "preco_unitario": 5.0,
            "total": 15.0,
            "data": "01/01/2025 12:00"
        }
    ]

    with open(ARQUIVO_VENDAS, "w", encoding="utf-8") as f:
        json.dump(vendas_mock, f, indent=4)


def test_faturamento_total():
    total = faturamento_total()
    assert total == 32.0


def test_vendas_por_produto():
    relatorio = vendas_por_produto()

    assert relatorio["Coxinha"] == 5
    assert relatorio["Pastel"] == 1
