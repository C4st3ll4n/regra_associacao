import pandas as pd
from apyori import apriori

MAX_RULES = 8

data = pd.read_csv('mercado.csv', header=None)

transacoes = []

for t in data.values:
    transacoes.append([str(item) for item in t])


regras = list(apriori(transacoes, min_support=0.032, min_confidence=0.2, min_lift=1.5, min_length=2))

temp_results = [list(x) for x in regras]
total_rules = (len(temp_results))

formResult = []

for indice in range(0, total_rules):
    formResult.append([list(x) for x in temp_results[indice][2]])

for fr in formResult:
    print(fr)
