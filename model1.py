import sqlite3

# Classe Table (superclasse):
class Table:
    def __init__(self):
        # Inicializa a conexão com o banco de dados e cria um cursor
        self.module = sqlite3
        self.conn = self.module.connect("schoolDB.db")
        self.cursor = self.conn.cursor()

    def close(self):
        # Fecha o cursor e a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()

# Classe Aluno:
class Aluno(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Aluno se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Aluno(
            id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_aluno VARCHAR(30) NOT NULL,
            idade_aluno INTEGER NOT NULL,
            serie_aluno VARCHAR(30) NOT NULL
        );""")
        self.conn.commit()

    def add_aluno(self, nome_aluno: str, idade_aluno: int, serie_aluno: str):
        # Insere um novo aluno na tabela Aluno
        self.cursor.execute("""
        INSERT INTO Aluno (nome_aluno, idade_aluno, serie_aluno)
        VALUES (?, ?, ?);
        """, (nome_aluno, idade_aluno, serie_aluno))
        self.conn.commit()

    def select_aluno(self):
        # Seleciona todos os alunos da tabela Aluno
        self.cursor.execute("SELECT * FROM Aluno;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_aluno': registro[1],
                'idade_aluno': registro[2],
                'serie_aluno': registro[3]})
        return registros

    def del_aluno(self, id: int):
        # Ativa chaves estrangeiras e deleta um aluno pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Aluno WHERE id_aluno = ?;", (id,))
        self.conn.commit()

    def update_aluno(self, id_aluno: int, nome_aluno: str, idade_aluno: int, serie_aluno: str):
        # Atualiza os dados de um aluno existente pelo id
        self.cursor.execute("""
            UPDATE Aluno SET nome_aluno = ?, idade_aluno = ?, serie_aluno = ?
            WHERE id_aluno = ?;
            """, (nome_aluno, idade_aluno, serie_aluno, id_aluno))
        self.conn.commit()

# Classe Professor:
class Professor(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Professor se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Professor(
            id_professor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_professor VARCHAR(30) NOT NULL,
            disciplina_professor VARCHAR(30) NOT NULL
        );""")
        self.conn.commit()

    def add_professor(self, nome_professor: str, disciplina_professor: str):
        # Insere um novo professor na tabela Professor
        self.cursor.execute("""
        INSERT INTO Professor (nome_professor, disciplina_professor)
        VALUES (?, ?);
        """, (nome_professor, disciplina_professor))
        self.conn.commit()

    def select_professor(self):
        # Seleciona todos os professores da tabela Professor
        self.cursor.execute("SELECT * FROM Professor;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_professor': registro[1],
                'disciplina_professor': registro[2]})
        return registros

    def del_professor(self, id: int):
        # Ativa chaves estrangeiras e deleta um professor pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Professor WHERE id_professor = ?;", (id,))
        self.conn.commit()

    def update_professor(self, id_professor: int, nome_professor: str, disciplina_professor: str):
        # Atualiza os dados de um professor existente pelo id
        self.cursor.execute("""
            UPDATE Professor SET nome_professor = ?, disciplina_professor = ?
            WHERE id_professor = ?;
            """, (nome_professor, disciplina_professor, id_professor))
        self.conn.commit()

# Classe Disciplina:
class Disciplina(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Disciplina se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Disciplina(
            id_disciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_disciplina VARCHAR(30) NOT NULL,
            carga_horaria INTEGER NOT NULL
        );""")
        self.conn.commit()

    def add_disciplina(self, nome_disciplina: str, carga_horaria: int):
        # Insere uma nova disciplina na tabela Disciplina
        self.cursor.execute("""
        INSERT INTO Disciplina (nome_disciplina, carga_horaria)
        VALUES (?, ?);
        """, (nome_disciplina, carga_horaria))
        self.conn.commit()

    def select_disciplina(self):
        # Seleciona todas as disciplinas da tabela Disciplina
        self.cursor.execute("SELECT * FROM Disciplina;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_disciplina': registro[0],
                'nome_disciplina': registro[1],
                'carga_horaria': registro[2]})
        return registros

    def del_disciplina(self, id: int):
        # Ativa chaves estrangeiras e deleta uma disciplina pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Disciplina WHERE id_disciplina = ?;", (id,))
        self.conn.commit()

    def update_disciplina(self, id_disciplina: int, nome_disciplina: str, carga_horaria: int):
        # Atualiza os dados de uma disciplina existente pelo id
        self.cursor.execute("""
            UPDATE Disciplina SET nome_disciplina = ?, carga_horaria = ?
            WHERE id_disciplina = ?;
            """, (nome_disciplina, carga_horaria, id_disciplina))
        self.conn.commit()

# Classe Turma:
class Turma(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Turma se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Turma(
            id_turma INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_turma VARCHAR(30) NOT NULL,
            ano_turma INTEGER NOT NULL
        );""")
        self.conn.commit()

    def add_turma(self, nome_turma: str, ano_turma: int):
        # Insere uma nova turma na tabela Turma
        self.cursor.execute("""
        INSERT INTO Turma (nome_turma, ano_turma)
        VALUES (?, ?);
        """, (nome_turma, ano_turma))
        self.conn.commit()

    def select_turma(self):
        # Seleciona todas as turmas da tabela Turma
        self.cursor.execute("SELECT * FROM Turma;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_turma': registro[0],
                'nome_turma': registro[1],
                'ano_turma': registro[2]})
        return registros

    def del_turma(self, id: int):
        # Ativa chaves estrangeiras e deleta uma turma pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Turma WHERE id_turma = ?;", (id,))
        self.conn.commit()

    def update_turma(self, id_turma: int, nome_turma: str, ano_turma: int):
        # Atualiza os dados de uma turma existente pelo id
        self.cursor.execute("""
            UPDATE Turma SET nome_turma = ?, ano_turma = ?
            WHERE id_turma = ?;
            """, (nome_turma, ano_turma, id_turma))
        self.conn.commit()

# Objetos de cada tabela:
# Cria instâncias de cada classe para interação com o banco de dados
obj_aluno = Aluno()
obj_professor = Professor()
obj_disciplina = Disciplina()
obj_turma = Turma()
