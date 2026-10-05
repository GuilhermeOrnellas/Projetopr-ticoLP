# 🌲 Dashboard Ambiental: Desmatamento e Preservação no Brasil

* **Disciplina:** LINGUAGENS DE PROGRAMAÇÃO
* **Professor:** Alexandre Neves Lousada
* **Aluno:** Guilherme Arnellas Chagas

Projeto desenvolvido para a disciplina de Linguagem de Programação / Análise de Dados, com o objetivo de analisar espacial e temporalmente os dados de desmatamento, queimadas e emissões de CO₂ nos biomas brasileiros.

---

## 🔗 Links de Acesso ao Projeto

* **Dashboard Interativo (Streamlit Cloud):** [Aceder ao Dashboard](https://projetopr-ticolp-2y9eerb72fyavjxuul8gsl.streamlit.app/)
* **Página de Apresentação (GitHub Pages):** [Aceder ao Site Estático](https://guilhermeornellas.github.io/Projetopr-ticoLP/)
* **Notebook de Análise Exploratória:** [Ver Notebook no GitHub](https://github.com/GuilhermeOrnellas/Projetopr-ticoLP/blob/main/projeto-desmatamento/notebooks/analise_desmatamento.ipynb)
* **Repositório do Código-Fonte:** [Ver Repositório no GitHub](https://github.com/GuilhermeOrnellas/Projetopr-ticoLP)

---

## 📊 Principais Indicadores (KPIs) Analisados

O painel interativo monitora em tempo real métricas cruciais para a tomada de decisão ambiental:
* **Área Desmatada Total (km²):** Monitoramento acumulado e histórico da supressão vegetal.
* **Focos de Queimada:** Contagem de ocorrências e concentração temporal/geográfica.
* **Emissões de CO₂ (ton):** Estimativa do impacto ambiental das áreas afetadas.
* **Coeficiente de Correlação de Pearson:** Análise estatística avançada comprovando a relação direta entre o desmatamento e o aumento de queimadas.

---

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem principal)
* **Streamlit** (Construção do dashboard web)
* **Pandas & NumPy** (Manipulação e computação de dados)
* **Plotly** (Gráficos interativos e mapas de calor)
* **Jupyter Notebook** (Análise exploratória de dados)
* **Git & GitHub** (Controle de versão e hospedagem)

---

## 📂 Estrutura do Repositório

```text
Projetopr-ticoLP/
│
├── projeto-desmatamento/
│   ├── dados/
│   │   └── simulacao_desmatamento_Brasil.csv
│   ├── notebooks/
│   │   └── analise_desmatamento.ipynb
│   ├── app.py
│   └── requirements.txt
│
├── index.html
└── README.md

## Como executar o projeto localmente 
1. Instale as dependências: `pip install -r requirements.txt` 
2. Execute o dashboard: `python -m streamlit run app.py` 

## Funcionalidades Avançadas Implementadas 
* Dashboard Multipágina (Streamlit) 
* Correlação Estatística (Pandas/NumPy e Regressão OLS)