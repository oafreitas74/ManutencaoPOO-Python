# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:57:25 2019

@author: Orlando Freitas

"""
import arquivo

class Quarto:
    lista = []
    def __init__(self,mes,nQuarto,nAvarias,agua,luz,cAvarias):
        self.__mes = mes
        self.__nQuarto = nQuarto
        self.__nAvarias = nAvarias
        self.__consumoAgua = agua
        self.__consumoLuz = luz
        self.__custoAvarias = cAvarias

    def guardarQuarto(self):
        self.__class__.lista.append(self)    

    def get_nQuarto(self):
        return self.__nQuarto
    def get_mes(self):
        return self.__mes
    def get_nAvarias(self):
        return self.__nAvarias
    def get_consumoAgua(self):
        return self.__consumoAgua
    def get_consumoLuz(self):
        return self.__consumoLuz
    def get_custoAvarias(self):
        return self.__custoAvarias

    def print(self):
        print("Quarto ",self.__nQuarto)
        print("Mes ",self.__mes)
        print("Nº Avarias ",self.__nAvarias)
        print("Consumo Agua ",self.__consumoAgua)
        print("Consumo Luz ",self.__consumoLuz)
        print("Custo Avarias ",self.__custoAvarias)
        
    def verQuarto(self):
        for i in range(len(self.__class__.lista)):
            print(self.__class__.lista[i].print()) 
        

                
    def relatorioQuarto(self):
        n = int(input('Qual o nº do quarto? '))
        listaLuz = arquivo.carregarDados('luz.txt',n)
        listaAgua = arquivo.carregarDados('agua.txt',n)
        listaAvaria = arquivo.carregarDadosAvaria('avaria.txt',n)
        listaMes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        SnAvarias=0
        Sagua=0
        Sluz=0
        ScAvarias = 0
        for i in range(12):
            mes = listaMes[i]
            luz = listaLuz[i]
            Sluz += int(listaLuz[i])
            agua = listaAgua[i]
            Sagua += int(listaAgua[i])
            nAvarias = listaAvaria[i][0]
            SnAvarias += int(listaAvaria[i][0])
            cAvarias = listaAvaria[i][1]
            ScAvarias += listaAvaria[i][1]
            q = Quarto(mes,n,nAvarias,agua,luz,cAvarias)
            q.guardarQuarto()
        q = Quarto('Totais Ano',n,SnAvarias,Sagua,Sluz,ScAvarias)
        q.guardarQuarto()    
        self.verQuarto()  
