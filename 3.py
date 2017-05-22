#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

class Planeta:
	def __init__(self,nome,massa,x,y):
		self.n=nome
		self.m=massa
		self.x=x
		self.y=y
		
	def distancia(self):
		return math.sqrt(self.x**2+self.y**2)
	
	def forcag(self):
		G=6.67408*10**(-11)
		ms=1.98892*10**(30)
		return G*ms*self.m/(self.distancia())**2
		
	def periodo(self):
		return math.sqrt(self.distancia()**3)
		
massa=input("Massa do planeta:\n")
nome=raw_input("Nome:\n")
x=input("\nPosição em x:\n")
y=input("\nPosição em y:\n")
p1=Planeta(nome,massa,x,y)

print "\nDistância do planeta ",p1.n,"ao Sol: ",p1.distancia(),"\nForça Gravitacional: ",p1.forcag(),"\nPeríodo de translação: ",p1.periodo()
