import socket
from bancodedados import Banco
import threading
import json

def tratar_mensagem(mensagem):
    """
    Função responsável por processar a mensagem recebida do cliente e executar a operação correspondente.

    Parameters:
        mensagem (str): A mensagem recebida do cliente.

    Returns:
        str: A resposta a ser enviada de volta ao cliente.
    """
    l = mensagem.split("-")
    envia = ''

    if l[0] == '-1':
        envia = "-1"
    elif l[0] == '-2':
        envia = "-2"
    elif l[0] == '0':
        email = l[1]
        senha = l[2]

        verificar = banco.verificar_adminsenha(email, senha)

        if verificar:
            envia = "admin"
        else:
            entrar = banco.entrar(email, senha)

            if entrar:
                entrar = str(entrar)
                envia = entrar
            else:
                envia = '0'

    elif l[0] == '1':
        email = l[1]
        dados_usuario = banco.consultar_dados_usuario(email)

        if dados_usuario:
            envia = f"{dados_usuario['id']}-{dados_usuario['nome']}-{dados_usuario['cargo']}-{dados_usuario['departamento']}-{dados_usuario['salario']}-{dados_usuario['dataadmissão']}-{dados_usuario['registrofaltas']}-{dados_usuario['relatoriopagamento']}-{dados_usuario['licenças']}-{dados_usuario['beneficios']}-{dados_usuario['avaliacoesprojetos']}-{dados_usuario['relatoriomensal']}"
        else:
            envia = ''

    elif l[0] == '2':  
        email = l[1]
        nome = l[2]
        endereco = l[3]
        cpf = l[4]
        nascimento = l[5]
        senha = l[6]
        if banco.cadastrarusuario(email, nome, endereco, cpf, nascimento, senha):
            envia = '1'
            print("usuario cadastrado")
        else:
            envia = '0'

    elif l[0] == '3':
        email = l[1]
        cpf = l[2]
        nova_senha = l[3]
        if banco.redefinir_senha(cpf, email, nova_senha):
            envia = '1'
            print("senha redefinida com sucesso")
        else:
            envia = '0'
    
    elif l[0] == '4':
        cpf = l[1]
        resultado = banco.buscar_pessoa(cpf)
        if resultado is not None:
            envia = '4-' + str(resultado[1]) + '-' + resultado[0]

           
            if len(resultado) > 2:
                envia += '-' + resultado[2]  
                envia += '-' + resultado[3]  
                envia += '-' + resultado[4] 
                envia += '-' + resultado[5] 
            else:
                envia += '-0'

            print('busca realizada com sucesso')
        else:
            envia = '0'


    elif l[0] == '5':
        id = l[1]
        cargo = l[2]
        departamento = l[3]
        salario = l[4]
        dataadmissao = l[5]
        relatoriopagamento = l[6]
        registrofaltas = l[7]
        relatoriomensal = l[8]
        licencas = l[9]
        avaliacoesprojetos = l[10]
        beneficios = l[11]

        banco.salvar_registro_antigo_adm(id)

        if banco.atualizar_dados_adm(id, cargo, departamento, salario, dataadmissao, relatoriopagamento, registrofaltas, relatoriomensal, licencas, avaliacoesprojetos, beneficios):
            envia = '1'
            print('Dados atualizados com sucesso')
        else:
            envia = '0'

    elif l[0] == '6':
        id = l[1]
        cargo = l[2]
        departamento = l[3]
        salario = l[4]
        dataadmissao = l[5]
        relatoriopagamento = l[6]
        registrofaltas = l[7]
        relatoriomensal = l[8]
        licencas = l[9]
        avaliacoesprojetos = l[10]
        beneficios = l[11]
        if banco.cadastraradm(id, cargo, departamento, salario, dataadmissao, relatoriopagamento, registrofaltas, relatoriomensal, licencas, avaliacoesprojetos, beneficios):
            envia = '1'
            print('dados cadastrado com sucesso')
        else:
            envia = '0'

    elif l[0] == '7':
        email = l[1]
        novo_email = l[2]
        if banco.alterar_email(email, novo_email):
            envia = '1'
            print('Email alterado com sucesso')
        else:
            envia = '0'

    elif l[0] == '8':
        senha = l[1]
        nova_senha = l[2]
        if banco.alterar_senha(senha, nova_senha):
            envia = '1'
            print('Senha alterada com sucesso')
        else:
            envia = '0'
    elif l[0] == '9':
        email = l[1]
        print('Recebido pedido de ID do usuário com email:', email)
        usuario_id = banco.get_id_usuario(email)
        if usuario_id is not None:
            envia = str(usuario_id)
        else:
            envia = '0'
    elif l[0] == '10':
        id_usuario = int(l[1])
        relatorios_mensais_antigos = banco.obter_relatorios_mensais_antigos(id_usuario)

        relatorios_str = ",".join([f"{relatorio['relatoriomensais']} | {relatorio['data_atualizacao']}" for relatorio in relatorios_mensais_antigos])
        envia = f"10-{relatorios_str}"
    elif l[0] == '11':
        id_usuario = int(l[1])
        avaliacoes_mensais_antigas = banco.obter_avaliacoes_mensais_antigas(id_usuario)

        avaliacao_str = ",".join([f"{avaliacao['avaliacoesprojetoss']} | {avaliacao['data_atualizacao']}" for avaliacao in avaliacoes_mensais_antigas])
        envia = f"11-{avaliacao_str}"
    elif l[0] == '12':
        id_usuario = int(l[1])
        pagamentos_mensais_antigos = banco.obter_pagamentos_mensais_antigos(id_usuario)

        pagamento_str = ",".join([f"{pagamento['avaliacoesprojetoss']} | {pagamento['data_atualizacao']}" for pagamento in pagamentos_mensais_antigos])
        envia = f"12-{pagamento_str}"
        
    return envia

    
class ClientThread(threading.Thread):
    """
    Classe que representa uma thread para lidar com a comunicação com um cliente.

    ...

    Attributes
    ----------
    connection : socket
        O objeto de conexão com o cliente.

    Methods
    -------
    __init__(self, connection)
        Construtor da classe. Inicializa o objeto de conexão com o cliente.
        
    run(self)
        Executa a thread do cliente.
    """
   
    def __init__(self, connection):
        super().__init__()
        self.con = connection

    def run(self):
        """
        Método executado pela thread ao iniciar a execução.

        Responsável por receber as mensagens do cliente, processá-las e enviar a resposta de volta.
        """
        while True:
            recebe = self.con.recv(1024)
            enviar = tratar_mensagem(recebe.decode())
            if enviar == "-1":
                self.con.send(enviar.encode())
                break
            else:
                self.con.send(enviar.encode())


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8085
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    banco = Banco()

    while True:
        server_socket.listen(10)
        print("esperando cliente...")
        con, cliente = server_socket.accept()
        print("cliente aceito...")
        sinc = threading.Lock()
        newThread = ClientThread(con)
        newThread.start()
