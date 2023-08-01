import mysql.connector as mysql
import threading
import datetime

class Banco:
    """
    Classe que representa o banco de dados do aplicativo.

    ...

    Attributes
    ----------
    conexao : mysql.connector.connection.MySQLConnection
        A conexão com o banco de dados.
    cursor : mysql.connector.cursor.MySQLCursor
        O cursor para executar comandos SQL no banco de dados.
    lock : (threading.Lock)
        Um objeto de bloqueio para garantir a exclusão mútua ao acessar o banco de dados.
    """
    def __init__(self) -> None:
        """
        Classe responsável por realizar operações de banco de dados usando MySQL.

        ...
        
        Attributes:
            lock (threading.Lock): Um objeto de bloqueio para garantir a exclusão mútua ao acessar o banco de dados.
            conexao (mysql.connector.connection.MySQLConnection): Objeto de conexão com o banco de dados.
            cursor (mysql.connector.cursor.MySQLCursor): Cursor usado para executar consultas e comandos SQL.
        """
        self.lock = threading.Lock()
        self.conexao = mysql.connect(host='localhost', db='cadastro', user='root', passwd='Lhamas123!')
        self.cursor = self.conexao.cursor()

        # Cria a tabela "cadastrar" se ela não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cadastrar (
                            id INTEGER PRIMARY KEY AUTO_INCREMENT,
                            nome TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            email VARCHAR(50) NOT NULL,
                            nascimento TEXT NOT NULL,
                            cpf VARCHAR(11) NOT NULL,
                            senha TEXT NOT NULL
                        );''')
        # Cria a tabela "cadastro_adm" se ela não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro_adm (
                        id TEXT NOT NULL,
                        cargo TEXT NOT NULL,
                        departamento TEXT NOT NULL,
                        salario TEXT NOT NULL,
                        dataadmissão TEXT NOT NULL,
                        relatoriopagamento TEXT NOT NULL,
                        registrofaltas TEXT NOT NULL,
                        relatoriomensal TEXT NOT NULL,
                        licenças TEXT NOT NULL,
                        avaliacoesprojetos TEXT NOT NULL,
                        beneficios TEXT NOT NULL
                    );''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS historico_atualizacoes_adm (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        id_usuario INT NOT NULL,
                        relatoriopagamentos VARCHAR(255),
                        relatoriomensais VARCHAR(255),
                        avaliacoesprojetoss VARCHAR(255),
                        data_atualizacao DATETIME
                    );''')

    def cadastrarusuario(self, email, nome, endereco, cpf, nascimento, senha):
        """
        Cadastra um usuário no banco de dados.

        Parameters:
            email (str): Email do usuário.
            nome (str): Nome do usuário.
            endereco (str): Endereço do usuário.
            cpf (str): CPF do usuário.
            nascimento (str): Data de nascimento do usuário.
            senha (str): Senha do usuário.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        self.cursor.execute('SELECT * FROM cadastrar WHERE email = %s', (email,))
        resultado = self.cursor.fetchone()
        if resultado is None:
            self.cursor.execute('INSERT INTO cadastrar(email, nome, endereco, cpf, nascimento, senha) VALUES (%s, %s, %s, %s, %s, %s)',
                            (email, nome, endereco, cpf, nascimento, senha))
            self.conexao.commit()
            return True
        return False

    def entrar(self, email, senha):
        """
        Verifica as credenciais de um usuário para fazer login.

        Parameters:
            email (str): Email do usuário.
            senha (str): Senha do usuário.

        Returns:
            tuple: Dados do usuário se o login for bem-sucedido, None caso contrário.
        """
        self.cursor.execute('SELECT * FROM cadastrar WHERE email=%s AND senha=%s', (email, senha))
        resultado = self.cursor.fetchone()
        if resultado is not None:
            return resultado
        return None
    
    def cadastraradm(self, id, cargo, departamento, salario, dataadmissao, relatoriopagamento, registrofaltas, relatoriomensal, licencas, avaliacoesprojetos, beneficios):
        """
        Cadastra um administrador no banco de dados.

        Parameters:
            id (str): ID do administrador.
            cargo (str): Cargo do administrador.
            departamento (str): Departamento do administrador.
            salario (str): Salário do administrador.
            dataadmissao (str): Data de admissão do administrador.
            relatoriopagamento (str): Relatório de pagamento do administrador.
            registrofaltas (str): Registro de faltas do administrador.
            relatoriomensal (str): Relatório mensal do administrador.
            licencas (str): Licenças do administrador.
            avaliacoesprojetos (str): Avaliações de projetos do administrador.
            beneficios (str): Benefícios do administrador.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        self.lock.acquire()
        try:
            self.cursor.execute('SELECT cargo FROM cadastro_adm WHERE id=%s', (id,))
            resultado = self.cursor.fetchone()
            if resultado is None:
                self.cursor.fetchall()

                self.cursor.execute('INSERT INTO cadastro_adm(id, cargo, departamento, salario, dataadmissão, relatoriopagamento, registrofaltas, relatoriomensal, licenças, avaliacoesprojetos, beneficios) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                    (id, cargo, departamento, salario, dataadmissao, relatoriopagamento, registrofaltas, relatoriomensal, licencas, avaliacoesprojetos, beneficios))
                self.conexao.commit()
                return True
            return False
        except mysql.Error as error:
            print(f"Erro ao cadastrar administrador: {error}")
            return False
        finally:
            self.lock.release()

    def atualizar_dados_adm(self, id, cargo, departamento, salario, dataadmissao, relatoriopagamento, registrofaltas, relatoriomensal, licencas, avaliacoesprojetos, beneficios):
        """
        Atualiza os dados de um administrador no banco de dados e salva os dados antigos no histórico.

        Parameters:
            id (str): ID do administrador.
            cargo (str): Cargo do administrador.
            departamento (str): Departamento do administrador.
            salario (str): Salário do administrador.
            dataadmissao (str): Data de admissão do administrador.
            relatoriopagamento (str): Relatório de pagamento do administrador.
            registrofaltas (str): Registro de faltas do administrador.
            relatoriomensal (str): Relatório mensal do administrador.
            licencas (str): Licenças do administrador.
            avaliacoesprojetos (str): Avaliações de projetos do administrador.
            beneficios (str): Benefícios do administrador.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """

        self.lock.acquire()
        try:
            self.cursor.execute('SELECT * FROM cadastro_adm WHERE id=%s', (id,))
            resultado = self.cursor.fetchone()

            if resultado is not None:
                self.cursor.execute("""
                    UPDATE cadastro_adm
                    SET cargo = %s, departamento = %s, salario = %s, dataadmissão = %s, relatoriopagamento = %s, registrofaltas = %s,
                    relatoriomensal = %s, licenças = %s, avaliacoesprojetos = %s, beneficios = %s
                    WHERE id = %s
                """, (cargo, departamento, salario, dataadmissao, relatoriopagamento, registrofaltas, relatoriomensal, licencas, avaliacoesprojetos, beneficios, id))

                self.conexao.commit()
                return True
            return False
        except mysql.Error as error:
            print(f"Erro ao atualizar dados do administrador: {error}")
            return False
        finally:
            self.lock.release()

    def salvar_registro_antigo_adm(self, id):
        """
        Salva um registro antigo do administrador na tabela "historico_atualizacoes_adm".

        Parameters:
            id (int): O ID do administrador cujo registro antigo será salvo.

        Realiza uma consulta para obter os dados do administrador com o ID fornecido.
        Se o resultado não for nulo, insere uma nova entrada na tabela "historico_atualizacoes_adm"
        com as colunas relevantes e a data atual.

        Em caso de erro durante a execução do SQL, imprime uma mensagem de erro.

        Este método é usado para armazenar um registro antigo do administrador
        sempre que houver uma atualização de informações.

        """
        try:
            self.cursor.execute('SELECT * FROM cadastro_adm WHERE id=%s', (id,))
            resultado = self.cursor.fetchone()

            if resultado is not None:
                # Create a record in the "historico_atualizacoes_adm" table with relevant columns
                data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.cursor.execute("""
                    INSERT INTO historico_atualizacoes_adm
                    (id_usuario, relatoriopagamentos, relatoriomensais, avaliacoesprojetoss, data_atualizacao)
                    VALUES (%s, %s, %s, %s, %s)
                """, (resultado[0], resultado[5], resultado[7], resultado[9], data_atual))
                self.conexao.commit()
        except mysql.Error as error:
            print(f"Erro ao salvar registro antigo do administrador: {error}")

    def obter_relatorios_mensais_antigos(self, id_usuario):
        """
        Obtém relatórios mensais antigos do administrador a partir da tabela "historico_atualizacoes_adm".

        Parameters:
            id_usuario (int): O ID do administrador cujos relatórios antigos serão obtidos.

        Realiza uma consulta para obter os relatórios mensais antigos do administrador com o ID fornecido.
        Retorna uma lista contendo dicionários com informações sobre os relatórios antigos,
        incluindo o relatório em si e a data de atualização.

        Em caso de erro durante a execução do SQL, imprime uma mensagem de erro e retorna uma lista vazia.

        Este método é usado para exibir os relatórios mensais antigos do administrador.

        """
        try:
            self.cursor.execute('SELECT relatoriomensais, data_atualizacao FROM historico_atualizacoes_adm WHERE id_usuario=%s', (id_usuario,))
            resultados = self.cursor.fetchall()

            relatorios_mensais_antigos = []

            for resultado in resultados:
                relatorio_mensal_antigo = {
                    'relatoriomensais': resultado[0],
                    'data_atualizacao': resultado[1]
                }
                relatorios_mensais_antigos.append(relatorio_mensal_antigo)

            return relatorios_mensais_antigos

        except mysql.Error as error:
            print(f"Erro ao obter avaliações mensais antigas do administrador: {error}")
            return []
        
    def obter_avaliacoes_mensais_antigas(self, id_usuario):
        """
        Obtém avaliações mensais antigas do administrador a partir da tabela "historico_atualizacoes_adm".

        Parameters:
            id_usuario (int): O ID do administrador cujas avaliações antigas serão obtidas.

        Realiza uma consulta para obter as avaliações mensais antigas do administrador com o ID fornecido.
        Retorna uma lista contendo dicionários com informações sobre as avaliações antigas,
        incluindo a avaliação em si e a data de atualização.

        Em caso de erro durante a execução do SQL, imprime uma mensagem de erro e retorna uma lista vazia.

        Este método é usado para exibir as avaliações mensais antigas do administrador.

        """
        try:
            self.cursor.execute('SELECT avaliacoesprojetoss, data_atualizacao FROM historico_atualizacoes_adm WHERE id_usuario=%s', (id_usuario,))
            resultados = self.cursor.fetchall()

            avaliacoes_mensais_antigas = []

            for resultado in resultados:
                avaliacao_mensal_antiga = {
                    'avaliacoesprojetoss': resultado[0],
                    'data_atualizacao': resultado[1]
                }
                avaliacoes_mensais_antigas.append(avaliacao_mensal_antiga)

            return avaliacoes_mensais_antigas

        except mysql.Error as error:
            print(f"Erro ao obter avaliações mensais antigas do administrador: {error}")
            return []
        
    def obter_pagamentos_mensais_antigos(self, id_usuario):
        """
        Obtém pagamentos mensais antigos do administrador a partir da tabela "historico_atualizacoes_adm".

        Parameters:
            id_usuario (int): O ID do administrador cujos pagamentos antigos serão obtidos.

        Realiza uma consulta para obter os pagamentos mensais antigos do administrador com o ID fornecido.
        Retorna uma lista contendo dicionários com informações sobre os pagamentos antigos,
        incluindo o pagamento em si e a data de atualização.

        Em caso de erro durante a execução do SQL, imprime uma mensagem de erro e retorna uma lista vazia.

        Este método é usado para exibir os pagamentos mensais antigos do administrador.

        """
        try:
            self.cursor.execute('SELECT relatoriopagamentos, data_atualizacao FROM historico_atualizacoes_adm WHERE id_usuario=%s', (id_usuario,))
            resultados = self.cursor.fetchall()

            pagamentos_mensais_antigos = []

            for resultado in resultados:
                pagamento_mensal_antigo = {
                    'avaliacoesprojetoss': resultado[0],
                    'data_atualizacao': resultado[1]
                }
                pagamentos_mensais_antigos.append(pagamento_mensal_antigo)

            return pagamentos_mensais_antigos

        except mysql.Error as error:
            print(f"Erro ao obter avaliações mensais antigas do administrador: {error}")
            return []

    def get_id_usuario(self, email):
        """
        Obtém o ID do usuário (administrador) com base no email fornecido.

        Parameters:
            email (str): O email do usuário (administrador) cujo ID será obtido.

        Realiza uma consulta para obter o ID do usuário (administrador) associado ao email fornecido.
        Retorna o ID se encontrado, caso contrário, retorna None.

        """
        self.cursor.execute("SELECT id FROM cadastrar WHERE email = %s", (email,))
        resultado = self.cursor.fetchone()
        print('id', resultado)
        if resultado:
            return resultado[0]
        else:
            return None

    def consultar_dados_usuario(self, email):
        """
        Consulta os dados de um usuário no banco de dados.

        Parameters:
            email (str): Email do usuário.

        Returns:
            dict: Dicionário contendo os dados do usuário, ou um dicionário vazio se o usuário não for encontrado.
        """
        dados_usuario = {}

        query = '''
            SELECT cadastrar.id, cadastrar.nome, cadastrar.endereco, cadastrar.email, cadastrar.nascimento, cadastrar.cpf,
            cadastro_adm.cargo, cadastro_adm.departamento, cadastro_adm.salario, cadastro_adm.dataadmissão,
            cadastro_adm.relatoriopagamento, cadastro_adm.registrofaltas, cadastro_adm.relatoriomensal,
            cadastro_adm.licenças, cadastro_adm.avaliacoesprojetos, cadastro_adm.beneficios
            FROM cadastrar
            LEFT JOIN cadastro_adm ON cadastrar.id = cadastro_adm.id
            WHERE cadastrar.email = %s
        '''
        self.cursor.execute(query, (email,))
        resultado = self.cursor.fetchone()

        if resultado:
            dados_usuario['id'] = resultado[0]
            dados_usuario['nome'] = resultado[1]
            dados_usuario['endereço'] = resultado[2]
            dados_usuario['email'] = resultado[3]
            dados_usuario['nascimento'] = resultado[4]
            dados_usuario['cpf'] = resultado[5]
            dados_usuario['cargo'] = resultado[6]
            dados_usuario['departamento'] = resultado[7]
            dados_usuario['salario'] = resultado[8]
            dados_usuario['dataadmissão'] = resultado[9]
            dados_usuario['relatoriopagamento'] = resultado[10]
            dados_usuario['registrofaltas'] = resultado[11]
            dados_usuario['relatoriomensal'] = resultado[12]
            dados_usuario['licenças'] = resultado[13]
            dados_usuario['avaliacoesprojetos'] = resultado[14]
            dados_usuario['beneficios'] = resultado[15]

        return dados_usuario

        
    def redefinir_senha(self, cpf, email, nova_senha):
        """
        Redefine a senha de um usuário.

        Parameters:
            cpf (str): CPF do usuário.
            email (str): Email do usuário.
            nova_senha (str): Nova senha para o usuário.

        Returns:
            bool: True se a redefinição for bem-sucedida, False caso contrário.
        """
        try:
            self.cursor.execute('SELECT * FROM cadastrar WHERE cpf=%s AND email=%s', (cpf, email))
            resultado = self.cursor.fetchone()
            if resultado is not None:
                self.cursor.execute('UPDATE cadastrar SET senha=%s WHERE cpf=%s', (nova_senha, cpf))
                self.conexao.commit()
                return True
            return False
        except mysql.Error as error:
            print(f"Erro ao redefinir a senha: {error}")
            return False

    def alterar_email(self, email, novo_email):
        """
        Altera o email de um usuário.

        Parameters:
            email (str): Email atual do usuário.
            novo_email (str): Novo email para o usuário.

        Returns:
            bool: True se a alteração for bem-sucedida, False caso contrário.
        """
        try:
            self.cursor.execute('SELECT * FROM cadastrar WHERE email=%s', (email,))
            resultado = self.cursor.fetchone()
            if resultado is not None:
                self.cursor.execute('UPDATE cadastrar SET email=%s WHERE email=%s', (novo_email, email))
                self.conexao.commit()
                return True
            return False
        except mysql.Error as error:
            print(f"Erro ao alterar o email: {error}")
            return False

    def alterar_senha(self, senha, nova_senha):
        """
        Altera a senha de um usuário.

        Parameters:
            senha (str): Senha atual do usuário.
            nova_senha (str): Nova senha para o usuário.

        Returns:
            bool: True se a alteração for bem-sucedida, False caso contrário.
        """
        try:
            self.cursor.execute('SELECT * FROM cadastrar WHERE senha=%s', (senha,))
            resultado = self.cursor.fetchone()
            if resultado is not None:
                self.cursor.execute('UPDATE cadastrar SET senha=%s WHERE senha=%s', (nova_senha, senha))
                self.conexao.commit()
                return True
            return False
        except mysql.Error as error:
            print(f"Erro ao alterar a senha: {error}")
            return False

    def verificar_adminsenha(self, email, senha):
        """
        Verifica se as credenciais fornecidas correspondem à conta de administrador.

        Parameters:
            email (str): Email fornecido.
            senha (str): Senha fornecida.

        Returns:
            bool: True se as credenciais de administrador estiverem corretas, False caso contrário.
        """
        return email.strip() == 'ADMIN' and senha.strip() == 'ADMIN123'


    def buscar_pessoa(self, cpf):
        """
        Busca uma pessoa pelo CPF.

        Parameters:
            cpf (str): CPF da pessoa.

        Returns:
            tuple: Dados da pessoa encontrada no banco de dados.
        """
        try:
            self.cursor.execute('SELECT nome, id FROM cadastrar WHERE cpf = %s', (cpf,))
            resultado = self.cursor.fetchone()

            if resultado:
                id_funcionario = resultado[1]

                self.cursor.execute('SELECT cargo, departamento, salario, dataadmissão FROM cadastro_adm WHERE id = %s', (id_funcionario,))
                especificacoes = self.cursor.fetchone()

                if especificacoes:
                    resultado += especificacoes

            return resultado
        except mysql.Error as error:
            print(f"Erro ao buscar pessoa: {error}")
            return None


