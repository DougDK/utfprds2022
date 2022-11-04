pyenv virtualenv 3.10.6 ppb2026
pyenv local ppb2026
pip install -r requirements.txt

export FLASK_DEBUG=True
export FLASK_APP=main