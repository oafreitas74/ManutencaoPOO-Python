# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:50:13 2019

@author: Orlando Freitas

"""
import arquivo

class Material:
    uID = 0
    lista = []
    def __init__(self,nome,qta,tipo,preçoCompra,preço):
        self.__idMat = None
        self.__nome = nome
        self.__qta = qta
        self.__tipo = tipo
        self.__preçoCompra = preçoCompra
        self.__preço = preço
        
    def guardarMaterial(self):
        self.__class__.uID += 1
        self.__idMat = self.__class__.uID
        self.__class__.lista.append(self)    
                
    def get_idMaterial(self):
        return self.__idMat
    def get_nome(self):
        return self.__nome
    def get_qta(self):
        return self.__qta
    def get_tipo(self):
        return self.__tipo
    def get_preçoCompra(self):
        return self.__preçoCompra
    def get_preço(self):
        return self.__preço

    def print(self):
        print('IdMaterial: ',self.__idMat)
        print('Nome: ',self.__nome)
        print('Quantidade: ',self.__qta)
        print('Tipo de Material: ',self.__tipo)
        print('Preço Compra: ',self.__preçoCompra)
        print('Preço: ',self.__preço)
    
    def verMateriaisTodos(self):
        for i in range(len(self.__class__.lista)):
            print(self.__class__.lista[i].print()) 
        
    def procuraMaterialID(self,idF):
        print(self.__class__.lista[idF-1].print())
                
    def procuraMaterialNome(self,nome):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_nome() == nome):
                print(self.__class__.lista[i].print())
                
    def procuraMaterialTipo(self,tipo):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_tipo() == tipo):
                print(self.__class__.lista[i].print())

    def procurarMaterial(self,esc):
    
        if esc == 'idMaterial':
            procID = int(input('Qual ID de procura? '))
            self.procuraMaterialID(procID)
        elif esc == 'Nome':
            procNome = input('Qual nome de procura? ')
            self.procuraMaterialNome(procNome)
        elif esc == 'Tipo':
            procTipo = input('Qual tipo de material de procura? ')
            self.procuraMaterialTipo(procTipo)
        elif esc == 'Todos':
            self.verMateriaisTodos()
        else:
            self.procurarMaterial()
            
    def inserirMaterial(self):
        nome = input("Nome ")
        qta = int(input("Quantidades "))
        tipo = input("Tipo de Material ")
        preçoCompra = int(input("Preço Compra "))
        mate = Material(nome,qta,tipo,preçoCompra,preçoCompra*1.3)
        mate.guardarMaterial()
    
    def listaMaterial(self):       
        arqlista = []
        for i in range(len(self.__class__.lista)):
            linha = []
            linha.append(self.__class__.lista[i].get_idMaterial())
            linha.append(self.__class__.lista[i].get_nome())
            linha.append(self.__class__.lista[i].get_qta())
            linha.append(self.__class__.lista[i].get_tipo())
            linha.append(self.__class__.lista[i].get_preçoCompra())
            linha.append(self.__class__.lista[i].get_preço())
            arqlista.append(linha) 
        return arqlista
    
    def arquivarMaterial(self):
        lista = self.listaMaterial()
        arquivo.arquivoGravar('material.txt','w',lista,5)

    def carregarArquivo(self):
        lista = arquivo.lerArquivo('material.txt','r')
        for line in lista:
            nome = line[1]
            qta = line[2]
            tipo = line[3]
            preçoCompra = line[4]
            preço = line[5]
            m = Material(nome,qta,tipo,preçoCompra,preço)
            m.guardarMaterial()
        print('arquivo carregado')    
        
    def mMaterial(self,esc,op):
        if esc == 'Procurar Material':
            self.procurarMaterial(op)
        elif esc == 'Inserir Material':
            self.inserirMaterial()
        elif esc == 'Arquivar Material':
            self.arquivarMaterial()
        else:
            print('Escolha não existe')