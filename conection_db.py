import psycopg2


class Connection:
    CONNECTION_DB = {
        'workshop': {
            'HOST': 'localhost',
            'PORT': '5432',
            'USERNAME': 'postgres',
            'PASSWORD': 'coderslab',
            'DATABASE': 'workshop'
        },
        'admin': {
            'HOST': 'localhost',
            'PORT': '5432',
            'USERNAME': 'postgres',
            'PASSWORD': 'coderslab',
            'DATABASE': 'postgres'
        }
    }

    @classmethod
    def connect(cls, connection=CONNECTION_DB['workshop']):
        conn = False
        while conn is False:
            try:
                conn = psycopg2.connect(
                    user=connection['USERNAME'],
                    password=connection['PASSWORD'],
                    host=connection['HOST'],
                    port=connection['PORT'],
                    dbname=connection['DATABASE']
                )
                conn.autocommit = True
            except psycopg2.OperationalError as error:
                print(f'Płąd połączenia:', error)
                if str(error).split(" ")[2] == 'database':
                    print(f"Tworzenie bazy danych {connection['DATABASE']}")
                    cls._db_create(connection['DATABASE'])
                else:
                    conn = None
        return conn

    @classmethod
    def disconnect(cls,cur):
        if cur:
            cur.close()

    @classmethod
    def _db_create(cls, db_name):
        connection = cls.CONNECTION_DB['admin']
        conn = psycopg2.connect(
            user=connection['USERNAME'],
            password=connection['PASSWORD'],
            host=connection['HOST'],
            port=connection['PORT'],
            dbname=connection['DATABASE']
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE {db_name};")
        conn.close()


if __name__ == "__main__":
    connect_db = Connection()
    connect_db.connect()
