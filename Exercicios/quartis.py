import numpy as np
import matplotlib.pyplot
import pandas

dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])

q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75)

print(f'Primeiro: {q1}; Segundo {q2}; Terceiro {q3}')

