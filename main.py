import json
import os

ARQUIVO_PRODUTOS = "data/produtos.json"

# ========================
# FUNÇÕES DE VALIDAÇÃO
# ========================

def input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("❌ Valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("❌ Digite um número válido.")

def input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("❌ Valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("❌ Digite um valor numérico válido.")

# ========================
# PERSISTÊNCIA
# ========================

def carregar_produtos():
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return []

    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

produtos = carregar_produtos()

# ========================
# REGRAS DE NEGÓCIO
# ========================

def gerar_novo_id():
    if not produtos:
        return 1
    return max(p["id"] for p in produtos) + 1

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("❌ Nome não pode ser vazio.")
        return

    preco = input_float("Preço: R$ ")
    estoque = input_int("Quantidade em estoque: ")

    produto = {
        "id": gerar_novo_id(),
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)
    salvar_produtos(produtos)

    print("✅ Produto cadastrado com sucesso!")

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
        quantidade = input_int("Quantidade para vender: ")

        for produto in produtos:
            if produto["id"] == produto_id:
                if quantidade > produto["estoque"]:
                    print("❌ Estoque insuficiente.")
                    return

                total = produto["preco"] * quantidade
                produto["estoque"] -= quantidade
                salvar_produtos(produtos)

                print(f"🧾 Venda realizada! Total: R$ {total:.2f}")
                return

        print("❌ Produto não encontrado.")

    except ValueError:
        print("❌ Entrada inválida.")

# ========================
# MENU
# ========================

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
