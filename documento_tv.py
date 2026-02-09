import asyncio
import websockets
import json
import os
import time

TV_IP = "192.168.0.32"   # <-- coloque o IP da sua TV
KEY_FILE = "lg_client_key.txt"

# Conectar à TV via WebSocket
async def conectar():
    uri = f"ws://{TV_IP}:3000/"
    return await websockets.connect(uri)

# Pareamento com manifest e permissões
async def parear(ws):
    print("🔑 Pareando com a TV... Aceite na tela da TV.")

    payload = {
        "id": "register_0",
        "type": "register",
        "payload": {
            "pairingType": "PROMPT",
            "manifest": {
                "permissions": [
                    "CONTROL_INPUT_TEXT",
                    "CONTROL_MOUSE_AND_KEYBOARD",
                    "CONTROL_AUDIO",
                    "CONTROL_POWER"
                ]
            }
        }
    }

    await ws.send(json.dumps(payload))

    while True:
        resposta = json.loads(await ws.recv())
        print("TV:", resposta)
        if "client-key" in resposta.get("payload", {}):
            key = resposta["payload"]["client-key"]
            with open(KEY_FILE, "w") as f:
                f.write(key)
            print("✅ Pareamento concluído!")
            return key

# Registro com a client-key
async def registrar(ws, client_key):
    payload = {
        "id": "register_1",
        "type": "register",
        "payload": {
            "client-key": client_key,
            "manifest": {
                "permissions": [
                    "CONTROL_INPUT_TEXT",
                    "CONTROL_MOUSE_AND_KEYBOARD",
                    "CONTROL_AUDIO",
                    "CONTROL_POWER"
                ]
            }
        }
    }

    await ws.send(json.dumps(payload))
    print("Registro:", await ws.recv())

# Enviar comando usando handleKey
async def enviar_comando(ws, comando):
    payload = {
        "id": f"cmd_{int(time.time() * 1000)}",
        "type": "request",
        "uri": "ssap://com.webos.service.command/handleKey",
        "payload": {"key": comando}
    }

    await ws.send(json.dumps(payload))
    resposta = await ws.recv()
    print("Resposta comando:", resposta)

# Loop principal
async def main():
    ws = await conectar()

    if not os.path.exists(KEY_FILE):
        client_key = await parear(ws)
    else:
        with open(KEY_FILE) as f:
            client_key = f.read().strip()

    await registrar(ws, client_key)
    print("✅ Conectado com sucesso!")

    mapa = {
        # Direções
        "w": "Up",
        "s": "Down",
        "a": "Left",
        "d": "Right",

        # OK / Voltar
        "e": "Enter",
        "b": "Back",

        # Volume
        "+": "VolumeUp",
        "-": "VolumeDown",
        "m": "Mute",

        # Canal
        "c+": "ChannelUp",
        "c-": "ChannelDown",

        # Home / Menu
        "h": "Home",
        "x": "Exit",

        # Player
        "p": "Play",
        "o": "Pause",
        "f": "FastForward",
        "r": "Rewind",
        "n": "Stop",

        # Energia
        "power": "Power"
    }

    print("\n🎮 Controle pronto!")
    print("Digite q para sair\n")

    while True:
        cmd = input(">> ").lower()

        if cmd == "q":
            print("👋 Saindo...")
            break

        if cmd in mapa:
            await enviar_comando(ws, mapa[cmd])
        else:
            print("❌ Comando não encontrado")

asyncio.run(main())
