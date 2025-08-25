menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito no valor de R$ {valor:.2f} concluído!")
            
        else:
            print("Falha na operação. Tente novamente!!")

    elif opcao == "2":
        valor = float(input("Informe valor a ser sacado:  "))
        if valor > saldo:
            print("Saldo Insuficiente!")
        elif valor > limite:
            print("Valor não permitido!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Máximo de saques já realizados.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque no valor de R$ {valor:.2f} realizado")
        else:
            print("Operação não concluída, tente novamente")
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema!!")
        break

    else:
        print("Operação inválida, por favor, selecione opção desejada!")

