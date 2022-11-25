import numpy as np
import math
from numpy import genfromtxt
import time
from PIL import Image


def teste_cgne(nome_sinal):
    inicio = time.time()

    iniciodeverdade = time.time()

    sinal_g = genfromtxt('sinais/{}'.format(nome_sinal), delimiter=',')

    matriz_h = genfromtxt('modelos/H-2.csv', delimiter=',')

    print(sinal_g.shape)
    fim = time.time()
    print('import levou', fim - inicio)
    inicio = time.time()

    Linha_S = 436
    Coluna_N = 64
    i = 0

    n=1
    s=1

    #calculo do ganho de sinal
    for n in range(Coluna_N):
        for s in range (Linha_S):
            gs = 100+((1/20)*s*math.sqrt(s))
            sinal_g[i] = sinal_g[i]*gs
            i=i+1

    fim = time.time()
    print('calculo de ganho levou', fim - inicio)
    inicio = time.time()

    #CGNE
    f = 0
    r = sinal_g
    Ht = np.transpose(matriz_h)
    p = np.matmul(Ht,r)
    erro = 1
    i = 0

    fim = time.time()
    print('primeira iteracao levou', fim - inicio)
    inicio = time.time()

    while np.absolute(erro) > 0.0001:
        rt = np.transpose(r)
        pt = np.transpose(p)
        fator_alfa = np.matmul(rt,r)
        denominador_alfa = np.matmul(pt,p)
        alfa = np.divide(fator_alfa, denominador_alfa)

        f = np.add(f,alfa*p)

        aH = matriz_h*alfa
        r_anterior = r
        aHp = np.matmul(aH, p)
        r = np.subtract(r, aHp) 

        #calculo do erro
        fator_beta = np.matmul(np.transpose(r), r)
        denominador_beta = np.matmul(np.transpose(r_anterior), r_anterior)
        beta = np.divide(fator_beta, denominador_beta)

        #calculo dos elementos que efetuam a soma que resultam em Pi+1
        e1 = np.matmul(Ht, r)
        e2 = beta*p
        p = np.add(e1, e2)

        erro = np.subtract(np.linalg.norm(r), np.linalg.norm(r_anterior))
        print(erro)
        

    fim = time.time()
    print('tudo levou', fim - iniciodeverdade)

    f_imagem = np.reshape(f, (30, 30))
    im = Image.fromarray(f_imagem)
    im = im.convert('RGB')
    im.save("./imagensprocessadas/{}.jpeg".format(nome_sinal.split('.')[0]))

    print("pronto")
