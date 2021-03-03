import numpy as np
import matplotlib.pyplot as plt
import math

def calcula_umMembro(tempo, omega):
    return 1/2 + 2/math.pi *( np.sin(omega * tempo))

def calcula_tresMembros(tempo, omega):
    print("calcula_tresMembros()")
    print("tempo: ",tempo)
    print("omega: ",omega)
    print("omega*tempo: " ,omega * tempo)
    return 1/2 + 2/math.pi *( (np.sin(omega * tempo) + (1/3*np.sin(3* omega * tempo)) ))

def calcula_cincoMembros(tempo, omega):
    return 1/2 + 2/math.pi *( (np.sin(omega * tempo) + (1/3*np.sin(3* omega * tempo)) + (1/5*np.sin(5* omega * tempo)) + (1/7*np.sin(7* omega * tempo)) ))


ra = 28
freq = 100 * ra
'''
print('Amplitude')
amp = input()
print('Fase')
fase = input()
'''
omega = 2 * math.pi * freq
print('Passo')
passo = float(input() )
print('Tempo')
tempoFinal = float(input())

tempos = np.arange(0.0, tempoFinal, passo)   #retorna lista com valores de tempo no passo dado [tempo * 0.1 for x in range(0, 10)]
ft = calcula_tresMembros(tempos, omega) #calculando com 1 termo

print("tempos: ",tempos)
print("ft: ",ft)


plt.xlabel('x')  
plt.ylabel('f(x)')  
plt.title('Senoide')   
plt.grid(True)  
plt.plot(tempos,ft)
plt.show()