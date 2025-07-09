import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from service.DB.ConnectBD import ConnectBD

class DataBaseService:
    def __init__(self, connectBD: ConnectBD, database: str):
        self.connectBD = connectBD
        self._database = database
        self.starter()

    def starter(self):
        try:
            self.create_data_base()
            self.create_all_tables()

        except psycopg2.Error as e:
            print("Erro no stater")
            print(e)

    def create_data_base(self):
        conn = self.connectBD.create_connect()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        try:
            cur.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), (self._database,))
            exists = cur.fetchone()

            if not exists:
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self._database)))
                print(f"Banco de dados '{self._database}' criado com sucesso.")

        except psycopg2.Error as e:
            print(f"Erro ao conectar ou criar banco de dados: {e}")
            if conn:
                conn.rollback()

        finally:
            cur.close()
            conn.close()

    def create_table_user(self):
        conn, cur = self.connectBD.open_connect()

        if self.table_exists('users') is True:
            return

        cur.execute("""
                       CREATE TABLE users (
                           user_id SERIAL PRIMARY KEY,
                           name VARCHAR(255) NOT NULL,
                           email VARCHAR(255) UNIQUE NOT NULL,
                           passkey VARCHAR(255)
                       );
                      """)

        conn.commit()

        self.connectBD.close_connection()

    def create_table_groups(self):
        conn, cur = self.connectBD.open_connect()

        if self.table_exists('groups') is True:
            return

        cur.execute("""
                        CREATE TABLE groups (
                            group_id SERIAL PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            description TEXT,
                            status_group VARCHAR(50) NOT NULL,
                            maximum_value DECIMAL(10, 2),
                            minimum_value DECIMAL(10, 2),
                            draw_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                            meet_date TIMESTAMP WITHOUT TIME ZONE,
                            location VARCHAR(255),
                            created_user_id INTEGER NOT NULL,
                            
                            CONSTRAINT fk_creator
                                FOREIGN KEY (created_user_id)
                                REFERENCES users (user_id)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE
                        );
                         """)

        conn.commit()
        self.connectBD.close_connection()

    def create_table_gifts(self):
        conn, cur  = self.connectBD.open_connect()

        if self.table_exists('gifts') is True:
            return

        cur.execute("""
                        CREATE TABLE gifts (
                            gift_id SERIAL PRIMARY KEY,
                            gift_name VARCHAR(255) NOT NULL 
                        );
                         """)

        conn.commit()
        self.connectBD.close_connection()

    def create_table_users_groups(self):
        conn, cur = self.connectBD.open_connect()

        if self.table_exists('users_groups') is True:
            return

        cur.execute("""
                        CREATE TABLE users_groups (
                            user_group_id SERIAL PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            recipient_user_id INTEGER,
                            group_id INTEGER NOT NULL,
                            grift_select_id INTEGER,
                            
                            CONSTRAINT fk_ug_user
                                FOREIGN KEY (user_id)
                                REFERENCES users (user_id)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE,
                            
                            CONSTRAINT fk_ug_recipient_user
                                FOREIGN KEY (recipient_user_id)
                                REFERENCES users (user_id)
                                ON DELETE SET NULL
                                ON UPDATE CASCADE,
                            
                            CONSTRAINT fk_ug_group
                                FOREIGN KEY (group_id)
                                REFERENCES groups (group_id)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE,
                            
                            CONSTRAINT fk_ug_gift_select
                                FOREIGN KEY (grift_select_id)
                                REFERENCES gifts (gift_id)
                                ON DELETE SET NULL
                                ON UPDATE CASCADE,
                                
                            CONSTRAINT chk_user_recipient_not_equal
                                CHECK (user_id <> recipient_user_id)
                        );
                         """)

        conn.commit()
        self.connectBD.close_connection()

    def create_table_wish_list(self):
        conn, cur = self.connectBD.open_connect()

        if self.table_exists('wish_list') is True:
            return

        cur.execute("""
                        CREATE TABLE wish_list (
                            wish_list_id SERIAL PRIMARY KEY,
                            user_group_id INTEGER NOT NULL,
                            gift_id INTEGER NOT NULL,
            
                            CONSTRAINT fk_ug_users_groups
                                FOREIGN KEY (user_group_id)
                                REFERENCES users_groups (user_group_id)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE,
                                
                            CONSTRAINT fk_ug_gifts
                                FOREIGN KEY (gift_id)
                                REFERENCES gifts (gift_id)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE
                        );
                         """)

        conn.commit()
        self.connectBD.close_connection()

    def create_table_letters(self):
        conn, cur = self.connectBD.open_connect()

        if self.table_exists('letters') is True:
            return

        cur.execute("""
                        CREATE TABLE letters (
                            letter_id SERIAL PRIMARY KEY,
                            user_group_id INTEGER NOT NULL,
                            message TEXT,
                            
                            CONSTRAINT fk_ug_users_groups
                                FOREIGN KEY (user_group_id)
                                REFERENCES users_groups (user_group_id)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE
                        );
                         """)

        conn.commit()
        self.connectBD.close_connection()

    def create_all_tables(self):
        self.create_table_user()
        self.create_table_groups()
        self.create_table_gifts()
        self.create_table_users_groups()
        self.create_table_wish_list()
        self.create_table_letters()

    def table_exists(self, table_name):
        conn, cur = self.connectBD.open_connect()

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
            self.connectBD.close_connection()