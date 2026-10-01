import pandas as pd
import ast
from collections import Counter
import matplotlib.pyplot as plt

fonte = pd.read_csv('steam.csv')

contador = Counter()

for idiomas in fonte['Supported languages']:
    lista = ast.literal_eval(idiomas)

    for idioma in lista:
        idioma = idioma.strip().lower()

        if idioma in ['english', 'portuguese - brazil', 'spanish - spain']:
            contador[idioma] += 1

english = contador['english']
portuguese = contador['portuguese - brazil']
spanish = contador['spanish - spain']

valores = [contador['english'], contador['portuguese - brazil'], contador['spanish - spain']]
idiomas = ['Inglês', 'Português', 'Espanhol']

plt.bar(idiomas, valores, color = ['red', 'orange', 'yellow'])

plt.title('Quantidade de jogos por idioma')
plt.xlabel('Idiomas')
plt.ylabel('Valores')

for i, valor in enumerate(valores):
    plt.text(i, valor, str(valor), ha = 'center', va = 'bottom')

plt.show()
