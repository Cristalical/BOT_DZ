import psycopg2 as p2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    connection = p2.connect(user="postgres",
                            password="qwerty",
                            host="127.0.0.1",
                            port="5432",
                            database="dz_bot_bd")
    # Создание изолированной среды для создания бд
    """
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    """
    # Курсор отвечающий за выполнение операций с бд
    cursor = connection.cursor()
    # Создание бд
    '''
    sql_create_db = "CREATE DATABASE dz_bot_bd "
    cursor.execute(sql_create_db)
    '''
    create_table_query = '''CREATE TABLE IF NOT EXISTS all_homework 
                          (all_homework_id integer primary key NOT NULL,
                          lessons text NOT NULL,
                          description text NOT NULL,
                          deadline date NOT NULL,
                          format text NOT NULL,
                          image_date bytea NOT NULL)'''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица была создана наверное)")
    # Вывод сведений о базе данных
    print("Информация о сервере базы данных...")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")
except (Exception, p2.Error) as error:
    print("Ошибка при работе с базой данных:", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с базой данных прервано...")