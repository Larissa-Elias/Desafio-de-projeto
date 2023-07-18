menu = """
[1] Depósito
[2] Saque
[0] Extrato
[9] Sair
"""

saldo = 0
limite = 500
extrato = "**"
numero_saque = 0
LIMITE_SAQUE = 3

while  True:


    opcao = input(menu)
    if opcao == "1":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor que foi informado é inválido! Tente novamente!") 


    elif opcao == "2":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação inválida! Você não possui saldo o suficiente!")
        elif excedeu_limite:
            print("Operação inválida! O valor do saque excedeu ao limite estimado!")
        elif excedeu_saques:
            print("Operação inválida! O número máximo de saques foram execultados!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else:
            print("Operação inválida! O valor informado é inválido!")    

    elif opcao == "0":
        print("Extrato")
        print("\n#####EXTRATO#####")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("##################################")

    elif opcao == "9":
        break        

    else:
        print("Informe uma opção válida!")
            

