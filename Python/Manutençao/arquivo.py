# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:57:25 2019

@author: Orlando Freitas

"""
# Função para abrir arquivos de texto
def abrirArquivo(arquivo,modo):
    try:
        f = open (arquivo, modo)
        return f
        f.close()
    except:
        print ('Não existe arquivo')

# Função para gravar os dados no arquivo de texto
def arquivoGravar(arquivo,modo,lista,tam):
    f = abrirArquivo(arquivo,modo)
    for line in lista:
        linha = ''
        for elemento in line:
            linha = linha + str(elemento) + '\n' 
        linha = linha.replace('\n', '\t',tam) 
        f.write(linha)

# Função que returna em lista os dados do arquivo        
def lerArquivo(arquivo,modo):
    f = abrirArquivo(arquivo,modo)
    lista = []
    for line in f:
        line = line.replace('\n', '\t')
        lista.append(line.split('\t'))
    return lista    

# Função que vai carregar os dados referentes a um quarto
def carregarDados(arq,qtr):
    f = abrirArquivo(arq,'r')
    for i, line in enumerate(f):
        if i == qtr-1:
            line = line.replace('\n', '\t')
            line = line.split('\t')
            return line

# Função que separar os dados por mes referentes a um quarto
def carregarDadosAvaria(arq,qtr):
    lmes = []
    meses = ['/01/','/02/','/03/','/04/','/05/','/06/','/07/','/08/','/09/','/10/','/11/','/12/']
    for mes in meses:
        soma = 0.00
        contagem = 0
        m = []
        f = abrirArquivo(arq,'r')
        for line in f:
            line = line.replace('\n', '\t')
            line = line.split('\t')        
            if int(line[1]) == qtr:
                if line[5].find(mes) > 0:# .find(), vai procurar na string ocorrência igual ao mes
                    mObra = line[7].replace(',','.')#substituir a virgual por ponto para fazer o calculo
                    cMaterial = line[8].replace(',','.') 
                    soma += float(mObra)+float(cMaterial)
                    contagem += 1
        m.append(contagem)
        m.append(soma)
        lmes.append(m)
    return lmes
