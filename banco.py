acao = -1
print("""
  [0] SAQUE
  [1] DEPOSITO
  [2] EXTRATO
  [3] SAIR
"""
)


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
 acao =int(input("digite um numero para realizar uma ação "))

 if acao == 0:
   saque = int(input("quanto voce quer sacar "))
   if saque > saldo:
      print("saldo insuficiente \n")
   elif saque>limite:
      print("limite de saque excedido \n ")
   elif numero_saques>=LIMITE_SAQUES:
      print("numero de saques diarios excedido \n")
   else:
      print(f"saque de {saque} R$, concluido com sucesso \n")
      numero_saques += 1
      extrato += f"saque: {saque} reais \n"
      saldo -= saque

   
 elif acao == 1:
    deposito =int(input("quanto voce quer depositar  "))
    if deposito > 0:
       print(f"deposito de  {deposito} R$, concluido com sucesso \n")
       saldo += deposito
       extrato+= f"deposito {deposito} reais\n"
    else:print("valor invalido")
 elif acao == 2:
    print("================================================")
    print(extrato)
    print(f"seu saldo atual é de {saldo} R$ ")
    print("================================================")
 elif acao == 3:
    print("obrigado por utilizar nosso banco")
    break
 else:
    print("operacao invalida \n")

    

