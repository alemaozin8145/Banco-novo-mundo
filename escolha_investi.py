import json
import sys


CAMINHO = "dados.json"
CAMINHO2 = "investimentos.json"

if len(sys.argv) !=4:
    print(json.dumps({"erro": "uso incorreto"}))
    sys.exit(0)

cpf = sys.argv[1]
escolha = sys.argv[2]
numero = sys.argv[3]
with open(CAMINHO, "r", encoding="utf-8") as f:
    dados = json.load(f)

with open(CAMINHO2, "r", encoding="utf-8") as f2:
    investimentos = json.load(f2)

if cpf not in dados["cpf"]:
    print("Cpf invalido")
    sys.exit(1)

numero_valido = int(numero)
if numero_valido>=1 and numero_valido<=20:
   print("carregando dados...")
   tamanho = len(dados["cpf"][cpf]["investimentos"])
   tamanho_valido = tamanho+1
   i=1
   for i in range(1,tamanho):
      try:
       i_valido = str(i)
       if investimentos[numero]["nome"] in dados["cpf"][cpf]["investimentos"][i_valido]["nome"]:
          print("Esse investimento ja esta registrado")
          sys.exit(2)
       i+1
      except(KeyError):
         print("ok")

   dados["cpf"][cpf]["investimentos"][tamanho_valido] = {
       "ticker": investimentos[numero]["ticker"],
       "nome": investimentos[numero]["nome"],
       "valor_mercado": investimentos[numero]["valor_mercado"],
       "pl": investimentos[numero]["pl"],
       "p_vp": investimentos[numero]["p_vp"],
       "dividend_yield": investimentos[numero]["dividend_yield"],
       "margem_liquida": investimentos[numero]["margem_liquida"],
       "setor": investimentos[numero]["setor"]
   }
   with open(CAMINHO, "w", encoding="utf-8") as f3:
    json.dump(dados, f3, indent=4, ensure_ascii=False)
   print(investimentos[numero]["nome"] + " adicionado a os seus investimentos")
   sys.exit(3)
else:
    print("Erro inesperado")
    sys.exit(4)
