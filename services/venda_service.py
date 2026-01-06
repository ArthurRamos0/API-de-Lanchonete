from datetime import datetime
import csv
from utils.file_utils import carregar_json, salvar_json
from services.produto_service import listar_produtos

ARQUIVO_VENDAS = "data/vendas.json"


def registrar_venda():
    produtos = listar_produtos()
    if not produtos:
        return

    try:
        produto_id = int(input("\nID do produto: "))
        quantidade = int(input("Quantidade: "))

        for p in produtos:
            if p["id"] == produto_id:
                if quantidade > p["estoque"]:
                    print("❌ Estoque insuficiente.")
                    return

                p["estoque"] -= quantidade
                salvar_json("data/produtos.json", produtos)

                vendas = carregar_json(ARQUIVO_VENDAS)
                total = p["preco"] * quantidade

                vendas.append({
                    "produto_id": p["id"],
                    "produto_nome": p["nome"],
                    "quantidade": quantidade,
                    "preco_unitario": p["preco"],
                    "total": total,
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                })

                salvar_json(ARQUIVO_VENDAS, vendas)

                print(f"🧾 Venda registrada! Total: R$ {total:.2f}")
                return

        print("❌ Produto não encontrado.")

    except ValueError:
        print("❌ Entrada inválida.")


def exportar_vendas_csv():
    vendas = carregar_json(ARQUIVO_VENDAS)
    if not vendas:
        print("⚠️ Nenhuma venda registrada.")
        return

    with open("data/relatorio_vendas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Data", "Produto", "Quantidade", "Preço Unitário", "Total"])

        for v in vendas:
            writer.writerow([
                v["data"],
                v["produto_nome"],
                v["quantidade"],
                f"{v['preco_unitario']:.2f}",
                f"{v['total']:.2f}"
            ])

    print("✅ Relatório exportado com sucesso!")

def listar_vendas():
    vendas = carregar_json(ARQUIVO_VENDAS)

    if not vendas:
        print("⚠️ Nenhuma venda registrada.")
        return

    print("\n📊 RELATÓRIO DE VENDAS")
    for v in vendas:
        print(
            f"{v['data']} | {v['produto_nome']} | "
            f"Qtd: {v['quantidade']} | Total: R$ {v['total']:.2f}"
        )