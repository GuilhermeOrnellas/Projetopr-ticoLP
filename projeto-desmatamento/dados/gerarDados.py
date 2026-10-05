import pandas as pd
import numpy as np
import random
from datetime import date, timedelta

np.random.seed(42)
dias = [date(2015, 1, 1) + timedelta(days=x) for x in range(0, 3650, 30)]
estados_biomas = {
    'Norte': [('AM', 'Amazônia'), ('PA', 'Amazônia')],
    'Centro-Oeste': [('MT', 'Cerrado'), ('GO', 'Cerrado')],
    'Nordeste': [('BA', 'Caatinga'), ('MA', 'Cerrado')],
    'Sudeste': [('SP', 'Mata Atlântica'), ('MG', 'Cerrado')]
}

dados = []
for d in dias:
    for regiao, ufs in estados_biomas.items():
        for uf, bioma in ufs:
            desmatada = np.random.uniform(10, 500)
            queimadas = int(desmatada * np.random.uniform(0.5, 2.5))
            dados.append({
                'ano': d.year,
                'mes': d.month,
                'data': d,
                'regiao': regiao,
                'uf': uf,
                'bioma': bioma,
                'area_desmatada_km2': desmatada,
                'area_preservada_km2': np.random.uniform(1000, 5000),
                'focos_queimada': queimadas,
                'chuva_mm': np.random.uniform(0, 300),
                'temperatura_media': np.random.uniform(22, 35),
                'emissoes_co2': desmatada * 1.5,
                'unidades_conservacao': random.randint(5, 50),
                'nivel_risco': random.choice(['Baixo', 'Médio', 'Alto', 'Crítico'])
            })

df = pd.DataFrame(dados)
df.to_csv('dados/simulacao_desmatamento_brasil.csv', index=False)
print("Arquivo simulacao_desmatamento_brasil.csv criado com sucesso na pasta dados/")