import sys
import json

if len(sys.argv) !=3:
    print(json.dumps({"erro": "uso incorreto"}))
    sys.exit(0)

CAMINHO = "dados.json"

cpf = sys.argv[1]
senha = sys.argv[2]

with open(CAMINHO, "r", encoding="utf-8") as f_1:
    dados = json.load(f_1)



if cpf not in dados["cpf"]:
    print("Cpf nao encontrado")
    sys.exit(0)

if not senha == dados["cpf"][cpf]["senha"]:
   print("Senha incorreta")
   sys.exit(1) 
tamanho = len(dados["cpf"][cpf]["transferencias"])
i = 1
try: 
 for i in range(1,tamanho):
    i_valido = str(i)
    print(dados["cpf"][cpf]["transferencias"][i_valido])
    i+1
except(KeyError):
   print("")

sys.exit(2)
