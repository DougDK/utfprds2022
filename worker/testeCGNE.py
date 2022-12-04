import numpy as np
import math
from numpy import genfromtxt
import time
from PIL import Image
import pandas as pd

def teste_cgne(nome_sinal):
    inicio = time.time()

    iniciodeverdade = time.time()

    sinal_g = genfromtxt('C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/{}'.format(nome_sinal), delimiter=',')

    if(nome_sinal=="A-60x60-1.csv" or nome_sinal=="G-1.csv" or nome_sinal=="G-2.csv"):
        #matriz_h = genfromtxt('C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/modelos/H-1.csv', delimiter=',')
        pandas_dataframe = pd.read_csv("C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/modelos/H-1.csv", delimiter=",", header=None)
        matriz_h = pandas_dataframe.to_numpy()
        Linha_S = 794
        Coluna_N = 64

    if(nome_sinal=="A-30x30-1.csv" or nome_sinal=="g-30x30-1.csv" or nome_sinal=="g-30x30-2.csv"):
        #matriz_h = genfromtxt('C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/modelos/H-2.csv', delimiter=',')
        pandas_dataframe = pd.read_csv("C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/modelos/H-2.csv", delimiter=",", header=None)
        matriz_h = pandas_dataframe.to_numpy()
        Linha_S = 436
        Coluna_N = 64

    fim = time.time()
    print('import levou', fim - inicio)
    inicio = time.time()

    i = 0

    n=1
    s=1

    #calculo do ganho de sinal
    for n in range(Coluna_N):
        for s in range (Linha_S):
            gs = 100+((1/20)*s*math.sqrt(s))
            sinal_g[i] = sinal_g[i]*gs
            i=i+1


    #CGNE
    f = 0
    r = sinal_g
    Ht = np.transpose(matriz_h)
    p = np.matmul(Ht,r)
    erro = 1
    i = 0

    while (np.absolute(erro) > 0.0001) and (i<30):
        i = i+1
        rt = np.transpose(r)
        pt = np.transpose(p)
        fator_alfa = np.matmul(rt,r)
        denominador_alfa = np.matmul(pt,p)
        alfa = np.divide(fator_alfa, denominador_alfa)

        f = np.add(f,alfa*p)

        aH = alfa*matriz_h
        #aH = matriz_h*alfa
        r_anterior = r
        aHp = np.matmul(aH, p)
        r = np.subtract(r, aHp) 

        
        fator_beta = np.matmul(np.transpose(r), r)
        denominador_beta = np.matmul(np.transpose(r_anterior), r_anterior)
        beta = np.divide(fator_beta, denominador_beta)

        #calculo dos elementos que efetuam a soma que resultam em Pi+1
        e1 = np.matmul(Ht, r)
        e2 = beta*p
        p = np.add(e1, e2)

        #calculo do erro
        erro = np.subtract(np.linalg.norm(r), np.linalg.norm(r_anterior))
        
        
    print(erro)
    print(i)

    fim = time.time()
    print('tudo levou', fim - iniciodeverdade)
    fim = fim - iniciodeverdade
    if(nome_sinal=="A-30x30-1.csv" or nome_sinal=="g-30x30-1.csv" or nome_sinal=="g-30x30-2.csv"):
        f_imagem = np.reshape(f, (30, 30))
        im = Image.fromarray(f_imagem)
        im = im.convert('RGB')
        im.save("C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/imagensprocessadas/{}.jpeg".format(fim))
    
    if(nome_sinal=="A-60x60-1.csv" or nome_sinal=="G-1.csv" or nome_sinal=="G-2.csv"):
        f_imagem = np.reshape(f, (60, 60))
        im = Image.fromarray(f_imagem)
        im = im.convert('RGB')
        im.save("C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/imagensprocessadas/{}.jpeg".format(fim))

    print("pronto")
