from services.produto_service import gerar_novo_id

def test_gerar_novo_id_lista_vazia():
    produtos = []
    assert gerar_novo_id(produtos) == 1

def test_gerar_novo_id_lista_com_dados():
    produtos = [{"id": 1}, {"id": 2}, {"id": 5}]
    assert gerar_novo_id(produtos) == 6
