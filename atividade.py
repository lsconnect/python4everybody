import sqlite3

con = sqlite3.connect('dbjogos.sqlite')
cur = con.cursor()

# Clear table data
cur.executescript('''
CREATE TABLE IF NOT EXISTS tb_plataformas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS tb_jogos (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    nome TEXT UNIQUE,
    ano INTEGER,
    valor REAL,
    plataforma_id INTEGER
);
''')


def printsection(s):
    s = "=< " + s + " >="
    while len(s) < 78:
        s = "=" + s + "="
    print(s)


while True:
    printsection("Sistema de Cadastro de Jogos")
    print("1 - Inserir Jogo")
    print("2 - Excluir Jogo")
    print("3 - Listar Jogos")
    print("0 - Sair")

    opcao = int(input("Digite a opcao desejada: "))
    if opcao == 1:
        printsection("Cadastrando Jogo")
        nome = input("Digite o nome: ")
        ano = int(input("Digite o ano: "))
        valor = float(input("Digite o valor: "))
        plataforma = input("Digite a plataforma: ")

        plataforma = plataforma.lower()
        cur.execute('''INSERT OR IGNORE INTO tb_plataformas (nome)
            VALUES (?) ''', (plataforma,))
        cur.execute('SELECT id FROM tb_plataformas WHERE nome = ? ', (plataforma,))
        plataforma_id = cur.fetchone()[0]
        print(plataforma_id)

        # Inserção de dados no array
        cur.execute('''INSERT OR REPLACE INTO tb_jogos (nome, ano, valor, plataforma_id)
            VALUES (?, ?, ?, ?)''', (nome, ano, valor, plataforma_id))
    elif opcao == 3:
        slct = '''SELECT tb_jogos.nome, tb_jogos.ano, tb_jogos.valor, tb_plataformas.nome FROM tb_jogos JOIN 
                  tb_plataformas ON tb_jogos.plataforma_id = tb_plataformas.id'''
        for row in cur.execute(slct):
            print(str(row[0]), row[1])

    con.commit()

