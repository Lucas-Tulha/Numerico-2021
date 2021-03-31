#Módulos Necessários
import numpy as np
from matplotlib import pyplot as plt
from math import exp, cos, sin
#---------------------------------------------------------------------------------------------------

#Funções

#Calcula o passo para este n
def calcular_passo(T0, Tf, n):
    return (Tf - T0) / n

#Aproximar valores
def aproximar(valor):
    return int(valor *100000000) / 100000000

#Calcular valores de T que serão abordados neste intervalo
def calcular_lista_t(T0, Tf, h):
    lista_t = []
    t = T0

    while t <= Tf:
        lista_t.append(t)
        t = aproximar(t + h)

    return lista_t
#---------------------------------------------------------------------------------------------------

#RUNGE-KUTTA, nessa parte vao ficar todos os metodos pedidos como de Runge-Kutta

#Calcular taxa de crescimento de X num dado ponto
#(específico para o exercício 1.1)
def calcular_k1_1(x, A):
    return np.dot(A, x)

#Calcular próximo ponto com o desvio do método de Runge-Kutta de Ordem 4
def calcular_prox_ponto(x, k, h):
    return (h * k) + x

#Calcula uma lista de valores para x usando o Método de Runge-Kutta de Ordem 4
def RK4(x0, h, lista_t, A):
    #Inicia a lista de valores de vetores x
    lista_x = [x0]

    xi = x0

    for t in lista_t:
        #k1
        k1 = calcular_k1_1(xi, A)
        x_prov = calcular_prox_ponto(xi, k1, h / 2) #x provisório
        #k2
        k2 = calcular_k1_1(x_prov, A)
        x_prov = calcular_prox_ponto(xi, k2, h / 2)
        #k3
        k3 = calcular_k1_1(x_prov, A)
        x_prov = calcular_prox_ponto(xi, k3, h)
        #k4
        k4 = calcular_k1_1(x_prov, A)

        #média ponderada dos k
        kp = (k1 + 2*k2 + 2*k3 + k4) / 6

        #valor de x estimado para este t:
        x = calcular_prox_ponto(xi, kp, h)
        lista_x.append(x)

        #Atualiza o valor de xi para x
        xi = x

    return lista_x

#Calcula os erros de cada aproximação dos vetores x em cada t, tomando como erro
#a maior diferença entre cada um dos 4 valores de x explícito e aproximado
#(específico para o exercício 1.1)
def calcular_erros1_1(lista_x_exp, lista_x, lista_t):
    lista_erro = []

    for i in range(len(lista_t)):
        maior_erro = 0
        for j in range(0, 4):
            erro = abs(lista_x_exp[j](lista_t[i]) - lista_x[i][j])

            if erro >= maior_erro:
                maior_erro = erro

        lista_erro.append(maior_erro)

    return lista_erro, max(lista_erro)

#Resolve o exercício 1, iterando o cálculo do Método de Runge-Kutta e dos erros
#obtidos para cada n e plotando um gráfico
def exercicio1_1(T0, Tf, lista_n, x0, A, lista_x_exp):
    lista_erro_max = []
    for n in lista_n:
        #Parâmetros do intervalo
        h = calcular_passo(T0, Tf, n)
        lista_t = calcular_lista_t(T0, Tf, h)

        #Runge-Kutta de Ordem 4 para calcular os valores dos vetores x
        lista_x = RK4(x0, h, lista_t, A)

        #Cálculo dos erros, usando os valores explícitos de x, incluindo lista de maiores erros
        lista_erro, erro_max = calcular_erros1_1(lista_x_exp, lista_x, lista_t)
        lista_erro_max.append(erro_max)

        #Plotagem do Gráfico
        plt.plot(lista_t, lista_erro)
        plt.xlabel('t')
        plt.ylabel('Erro(t,n=' + str(n) + ')')
        plt.title('Erro dos valores aproximados de x para cada t num passo ' + str(h))
        plt.show()

    #Cálculo da Razão dos Erros
    lista_R = []
    for i in range (0,5):
        lista_R.append(lista_erro_max[i]/lista_erro_max[i+1])
        print("O valor de R"+str(i+1)+" eh igual a " +str(lista_R[i]))
    plt.show() #Essa parte é necessária?
#---------------------------------------------------------------------------------------------------

#Euler explicito, nessa parte vao ficar todos os metodos pedidos como de Euler explicito
def euler_exp():

    return

#Resolve o Exercício 2.2
def exercicio2_1(T0, Tf, n, x0, y0, derivadaX, derivadaY, plotar):
    #Parâmetros do intervalo
    h = calcular_passo(T0, Tf, n)
    lista_t = calcular_lista_t(T0, Tf, h)

    #Cálculo do Método de Euler Explícito
    lista_x = []
    lista_y = []







    #Plotagem do Gráfico
    if plotar:
        plt.plot(lista_t, lista_x, label = 'Coelhos', color = 'blue')
        plt.plot(lista_t, lista_y, label = 'Raposas', color = 'red')
        plt.title("Modelo presa predador com Euler Explícito e n = " + str(n))
        plt.show()
#---------------------------------------------------------------------------------------------------

########################EXERCICO 1 PARTE 2##########################################################

def exercicio1_2(T0, Tf, funcao_x, x0, A, derivada_x):
   
    n=5000
    h =  calcular_passo(T0, Tf, n)
    lista_T = calcular_lista_t(T0, Tf, h)
    
    for t in range 
    T = lista_T[i]
