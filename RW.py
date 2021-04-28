# Intento de RW
"""
deltaV = a*b(lambda-Vtot)
sin competencia de estímulos -> deltaV = k (lambda-V)
"""
import numpy as np
import matplotlib.pyplot as plt 
#import random
#sección donde se definen/toman los eventos
stimuli = [[1,1],
           [1,1],
           [1,1],
           [1,1],
           [1,0],
           [1,0],
           [1,0]] #ver si anda asi, sino por separado las listas
cs = [1,1,1,1,1,1,1,1,1,1]
us = [1,1,1,1,1,1,0,0,0,0]

#Aca empieza el algoritmo de aprendizaje
a = .2 # constante de aprendizaje uniestimular (si hay competencia de estimulos aca definir "a" y "b")
cs = np.array(cs)
us = np.array(us)
FA = np.zeros_like(cs) #FA es Fuerza Asociativa
magnitudEI = us*100
for t in range(0,len(us)-1): #pierdo el último ensayo porque sino se rompe al usar t+1 despues. Considerar "extender" la lista de ceros un valor al prealocar.
    sorpresa = magnitudEI[t] - FA[t]*cs[t] #esto seria el parentesis de la ecuasion
    delta = sorpresa * a
    FA[t+1] = FA[t] + delta * cs[t] #registro acumulado. se actualiza la FA esperada+la obtenida, solo si se presento el EC (no queremos que haya aprendizajes raros en la extincion)
    print(FA[t])
plt.plot(FA)
