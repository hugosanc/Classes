#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

class Planeta:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		
	def operacao(self,outro):
		return math.sqrt((self.x-outro.x)**2+(self.y-outro.y)**2)

print "\nPlaneta 1"		
x1=input("\nPosição em x:\n")
y1=input("\nPosição em y:\n")
p1=Planeta(x1,y1)
print "\nPlaneta 2"		
x2=input("\nPosição em x:\n")
y2=input("\nPosição em y:\n")
p2=Planeta(x2,y2)

print "\nDistancia entre os planetas:\n",p1.operacao(p2)
