# lab2-sist-dist-ufrj
Laboratório 2 da disciplina de Sistemas Distribuídos da UFRJ

O objetivo deste Laboratório é desenvolver uma aplicação distribuída básica para aplicar os conceitos estudados sobre arquitetura de software em camada e arquitetura de sistema centralizada (cliente/servidor); e seguir praticando com a programação usando sockets.

A aplicação que vamos desenvolver consiste em contar as ocorrências das palavras em um arquivo texto.

• Entrada: usuário informa o nome do arquivo texto.

• Saída (com sucesso): a aplicação exibe a lista das 10 palavras mais encontradas no arquivo, ordenadas da mais frequente para a menos frequente, e o número de ocorrências de cada palavra.

• Saída (com erro): informa que o arquivo solicitado não foi encontrado.

Proposta de arquitetura de sistema:

1. Lado cliente: implementa a camada de interface com o usuário. O usuário poderá solicitar o processamento de um ou mais arquivos em uma única execução da aplicação: o programa espera pelo nome do arquivo, faz o processamento, retorna o resultado, e então aguarda um novo pedido de arquivo ou o comando de finalização.

2. Lado servidor: implementa a camada de processamento e a camada de acesso aos dados. Implemente um servidor iterativo, isto é, que trata as requisições 
de um cliente de cada vez, em um único fluxo de execução. Terminada a interação com um cliente, ele poderá voltar a esperar por nova conexão. Dessa forma, o programa do servidor fica em loop infinito.
