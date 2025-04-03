import json
import os
import re

# Carrega os dados do arquivo anterior
with open("dados_economicos.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Define os países do G20
G20 = {
    "Alemanha", "Arábia Saudita", "Argentina", "Austrália", "Brasil",
    "Canadá", "China", "Coreia do Sul", "Estados Unidos", "França",
    "Índia", "Indonésia", "Itália", "Japão", "México",
    "Reino Unido", "Rússia", "Turquia", "África do Sul", "União Europeia"
}

# Configurações por indicador
indicadores = {
    "Crescimento do PIB": {"ordem": "desc"},
    "PIB": {"ordem": "desc"},
    "Taxa de Juros": {"ordem": "asc"},
    "Inflação": {"ordem": "asc"},
    "Desemprego": {"ordem": "asc"},
    "Dívida / PIB": {"ordem": "asc"},
}

# Cria pasta de saída
os.makedirs("resultados_json", exist_ok=True)

for indicador, config in indicadores.items():
    mundo = []
    g20 = []

    # Agrupa os dados
    for pais, dados_pais in dados.items():
        valor = dados_pais.get(indicador)
        if valor is None:
            continue
        mundo.append((pais, valor))
        if pais in G20:
            g20.append((pais, valor))

    # Ordena os dados
    reverse = config["ordem"] == "desc"
    mundo.sort(key=lambda x: x[1], reverse=reverse)
    g20.sort(key=lambda x: x[1], reverse=reverse)

    # Salva arquivos
    def salvar(nome, grupo):
        nome_arquivo = re.sub(r"[^a-zA-Z0-9_áéíóúàèìòùãõç]", "_", nome.lower())
        caminho = f"resultados_json/{nome_arquivo}_{grupo}.json"
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(
                [{"país": p, "valor": v} for p, v in (mundo if grupo == "mundo" else g20)],
                f, ensure_ascii=False, indent=4
            )
        print(f"✅ Arquivo salvo: {caminho}")

    salvar(indicador, "mundo")
    salvar(indicador, "g20")

print("\n🏁 Todos os arquivos foram gerados na pasta 'resultados_json'")
