import sys
import json

CAMINHO = "dados.json"

# valida argumentos
if len(sys.argv) != 3:
    print(json.dumps({"erro": "uso incorreto"}))
    sys.exit(3)

cpf = sys.argv[1]
senha = sys.argv[2]

# carrega dados
with open(CAMINHO, "r", encoding="utf-8") as f:
    dados = json.load(f)

# garante estrutura
if "cpf" not in dados:
    dados["cpf"] = {}

# verifica se já existe
if cpf in dados["cpf"] and senha == dados["cpf"][cpf]["senha"]:
    sys.exit(1)
else:
    sys.exit(2)

