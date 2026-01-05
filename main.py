import json
import os

ARQUIVO_PRODUTOS = "data/produtos.json"


def carregar_produtos():
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return []

    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)


produtos = carregar_produtos()


def gerar_novo_id():
    if not produtos:
        return 1
    return max(p["id"] for p in produtos) + 1


def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    estoque = int(input("Quantidade em estoque: "))

    produto = {
        "id": gerar_novo_id(),
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)
    salvar_produtos(produtos)

    print("✅ Produto cadastrado e salvo com sucesso!")


def listar_produtos():
    if not produtos:
        print("⚠️ Nenhum produto cadastrado.")
        return

    print("\n📦 PRODUTOS CADASTRADOS")
    for p in produtos:
        print(f"{p['id']} - {p['nome']} | R$ {p['preco']:.2f} | Estoque: {p['estoque']}")


def registrar_venda():
    listar_produtos()

    try:
        produto_id = int(input("\nID do produto: "))
        quantidade = int(input("Quantidade: "))

        for produto in produtos:
            if produto["id"] == produto_id:
                if produto["estoque"] >= quantidade:
                    total = produto["preco"] * quantidade
                    produto["estoque"] -= quantidade
                    salvar_produtos(produtos)
                    print(f"🧾 Venda realizada! Total: R$ {total:.2f}")
                else:
                    print("❌ Estoque insuficiente.")
                return

        print("❌ Produto não encontrado.")

    except ValueError:
        print("❌ Entrada inválida.")


def menu():
    while True:
        print("""
🛒 SISTEMA PDV
1️⃣ Cadastrar produto
2️⃣ Listar produtos
3️⃣ Registrar venda
4️⃣ Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            registrar_venda()
        elif opcao == "4":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida.")


menu()
