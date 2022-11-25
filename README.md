# Configurar RabbitMQ
sudo apt-get install rabbitmq-server
rabbitmq-plugins enable rabbitmq_management
Server: 0.0.0.0:5672
Management: 0.0.0.0:15672

# Configurar Virtualenv
## Com pyenv
```python
pyenv virtualenv 3.10.6 utfprds2022
pyenv local utfprds2022
```

## Sem pyenv
Garantido que funciona com Python 3.10.6
Qualquer outra versão, não é garantido
```python
python -m virtualenv utfprds2022
```

# Instalar Dependencias e Rodar Flask
```python
pip install -r requirements.txt
export FLASK_DEBUG=True
export FLASK_APP=main
flask run
```