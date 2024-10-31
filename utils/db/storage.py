import psycopg2 as p2

class DatebaseManager:
    def __init__(self):
        try:
            self.info_db = {"user": "postgres",
                            "password": "qwerty",
                            "host": "127.0.0.1",
                            "port": "5432",
                            "database": "dz_bot_bd"}
            self.conn = p2.connect(**self.info_db)
            self.cur = self.conn.cursor()
            print("Ура")
        except:
            print("error")

    def create_db(self):
        self.query("CREATE DATABASE dz_bot_bd")

    def create_table(self):
        self.query('''CREATE TABLE IF NOT EXISTS all_homework 
                    (all_homework_id integer primary key NOT NULL,
                    lessons text NOT NULL,
                    description text NOT NULL,
                    deadline data NOT NULL,
                    format text NOT NULL,
                    image_date bytea NOT NULL)''')

    def query(self, arg, values=None):
        if values in None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def close(self):
        self.conn.close()
        self.cur.close()