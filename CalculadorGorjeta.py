# Função principal que calcula a gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    
    # Calcula o valor da gorjeta com base no valor da conta e na porcentagem desejada.
    #
    # Parâmetros:
    # valor_conta (float): valor total da conta
    # porcentagem_gorjeta (float): porcentagem da gorjeta (ex: 10 para 10%)
    #
    # Retorna:
    # float: valor da gorjeta
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Função auxiliar para imprimir o resultado formatado
def exibir_resultado(valor_conta, porcentagem_gorjeta):
    gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Para uma conta de R$ {valor_conta:.2f} com {porcentagem_gorjeta}% de gorjeta, você deve deixar R$ {gorjeta:.2f}.")

# Função que simula o fluxo principal do programa
def main():
    # Simulação de entrada dos valores pagos e do percentual desejado como gorjeta
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada: "))

        if valor_conta < 0 or porcentagem_gorjeta < 0:
            print("Os valores não podem ser negativos.")
            return

        exibir_resultado(valor_conta, porcentagem_gorjeta)

    except ValueError:
        print("Erro: você deve digitar números válidos.")

# Executa o programa
if __name__ == "__main__":
    main()
