# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:50:13 2019

@author: Orlando Freitas

"""
import arquivo

class Funcionario:
    uID = 0
    lista = []
    def __init__(self,nome,morada,localidade,codP,pais,nacinalidade,dataN,dataA,telefone,cc,nif,dep):
        self.__idFunc = None
        self.__nome = nome
        self.__morada = morada
        self.__localidade = localidade
        self.__codigoPostal = codP
        self.__pais = pais
        self.__nacinalidade = nacinalidade
        self.__dataNascimento = dataN
        self.__dataAdmissao = dataA
        self.__telefone = telefone
        self.__cc = cc
        self.__nif = nif
        self.__departamento = dep
   
    def guardarFuncionario(self):
        self.__class__.uID += 1
        self.__idFunc = self.__class__.uID
        self.__class__.lista.append(self)    
                
    def get_idFuncionario(self):
        return self.__idFunc
    def get_nome(self):
        return self.__nome
    def get_morada(self):
        return self.__morada
    def get_localidade(self):
        return self.__localidade
    def get_codigoPostal(self):
        return self.__codigoPostal
    def get_pais(self):
        return self.__pais
    def get_nacinalidade(self):
        return self.__nacinalidade
    def get_dataNascimento(self):
        return self.__dataNascimento
    def get_dataAdmissao(self):
        return self.__dataAdmissao
    def get_telefone(self):
        return self.__telefone
    def get_cc(self):
        return self.__cc
    def get_nif(self):
        return self.__nif
    def get_departamento(self):
        return self.__departamento
    
    def get_listaNomeFuncionario(self,i):
        return self.__class__.lista[i].get_nome()
    
    def print(self):
        print("Nº Funcionario ",self.__idFunc)
        print("Nome ",self.__nome)
        print("Morada ",self.__morada)
        print("Localidade ",self.__localidade)
        print("Codigo Postal ",self.__codigoPostal)
        print("Pais ",self.__pais)
        print("Nacinalidade ",self.__nacinalidade)
        print("Data Nascimento ",self.__dataNascimento)
        print("Data Admissao ",self.__dataAdmissao)
        print("Telefone ",self.__telefone)
        print("CC ",self.__cc)
        print("NIF ",self.__nif)
        print("Departamento ",self.__departamento)
        
    def verFuncionariosTodos(self):
        for i in range(len(self.__class__.lista)):
            print(self.__class__.lista[i].print()) 
        
    def procuraFuncionarioID(self,idF):
        print(self.__class__.lista[idF-1].print())
                
    def procuraFuncionarioNome(self,nome):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_nome() == nome):
                print(self.__class__.lista[i].print())
                
    def procuraFuncionarioDep(self,dep):
        for i in range(len(self.__class__.lista)):
            if(self.__class__.lista[i].get_departamento() == dep):
                print(self.__class__.lista[i].print())

    def procurarFuncionario(self,esc):   
        if esc == 'idFuncionario':
            procID = int(input('Qual ID de procura? '))
            self.procuraFuncionarioID(procID)
        elif esc == 'Nome':
            procNome = input('Qual nome de procura? ')
            self.procuraFuncionarioNome(procNome)
        elif esc == 'Departamento':
            procDep = input('Qual departamento de procura? ')
            self.procuraFuncionarioDep(procDep)
        elif esc == 'Todos':
            self.verFuncionariosTodos()
        else:
            self.procurarFuncionario()
    
    def criarfuncionario(self):
        nome = input("Nome ")
        morada = input("Morada ")
        localidade = input("Localidade ")
        codP = input("Codigo Postal '0000-000' ")
        pais = input("Pais ")
        nacinalidade = input("Nacinalidade ")
        dataN = input("Data Nascimento 'd/m/Y, H:M:S' ")
        dataA = input("Data Admissao %d/%m/%Y, %H:%M:%S ")
        telefone = input("Telefone ")
        cc = input("CC ")
        nif = input("NIF ")
        dep = input("Departamento ")
        f = Funcionario(nome,morada,localidade,codP,pais,nacinalidade,dataN,dataA,telefone,cc,nif,dep)
        f.guardarFuncionario()
  
    def listaFuncionario(self):       
        arqlista = []
        for i in range(len(self.__class__.lista)):
            linha = []
            linha.append(self.__class__.lista[i].get_idFuncionario())
            linha.append(self.__class__.lista[i].get_nome())
            linha.append(self.__class__.lista[i].get_morada())
            linha.append(self.__class__.lista[i].get_localidade())
            linha.append(self.__class__.lista[i].get_codigoPostal())
            linha.append(self.__class__.lista[i].get_pais())
            linha.append(self.__class__.lista[i].get_nacinalidade())
            linha.append(self.__class__.lista[i].get_dataNascimento())
            linha.append(self.__class__.lista[i].get_dataAdmissao())
            linha.append(self.__class__.lista[i].get_telefone())
            linha.append(self.__class__.lista[i].get_cc())
            linha.append(self.__class__.lista[i].get_nif())
            linha.append(self.__class__.lista[i].get_departamento())
            arqlista.append(linha)    
        return arqlista
    
    def arquivarFuncionario(self):
        lista = self.listaFuncionario()
        arquivo.arquivoGravar('funcionarios.txt','w',lista,12) 

    def carregarArquivo(self):
        lista = arquivo.lerArquivo('funcionario.txt','r')
        for line in lista:
            nome = line[1]
            morada = line[2]
            localidade = line[3]
            codP = line[4]
            pais = line[5]
            nacinalidade = line[6]
            dataN = line[7]
            dataA = line[8]
            telefone = line[9]
            cc = line[10]
            nif = line[11]
            dep = line[12]
            f=Funcionario(nome,morada,localidade,codP,pais,nacinalidade,dataN,dataA,telefone,cc,nif,dep)
            f.guardarFuncionario()
        print('arquivo carregado')  
        
    def mFuncionario(self,esc,op):    
        if esc == 'Procurar Funcionario':
            self.procurarFuncionario(op)
        elif esc == 'Criar Funcionario':
            self.criarfuncionario()
        elif esc == 'Aquivar Funcionario':
            self.arquivarFuncionario()
        else:
            print('Escolha não existe')