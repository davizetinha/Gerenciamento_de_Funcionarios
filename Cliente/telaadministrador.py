# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaadministrador.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Telaadministrador(object):
    """
    Configura a interface do usuário para a tela do administrador.

    ...

    Methods
    -------
    def setupUi(self, MainWindow)
        Configura a interface gráfica da janela principal.

    def retranslateUi(self, MainWindow)
        Configura as traduções dos textos exibidos na interface do usuário.
    """

    def setupUi(self, MainWindow):
        """
        Configura a interface do usuário da janela do administrador.

        Parameters:
            MainWindow (QtWidgets.QMainWindow): A referência para a janela principal.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 311, 51))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 80, 481, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 110, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 41, 21))
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-130, 640, 1201, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(470, 340, 331, 41))
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(210, 400, 81, 16))
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(220, 430, 71, 16))
        self.label_22.setObjectName("label_22")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(290, 340, 141, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 10, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(470, 220, 241, 21))
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(100, 340, 181, 21))
        self.label_20.setObjectName("label_20")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(-110, 140, 1201, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 490, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(470, 250, 221, 81))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(470, 370, 221, 81))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 370, 221, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 400, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 430, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(290, 370, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 220, 51, 21))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(180, 250, 111, 21))
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 310, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 280, 61, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 220, 139, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(290, 250, 139, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 280, 139, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(290, 310, 139, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(-130, 460, 1201, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 190, 20, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 190, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 530, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 51, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 160, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Define o texto dos elementos da interface do usuário.

        Parameters:
            MainWindow (QtWidgets.QMainWindow): A referência para a janela principal.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">TELA ADMINISTRADOR</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "BUSCAR"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cpf:</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Avaliação mensal dos projetos:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Beneficios:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Licenças:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Sair"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Relatorio de desempenho mensal:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Relatorios de pagamento:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Cadastrar Dados"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Quantidade de faltas no mês:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sem Beneficios"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Adicional noturno"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vale transporte"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Férias remuneradas"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Sem Licenças"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Licença-paternidade"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Licença médica"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Licença-maternidade"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_3.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_3.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_3.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_3.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_3.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_3.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_3.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_3.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_3.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_3.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_3.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_3.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_3.setItemText(31, _translate("MainWindow", "31"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cargo:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Departamento:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Data de admissão:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Salario:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Id:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Atualizar Dados"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nome:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Telaadministrador()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())