import psycopg2 as p2

class DatabaseManager:
    def __init__(self):
        try:
            # self.info_db = {
            #     "user": "myuser",
            #     "password": "Qwerty123",
            #     "host": "62.233.43.188",
            #     "port": "5432",
            #     "database": "dz_bot"
            # }
            self.info_db = {
                "user": "postgres",
                "password": "qwerty",
                "host": "127.0.0.1",
                "port": "5432",
                "database": "postgres"
            }
            self.conn = p2.connect(**self.info_db)
            self.cur = self.conn.cursor()
            print("Ура")
        except p2.Error as e:
            print("Error:", e)

    def create_db(self):
        try:
            conn = p2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres")
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute("CREATE DATABASE dz_bot_bd")
            cur.close()
            conn.close()
            print("Database created successfully")
        except p2.Error as e:
            print("Error creating database:", e)

    def create_table(self):
        self.query('''CREATE TABLE IF NOT EXISTS all_homework
                    (all_homework_id SERIAL PRIMARY KEY,
                    lessons TEXT NOT NULL,
                    description TEXT NOT NULL,
                    deadline DATE NOT NULL,
                    format TEXT NOT NULL,
                    image_date BYTEA)''')

    def query(self, arg, values=None):
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            self.conn.commit()
        except p2.Error as e:
            print("Error executing query:", e)

    def fetchone(self, arg, values=None):
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            return self.cur.fetchone()
        except p2.Error as e:
            print("Error fetching one:", e)

    def fetchall(self, arg, values=None):
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            return self.cur.fetchall()
        except p2.Error as e:
            print("Error fetching all:", e)

    def close(self):
        try:
            self.cur.close()
            self.conn.close()
            print("Connection closed")
        except p2.Error as e:
            print("Error closing connection:", e)

# Usage
# b = DatabaseManager()
# b.create_db()
# b.create_table()
# b.close()