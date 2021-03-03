import matplotlib.pyplot as plt
from numpy import arange, sin, cos, pi

# Variaveis de ambiente

#RA Aluno grupo exemplo
ra = 8
print("RA: " ,ra)

#Quantidade de termos
termLen = 1

#Frequencia de onda
frequency = 100*ra
print("Frequencia: " ,frequency)

#Valor de variavel omega
omega = 2*pi*frequency

#Valor inicial de tempo
tInicial = 0

#Valor final de tempo
tFinal = 10

#Valor de detalhamento de intervalo de escala
passo = 0.1

#termos da equacao
def getTermosEquacao(qtd_Termos):

    print("OMEGA: ",omega)
    expression  = 0.5

    s = []
    

    if qtd_Termos > 1:
        array = arange(tInicial, (tFinal+passo), passo)

        for tempo in array:
            expression  = (1/1)*(1*sin(omega*tempo))
            # print("EQ: (1/1)*(1*sin(", omega, " * " ,tempo, "))")
            # print("ENTRANDO NA CONDICAO")
            #range(inicio, final, saltos)
            for item in range(3, qtd_Termos*2, 2):
                # print(item)
                # print("EXPRESSION (",item,"): " ,expression)
                # print("EQ: (1/",item,")*(" ,item, "*sin(", omega, " * " ,tempo, "))")
                expression = expression + (1/item)*(item*sin(omega*tempo))
                # print("EQ: (1/",item,")*(" ,item, "*sin(", omega, " * " ,tempo, "))")
            
            # print("ADD NA LISTA S[]")
            s.append(0.5 + (2/pi)*expression)
    
        return s

    return expression
        

function = getTermosEquacao(2)
# x = arange(0, function, step)

y = arange(tInicial, (tFinal+passo), passo)

print("EQ FINAL: ",function)
print("Y: ",y)

# for item in y:
#     plt.plot(y, 0.5)

plt.grid(True)  
plt.plot(y, function)
plt.show()

