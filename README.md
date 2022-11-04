# Configurar Virtualenv
## Com pyenv
```python
pyenv virtualenv 3.10.6 utfprds2022
pyenv local utfprds2022
```

## Sem pyenv
```python
python -m virtualenv utfprds2022
```

# Instalar Dependencias e Rodar Flask
```python
pip install -r requirements.txt
export FLASK_DEBUG=True
export FLASK_APP=main
```