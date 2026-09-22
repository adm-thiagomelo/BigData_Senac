import pandas as pd

import mysql.connector

conexao = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "meu_ecommerce",
)

cursor = conexao.cursor()

query = "SELECT * FROM produtos"

cursor.execute(query)

resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

cursor.close()
conexao.close()
