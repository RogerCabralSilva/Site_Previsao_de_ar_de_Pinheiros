import sqlite3
from passlib.hash  import bcrypt

def cadastrar_usuario(nome, email, senha):
  conn = sqlite3.connect("usuarios.db")
  cursor = conn.cursor()

  try:
      senha_hash = bcrypt.hash(senha)
      cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                     (nome, email, senha_hash))
      conn.commit()
      print(f"usuario{nome} cadastrado com sucesso!")
  except sqlite3.IntegrityError:
     print("erro: E-Mail já cadastrado.")
  finally:
     conn.close()

def login_usuarios(email, senha):
   conn = sqlite3.connect('usuarios.db')
   cursor = conn.cursor()

   cursor.execute("SELECT nome, senha FROM usuarios WHERE email = ?", (email,))
   resultado = cursor.fetchone()

   conn.close()

   if resultado:
      nome_armazenado, senha_armazenada = resultado
      if bcrypt.verify(senha, senha_armazenada):
         print(f"Login realizado com sucesso! Bem-vindo, {nome_armazenado}")
      else:
         print("Senha incorreta.")
   else:
      print("usuário não encontrado.")