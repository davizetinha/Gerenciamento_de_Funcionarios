import socket

class Cliente:
    """
    Classe que representa um cliente que se conecta a um servidor usando sockets.
    
    ...

    Attributes
    ----------
    ip : str
        O endereço IP do servidor.
    port : int
        A porta de conexão do servidor.
    address : tuple
        A tupla contendo o endereço IP e a porta de conexão.
    cliente_socket : socket
        O objeto de socket usado para a conexão com o servidor.


    Methods
    -------
    __init__(self)
        Construtor da classe. Inicializa a classe do cliente.
        
    enviar(self, mensagem)
        Envia uma mensagem para o servidor e recebe a resposta.
    """

    def __init__(self):
        """
        Inicializa um objeto Cliente.

        Cria um socket de cliente e estabelece a conexão com o servidor.

        Attributes:
        ----------
            ip (str): O endereço IP do servidor.
            port (int): A porta do servidor.
            address (tuple): A tupla contendo o endereço IP e a porta do servidor.
            cliente_socket (socket): O socket de cliente usado para a comunicação com o servidor.
        """
        self.ip = '192.168.18.80'
        self.port = 8085
        self.address = (self.ip, self.port)
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente_socket.connect(self.address)

    def enviar(self, mensagem):
        """
        Envia uma mensagem para o servidor e retorna a resposta recebida.

        Parameters:
        ----------
            mensagem (str): A mensagem a ser enviada para o servidor.

        Returns:
        --------
            str: A resposta recebida do servidor.
        """
        
        self.cliente_socket.sendall(mensagem.encode())
        recebeu = self.cliente_socket.recv(1024).decode()
        if recebeu == '-1':  # sair
            self.cliente_socket.close()
        elif recebeu == '-2':  # desconectar
            self.cliente_socket.close()
        return recebeu
