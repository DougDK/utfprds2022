import numpy as np
import math
from matplotlib import pyplot as plt
from numpy import genfromtxt
import time
from PIL import Image


def teste_cgnr(nome_sinal):
    inicio = time.time()

    iniciodeverdade = time.time()

    sinal_g = genfromtxt('sinais/{}'.format(nome_sinal), delimiter=',')

    matriz_h = genfromtxt('modelos/H-2.csv', delimiter=',')

    fim = time.time()
    print('import levou', fim - inicio)
    inicio = time.time()

    Linha_S = 436
    Coluna_N = 64
    i = 0

    s = 1
    n = 1

    #calculo do ganho de sinal
    for n in range(Coluna_N):
        for s in range (Linha_S):
            gs = 100+((1/20)*s*math.sqrt(s))
            sinal_g[i] = sinal_g[i]*gs
            i=i+1
            
    print(i)
    #CGNR
    f = 0
    r = sinal_g
    Ht = np.transpose(matriz_h)
    z = np.matmul(Ht,r)
    p = z
    erro = 1
    i = 0


    while np.absolute(erro) > 0.0001:
        w = np.matmul(matriz_h, p)
        norma_z = np.linalg.norm(z)
        norma_w = np.linalg.norm(w)
        fator_alfa = np.power(norma_z, 2)
        denominador_alfa = np.power(norma_w, 2)
        alfa = np.divide(fator_alfa, denominador_alfa)
        ap = np.dot(alfa, p)
        f = np.add(f, ap)
        aw = np.dot(alfa, w)
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
        p = np.add(z, np.dot(beta, p))
        print(erro)

    fim = time.time()
    print('tudo levou', fim - iniciodeverdade)

    f_imagem = np.reshape(f, (30, 30))
    im = Image.fromarray(f_imagem)
    im = im.convert('RGB')
    im.save("./imagensprocessadas/{}.jpeg".format(nome_sinal.split('.')[0]))
    
    print("pronto")