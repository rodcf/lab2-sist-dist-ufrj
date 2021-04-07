import socket as sock
from collections import Counter

HOST = '' # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORT = 5000 # porta onde chegarao as mensagens para essa aplicacao

NUMBER_OF_WORDS = 10 # numero de palavras mais encontradas desejado

# cria um socket para comunicacao
serverSocket = sock.socket() # valores default: socket.AF_INET, socket.SOCK_STREAM  

# vincula a interface e porta para comunicacao
serverSocket.bind((HOST,PORT))

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
serverSocket.listen(1)

while True:

    print('O servidor esta pronto para receber conexoes')

    # aceita a primeira conexao da fila (chamada pode ser BLOQUEANTE)
    connectionSocket, address = serverSocket.accept() # retorna um novo socket e o endereco do par conectado

    # imprime o par (IP,PORTA) da conexao 
    print('Conectado com: ', address)

    # depois de conectar-se, espera uma mensagem (chamada pode ser BLOQUEANTE)
    receivedMsg = connectionSocket.recv(2048) # argumento indica a qtde maxima de dados

    while receivedMsg:

        # transforma a mensagem recebida em bytes para string
        receivedMsgString = str(receivedMsg,encoding='utf-8')

        # imprime a mensagem recebida
        print('Mensagem recebida: ', receivedMsgString)

        # acrescenta o formato .txt no fim do nome do arquivo caso necessario
        if not receivedMsgString.endswith('.txt'):
            receivedMsgString += '.txt'

        try:
            # le o arquivo de nome igual a mensagem recebida
            with open('arquivos/' + receivedMsgString, 'rt') as txtFile:
                
                # instancia um dicionario do tipo Counter a partir da lista de palavras contidas no arquivo
                # onde cada par (chave, valor) representa uma palavra e o numero de vezes que ela aparece
                counter = Counter(txtFile.read().lower().split())

                # pega a lista das n palavras mais frequentes do dicionario, onde n é NUMBER_OF_WORDS
                mostCommonWords = counter.most_common(NUMBER_OF_WORDS)

                # transforma a lista de palavras mais frequentes em string
                msgToSend = str(mostCommonWords)

                # envia a lista de palavras mais frequentes para o cliente
                connectionSocket.send(bytes(msgToSend, encoding='utf-8'))

        # caso um arquivo com o nome requisitado nao seja encontrado, envia mensagem de erro para o cliente
        except FileNotFoundError:
            msgToSend = 'ERRO - Arquivo nao encontrado!'
            connectionSocket.send(bytes(msgToSend, encoding='utf-8'))
            
        # imprime a mensagem enviada
        print('Mensagem enviada: ', msgToSend)
        
        # espera uma nova mensagem (chamada pode ser BLOQUEANTE)
        receivedMsg = connectionSocket.recv(2048) # argumento indica a qtde maxima de dados
    
    # fecha o socket da conexao
    connectionSocket.close()
    
    # imprime mensagem de conexao encerrada
    print('Conexao encerrada com: ', address)