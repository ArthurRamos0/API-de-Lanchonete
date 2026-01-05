produtos = []
contador_id = 1


def cadastrar_produto():
    global contador_id

    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    estoque = int(input("Quantidade em estoque: "))

    produto = {
        "id": contador_id,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)
    contador_id += 1

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
        quantidade = int(input("Quantidade: "))

        for produto in produtos:
            if produto["id"] == produto_id:
                if produto["estoque"] >= quantidade:
                    total = produto["preco"] * quantidade
                    produto["estoque"] -= quantidade
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
