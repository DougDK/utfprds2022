import requests
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO

file_path='/home/douglas/Downloads/Sinal da imagem 1 (30 x 30 pixels).csv'
file_name=file_path.split('/')[-1].split('.')[0]

def enviar_sinal(file_path):
    files = {'sinal': open(file_path,'rb')}
    post_response = requests.post(url="http://127.0.0.1:5000/reconstrucaosinal", files=files)
    return post_response

def receber_sinal(file_name):
    get_response = requests.get(url="http://127.0.0.1:5000/sinal", json={"nome":file_name})
    image = Image.open(BytesIO(get_response.content))
    plt.gray()
    plt.imshow(image)
    plt.show()