#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

class Derivada:
	def __init__(self, x,funcao):
		self.x=x
		self.f=funcao
		
	def deriva(self):
		h=10**(-9)
		if self.f=="seno":
			return (np.sin(self.x+h)-np.sin(self.x))/h
		if self.f=="coseno":
			return (np.cos(self.x+h)-np.cos(self.x))/h
			
x=input("Informe o ponto:\n")
funcao=raw_input("Seno ou coseno?\n")
f1=Derivada(x,funcao)

print "Derivada de f(x):",f1.deriva()

