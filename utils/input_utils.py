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
