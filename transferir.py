import json
import sys

CAMINHO = "dados.json"
CAMINHO2 = "investimentos.json"
VERMELHO = "\033[31m"
RESET = "\033[0m"
if len(sys.argv) !=5:
    print(json.dumps({"erro": "uso incorreto"}))
    sys.exit(0)

cpf = sys.argv[1]
senha = sys.argv[2]
cpf_pagamento = sys.argv[3]
valor = sys.argv[4]
valor_valido = float(valor)
with open(CAMINHO, "r", encoding="utf-8") as f_1:
    dados = json.load(f_1)

with open(CAMINHO2, "r", encoding="utf-8") as f_2:
    investmentos = json.load(f_2)

if cpf not in dados["cpf"]:
    print("Esse cpf nao e valido")
    sys.exit(0)

if cpf_pagamento not in dados["cpf"]:
    print("O cpf informado nao e valido")
    sys.exit(1)

if dados["cpf"][cpf]["saldo"] >= valor_valido:
    if senha == dados["cpf"][cpf]["senha"]:
     if cpf == cpf_pagamento:
        print("Voce nao pode transferir para si mesmo")
        sys.exit(6)
     else:
       try:
         dados["cpf"][cpf]["saldo"] -= valor_valido
         dados["cpf"][cpf_pagamento]["saldo"] += valor_valido
 
         transfer = len(dados["cpf"][cpf]["transferencias"])
         transfer_2 = len(dados["cpf"][cpf]["transferencias"])
         transfer_valido =1
         transfer_valido_2 =1
         transfer_valido +=transfer
         transfer_valido_2 += transfer_2
         dados["cpf"][cpf]["transferencias"][transfer_valido] = {
            "transferencia_paga": cpf_pagamento,
            "valor": valor
         }
         dados["cpf"][cpf_pagamento]["transferencias"][transfer_valido_2] = {
            "transferencia_recebido": cpf_pagamento,
            "valor": valor
         }
        
         with open(CAMINHO, "w", encoding="utf-8") as f3:
          json.dump(dados, f3, indent=4, ensure_ascii=False)
        
         print("Valor pago: " + valor)
         valor_print = str(valor_valido)
         print(dados["cpf"][cpf]["transferencias"][valor_print]["transferencia_paga"])
         print(dados["cpf"][cpf]["transferencias"][valor_print]["valor"])
      
         sys.exit(3)
       except(ValueError):
          print("ok")
    
    else:
       print("Senha incorreta")
       sys.exit(4)
else:
   print("valor insuficiente")
   sys.exit(5)

