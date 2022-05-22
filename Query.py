class Query():

    def __init__(self):
        # init parameters
        self.parameters = []
        self.tables = []
        self.wheres = []
        self.query = "SELECT "

    def append_parameters(self, parameter):
        """receives parameters to append to the query"""
        """receives dict and checks which boxes are checked, then returns a query"""
        self.parameters.append(parameter)

    def get_parameters(self):
        return self.parameters

    def append_tables(self, table):
        # receives tables and sets them in the form 'table as ?'
        self.tables.append(table)

    def append_wheres(self, where):
        """receives parameters to append to the query"""
        """receives dict and checks which boxes are checked, then returns a query"""
        self.wheres.append(where)

    def get_query(self):
        # puts together query with everything
        if len(self.parameters) > 0:
            self.query += ', '.join(self.parameters)
        else:
            self.query += ' * '
        self.query += ' FROM '
        self.query += ', '.join(self.tables)
        if len(self.wheres) > 0:
            self.query += ' WHERE '
            self.query += ' AND '.join(self.wheres)
        print(self.query)
        return self.query
