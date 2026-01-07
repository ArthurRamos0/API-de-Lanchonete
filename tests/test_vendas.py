import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.venda_service import registrar_venda


def test_registrar_venda_com_sucesso(tmp_path):
    produtos_file = tmp_path / "produtos.json"
    vendas_file = tmp_path / "vendas.json"

    produtos_file.write_text("""
    [
        {"id": 1, "nome": "Hambúrguer", "preco": 15.0, "estoque": 10}
    ]
    """, encoding="utf-8")

    vendas_file.write_text("[]", encoding="utf-8")

    venda = registrar_venda(
        produto_id=1,
        quantidade=2,
        arquivo_produtos=str(produtos_file),
        arquivo_vendas=str(vendas_file)
    )

    assert venda["produto_id"] == 1
    assert venda["quantidade"] == 2
    assert venda["total"] == 30.0


def test_venda_com_estoque_insuficiente(tmp_path):
    produtos_file = tmp_path / "produtos.json"
    vendas_file = tmp_path / "vendas.json"

    produtos_file.write_text("""
    [
        {"id": 1, "nome": "Suco", "preco": 5.0, "estoque": 1}
    ]
    """, encoding="utf-8")

    vendas_file.write_text("[]", encoding="utf-8")

    try:
        registrar_venda(
            produto_id=1,
            quantidade=5,
            arquivo_produtos=str(produtos_file),
            arquivo_vendas=str(vendas_file)
        )
        assert False  # não deveria chegar aqui
    except ValueError as e:
        assert "Estoque insuficiente" in str(e)
