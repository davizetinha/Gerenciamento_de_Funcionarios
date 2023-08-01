import mysql.connector as mysql
from cliente import Cliente
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QStackedWidget

import re

from telalogin_cadastro import Telalogin
from telacadastro import Telacadastro
from teladousuario import Teladousuario
from telaadministrador import Telaadministrador
from telaloginadministador import Telaadm
from configuraçoes import Config
from alterarsenha import Alterarsenha   
from alteraremail import Alteraremail
from telatrocarsenha import Trocarsenha
from mesesanteriores import Mesesanteriores

class MainMultitelas(QtWidgets.QWidget):
    def setupUi(self, Main):
        """
        Classe:
        Configura a interface gráfica do usuário para a aplicação principal.

        Parameters:
            Main (QMainWindow): Referência para a janela principal.
        """
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()

        self.telalogin_cadastro = Telalogin()     
        self.telalogin_cadastro.setupUi(self.stack0)
        
        self.telacadastro = Telacadastro()
        self.telacadastro.setupUi(self.stack1)

        self.teladousuario = Teladousuario()
        self.teladousuario.setupUi(self.stack2)

        self.telaadministrador = Telaadministrador()
        self.telaadministrador.setupUi(self.stack3)

        self.telaloginadministador = Telaadm()
        self.telaloginadministador.setupUi(self.stack4)

        self.configuraçoes = Config()
        self.configuraçoes.setupUi(self.stack5)

        self.alterarsenha = Alterarsenha()
        self.alterarsenha.setupUi(self.stack6)

        self.alteraremail = Alteraremail()
        self.alteraremail.setupUi(self.stack7)

        self.telatrocarsenha = Trocarsenha()
        self.telatrocarsenha.setupUi(self.stack8)

        self.mesesanteriores = Mesesanteriores()
        self.mesesanteriores.setupUi(self.stack9)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)

