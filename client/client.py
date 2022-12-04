import requests
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO

#file_path='C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/sinais/A-60x60-1.csv'
#file_name=file_path.split('/')[-1].split('.')[0]

def enviar_sinal(file_path, algoritmo):
    files = {'sinal': open(file_path,'rb')}
    post_response = requests.post(
        url="http://127.0.0.1:5000/reconstrucaosinal",
        files=files,
        data={"tipo":algoritmo})
    return post_response

def receber_sinal(file_name):
    get_response = requests.get(url="http://127.0.0.1:5000/sinal", json={"nome":file_name})
    image = Image.open(BytesIO(get_response.content))
    plt.gray()
    plt.imshow(image)
    plt.show()

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

    #sinais de teste
    enviar_sinal(file_path_sinal_1, "CGNE")
    enviar_sinal(file_path_sinal_1, "CGNR")

    enviar_sinal(file_path_sinal_2, "CGNE")
    enviar_sinal(file_path_sinal_2, "CGNR")

    enviar_sinal(file_path_sinal_4, "CGNE")
    enviar_sinal(file_path_sinal_4, "CGNR")

    enviar_sinal(file_path_sinal_5, "CGNE")
    enviar_sinal(file_path_sinal_5, "CGNR")

    #sinais da prova
    enviar_sinal(file_path_sinal_3, "CGNE")
    enviar_sinal(file_path_sinal_3, "CGNR")

    enviar_sinal(file_path_sinal_6, "CGNE")
    enviar_sinal(file_path_sinal_6, "CGNR")


if __name__ == '__main__':
    main()