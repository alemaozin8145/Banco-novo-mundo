import json
import sys

CAMINHO = "dados.json"
CAMINHO2 = "investimentos.json"
VERMELHO = "\033[31m"
RESET = "\033[0m"
if len(sys.argv) !=4:
    print(json.dumps({"erro": "uso incorreto"}))
    sys.exit(0)

cpf = sys.argv[1]
senha = sys.argv[2]
escolha = sys.argv[3]
with open(CAMINHO, "r", encoding="utf-8") as f:
    dados = json.load(f)

with open(CAMINHO2, "r", encoding="utf-8") as f:
    investmentos = json.load(f)
if cpf in dados["cpf"]:
    print()
else:
    print(json.dumps({"status_cpf": "cpf invalido"}))
    sys.exit(1)

if senha == dados["cpf"][cpf]["senha"]:
    print()

if escolha == "-i":
    try:
     print("investimentos: ")
     tamanho_investimentos = len(dados["cpf"][cpf]["investimentos"])
     i_tmn_inv = 1
     for i_2 in range(0,tamanho_investimentos):
         i_2_valido = str(i_tmn_inv)
         print(VERMELHO + dados["cpf"][cpf]["investimentos"][i_2_valido]["nome"] + RESET)
         print(dados["cpf"][cpf]["investimentos"][i_2_valido]["ticker"])
         print(dados["cpf"][cpf]["investimentos"][i_2_valido]["valor_mercado"])
         print(dados["cpf"][cpf]["investimentos"][i_2_valido]["pl"])
         print(dados["cpf"][cpf]["investimentos"][i_2_valido]["p_vp"])
         print(dados["cpf"][cpf]["investimentos"][i_2_valido]["dividend_yield"])
         print(dados["cpf"][cpf]["investimentos"][i_2_valido]["margem_liquida"])
         print(dados["cpf"][cpf]["investimentos"][i_2_valido]["setor"]) 
         i_tmn_inv+=1
    except(KeyError):
        print("Esses sao todos os seus investimentos")
elif escolha == "-ip":
    print("investimentos possiveis: ")
    i_int =1
    for i in range(1,21):
     i = str(i_int)
     print(VERMELHO + i + investmentos[i]["nome"] + RESET)
     print(investmentos[i]["ticker"])
     print(investmentos[i]["valor_mercado"])
     print(investmentos[i]["pl"])
     print(investmentos[i]["p_vp"])
     print(investmentos[i]["dividend_yield"])
     print(investmentos[i]["margem_liquida"])
     print(investmentos[i]["setor"])
     i_int+=1
elif escolha == "-d":
    try:
      print(".............")

      print(json.dumps({"usuario": dados["cpf"][cpf]["nome"]}))     
      print(json.dumps({"saldo": dados["cpf"][cpf]["saldo"]}))
      print(json.dumps({"poupanca": dados["cpf"][cpf]["poupanca"]}))
      print(json.dumps({"Telefone": dados["cpf"][cpf]["tel"]}))
      print(json.dumps({"Gmail": dados["cpf"][cpf]["gmail"]}))
    
      print("investimentos: ")
      tmn_ivesti = len(dados["cpf"][cpf]["investimentos"])
      investeimentos_i = 1
      for i_2_2 in range(0,tmn_ivesti):
          i_2_valido_2 = str(investeimentos_i)
          print(VERMELHO + dados["cpf"][cpf]["investimentos"][i_2_valido_2]["nome"] + RESET)
          print(dados["cpf"][cpf]["investimentos"][i_2_valido_2]["ticker"])
          print(dados["cpf"][cpf]["investimentos"][i_2_valido_2]["valor_mercado"])
          print(dados["cpf"][cpf]["investimentos"][i_2_valido_2]["pl"])
          print(dados["cpf"][cpf]["investimentos"][i_2_valido_2]["p_vp"])
          print(dados["cpf"][cpf]["investimentos"][i_2_valido_2]["dividend_yield"])
          print(dados["cpf"][cpf]["investimentos"][i_2_valido_2]["margem_liquida"])
          print(dados["cpf"][cpf]["investimentos"][i_2_valido_2]["setor"]) 
          investeimentos_i+=1
    except(KeyError):
         print("Esses sao todos os seus investimentos")

sys.exit(2)