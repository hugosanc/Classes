#!/usr/bin/env python
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

periodo={"Mercúrio":0.241,"Vênus":0.615,"Terra":1,"Marte":1.88,"Júpiter":11.86,"Saturno":29.5,"Urano":84,"Plutão":248}
distancia={"Mercúrio":0.387,"Vênus":0.723,"Terra":1,"Marte":1.523,"Júpiter":5.202,"Saturno":9.539,"Urano":19.18,"Plutão":39.44}

p=[t**2 for t in periodo.values()]
d=[x**3 for x in distancia.values()]

ax=plt.gca()
plt.yscale('log')
plt.xscale('log')
ax.autoscale()

plt.rc('text',usetex=True)
plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
plt.xlabel(r'\textnormal{$r^3$} (UA)')
plt.ylabel(r'\textnormal{$T^2$} (anos)')
plt.title(r'\ntextnormal{Lei de Kepler}')

plt.plot(p,d,'blue',linewidth=2)
plt.grid()
plt.savefig("kepler.pdf",dpi=96)
plt.show()
