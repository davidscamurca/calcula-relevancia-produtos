import sys

# Algoritmo: Ler arquivo > Calcula Pontuacao > Soma produtos duplicados > Ordena por pontuacao > Salva arquivo

# Verificando se os arquivos de entrada e saida foram especificados
if len(sys.argv) < 3:
    print ('Usar: ordenacaoProdutos.py <produto_vendas_visitas.txt> <produtos_ordenados.txt>')
    print ('AVISO: Utilize paths corretos, nao estou realizando tratamentos de excecao para os arquivos')
    sys.exit(0)

# Calculando a pontuacao de cada produto
def produtosScore(pontosVendas, pontosVisitas):
    return 2 * pontosVendas + pontosVisitas

# Criando uma lista com os dados.
def adicionarProdutosLista(outList):   
    # Abrindo arquivo de entrada em modo leitura
    arquivoEntrada = open(sys.argv[1],'r')

    # Percorrendo e separando os dados em variaveis
    for linha in arquivoEntrada:
        campos = linha.split(';')
        idProduto = campos[0]
        pontosVendas = campos[1]
        pontosVisitas = campos[2]
        # Adicionando produto com pontuacao calculada
        outList.append([idProduto, produtosScore(int(pontosVendas), int(pontosVisitas))])
    
    # Fechando o arquivo de entrada 
    arquivoEntrada.close()

# Somando pontos de vendas e visitas para IDs duplicados
def somarProdutosDuplicados(auxList):
    i = len(auxList) - 1 #Tamanho da Lista
    auxList.sort(key=lambda x: x[0], reverse=True) #OrdenandoPorID
    while i > 0:  
        if auxList[i][0] == auxList[i - 1][0]: # Verificando IDs duplicados
            auxList[i-1][1] = (auxList[i][1] + auxList[i - 1][1]) # Somando pontos IDs duplicados
            auxList.pop(i) # Retirando IDcorrent duplicado, deixando 1 com valores atualizados
        i -= 1

# Ordenando produtos que possuem a maior pontuacao
def ordenarProdutos(auxList):
    auxList.sort(key=lambda x: x[1], reverse=True) #MaiorParaMenor

# Salvando os dados no arquivo.
def salvarArquivoSaida(auxList):
    
    # Abrindo o arquivo de saida em modo escrita
    saida = open(sys.argv[2],'w')
    
    for item in auxList:
        saida.write(str(item[0]) + ';' + str(item[1]) + '\n') # Formato de saida (id;score)

    # Fechando o arquivo de saida
    saida.close()

# Lista auxiliar
auxList = []

# Alimentando a lista auxiliar
adicionarProdutosLista(auxList)

# Somando os valores dos produtos duplicados.
somarProdutosDuplicados(auxList)

# Ordenando os produtos
ordenarProdutos(auxList)

# Salvando no arquivo de saida
salvarArquivoSaida(auxList)