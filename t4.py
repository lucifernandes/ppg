import matplotlib.pyplot as plt
import numpy as np
import scipy.io
from scipy.signal import find_peaks

mat = scipy.io.loadmat('5.mat')
for i in mat:
    if '__' not in i and 'readme' not in i:
        np.savetxt('files.csv', mat['ppg_inv'], delimiter=',')

ppginvFile = open('files.csv', 'r')
ppginv = ppginvFile.read().split(',')  #Lista dos valores de cada amostra
tempo = [] #Lista com os valores pontuais de cada amostra durante a coleta de amostras

amostra = len(ppginv)
prf = 500  #Frequencia de Repeticao de Pulso / fs
t = (amostra/prf) #Tempo da amostragem varia de 0 a t / hrw...... em segundos.....

for i in range(amostra):
    #ppg.append(ppginv[i])
    tempo.append(i*t/amostra)
    ppginv[i] = float(ppginv[i])  #Mudando o tipo do valor ppg de str para int

y = np.array(ppginv)
x = np.array(tempo)
peaks, _ = find_peaks(ppginv, distance=290) #encontrando picos
np.diff(peaks)

plt.plot(tempo, ppginv)
plt.plot(x[peaks], y[peaks], "x")
plt.show()

xt = []
xt = x[peaks]
dt = []
i = 1
while(i<len(xt)):
    dt.append(xt[i]-xt[i-1])
    i = i+1

media = sum(dt)/len(dt)
vfc = 60/media #bpm
print("Intervalos de tempo:",dt)
print("VFC:",vfc)


