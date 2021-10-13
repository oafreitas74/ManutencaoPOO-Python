# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:41:33 2019
@author: Orlando Freitas

"""

import Class_Funcionario
import Class_Avaria
import Class_Material
import Class_Quarto


def menuEscolha(lista,saida,texto,cabecalho,N):
    y = 1
    print(cabecalho.center(N,'=')) # cabeçalho centrado 
    for i in lista:
        print(y,'- >',i)
        y += 1
    print(y,'- >',texto)
    escolha = int(input('\nEscolha um da lista '))
    if escolha < -1 or escolha > y:
        print('Valor invalido ')
        # se a escolha não estiver dentro da lista apresentada, regressa ao inicio da função 
        menuEscolha(lista,saida,texto) 
        escolha = 0
    if escolha == y:
        if saida == 0:
            return texto 
        else:
            menuInicial() # regressar ao menu inicial
    else:
        return lista[escolha-1]

def sairAplicacao():
    print('A sair ...')
    
def relatorioQuarto():
    print('relatorio')
    
def menuInicial():
    texto = 'Voltar ao menu inicial'
    inicio = ['Funcionario','Avaria','Material','Relatorio Quarto']
    esc = menuEscolha(inicio, 0,'Sair da aplicação',' Menu Inicial ',50)
    op = ''
    if esc == 'Funcionario':
        inicio = ['Procurar Funcionario','Criar Funcionario','Arquivar Funcionario']
        esc = menuEscolha(inicio,  1,texto,' Funcionario ',50)       
        if esc == 'Procurar Funcionario':
            pFunc = ['idFuncionario','Nome','Departamento','Todos']
            op = menuEscolha(pFunc, 1, texto,' Procurar Funcionario ',50)
        funcionario.mFuncionario(esc,op)
        menuInicial()
    elif esc == 'Avaria':
        inicio = ['Procurar Avaria','Criar Avaria','Executar Avaria','Arquivar Avarias']
        esc = menuEscolha(inicio, 1, texto,' Avaria ',50)
        if esc == 'Procurar Avaria':  
            pAvaria = ['idAvaria','Quarto','Funcionario','Estado','Todas']
            op = menuEscolha(pAvaria, 1, texto,' Procurar Avaria ',50)
        avaria.mAvaria(esc,op)
        menuInicial()
    elif esc == 'Material':
        inicio = ['Procurar Material','Inserir Material','Arquivar Material']
        esc = menuEscolha(inicio, 1, texto,' Material ',50)
        if esc == 'Procurar Material': 
            pMaterial = ['idMaterial','Nome','Tipo','Todos']
            op = menuEscolha(pMaterial, 1, texto,' Procurar Material ',50)
        material.mMaterial(esc,op)
        menuInicial()
    elif esc == 'Relatorio Quarto':
        quarto.relatorioQuarto()
        menuInicial()    
    elif esc == 'Sair da aplicação':
        sairAplicacao()
    else:
        menuInicial()
        

material = Class_Material.Material('','','','','')
material.carregarArquivo()  
funcionario= Class_Funcionario.Funcionario('','','','','','','','','','','','')
funcionario.carregarArquivo()    
avaria = Class_Avaria.Avaria('','','','','','','','','','','')  
avaria.carregarArquivo()
quarto = Class_Quarto.Quarto('','','','','','')
menuInicial()