from services.produto_service import cadastrar_produto, listar_produtos
from services.venda_service import (
    registrar_venda,
    exportar_vendas_csv,
    listar_vendas
)

def menu():
    while True:
        print("""
🛒 SISTEMA PDV
1️⃣ Cadastrar produto
2️⃣ Listar produtos
3️⃣ Registrar venda
4️⃣ Ver relatório de vendas
5️⃣ Exportar vendas (CSV)
6️⃣ Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            registrar_venda()
        elif opcao == "4":
            listar_vendas()
        elif opcao == "5":
            exportar_vendas_csv()
        elif opcao == "6":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.")