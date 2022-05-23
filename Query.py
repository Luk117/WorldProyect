class Query():

    def __init__(self):
        # init parameters
        self.parameters = []
        self.tables = []
        self.wheres = []
        self.query = "SELECT "

    def append_parameters(self, parameters):
        """receives parameters to append to the query"""
        """receives dict and checks which boxes are checked, then returns a query"""
        if type(parameters) is list:
            for parameter in parameters:
                self.parameters.append(parameter)
        else:
            self.parameters.append(parameters)

    def get_parameters(self):
        return self.parameters

    def append_tables(self, tables):
        # receives tables and sets them in the form 'table as ?'
        if type(tables) is list:
            for table in tables:
                self.parameters.append(table)
        else:
            self.tables.append(tables)


    def append_wheres(self, where):
        """receives parameters to append to the query"""
        """receives dict and checks which boxes are checked, then returns a query"""
        self.wheres.append(where)

    def get_query(self):
        # puts together query with everything
        self.query += ', '.join(self.parameters)
        self.query += ' FROM '
        self.query += ', '.join(self.tables)
        if self.wheres:  # determine if wheres is empty
            self.query += ' WHERE '
            self.query += ' AND '.join(self.wheres)
        print(self.query)
        return self.query
