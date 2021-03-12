from apyori import apriori
import pandas as pd

MAX_RULES = 8

data = pd.read_csv('mercado_2.csv', header=None)

transactions = []

for t in data.values:
    transactions.append([str(item) for item in t])

regras = list(apriori(transactions, min_support=0.003, min_confidence=0.4, min_lift=4.5, min_length=2))

temp_results = [list(x) for x in regras]
formResult = []

for indice in range(0, MAX_RULES):
    formResult.append([list(x) for x in temp_results[indice][2]])

for fr in formResult:
    print(fr)
