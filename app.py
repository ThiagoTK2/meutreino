from flask import Flask, render_template, request, redirect, url_for, flash

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

@app.route('/submit-treino', methods=['POST'])
def submit_treino():
    # Aqui você pega os dados do formulário
    pesos = request.form.to_dict()
    
    # Exemplo de como você pode processar os pesos
    for key, value in pesos.items():
        print(f"Peso para série {key}: {value}")
        # Você pode salvar os pesos no banco de dados ou arquivo JSON aqui
    
    return redirect(url_for('treino'))


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

# Rota para a página 'Adicionar Novo Treino'
@app.route('/novo_treino')
def novo_treino():
    return render_template('novo_treino.html')


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


