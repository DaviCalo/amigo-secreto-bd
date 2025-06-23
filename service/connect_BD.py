import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class ConnectBD:
    def __init__(self, user, password, host, port, database):
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._database = database
        self._connection = None
        self.starter()

    def open_connect(self):
        self._connection = psycopg2.connect(user=self._user, password=self._password,
                                           host=self._host, port=self._port, database=self._database)
        return self._connection

    def close_connection(self):
        self._connection.close()

    def starter(self):
        conn = None
        try:
            self.create_data_base()
            self.create_table_user()

        except psycopg2.Error as e:
            print("Erro no stater")
            print(e)


    def create_data_base(self):
        conn = psycopg2.connect(user=self._user, password=self._password, host=self._host, port=self._port)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        try:
            cur.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), (self._database,))
            exists = cur.fetchone()

            if not exists:
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self._database)))
                print(f"Banco de dados '{self._database}' criado com sucesso.")
            else:
                print(f"Banco de dados '{self._database}' já existe.")

        except psycopg2.Error as e:
            print(f"Erro ao conectar ou criar banco de dados: {e}")
            if conn:
                conn.rollback()
        finally:
            cur.close()
            conn.close()


    def create_table_user(self):
        conn = self.open_connect()
        cur = conn.cursor()

        if self.table_exists('users') is True:
            return

        cur.execute("""
                    CREATE TABLE users (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        passkey VARCHAR(255),
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                    );
                    
                    CREATE INDEX idx_users_email ON users (email);
                    
                    CREATE OR REPLACE FUNCTION update_updated_at_column()
                    RETURNS TRIGGER AS $$
                    BEGIN
                    NEW.updated_at = NOW();
                    RETURN NEW;
                    END;
                    $$ LANGUAGE plpgsql;
                    
                    CREATE TRIGGER update_users_updated_at
                    BEFORE UPDATE ON users
                    FOR EACH ROW
                    EXECUTE FUNCTION update_updated_at_column();
                   """)

        conn.commit()
        self.close_connection()

    def table_exists(self, table_name):
        conn = self.open_connect()
        if conn is None:
            print("Could not establish database connection to check table existence.")
            return False

        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_schema = 'public' AND table_name = %s
                );
            """, (table_name,))
            exists = cur.fetchone()[0]
            return exists

        except psycopg2.Error as e:
            print(f"Error checking table existence for '{table_name}': {e}")
            return False
        finally:
            self.close_connection()