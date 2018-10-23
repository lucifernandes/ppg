import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.io

ppginvFile = open('5_ppginv.txt', 'r')

ppginv = ppginvFile.read().split(',')

ppg = []   #Lista dos valores de cada amostra
ppgfinal = []
tempo = [] #Lista com os valores pontuais de cada amostra durante a coleta de amostras


prf = int(500)  #Frequencia de Repeticao de Pulso / fs
t = int(100/prf) #Tempo da amostragem varia de 0 a t / hrw

for i in range(100):
    ppg.append(ppginv[i])
    tempo.append(i*t/100)
    ppg[i] = float(ppg[i])*float(-1)   #Mudando o tipo do valor ppg de str para int
    ppg[i] = int(ppg[i])

print(ppginv)