class Main(QMainWindow, MainMultitelas):
    
    """
    Classe principal do aplicativo que herda da classe MainMultitelas e QMainWindow.
    Esta classe representa a janela principal do aplicativo.

    ...

    Attributes
    ----------
        
    Methods
    -------
        _init_(self, parent=None)
            Construtor da classe. Inicializa a janela e configura as conexões dos sinais e slots.

        botaocadastra(self)
            Função chamada quando o botão de cadastro é clicado. Realiza o cadastro de um novo usuário.

        botaoadmcadastra(self)
            Função chamada quando o botão de cadastro é clicado. Realiza o cadastro das informaçoes do usuario pelo administrador.

        botaoatualizar_dados(self)
            Função chamada quando o botão de cadastro é clicado. Realiza a atualização das informaçoes do usuario pelo administrador.

        botaoentrar(self)
            Função chamada quando o botão de entrar é clicado. Realiza o login do usuário.

        obter_dados_usuario(self, email):
            Atualiza a interface gráfica do usuário com os dados obtidos.

        botaobuscar(self)
            Função chamada quando o botão de buscar é clicado Exibe os dados encontrados na interface gráfica.
            
        botaoredefinirsenha(self)
            Função chamada quando o botão de redefinir senha é clicado. redefinindo a senha do usuario

        botaotrocaremail(self)
            Função chamada quando o botão de alterar email é clicado. redefinindo o email do usuario

        botaotrocarsenha(self)
            Função chamada quando o botão de alterar senha é clicado. redefinindo a senha do usuario

        botaovoltar(self)
            Função chamada quando o botão de voltar é clicado. voltando a tela anterior

        carregarJogosADM(self):
            Carrega os jogos cadastrados.

        botao_voltar(self):
            Função chamada quando o botão de voltar é clicado.

        botao_deslogar(self):
            Função chamada quando o botão de deslogar é clicado.

        telacadastrar(self):
            Abre a tela de cadastro de novos usuários.

        botaoconfigaracoes(self):
            Abre a tela de configurações do usuário.

        botaovoltarusuario(self):
            Função chamada quando o botão de voltar é clicado.

        botaoalterarsenha(self):
            Função chamada quando o botão de voltar é clicado.

        botaoalterarsenha(self):
            Função chamada quando o botão de voltar é clicado.

        botaovoltarconfiguracoes(self):
            Função chamada quando o botão de voltar é clicado.    
        
        exibir_relatorios_mensais_antigos(self):
            Exibe os relatórios mensais antigos na lista de widgets.
        
        exibir_avaliacoes_mensais_antigas(self):
            Exibe as avaliações mensais antigas na lista de widgets.
        
        exibir_pagamentos_mensais_antigos(self):
            Exibe os pagamentos mensais antigos na lista de widgets.

        botaomesesanteriores(self):
            Processa o evento de clicar no botão 'Mesesanteriores'.
        
        botao_sair(self):
            Finaliza a aplicação.

    """
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.serve = Cliente()

        self.telalogin_cadastro.pushButton_2.clicked.connect(self.telacadastrar)
        self.telalogin_cadastro.pushButton_3.clicked.connect(self.botaotrocarsenhaa)
        self.telalogin_cadastro.pushButton.clicked.connect(self.botaoentrar)
        self.telaloginadministador.pushButton_2.clicked.connect(self.botaovoltar)
        self.telatrocarsenha.pushButton.clicked.connect(self.botaoredefinirsenha)
        self.telatrocarsenha.pushButton_2.clicked.connect(self.botaovoltar)
        self.telaadministrador.pushButton.clicked.connect(self.botaobuscar)
        self.telaadministrador.pushButton_2.clicked.connect(self.botaoadmcadastra)
        self.telaadministrador.pushButton_3.clicked.connect(self.botaosair)
        self.telaadministrador.pushButton_4.clicked.connect(self.botaoatualizar_dados)
        self.teladousuario.pushButton_3.clicked.connect(self.botaosair)
        self.teladousuario.pushButton.clicked.connect(self.botaoconfigaracoes)
        self.teladousuario.pushButton_2.clicked.connect(self.botaomesesanteriores)
        self.mesesanteriores.pushButton_2.clicked.connect(self.botaovoltarusuario)
        self.mesesanteriores.pushButton_3.clicked.connect(self.botaosair)
        self.configuraçoes.pushButton_4.clicked.connect(self.botaovoltarusuario)
        self.configuraçoes.pushButton.clicked.connect(self.botaoalterarsenha)
        self.configuraçoes.pushButton_2.clicked.connect(self.botaoalteraremail)
        self.alterarsenha.pushButton_4.clicked.connect(self.botaovoltarconfiguracoes)
        self.alterarsenha.pushButton.clicked.connect(self.botaotrocarsenha)
        self.alteraremail.pushButton_4.clicked.connect(self.botaovoltarconfiguracoes)
        self.alteraremail.pushButton.clicked.connect(self.botaotrocaremail)
        self.telacadastro.pushButton_2.clicked.connect(self.botaocadastra)
        self.telacadastro.pushButton_3.clicked.connect(self.botaovoltar)

    def botaocadastra(self):
        """
        Processa o evento de cadastro de usuário quando o botão 'Cadastrar' é clicado.

        Realiza a validação dos campos e envia os dados para o servidor realizar o cadastro.
        Exibe mensagens de sucesso ou erro ao usuário.
        """
        email = self.telacadastro.lineEdit_6.text()
        senha = self.telacadastro.lineEdit_3.text()
        nome = self.telacadastro.lineEdit_2.text()
        endereco = self.telacadastro.lineEdit_5.text()
        cpf = self.telacadastro.lineEdit.text()
        nascimento = self.telacadastro.lineEdit_9.text()

        if not (nome == '' or endereco == '' or cpf == '' or nascimento == '' or email == '' or senha == ''):
            if len(cpf) == 11 and re.match(r'^\d+$', cpf):
                msg = '2' + '-' + email + '-' + nome + '-' + endereco + '-' + cpf + '-' + nascimento + '-' + senha
                recebeu = self.serve.enviar(msg)
                if recebeu == '1':
                    QMessageBox.information(self, 'multitelas', 'Cadastro realizado com sucesso')
                    self.telacadastro.lineEdit_6.setText('')
                    self.telacadastro.lineEdit_2.setText('')
                    self.telacadastro.lineEdit.setText('')
                    self.telacadastro.lineEdit_9.setText('')
                    self.telacadastro.lineEdit_5.setText('')
                    self.telacadastro.lineEdit_3.setText('')
                else:
                    QMessageBox.warning(self, 'Cadastro de Pessoas', 'CPF já cadastrado.')
            else:
                QMessageBox.warning(self, 'Cadastro de Pessoas', 'CPF inválido. Verifique se contém 11 dígitos numéricos.')
        else:
            QMessageBox.warning(self, 'Cadastro de Pessoas', 'Todos os valores devem ser preenchidos.')

    def botaoadmcadastra(self):
        """
        Processa o evento de cadastro de informações do usuario quando o botão 'Cadastrar' é clicado.

        Realiza a validação dos campos e envia os dados para o servidor realizar o cadastro.
        Exibe mensagens de sucesso ou erro ao usuário.
        """
        id = self.telaadministrador.lineEdit_2.text()
        cargo = self.telaadministrador.lineEdit_6.text()
        departamento = self.telaadministrador.lineEdit_7.text()
        salario = self.telaadministrador.lineEdit_5.text()
        dataadmissao = self.telaadministrador.lineEdit_8.text()
        relatoriopagamento = self.telaadministrador.lineEdit_12.text()
        registrofaltas = self.telaadministrador.comboBox_3.currentText()
        relatoriomensal = self.telaadministrador.lineEdit_16.text()
        licencas = self.telaadministrador.comboBox.currentText()
        avaliacoesprojetos = self.telaadministrador.lineEdit_18.text()
        beneficios = self.telaadministrador.comboBox_2.currentText()

        if not (id == '' or cargo == '' or departamento == '' or salario == '' or dataadmissao == '' or relatoriopagamento == '' or registrofaltas == '' or relatoriomensal == '' or licencas == '' or avaliacoesprojetos == '' or beneficios == ''):
            msg = '6' + '-' + id + '-' + cargo + '-' + departamento + '-' + salario + '-' + dataadmissao + '-' + relatoriopagamento + '-' + registrofaltas + '-' + relatoriomensal + '-' + licencas + '-' + avaliacoesprojetos + '-' + beneficios
            recebeu = self.serve.enviar(msg)
            if recebeu == '1':
                QMessageBox.information(self, 'multitelas', 'Cadastro realizado com sucesso')
                self.telaadministrador.lineEdit_2.setText('')
                self.telaadministrador.lineEdit_6.setText('')
                self.telaadministrador.lineEdit_7.setText('')
                self.telaadministrador.lineEdit_5.setText('')
                self.telaadministrador.lineEdit_8.setText('')
                self.telaadministrador.lineEdit_12.setText('')
                self.telaadministrador.comboBox_3.setCurrentText('')
                self.telaadministrador.lineEdit_16.setText('')
                self.telaadministrador.comboBox.setCurrentText('')
                self.telaadministrador.lineEdit_18.setText('')
                self.telaadministrador.comboBox_2.setCurrentText('')
            else:
                QMessageBox.warning(self, 'Cadastro do funcionario', 'Já cadastrado.')
        else:
            QMessageBox.warning(self, 'Cadastro de Pessoas', 'Todos os valores devem ser preenchidos.')

    def botaoatualizar_dados(self):
        """
        Processa o evento de atualização de dados quando o botão 'Atualizar' é clicado.

        Realiza a validação dos campos e envia os dados para o servidor realizar a atualização.
        Exibe mensagens de sucesso ou erro ao usuário.
        """
        id = self.telaadministrador.lineEdit_2.text()
        cargo = self.telaadministrador.lineEdit_6.text()
        departamento = self.telaadministrador.lineEdit_7.text()
        salario = self.telaadministrador.lineEdit_5.text()
        dataadmissao = self.telaadministrador.lineEdit_8.text()
        relatoriopagamento = self.telaadministrador.lineEdit_12.text()
        registrofaltas = self.telaadministrador.comboBox_3.currentText()
        relatoriomensal = self.telaadministrador.lineEdit_16.text()
        licencas = self.telaadministrador.comboBox.currentText()
        avaliacoesprojetos = self.telaadministrador.lineEdit_18.text()
        beneficios = self.telaadministrador.comboBox_2.currentText()

        if not (id == '' or cargo == '' or departamento == '' or salario == '' or dataadmissao == '' or relatoriopagamento == '' or registrofaltas == '' or relatoriomensal == '' or licencas == '' or avaliacoesprojetos == '' or beneficios == ''):
            msg = '5' + '-' + id + '-' + cargo + '-' + departamento + '-' + salario + '-' + dataadmissao + '-' + relatoriopagamento + '-' + registrofaltas + '-' + relatoriomensal + '-' + licencas + '-' + avaliacoesprojetos + '-' + beneficios
            recebeu = self.serve.enviar(msg)
            if recebeu == '1':
                QMessageBox.information(self, 'multitelas', 'Dados atualizados com sucesso')
                self.telaadministrador.lineEdit_2.setText('')
                self.telaadministrador.lineEdit_6.setText('')
                self.telaadministrador.lineEdit_7.setText('')
                self.telaadministrador.lineEdit_5.setText('')
                self.telaadministrador.lineEdit_8.setText('')
                self.telaadministrador.lineEdit_12.setText('')
                self.telaadministrador.comboBox_3.setCurrentText('')
                self.telaadministrador.lineEdit_16.setText('')
                self.telaadministrador.comboBox.setCurrentText('')
                self.telaadministrador.lineEdit_18.setText('')
                self.telaadministrador.comboBox_2.setCurrentText('')
            else:
                QMessageBox.warning(self, 'Atualização de Dados', 'Falha ao atualizar os dados.')
        else:
            QMessageBox.warning(self, 'Atualização de Dados', 'Todos os valores devem ser preenchidos.')

    def botaoentrar(self):
        """
        Processa o evento de login quando o botão 'Entrar' é clicado.

        Realiza a validação dos campos e envia os dados para o servidor verificar as credenciais.
        Redireciona para a tela de usuário ou de administrador, dependendo do resultado.
        """

        self.email = self.telalogin_cadastro.lineEdit.text()
        senha = self.telalogin_cadastro.lineEdit_2.text()

        if not self.email or not senha:
            QMessageBox.warning(self, 'Login', 'Por favor, preencha todos os campos.')
            return

        msg = '0' + '-' + self.email + '-' + senha
        recebeu = self.serve.enviar(msg)

        if recebeu == "0":
            QMessageBox.information(self, 'Login', 'Não foi possível fazer o login. Senha ou usuário incorretos.')
        elif recebeu == "admin":
            self.QtStack.setCurrentIndex(3)
            QMessageBox.information(self, 'Login', 'Login como administrador realizado com sucesso.')
        else:
            QMessageBox.information(self, 'multitelas', 'Login realizado com sucesso.')
            self.obter_dados_usuario(self.email)  # Chamada para obter os dados do usuário
            self.usuario_id = self.serve.enviar('9-' + self.email)
            print(self.usuario_id)

    def obter_dados_usuario(self, email):
        """
        Obtém os dados do usuário logado a partir do servidor.

        Envia uma solicitação para o servidor para obter os dados do usuário logado.
        Atualiza a interface gráfica do usuário com os dados obtidos.

        Parameters:
            email (str): Email do usuário logado.
        """
        msg = '1' + '-' + email
        dados_usuario_str = self.serve.enviar(msg)  # Agora recebe uma string ao invés de um dicionário
        
        if dados_usuario_str:
            dados_usuario_list = dados_usuario_str.split('-')  # Divide a string para obter os campos
            dados_usuario = {
                'id': dados_usuario_list[0],
                'nome': dados_usuario_list[1],
                'cargo': dados_usuario_list[2],
                'departamento': dados_usuario_list[3],
                'salario': dados_usuario_list[4],
                'dataadmissão': dados_usuario_list[5],
                'registrofaltas': dados_usuario_list[6],
                'relatoriopagamento': dados_usuario_list[7],
                'licenças': dados_usuario_list[8],
                'beneficios': dados_usuario_list[9],
                'avaliacoesprojetos': dados_usuario_list[10],
                'relatoriomensal': dados_usuario_list[11],
            }

            self.QtStack.setCurrentIndex(2)
            self.teladousuario.lineEdit_3.setText(dados_usuario.get('nome', ''))
            self.teladousuario.lineEdit.setText(str(dados_usuario.get('id', '')))
            self.teladousuario.lineEdit_2.setText(dados_usuario.get('cargo', ''))
            self.teladousuario.lineEdit_4.setText(dados_usuario.get('departamento', ''))
            self.teladousuario.lineEdit_5.setText(dados_usuario.get('salario', ''))
            self.teladousuario.lineEdit_6.setText(dados_usuario.get('dataadmissão', ''))
            self.teladousuario.lineEdit_13.setText(dados_usuario.get('registrofaltas', ''))
            self.teladousuario.lineEdit_10.setText(dados_usuario.get('relatoriopagamento', ''))
            self.teladousuario.lineEdit_11.setText(dados_usuario.get('licenças', ''))
            self.teladousuario.lineEdit_12.setText(dados_usuario.get('beneficios', ''))
            self.teladousuario.lineEdit_9.setText(dados_usuario.get('avaliacoesprojetos', ''))
            self.teladousuario.lineEdit_8.setText(dados_usuario.get('relatoriomensal', ''))

        else:
            print("Não foi possível obter os dados do usuário.")



    def botaobuscar(self):
        """
        Processa o evento de busca quando o botão 'Buscar' é clicado.

        Realiza a validação do campo de CPF e envia a solicitação para o servidor.
        Exibe os dados encontrados na interface gráfica.

        """
        cpf = self.telaadministrador.lineEdit.text()

        if cpf != '':
            msg = '4' + '-' + cpf
            recebeu = self.serve.enviar(msg)
            if recebeu.startswith('4-'):
                resultado = recebeu.split('-')
                id_encontrado = resultado[1]
                nome_encontrado = resultado[2]

                if resultado[3] == '0':
                    QMessageBox.warning(self, 'Busca de Pessoas', 'Funcionário sem cadastro completo.')
                    self.telaadministrador.lineEdit_6.setText('')
                    self.telaadministrador.lineEdit_7.setText('')
                    self.telaadministrador.lineEdit_5.setText('')
                    self.telaadministrador.lineEdit_8.setText('')
                else:
                    cargo = resultado[3]
                    departamento = resultado[4]
                    salario = resultado[5]
                    dataadmissão = resultado[6]

                    self.telaadministrador.lineEdit_6.setText(cargo)
                    self.telaadministrador.lineEdit_7.setText(departamento)
                    self.telaadministrador.lineEdit_5.setText(salario)
                    self.telaadministrador.lineEdit_8.setText(dataadmissão)

                self.telaadministrador.lineEdit_2.setText(id_encontrado)
                self.telaadministrador.lineEdit_3.setText(nome_encontrado)
            else:
                QMessageBox.warning(self, 'Busca de Pessoas', 'Pessoa não encontrada.')
        else:
            QMessageBox.warning(self, 'Busca de Pessoas', 'O CPF não pode estar vazio.')

    
    def botaoredefinirsenha(self):
        """
        Processa o evento de redefinição de senha quando o botão 'Redefinir Senha' é clicado.

        Realiza a validação dos campos e envia os dados para o servidor realizar a redefinição da senha.
        Exibe mensagens de sucesso ou erro ao usuário.
        """
        email = self.telatrocarsenha.lineEdit_2.text()
        cpf = self.telatrocarsenha.lineEdit.text()
        senha = self.telatrocarsenha.lineEdit_3.text()

        if email != '' and cpf != '' and senha != '':
            msg = '3' + '-' + email + '-' + cpf + '-' + senha
            recebeu = self.serve.enviar(msg)
            if recebeu == '1':
                QMessageBox.information(self, 'multitelas', 'Senha redefinida com sucesso')
                self.telatrocarsenha.lineEdit_2.setText('')
                self.telatrocarsenha.lineEdit.setText('')
                self.telatrocarsenha.lineEdit_3.setText('')
            else:
                QMessageBox.warning(self, 'Redefinição de Senha', 'Email ou CPF incorretos.')
        else:
            QMessageBox.warning(self, 'Redefinição de Senha', 'Por favor, preencha todos os campos.')

    def botaotrocaremail(self):
        """
        Processa o evento de alteração de email quando o botão 'Alterar Email' é clicado.

        Realiza a validação dos campos e envia os dados para o servidor realizar a alteração do email.
        Exibe mensagens de sucesso ou erro ao usuário.
        """
        email = self.alteraremail.lineEdit.text()
        novo_email = self.alteraremail.lineEdit_2.text()

        if email != '' and novo_email != '':
            msg = '7' + '-' + email + '-' + novo_email
            recebeu = self.serve.enviar(msg)
            if recebeu == '1':
                QMessageBox.information(self, 'multitelas', 'Email alterado com sucesso')
                self.alteraremail.lineEdit.setText('')
                self.alteraremail.lineEdit_2.setText('')
            else:
                QMessageBox.warning(self, 'Alteração de Email', 'O email antigo não foi encontrado.')
        else:
            QMessageBox.warning(self, 'Alteração de Email', 'Por favor, preencha todos os campos.')

    def botaotrocarsenha(self):
        """
        Processa o evento de troca de senha quando o botão 'Trocar Senha' é clicado.

        Realiza a validação dos campos e envia os dados para o servidor realizar a troca de senha.
        Exibe mensagens de sucesso ou erro ao usuário.
        """
        senha = self.alterarsenha.lineEdit.text()
        nova_senha = self.alterarsenha.lineEdit_2.text()

        if senha != '' and nova_senha != '':
            msg = '8' + '-' + senha + '-' + nova_senha
            recebeu = self.serve.enviar(msg)
            if recebeu == '1':
                QMessageBox.information(self, 'multitelas', 'Senha alterada com sucesso')
                self.alterarsenha.lineEdit.setText('')
                self.alterarsenha.lineEdit_2.setText('')
            else:
                QMessageBox.warning(self, 'Alteração de Senha', 'A senha antiga não é válida.')
        else:
            QMessageBox.warning(self, 'Alteração de Senha', 'Por favor, preencha todos os campos.')

    def botaovoltar(self):
        """
        Processa o evento de voltar para a tela de login quando o botão 'Voltar' é clicado.

        Limpa os campos de texto e volta para a tela de login.
        """
        self.QtStack.setCurrentIndex(0)
        self.telacadastro.lineEdit_6.setText('')
        self.telacadastro.lineEdit_2.setText('')
        self.telacadastro.lineEdit.setText('')
        self.telacadastro.lineEdit_9.setText('')
        self.telacadastro.lineEdit_5.setText('')
        self.telacadastro.lineEdit_3.setText('')
        self.telalogin_cadastro.lineEdit.clear()
        self.telalogin_cadastro.lineEdit_2.clear()
        self.teladousuario.lineEdit_3.setText('')
        self.teladousuario.lineEdit.setText('')
        self.teladousuario.lineEdit_2.setText('')
        self.teladousuario.lineEdit_4.setText('')
        self.teladousuario.lineEdit_5.setText('')
        self.teladousuario.lineEdit_6.setText('')
        self.teladousuario.lineEdit_13.setText('')
        self.teladousuario.lineEdit_10.setText('')
        self.teladousuario.lineEdit_11.setText('')
        self.teladousuario.lineEdit_12.setText('')
        self.teladousuario.lineEdit_9.setText('')
        self.teladousuario.lineEdit_8.setText('')

    def exibir_relatorios_mensais_antigos(self):
        """
            Exibe os relatórios mensais antigos na lista de widgets.

            Envia uma mensagem ao servidor solicitando os relatórios mensais antigos para o usuário.
            Recebe a resposta do servidor com os relatórios e os exibe na lista de widgets.
        """
        msg = '10-' + str(self.usuario_id)

        resposta = self.serve.enviar(msg)

        if resposta.startswith("10-"):
            relatorios_mensais_antigos = resposta[3:].split(",")

            self.mesesanteriores.listWidget_2.clear()

            for relatorio in relatorios_mensais_antigos:
                self.mesesanteriores.listWidget_2.addItem(relatorio)

    def exibir_avaliacoes_mensais_antigas(self):
        """
            Exibe as avaliações mensais antigas na lista de widgets.

            Envia uma mensagem ao servidor solicitando as avaliações mensais antigas para o usuário.
            Recebe a resposta do servidor com as avaliações e as exibe na lista de widgets.
        """
        msg = '11-' + str(self.usuario_id)

        resposta = self.serve.enviar(msg)

        if resposta.startswith("11-"):
            avaliacoes_mensais_antigas = resposta[3:].split(",")

            self.mesesanteriores.listWidget.clear()

            for avaliacao in avaliacoes_mensais_antigas:
                self.mesesanteriores.listWidget.addItem(avaliacao)

    def exibir_pagamentos_mensais_antigos(self):
        """
            Exibe os pagamentos mensais antigos na lista de widgets.

            Envia uma mensagem ao servidor solicitando os pagamentos mensais antigos para o usuário.
            Recebe a resposta do servidor com os pagamentos e os exibe na lista de widgets.
        """
        msg = '12-' + str(self.usuario_id)

        resposta = self.serve.enviar(msg)

        if resposta.startswith("12-"):
            pagamentos_mensais_antigos = resposta[3:].split(",")

            self.mesesanteriores.listWidget_3.clear()

            for pagamento in pagamentos_mensais_antigos:
                self.mesesanteriores.listWidget_3.addItem(pagamento)

    def botaomesesanteriores(self):
        """
        Processa o evento de clicar no botão 'Mesesanteriores'.

        Chama as funções para exibir relatórios, avaliações e pagamentos mensais antigos.
        Define a tela Mesesanteriores como a tela atual exibida, cujo índice é 9.
    """
        self.exibir_relatorios_mensais_antigos()
        self.exibir_avaliacoes_mensais_antigas()
        self.exibir_pagamentos_mensais_antigos()
        self.QtStack.setCurrentIndex(9)

    def telacadastrar(self):
        """
        Processa o evento de mudança para a tela de cadastro quando o botão 'Cadastrar' é clicado.

        Muda para a tela de cadastro e limpa os campos de texto.
        """
        self.QtStack.setCurrentIndex(1)

    def botaoconfigaracoes(self):
        """
        Processa o evento de mudança para a tela de configurações quando o botão 'Configurações' é clicado.

        Muda para a tela de configurações e limpa os campos de texto.
        """
        self.QtStack.setCurrentIndex(5)

    def botaovoltarusuario(self):
        """
        Processa o evento de voltar para a tela de usuário quando o botão 'Voltar' é clicado.

        Volta para a tela de usuário e limpa os campos de texto.
        """
        self.QtStack.setCurrentIndex(2)

    def botaotrocarsenhaa(self):

        self.QtStack.setCurrentIndex(8)

    def botaoalterarsenha(self):
        """
        Processa o evento de mudança para a tela de alteração de senha quando o botão 'Alterar Senha' é clicado.

        Muda para a tela de alteração de senha e limpa os campos de texto.
        """
        self.QtStack.setCurrentIndex(6)
        self.alterarsenha.lineEdit.clear()
        self.alterarsenha.lineEdit_2.clear()

    def botaoalteraremail(self):
        """
        Processa o evento de mudança para a tela de alteração de email quando o botão 'Alterar Email' é clicado.

        Muda para a tela de alteração de email e limpa os campos de texto.
        """
        self.QtStack.setCurrentIndex(7)
        self.alteraremail.lineEdit.clear()
        self.alteraremail.lineEdit_2.clear()

    def botaovoltarconfiguracoes(self):
        """
        Processa o evento de voltar para a tela de configurações quando o botão 'Voltar' é clicado.

        Volta para a tela de configurações e limpa os campos de texto.
        """
        self.QtStack.setCurrentIndex(5)
        self.alterarsenha.lineEdit.clear()
        self.alterarsenha.lineEdit_2.clear()
        self.alteraremail.lineEdit.clear()
        self.alteraremail.lineEdit_2.clear()

    def botaosair(self):
        """
        Processa o evento de logout quando o botão 'Sair' é clicado.

        Volta para a tela de login e limpa os campos de texto.
        """
        self.QtStack.setCurrentIndex(0)
        self.telalogin_cadastro.lineEdit.clear()
        self.telalogin_cadastro.lineEdit_2.clear()
        self.teladousuario.lineEdit_3.clear()
        self.teladousuario.lineEdit.clear()
        self.teladousuario.lineEdit_2.clear()
        self.teladousuario.lineEdit_4.clear()
        self.teladousuario.lineEdit_5.clear()
        self.teladousuario.lineEdit_6.clear()
        self.teladousuario.lineEdit_13.clear()
        self.teladousuario.lineEdit_10.clear()
        self.teladousuario.lineEdit_11.clear()
        self.teladousuario.lineEdit_12.clear()
        self.teladousuario.lineEdit_9.clear()
        self.teladousuario.lineEdit_8.clear()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui =  Main()
    sys.exit(app.exec_())