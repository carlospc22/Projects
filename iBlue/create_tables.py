import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    # Conectando na maquina local a database iblue
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    # create sparkify database with UTF8 encoding
    # Criando a database sparkify e utilizando UTF8 enconding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute(
        "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    

    # close connection to default database
    
    conn.close()
    # connect to sparkify database
    # Conectando com a database sparkify 
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    conn.set_session(autocommit=True)
    cur= conn.cursor()
    
    
def drop_tables(cur, conn):
    
    # Executa o drop de todas as tabelas
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()    


def create_tables(cur, conn):
    
    # Executa a criação de todas as tabelas

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()    


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()    


if __name__ == "__main__":
    main()