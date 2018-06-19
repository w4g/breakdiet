#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Sistema que seleciona os alimentos do arquivo "output.xlsx" que contém uma fonte de nutriente específico e quantidade de calorias

usage:
$ breakdiet.py <nutrient> <kcal>

Ex:
$ breakdiet.py Carboidratos 100
'''
import pandas as pd
import sys


df = pd.read_excel("output.xlsx")

def substituir(selecionado, kcal):
	for each in selecionado.index:
		calcularQtd = int(kcal) * selecionado["Gramas"][each]
		calcularQtd = calcularQtd / selecionado["Calorias"][each]
		print "{}: {}g".format(each, int(calcularQtd))

def classifica(tipo, kcal):
	selecionado = df.loc[df['Tipo'] == tipo.title()] # Tipo (ex: Carboidratos)
	selecionado = selecionado.loc[df['Calorias'] < 1000] # Seleciona os alimentos com menos de 1000 kcal
	numAlimentos = selecionado["Calorias"].count() # Conta os encontrados. /\
	substituir(selecionado, int(kcal))

classifica(sys.argv[1], sys.argv[2])