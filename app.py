
from flask import Flask, render_template, request, redirect, url_for, flash, session
import json

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'  # Necessária para usar flash messages

# Estrutura dos treinos com campo de peso
treinos = {
    1: {
        'nome': 'Treino de Peito e Tríceps',
        'exercicios': [
            {'nome': 'Supino Inclinado com Halters', 'series': 4, 'repeticoes': [30, 12, 12, 12], 'peso': [50, 70, 70, 70], 'video_url': 'videos/PeitoeTriceps/supino_inclinado_halters.mp4'},
            {'nome': 'Supino Inclinado com Barra', 'series': 3, 'repeticoes': 12, 'peso': [30, 40, 40], 'video_url': 'videos/PeitoeTriceps/supino_inclinado_barra.mp4'},
            {'nome': 'Fly inclinado', 'series': 3, 'repeticoes': 10, 'peso': [20, 25, 25], 'video_url': 'videos/PeitoeTriceps/supino_inclinado.mp4'}
        ]
    },
    2: {
        'nome': 'Treino de Pernas Posterior',
        'exercicios': [
            {'nome': 'Stiff', 'series': 4, 'repeticoes': 10, 'peso': [60, 80, 80, 80], 'video_url': 'static/videos/stiff.mp4'},
            {'nome': 'Cadeira flexora', 'series': 3, 'repeticoes': 12, 'peso': [40, 50, 50], 'video_url': 'static/videos/cadeira_flexora.mp4'},
            {'nome': 'Glúteo no cabo', 'series': 3, 'repeticoes': 12, 'peso': [15, 20, 20], 'video_url': 'static/videos/gluteo_cabo.mp4'}
        ]
    },
    3: {
        'nome': 'Treino de Costas e Bíceps',
        'exercicios': [
            {'nome': 'Puxada na frente', 'series': 4, 'repeticoes': 10, 'peso': [40, 60, 60, 60], 'video_url': 'static/videos/puxada_frente.mp4'},
            {'nome': 'Remada curvada', 'series': 3, 'repeticoes': 10, 'peso': [50, 70, 70], 'video_url': 'static/videos/remada_curvada.mp4'},
            {'nome': 'Rosca direta', 'series': 3, 'repeticoes': 12, 'peso': [20, 30, 30], 'video_url': 'static/videos/rosca_direta.mp4'}
        ]
    },
    4: {
        'nome': 'Treino de Ombro e Trapézio',
        'exercicios': [
            {'nome': 'Desenvolvimento', 'series': 4, 'repeticoes': 10, 'peso': [20, 30, 30, 30], 'video_url': 'static/videos/desenvolvimento.mp4'},
            {'nome': 'Elevação lateral', 'series': 3, 'repeticoes': 12, 'peso': [10, 15, 15], 'video_url': 'static/videos/elevacao_lateral.mp4'},
            {'nome': 'Encolhimento de ombros', 'series': 3, 'repeticoes': 12, 'peso': [40, 50, 50], 'video_url': 'static/videos/encolhimento_ombros.mp4'}
        ]
    },
    5: {
        'nome': 'Treino de Pernas Quadríceps',
        'exercicios': [
            {'nome': 'Agachamento', 'series': 4, 'repeticoes': 10, 'peso': [60, 80, 80, 80], 'video_url': 'static/videos/agachamento.mp4'},
            {'nome': 'Leg press', 'series': 3, 'repeticoes': 10, 'peso': [100, 120, 120], 'video_url': 'static/videos/leg_press.mp4'},
            {'nome': 'Extensão de pernas', 'series': 3, 'repeticoes': 12, 'peso': [40, 50, 50], 'video_url': 'static/videos/extensao_pernas.mp4'}
        ]
    },
}

usuarios = [
    {"id": 1, "username": "admin", "password": "senha123", "role": "admin", "treinos":[1,2,3]},
    {"id": 2, "username": "thiago", "password": "th9578", "role": "user", "treinos": [1,2,3,4,5]},
    {"id": 2, "username": "heloysa", "password": "helo2004", "role": "user", "treinos":[2,4,5]}
]


# Carregar usuários do arquivo JSON
try:
    with open('usuarios.json', 'r') as file:
        usuarios = json.load(file)["usuarios"]
except (FileNotFoundError, KeyError) as e:
    print("Erro ao carregar usuários:", e)
    usuarios = []

def encontrar_usuario(username):
    return next((user for user in usuarios if user["username"] == username), None)

@app.route('/submit-treino', methods=['POST'])
def submit_treino():
    pesos = request.form.to_dict()
    for key, value in pesos.items():
        print(f"Peso para série {key}: {value}")
    return redirect(url_for('treino'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/treino/<int:treino_id>')
def treino(treino_id):
    treino = treinos.get(treino_id)
    print("Treino encontrado:", treino)  # Adiciona esta linha para ver o valor de treino
    if treino is None:
        return "Treino não encontrado", 404
    return render_template('treino.html', treino=treino, treino_id=treino_id)


@app.route('/meus_treinos')
def meus_treinos():
    # Verifica se há uma lista de treinos na sessão
    if 'treinos' not in session or not session['treinos']:
        flash("Você não tem treinos definidos.")
        return redirect(url_for('login'))

    # Supondo que 'treinos' seja um dicionário global ou definido em algum lugar do seu código
    meus_treinos = [treinos[t] for t in session['treinos'] if t in treinos]

    return render_template('meus_treinos.html', meus_treinos=meus_treinos)


@app.route('/novo_treino')
def novo_treino():
    return render_template('novo_treino.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        usuario = encontrar_usuario(username)
        
        if usuario and usuario['senha'] == password:  # Alterado 'password' para 'senha'
            session['user_id'] = usuario['id']
            session['username'] = usuario['username']
            session['treinos'] = usuario.get('treinos', [])  # Defina os treinos do usuário
            return redirect(url_for('meus_treinos'))
        else:
            flash('Usuário ou senha incorretos. Tente novamente!')
            return redirect(url_for('login'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
