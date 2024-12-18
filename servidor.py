from flask import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/teste', methods=['POST'])
def mostrar_algo():
    return 'ACHOOUUUUUUU'

app.run(debug=True)