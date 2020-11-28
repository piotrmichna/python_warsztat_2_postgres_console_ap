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

    def column_add(self, name, col_type, col_param=None):
        if super().is_column(col_type):
            self.tab_col.append(DbColumn(name, col_type, col_param))
        else:
            print(f'  > column_add > Nieprawidłowy typ kolumny: {col_type}')



if __name__ == "__main__":
    user_id = DbColumn('id', 'serial', 'primary key')
    print(user_id.get_column())
