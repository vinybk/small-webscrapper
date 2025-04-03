# 🌍 Webscraper de Indicadores Econômicos por País

Este projeto coleta automaticamente indicadores econômicos de países a partir do site [Trading Economics](https://pt.tradingeconomics.com/matrix), e organiza os dados em arquivos JSON separados por indicador e grupo de países (Mundo e G20).

## ✅ Funcionalidades

- Coleta automática dos dados de:
  - PIB
  - Crescimento do PIB
  - Taxa de Juros
  - Inflação
  - Desemprego
  - Dívida Pública (% do PIB)
- Agrupamento por:
  - **Mundo** (todos os países disponíveis)
  - **G20** (20 maiores economias)
- Ordenação automática:
  - De acordo com a lógica econômica (ex: menor inflação = melhor)
- Geração de arquivos JSON separados por grupo e indicador

---

## 📦 Requisitos

- Python 3.8 ou superior
- Firefox instalado no sistema

### Instale os pacotes necessários:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

---

## 🚀 Como usar

### 1. Execute o scraper (coleta os dados da internet):

```bash
python 1-webscrapper.py
```

Isso irá gerar o arquivo `dados_economicos.json`.

### 2. Execute o filtro (organiza os dados por grupo):

```bash
python 2-filtrar.py
```

Isso irá gerar a pasta `resultados_json/` com todos os arquivos organizados.

---

## 📁 Estrutura do Projeto

```
webscrapper_paises/
├── 1-webscrapper.py           # Scraper principal
├── 2-filtrar.py               # Separador e organizador de arquivos
├── dados_economicos.json      # Arquivo bruto com todos os países
├── resultados_json/           # Arquivos finais por grupo e indicador
└── README.md                  # Este arquivo
```

---

## 🌐 G20 - Países considerados

- Alemanha, Arábia Saudita, Argentina, Austrália, Brasil, Canadá, China, Coreia do Sul, Estados Unidos, França, Índia, Indonésia, Itália, Japão, México, Reino Unido, Rússia, Turquia, África do Sul, União Europeia

---

## 📄 Licença

Este projeto é open-source e você pode usá-lo livremente. 🌱
