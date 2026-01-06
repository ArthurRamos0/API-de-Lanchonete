from services.produto_service import gerar_novo_id, cadastrar_produto


def test_gerar_novo_id_lista_vazia():
    produtos = []
    assert gerar_novo_id(produtos) == 1


def test_gerar_novo_id_com_produtos():
    produtos = [{"id": 1}, {"id": 2}, {"id": 3}]
    assert gerar_novo_id(produtos) == 4


def test_cadastrar_produto_com_dados_validos(tmp_path):
    arquivo = tmp_path / "produtos.json"
    arquivo.write_text("[]", encoding="utf-8")

    produto = cadastrar_produto(
        nome="Coxinha",
        preco=6.5,
        estoque=10,
        arquivo=str(arquivo)
    )

    assert produto["id"] == 1
    assert produto["nome"] == "Coxinha"
    assert produto["preco"] == 6.5
    assert produto["estoque"] == 10
