from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()  # obter segredo para sessao

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-default-key")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/etapas')
def etapas():
    return render_template('etapas.html')


@app.route('/checklist', methods=['GET', 'POST'])
def checklist():
    resultado = None
    if request.method == 'POST':
        diploma = 'tem_diploma' in request.form
        apostila = 'tem_apostila' in request.form
        traducao = 'tem_traducao' in request.form

        if not diploma:
            resultado = 'Obter seu diploma acadêmico.'
        elif not apostila:
            resultado = 'Apostilar seus documentos (Convenção de Haia).'
        elif not traducao:
            resultado = 'Fazer tradução juramentada dos documentos.'
        else:
            resultado = 'Você está pronto para dar entrada no Ministério da Educação Espanhol!'

    return render_template('checklist.html', resultado=resultado)


@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
