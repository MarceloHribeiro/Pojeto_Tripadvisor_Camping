import sqlite3
from sqlite3 import Error
from cores import Cores

def criar_tabelas(banco):
    
    conn = sqlite3.connect(banco)
    c = conn.cursor()

    try: 
        c.execute("""
        CREATE TABLE IF NOT EXISTS camping (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                descricao TEXT NOT NULL,
                nome TEXT NOT NULL
        );
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS endereco (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                logradouro TEXT NOT NULL,
                numero INTEGER,
                complemento TEXT NOT NULL,
				idcamping INTEGER NOT NULL,
                CONSTRAINT fk_camping FOREIGN KEY (idcamping) REFERENCES camping (id)
        );
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS infraestrutura (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
				idCamping INTEGER NOT NULL,
                CONSTRAINT fk_camping FOREIGN KEY (idCamping) REFERENCES camping (id)
        );
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS acomodacao (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                qtdPessoas INTEGER NOT NULL,
				idCamping INTEGER NOT NULL,
                CONSTRAINT fk_camping FOREIGN KEY (idCamping) REFERENCES camping (id)
        );
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS preco (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                valor INTEGER NOT NULL,
                descricao TEXT,
                idAcomodacao INTEGER NOT NULL,
                CONSTRAINT fk_acomodacao FOREIGN KEY (idAcomodacao) REFERENCES acomodacao (id)
        );
        """)
        
        return print(f"{Cores.BOLD}{Cores.OKGREEN}Tabelas criadas com sucesso!{Cores.ENDC}")
    except Error as e:
        print(e)

    conn.close()