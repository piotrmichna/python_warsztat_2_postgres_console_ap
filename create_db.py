import conection_db


class DbColumn(conection_db.Connection):
    COL_TYPE = ['serial', 'integer', 'varchar', 'timestamp']
    # COLTYPE_PARAM_DICT={}

    def __init__(self, name, col_type, col_param=None):
        self.col = {}

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