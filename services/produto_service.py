from utils.file_utils import carregar_json, salvar_json
from utils.input_utils import input_int, input_float

ARQUIVO_PRODUTOS = "data/produtos.json"


def listar_produtos():
    produtos = carregar_json(ARQUIVO_PRODUTOS)
    if not produtos:
        print("⚠️ Nenhum produto cadastrado.")
        return []

    print("\n📦 PRODUTOS CADASTRADOS")
    for p in produtos:
        print(f"{p['id']} - {p['nome']} | R$ {p['preco']:.2f} | Estoque: {p['estoque']}")

    return produtos

def gerar_novo_id(produtos):
    if not produtos:
        return 1
    return max(p["id"] for p in produtos) + 1

def cadastrar_produto(nome, preco, estoque, arquivo):
    produtos = carregar_json(arquivo)

    novo_produto = {
        "id": gerar_novo_id(produtos),
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(novo_produto)
    salvar_json(arquivo, produtos)

    return novo_produto

print("✅ Produto cadastrado com sucesso!")
