from flask import Flask, request, render_template, redirect

from Model import model1

app = Flask(__name__)

# Função para selecionar um item da lista de dicionários pelo ID
def listagem(lista: list, id: int):
    for i in lista:
        if i['id'] == id:
            return i
    raise ValueError("O item não foi encontrado na lista!")

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Páginas da Entidade Alunos

# Exibe a lista de Alunos
@app.route('/Aluno')
def lista_Alunos():
    All_Alunos = Aluno.select_aluno()
    return render_template('viewAlunos.html', Alunos=All_Alunos)

# Adiciona um novo Aluno
@app.route('/Aluno/novo', methods=['GET', 'POST'])
def add_aluno():
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona o novo aluno
        Aluno.add_aluno(data['nome'], data['idade'], data['matricula'])
        return redirect('/Aluno')
    return render_template('formAluno.html', title="Adicionar Novo Aluno", Aluno=None)

# Edita um Aluno existente
@app.route('/Aluno/editar/<int:id>', methods=['GET', 'POST'])
def edit_aluno(id):
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados do aluno
        Aluno.update_aluno(id, data['nome'], data['idade'], data['matricula'])
        return redirect('/Aluno')
    aluno = listagem(Aluno.select_aluno(), id)
    return render_template('formAluno.html', title="Editar Aluno", Aluno=aluno)

# Remove um Aluno da tabela
@app.route('/Aluno/remover/<int:id>', methods=['GET'])
def delete_aluno(id):
    Aluno.del_aluno(id)
    return redirect('/Aluno')

# Páginas da Entidade Professores

# Exibe a lista de Professores
@app.route('/Professor')
def lista_professores():
    All_Professores = Professor.select_professor()
    return render_template('viewProfessores.html', Professores=All_Professores)

# Adiciona um novo Professor
@app.route('/Professor/novo', methods=['GET', 'POST'])
def add_professor():
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona o novo professor
        Professor.add_professor(data['nome'], data['disciplina'])
        return redirect('/Professor')
    return render_template('formProfessor.html', title="Adicionar Novo Professor", Professor=None)

# Edita um Professor existente
@app.route('/Professor/editar/<int:id>', methods=['GET', 'POST'])
def edit_professor(id):
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados do professor
        Professor.update_professor(id, data['nome'], data['disciplina'])
        return redirect('/Professor')
    professor = listagem(Professor.select_professor(), id)
    return render_template('formProfessor.html', title="Editar Professor", Professor=professor)

# Remove um Professor da tabela
@app.route('/Professor/remover/<int:id>', methods=['GET'])
def delete_professor(id):
    Professor.del_professor(id)
    return redirect('/Professor')

# Páginas da Entidade Disciplinas

# Exibe a lista de Disciplinas
@app.route('/Disciplina')
def lista_disciplinas():
    All_Disciplinas = Disciplina.select_disciplina()
    return render_template('viewDisciplinas.html', Disciplinas=All_Disciplinas)

# Adiciona uma nova Disciplina
@app.route('/Disciplina/novo', methods=['GET', 'POST'])
def add_disciplina():
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona a nova disciplina
        Disciplina.add_disciplina(data['nome'], data['carga_horaria'])
        return redirect('/Disciplina')
    return render_template('formDisciplina.html', title="Adicionar Nova Disciplina", Disciplina=None)

# Edita uma Disciplina existente
@app.route('/Disciplina/editar/<int:id>', methods=['GET', 'POST'])
def edit_disciplina(id):
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados da disciplina
        Disciplina.update_disciplina(id, data['nome'], data['carga_horaria'])
        return redirect('/Disciplina')
    disciplina = listagem(Disciplina.select_disciplina(), id)
    return render_template('formDisciplina.html', title="Editar Disciplina", Disciplina=disciplina)

# Remove uma Disciplina da tabela
@app.route('/Disciplina/remover/<int:id>', methods=['GET'])
def delete_disciplina(id):
    Disciplina.del_disciplina(id)
    return redirect('/Disciplina')

# Páginas da Entidade Turmas

# Exibe a lista de Turmas
@app.route('/Turma')
def lista_turmas():
    All_Turmas = Turma.select_turma()
    return render_template('viewTurmas.html', Turmas=All_Turmas)

# Adiciona uma nova Turma
@app.route('/Turma/novo', methods=['GET', 'POST'])
def add_turma():
    professores = Professor.select_professor()
    disciplinas = Disciplina.select_disciplina()
    if request.method == "POST":
        data = request.form.to_dict()
        # Adiciona a nova turma
        Turma.add_turma(data['nome'], data['periodo'], data['professor_id'], data['disciplina_id'])
        return redirect('/Turma')
    return render_template('formTurma.html', title="Adicionar Nova Turma", Turma=None, Professores=professores, Disciplinas=disciplinas)

# Edita uma Turma existente
@app.route('/Turma/editar/<int:id>', methods=['GET', 'POST'])
def edit_turma(id):
    professores = Professor.select_professor()
    disciplinas = Disciplina.select_disciplina()
    if request.method == "POST":
        data = request.form.to_dict()
        # Atualiza os dados da turma
        Turma.update_turma(id, data['nome'], data['periodo'], data['professor_id'], data['disciplina_id'])
        return redirect('/Turma')
    turma = listagem(Turma.select_turma(), id)
    return render_template('formTurma.html', title="Editar Turma", Turma=turma, Professores=professores, Disciplinas=disciplinas)

# Remove uma Turma da tabela
@app.route('/Turma/remover/<int:id>', methods=['GET'])
def delete_turma(id):
    Turma.del_turma(id)
    return redirect('/Turma')

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')
