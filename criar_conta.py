import sys
import json

CAMINHO = "dados.json"

# valida argumentos
if len(sys.argv) != 6:
    print(json.dumps({"erro": "uso incorreto"}))
    sys.exit(1)

cpf = sys.argv[1]
senha = sys.argv[2]
nome = sys.argv[3]
tel = sys.argv[4]
gmail = sys.argv[5]
# carrega dados
with open(CAMINHO, "r", encoding="utf-8") as f:
    dados = json.load(f)

# garante estrutura
if "cpf" not in dados:
    dados["cpf"] = {}

# verifica se já existe
if cpf in dados["cpf"]:
    print(json.dumps({"status": "cpf_ja_existe"}))
    sys.exit(0)
# cria conta
dados["cpf"][cpf] = {
    "nome": nome,
    "senha": senha,
    "tel": tel,
    "gmail": gmail,
    "saldo": 0.0,
    "investimentos": {},
    "poupanca": "",
    "transferencias": {}
}

# salva arquivo
with open(CAMINHO, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print(json.dumps({"status": "conta_criada"}))

