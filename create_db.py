import conection_db


class DbColumn(conection_db.Connection):
    COL_TYPE = ['serial', 'integer', 'varchar', 'timestamp']
    # COLTYPE_PARAM_DICT={}

    def __init__(self, name, col_type, col_param=None):
        self.col = {}