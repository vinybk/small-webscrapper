from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.firefox import GeckoDriverManager
import time
import json

# Configura Firefox headless
print("🦊 Configurando Firefox (modo headless)...")
options = Options()
options.headless = True

# Inicia Firefox via GeckoDriverManager
print("🚀 Iniciando o Firefox...")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Acessa o site
url = "https://pt.tradingeconomics.com/matrix"
print(f"🌐 Acessando: {url}")
driver.get(url)

# Aguarda a página carregar
print("⏳ Aguardando 10 segundos para carregamento da tabela...")
time.sleep(10)

# Extrai o HTML
html = driver.page_source
driver.quit()
print("✅ HTML extraído e navegador fechado.")

# Processa com BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
tabela = soup.find("table")

if not tabela:
    print("❌ ERRO: Tabela não encontrada.")
    exit()

linhas = tabela.find_all("tr")[1:]
print(f"📊 {len(linhas)} países encontrados.")

# Índices dos indicadores na tabela
indicadores_idx = {
    "PIB": 1,
    "Crescimento do PIB": 2,
    "Taxa de Juros": 3,
    "Inflação": 4,
    "Desemprego": 5,
    "Dívida / PIB": 7
}

# Monta dicionário com os dados
dados = {}

print("🔁 Coletando dados país por país...")
for i, linha in enumerate(linhas):
    colunas = linha.find_all("td")
    if len(colunas) < 8:
        continue
    pais = colunas[0].text.strip()
    dados[pais] = {}
    for nome, idx in indicadores_idx.items():
        valor = colunas[idx].text.strip().replace(",", ".")
        try:
            valor = float(valor)
        except ValueError:
            valor = None
        dados[pais][nome] = valor
    print(f"✅ [{i+1}/{len(linhas)}] {pais} processado.")

# Salva em JSON
with open("dados_economicos.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("\n✅ Arquivo 'dados_economicos.json' gerado com sucesso!")
