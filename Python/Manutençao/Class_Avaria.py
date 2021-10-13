# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:50:13 2019

@author: Orlando Freitas

"""

import arquivo
import datetime
import Class_Funcionario

class Avaria:
    uID = 0
    lista = []
    def __init__(self,nQuarto,nTecnico,descriçao,dataCriaçao,dataConclusao,material,custoMaterial,custoMObra,tempo,estado,nFuncionario):
        self.__idAvaria = ''
        self.__nQuarto = nQuarto
        self.__nTecnico= nTecnico
        self.__descriçao = descriçao
        self.__dataCriaçao = dataCriaçao
        self.__dataConclusao = dataConclusao
        self.__material = material
        self.__custoMaterial = custoMaterial
        self.__custoMObra = custoMObra
        self.__tempo = tempo
        self.__estado = estado
        self.__nFuncionario = nFuncionario
 
    def guardarAvaria(self):
        self.__class__.uID += 1
        self.__idAvaria = self.__class__.uID
        self.__class__.lista.append(self)
    
    def get_idAvaria(self):
        return self.__idAvaria
    def get_nQuarto(self):
        return self.__nQuarto
    def get_nTecnico(self):
        return self.__nTecnico
    def get_descriçao(self):
        return self.__descriçao
    def get_dataCriaçao(self):
        return self.__dataCriaçao
    def get_dataConclusao(self):
        return self.__dataConclusao
    def get_material(self):
        return self.__material
    def get_custoMaterial(self):
        return self.__custoMaterial
    def get_custoMObra(self):    
        return self.__custoMObra
    def get_tempo(self):
        return self.__tempo
    def get_estado(self):
        return self.__estado
    def get_nFuncionario(self):
        return self.__nFuncionario

    def printAvariaCriada(self):
        print("IdAvaria: ",self.__idAvaria)
        print("Quarto: ",self.__nQuarto)
        print("Descriçao: ",self.__descriçao)
        print("Data Criaçao: ",self.__dataCriaçao)
        print("Estado: ",self.__estado)
        print("Quem fez pedido: ",self.__nFuncionario)
    
    def criarAvaria(self):
        nQuarto = int(input('Nº do Quarto '))
        nTecnico = ''
        descriçao = input('Descrição da Avaria ')
        data = datetime.datetime.now()
        dataCriaçao = data.strftime("%d/%m/%Y, %H:%M:%S")
        dataConclusao = ''
        material = ''
        custoMaterial = ''
        custoMObra = ''
        tempo = ''
        estado = 'Aberto'
        nFuncionario = int(input('Nº de Funcionario '))
        a = Avaria(nQuarto,nTecnico,descriçao,dataCriaçao,dataConclusao,material,custoMaterial,custoMObra,tempo,estado,nFuncionario)
        a.guardarAvaria()

    
    def finalizarAvaria(self,i,nTecnico,material,custoMaterial,tempo,custoMObra,estado):
        self.__class__.lista[i].__nTecnico = nTecnico
        self.__class__.lista[i].__material = material
        self.__class__.lista[i].__custoMaterial = custoMaterial
        self.__class__.lista[i].__tempo = tempo
        self.__class__.lista[i].__custoMObra = custoMObra
        self.__class__.lista[i].__estado = estado 
        if(self.__class__.lista[i].__estado == "Fechado"):
            data = datetime.datetime.now()
            self.__class__.lista[i].__dataConclusao = data.strftime("%d/%m/%Y, %H:%M:%S")
        else:
            self.__class__.lista[i].__dataConclusao = ""
        
    def printAvaria(self):
        f = Class_Funcionario.Funcionario('','','','','','','','','','','','')        
        print("IdAvaria: ",self.__idAvaria)
        print("Quarto: ",self.__nQuarto)
        ID = int(self.__nTecnico)
        print("Tecnico: ",f.get_listaNomeFuncionario(ID-1))
        print("Descriçao: ",self.__descriçao)
        print("Data Criaçao: ",self.__dataCriaçao)
        print("Material: ",self.__material)
        print("Custo Material: ",self.__custoMaterial)
        print("Custo MObra: ",self.__custoMObra)
        print("Tempo: ",self.__tempo)
        print("Estado : ",self.__estado) 
        if(self.__estado == "Fechado"):
            print("Data Conclusao: ",self.__dataConclusao)
        ID = int(self.__nFuncionario)
        print("Quem fez pedido: ",f.get_listaNomeFuncionario(ID-1))
        
    def verAvariasTodas(self):
        for i in range(len(self.__class__.lista)):
            print(self.__class__.lista[i].printAvaria()) 

    def procuraAvariaID(self,idA):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_idAvaria()==idA):
                print(self.__class__.lista[i].printAvaria())
                
    def procuraAvariaQuarto(self,quarto):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_nQuarto()==quarto):
                print(self.__class__.lista[i].printAvaria())
                
    def procuraAvariaFunc(self,func):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_nTecnico()==func):
                print(self.__class__.lista[i].printAvaria())
                
    def procuraAvariaEstado(self,est):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_estado()==est):
                print(self.__class__.lista[i].printAvaria())     
    
    def contarNAvariasQuarto(self,qtr):
        contagem = 0
        somaCusto = 0
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_nQuarto()==qtr):
                somaCusto =+ self.__class__.lista[i].get_custoMaterial()+self.__class__.lista[i].get_custoMObra()
                contagem =+ 1
        return contagem, somaCusto
    
    def listaAvarias(self):        
        arqlista = []
        linha = []
        for i in range(len(self.__class__.lista)):
            linha.clear()
            linha.append(self.__class__.lista[i].get_idAvaria())
            linha.append(self.__class__.lista[i].get_nQuarto())
            linha.append(self.__class__.lista[i].get_nTecnico())
            linha.append(self.__class__.lista[i].get_descriçao())
            linha.append(self.__class__.lista[i].get_dataCriaçao())
            linha.append(self.__class__.lista[i].get_dataConclusao())
            linha.append(self.__class__.lista[i].get_material())
            linha.append(self.__class__.lista[i].get_custoMaterial())
            linha.append(self.__class__.lista[i].get_custoMObra())
            linha.append(self.__class__.lista[i].get_tempo())
            linha.append(self.__class__.lista[i].get_estado())
            linha.append(self.__class__.lista[i].get_nFuncionario())
            arqlista.append(linha)        
        return arqlista
    
    def procurarAvaria(self,esc):
        if esc == 'idAvaria':
            procID = int(input('Qual ID de procura? '))
            self.procuraAvariaID(procID)
        elif esc == 'Quarto':
            procQta = input('Qual quarto de procura? ')
            self.procuraAvariaQuarto(procQta)
        elif esc == 'Funcionario':
            procFun = input('Qual funcionario de procura? ')
            self.procuraAvariaFunc(procFun)
        elif esc == 'Estado':
            op = int(input('Escolha uma opção.\n1- Aberto\n2- Fechado'))
            if op == 1:
                proEst = 'Aberto'
            else:
                proEst = 'Fechado'
            self.procuraAvariaEstado(proEst)
        elif esc == 'Todas':
            self.verAvariasTodas()
        else:
            self.procurarAvaria()
    
    def executarAvaria(self):
        uID = int(input('Qual o ID da avaria? '))
        uID = int(input('Qual o Nº do tecnico'))
        material = input('Qual material gasto? ')
        custoMaterial = int(input('Qual custo do material? '))
        tempo = int(input('Qual tempo de execução? '))
        custoMObra = tempo * 0.5
        op = int(input('Escolha uma opção.\n1- Aberto\n2- Fechado'))
        if op == 2:
            estado = 'Fechado'
        else:
            estado = 'Aberto' 
        self.finalizarAvaria(uID-1,material,custoMaterial,tempo,custoMObra,estado)
    
    def arquivarAvarias(self):
        lista = self.listaAvarias()
        arquivo.arquivoGravar('avaria.txt','w',lista,11)
         
    def carregarArquivo(self):
        lista = arquivo.lerArquivo('avaria.txt','r')
        for line in lista:
            nQuarto = line[1]
            nTecnico = line[2]
            descriçao = line[3]
            dataCriaçao = line[4]
            dataConclusao = line[5]
            material = line[6]
            custoMaterial = line[7]
            custoMObra = line[8]
            tempo = line[9]
            estado = line[10]
            nFuncionario = line[11]
            a=Avaria(nQuarto,nTecnico,descriçao,dataCriaçao,dataConclusao,material,custoMaterial,custoMObra,tempo,estado,nFuncionario)
            a.guardarAvaria()
        print('arquivo carregado')      
    
    def mAvaria(self,esc,op):    
        if esc == 'Procurar Avaria':
            self.procurarAvaria(op)
        elif esc == 'Criar Avaria':
            self.criarAvaria()
        elif esc == 'Executar Avaria':
            self.executarAvaria()
        elif esc == 'Arquivar Avarias':
            self.arquivarAvarias()
        else:
           print('Escolha não existe')
  
            