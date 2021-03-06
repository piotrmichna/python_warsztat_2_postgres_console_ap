import conection_db


class DbColumn(conection_db.Connection):
    COL_TYPE = ['serial', 'integer', 'varchar', 'timestamp']

    # COLTYPE_PARAM_DICT={}

    def __init__(self, name, col_type, col_param=None):
        self.col = {}
        self.add_column(name, col_type, col_param)

    def is_column(self, col_type):
        if col_type in self.COL_TYPE:
            return True
        else:
            return False

    def add_column(self, name, typ, param=None):
        if self.is_column(typ):
            self.col['name'] = name
            self.col['type'] = typ
            self.col['param'] = param
        else:
            raise ValueError("Parametry kolumny nie prawidłowe!")

    def get_column(self):
        if len(self.col) > 0:
            result = str(f"{self.col['name']} {self.col['type']}")
            if self.col['param']:
                result += str(f" {self.col['param']}")
            return result
        else:
            return ""


class DbTable(DbColumn):
    def __init__(self, name):
        self.name = name
        self.tab_col = []
        self.created = False

    def column_add(self, name, col_type, col_param=None):
        if super().is_column(col_type):
            self.tab_col.append(DbColumn(name, col_type, col_param))
        else:
            print(f'  > column_add > Nieprawidłowy typ kolumny: {col_type}')

    def get_table_sql(self):
        if len(self.tab_col) > 0:
            str_table = f"CREATE TABLE {self.name}(\n"
            n = 0
            for col in self.tab_col:
                str_table += col.get_column()
                n += 1
                if n < len(self.tab_col):
                    str_table += ',\n'
            return str_table + ')'
        else:
            return False

    def is_table_created(self):
        return self.created

    def crate_table(self):
        if self.created is not True:
            query = self.get_table_sql()
            if query:
                conn = super().connect()
                if conn is not None:
                    cur = conn.cursor()
                    try:
                        cur.execute(query)
                        print(f"Utworzono table {self.name}")
                    except Exception as e:
                        print(f"Tabla o nazwie: {self.name} już istnieje.")
                    self.created = True
                    super().disconnect(conn)


def db_create_user():
    user_table = DbTable('users')
    user_table.column_add('id', 'serial', 'primary key')
    user_table.column_add('username', 'varchar', '(255) UNIQUE')
    user_table.column_add('hashed_password', 'varchar', '(80)')
    user_table.crate_table()
    return user_table


def db_create_messages():
    messages_table = DbTable('messages')
    messages_table.column_add('id', 'serial', 'primary key')
    messages_table.column_add('from_id', 'integer', 'REFERENCES users(id) ON DELETE CASCADE')
    messages_table.column_add('to_id', 'integer', 'REFERENCES users(id) ON DELETE CASCADE')
    messages_table.column_add('text', 'varchar', '(250)')
    messages_table.column_add('creation_date', 'timestamp', 'DEFAULT CURRENT_TIMESTAMP')
    messages_table.crate_table()
    return messages_table
