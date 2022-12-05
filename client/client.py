import requests
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO
import time
import os
import random


def enviar_sinal(file_path, algoritmo, usuario):
    files = {'sinal': open(file_path,'rb')}
    post_response = requests.post(
        url="http://127.0.0.1:5000/reconstrucaosinal",
        files=files,
        data={"tipo":algoritmo, "usuario":usuario})
    return post_response

def receber_sinal(file_name, usuario):
    get_response = requests.get(url="http://127.0.0.1:5000/sinal", json={"nome":file_name, "usuario":usuario})
    image = Image.open(BytesIO(get_response.content))
    image.save("geeks.jpg")
    plt.gray()
    plt.imshow(image)
    plt.show()

def listar_sinais(usuario):
    get_response = requests.get(url="http://127.0.0.1:5000/listarsinais", json={"usuario":usuario})
    return get_response.json()["sinais"]

def main():

    file_path_sinal_1='C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/g-30x30-1.csv'
    file_name_sinal_1=file_path_sinal_1.split('/')[-1].split('.')[0]

    file_path_sinal_2='C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/g-30x30-2.csv'
    file_name_sinal_2=file_path_sinal_2.split('/')[-1].split('.')[0]

    file_path_sinal_3='C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/A-30x30-1.csv'
    file_name_sinal_3=file_path_sinal_3.split('/')[-1].split('.')[0]

    file_path_sinal_4='C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/G-1.csv'
    file_name_sinal_4=file_path_sinal_4.split('/')[-1].split('.')[0]

    file_path_sinal_5='C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/G-2.csv'
    file_name_sinal_5=file_path_sinal_5.split('/')[-1].split('.')[0]

    file_path_sinal_6='C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/A-60x60-1.csv'
    file_name_sinal_6=file_path_sinal_6.split('/')[-1].split('.')[0]

    usuario = "caraLegal"

    inicio = time.time()

    intervaloDeTempoMin = 2
    intervaloDeTempoMax = 6

    tempocorrido = 0

    while tempocorrido<60:

        tempodeespera = random.randint(intervaloDeTempoMin,intervaloDeTempoMax)

        algoritmoparausar = random.randint(1,2)

        match algoritmoparausar:
            case 1:
                algoritmo = "CGNE"

            case 2:
                algoritmo = "CGNR"

        sinalparaenviar = random.randint(1,6)

        match sinalparaenviar:
            case 1:
                enviar_sinal(file_path_sinal_1, algoritmo, usuario)
                print("Algoritmo: ", algoritmo, "Sinal: ", file_name_sinal_1)
            case 2:
                enviar_sinal(file_path_sinal_2, algoritmo, usuario)
                print("Algoritmo: ", algoritmo, "Sinal: ", file_name_sinal_2)
            case 3:
                enviar_sinal(file_path_sinal_3, algoritmo, usuario)
                print("Algoritmo: ", algoritmo, "Sinal: ", file_name_sinal_3)
            case 4:
                enviar_sinal(file_path_sinal_4, algoritmo, usuario)
                print("Algoritmo: ", algoritmo, "Sinal: ", file_name_sinal_4)
            case 5:
                enviar_sinal(file_path_sinal_5, algoritmo, usuario)
                print("Algoritmo: ", algoritmo, "Sinal: ", file_name_sinal_5)
            case 6:
                enviar_sinal(file_path_sinal_6, algoritmo, usuario)
                print("Algoritmo: ", algoritmo, "Sinal: ", file_name_sinal_6)

        print("Espera de ", tempodeespera, " segundos")

        time.sleep(tempodeespera)

        tempocorrido = time.time()-inicio
        print("Duracao do teste:", tempocorrido)


    time.sleep(10)
    sinais = listar_sinais(usuario)

    print(sinais)

    #for sinal in sinais:
    #    receber_sinal(sinal, usuario)
        
    

if __name__ == '__main__':
    main()