from hashlib import sha256
from data.conexao import Conexao


class User:
    def cadastrar_usuario(login,name,password):

        #Criptografando a senha
        senha = sha256(password.encode()).hexdigest()

        #Cadastrando as infos no banco de dados
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)

        sql = "INSERT INTO tb_usuarios(login,nome,senha) VALUES(%s,%s,%s);"
        valores=(login,name,password)

        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def logar_usuario(login,password):

        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)
        sql ="SELECT login,senha,nome FROM tb_usuarios WHERE login=%s AND senha=%s"
        valores = (login,password)
        cursor.execute(sql,valores)
        resultado = cursor.fetchone()

        if resultado:
            
            return True
        else:
            return False