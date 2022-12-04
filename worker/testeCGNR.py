import numpy as np
import math
from matplotlib import pyplot as plt
from numpy import genfromtxt
import time
from PIL import Image
import pandas as pd

pandas_dataframe_h1 = pd.read_csv("C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/modelos/H-1.csv", delimiter=",", header=None)
pandas_dataframe_h2 = pd.read_csv("C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/modelos/H-2.csv", delimiter=",", header=None)

def teste_cgnr(nome_sinal):
    inicio = time.time()

    iniciodeverdade = time.time()

    sinal_g = genfromtxt('C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/{}'.format(nome_sinal), delimiter=',')

    if(nome_sinal=="A-60x60-1.csv" or nome_sinal=="G-1.csv" or nome_sinal=="G-2.csv"):
        matriz_h = pandas_dataframe_h1.to_numpy()
        Linha_S = 794
        Coluna_N = 64

    if(nome_sinal=="A-30x30-1.csv" or nome_sinal=="g-30x30-1.csv" or nome_sinal=="g-30x30-2.csv"):
        matriz_h = pandas_dataframe_h2.to_numpy()
        Linha_S = 436
        Coluna_N = 64

    fim = time.time()
    print('import levou', fim - inicio)
    inicio = time.time()


    i = 0

    s = 1
    n = 1

    #calculo do ganho de sinal
    for n in range(Coluna_N):
        for s in range (Linha_S):
            gs = 100+((1/20)*s*math.sqrt(s))
            sinal_g[i] = sinal_g[i]*gs
            i=i+1
            
    #CGNR
    f = 0
    r = sinal_g
    Ht = np.transpose(matriz_h)
    z = np.matmul(Ht,r)
    p = z
    erro = 1
    i = 0


    while (np.absolute(erro) > 0.0001 and i<30):
        i=i+1
        w = np.matmul(matriz_h, p)
        norma_z = np.linalg.norm(z)
        norma_w = np.linalg.norm(w)
        fator_alfa = np.power(norma_z, 2)
        denominador_alfa = np.power(norma_w, 2)
        alfa = np.divide(fator_alfa, denominador_alfa)
        ap = alfa*p
        f = np.add(f, ap)
        aw = alfa*w
        r_anterior = r
        r = np.subtract(r, aw)

        #calculo do erro
        erro = np.subtract(np.linalg.norm(r), np.linalg.norm(r_anterior))

        z_anterior = z
        z = np.matmul(Ht, r)
        norma_z = np.linalg.norm(z)
        norma_z_anterior = np.linalg.norm(z_anterior)
        fator_beta = np.power(norma_z, 2)
        denominador_beta = np.power(norma_z_anterior, 2)
        beta = np.divide(fator_beta, denominador_beta)


        #calculo dos elementos que efetuam a soma que resultam em Pi+1
        p = np.add(z, beta*p)


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