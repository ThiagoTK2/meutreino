from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'  # Necessária para usar flash messages

# Estrutura dos treinos
treinos = {
    1: {
        'nome': 'Treino de Peito e Tríceps',
        'exercicios': [
            {'nome': 'Supino Inclinado', 'series': 4, 'repeticoes': [30, 12, 12, 12], 'video_url': 'static/videos/supino_inclinado.mp4'},
            {'nome': 'Tríceps na polia alta', 'series': 3, 'repeticoes': 12, 'video_url': 'static/videos/triceps_polia_alta.mp4'},
            {'nome': 'Fly inclinado', 'series': 3, 'repeticoes': 10, 'video_url': 'static/videos/fly_inclinado.mp4'}
        ]
    },
    2: {
        'nome': 'Treino de Pernas Posterior',
        'exercicios': [
            {'nome': 'Stiff', 'series': 4, 'repeticoes': 10, 'video_url': 'static/videos/stiff.mp4'},
            {'nome': 'Cadeira flexora', 'series': 3, 'repeticoes': 12, 'video_url': 'static/videos/cadeira_flexora.mp4'},
            {'nome': 'Glúteo no cabo', 'series': 3, 'repeticoes': 12, 'video_url': 'static/videos/gluteo_cabo.mp4'}
        ]
    },
    3: {
        'nome': 'Treino de Costas e Bíceps',
        'exercicios': [
            {'nome': 'Puxada na frente', 'series': 4, 'repeticoes': 10, 'video_url': 'static/videos/puxada_frente.mp4'},
            {'nome': 'Remada curvada', 'series': 3, 'repeticoes': 10, 'video_url': 'static/videos/remada_curvada.mp4'},
            {'nome': 'Rosca direta', 'series': 3, 'repeticoes': 12, 'video_url': 'static/videos/rosca_direta.mp4'}
        ]
    },
    4: {
        'nome': 'Treino de Ombro e Trapézio',
        'exercicios': [
            {'nome': 'Desenvolvimento', 'series': 4, 'repeticoes': 10, 'video_url': 'static/videos/desenvolvimento.mp4'},
            {'nome': 'Elevação lateral', 'series': 3, 'repeticoes': 12, 'video_url': 'static/videos/elevacao_lateral.mp4'},
            {'nome': 'Encolhimento de ombros', 'series': 3, 'repeticoes': 12, 'video_url': 'static/videos/encolhimento_ombros.mp4'}
        ]
    },
    5: {
        'nome': 'Treino de Pernas Quadríceps',
        'exercicios': [
            {'nome': 'Agachamento', 'series': 4, 'repeticoes': 10, 'video_url': 'static/videos/agachamento.mp4'},
            {'nome': 'Leg press', 'series': 3, 'repeticoes': 10, 'video_url': 'static/videos/leg_press.mp4'},
            {'nome': 'Extensão de pernas', 'series': 3, 'repeticoes': 12, 'video_url': 'static/videos/extensao_pernas.mp4'}
        ]
    },
}

# Usuário e senha fixos (para fins de teste)
USUARIO = 'admin'
SENHA = 'senha123'

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Rota para um treino específico
@app.route('/treino/<int:treino_id>')
def treino(treino_id):
    treino = treinos.get(treino_id)  # Retorna None se o ID não existir
    if treino is None:
        return "Treino não encontrado", 404
    return render_template('treino.html', treino=treino)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USUARIO and password == SENHA:
            return redirect(url_for('home'))  # Redireciona para a página inicial se o login for bem-sucedido
        else:
            flash('Usuário ou senha incorretos. Tente novamente!')
            return redirect(url_for('login'))  # Redireciona de volta ao login em caso de falha

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
