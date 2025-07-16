import sqlite3

# Conectar ao banco de dados 
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Cria a tabela
cursor.execute('''
  CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL,
               senha TEXT NOT NULL
              )
''')

conn.commit()
conn.close()