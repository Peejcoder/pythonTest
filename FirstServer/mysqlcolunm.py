class mysqlC(object):
    column_name=''
    column_type=''
    column_isnull=''

    def __init__(self,column_name,column_type)  :
        self.column_name=column_name
        self.column_type=column_type
