import mysql.connector


class RegistroDatos():

    def __init__(self):
        password = input("password: ")
        self.conexion = mysql.connector.connect(host="localhost",
                                                database="world",
                                                user="root",
                                                passwd=password,
                                                autocommit=True)

    # -------------------------------Metodos de paises------------------------------------------------------------------
    def buscar(self, query):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def agrega_pais(self, codigoadd, nombrepadd, continenteadd, regionadd, surfaceareaadd, independenciaadd,
                    poblacionpadd, expectativaadd, gnpadd,
                    gnpoldadd, localnameadd, gobiernoadd, cabezadeestadoadd, capitaladd, codigo2add):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO country (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, 
        LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2) VALUES('{}', '{}','{}', 
        '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(codigoadd, nombrepadd, continenteadd,
                                                                               regionadd, surfaceareaadd,
                                                                               independenciaadd, poblacionpadd,
                                                                               expectativaadd, gnpadd, gnpoldadd,
                                                                               localnameadd, gobiernoadd,
                                                                               cabezadeestadoadd, capitaladd,
                                                                               codigo2add)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def elimina_pais(self, codigoel):
        cursor = self.conexion.cursor()
        sql = '''DELETE FROM country WHERE Code = {}'''.format(codigoel)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def actualiza_pais(self, codigoac, nombrepac, continenteac, regionac, surfaceareaac, idependenciaac, poblacionpac,
                       expectativaac,
                       gnpac, gnpoldac, localnameac, gobiernoac, cabezadeestadoac, capitalac, codigo2ac):
        cur = self.conexion.cursor()
        sql = '''UPDATE country SET Name = '{}', Continent = '{}', Region = '{}', SurfaceArea = {}, IndepYear = 
        {},Population = {}, LifeExpectancy = {}, GNP = {}, GNPOld = {}, LocalName = '{}', GovernmentForm= 
        '{}', HeadOfState = '{}', Capital = {}, Code2 = '{}' WHERE Code = '{}' '''.format(nombrepac, continenteac,
                                                                                          regionac, surfaceareaac,
                                                                                          idependenciaac, poblacionpac,
                                                                                          expectativaac,
                                                                                          gnpac, gnpoldac, localnameac,
                                                                                          gobiernoac, cabezadeestadoac,
                                                                                          capitalac, codigo2ac,
                                                                                          codigoac)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

    # -------------------------------Metodos de Ciudades-------------------------------------------------------------------

    def agrega_ciudad(self, idadd, nombrecadd, codigopaiscadd, distritoadd, poblacioncadd):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO city (ID,Name,CountryCode,District,Population) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(idadd, nombrecadd, codigopaiscadd, distritoadd, poblacioncadd)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def elimina_ciudad(self, idel):
        cursor = self.conexion.cursor()
        sql = '''DELETE FROM city WHERE ID = {}'''.format(idel)
        cursor.execute(sql)
        self.conexion.commit()
        a = cursor.rowcount
        cursor.close()
        return a

    def actualiza_ciudad(self, id, nombrec, codigopaisc, distrito, poblacionc):
        cur = self.conexion.cursor()
        sql = '''UPDATE city SET Name='{}',CountryCode='{}',District='{}',Population={}
        WHERE ID = {} '''.format(nombrec, codigopaisc, distrito, poblacionc, id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

    # -------------------------------Metodos de lenguajes-------------------------------------------------------------------

    def buscar_lenguajes(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Countrylanguage"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_lenguaje(self, nomlenguaje):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM CountryLanguage WHERE Language = {}".format(nomlenguaje)
        cursor.execute(sql)
        nombreL = cursor.fetchall()
        cursor.close()
        return nombreL

    def busca_lenguajeYpais(self, nomlenguaje, codpais):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM CountryLanguage WHERE Language = {} AND countrycode = {}".format(nomlenguaje, codpais)
        cursor.execute(sql)
        nombreL = cursor.fetchall()
        cursor.close()
        return nombreL

    def agrega_lenguaje(self, addcodigopaisl, addlenguaje, addesofficial, addporcentaje):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO CountryLanguage (CountryCode, Language, IsOfficial, Percentage) 
        VALUES('{}', '{}','{}', '{}')'''.format(addcodigopaisl, addlenguaje, addesofficial, addporcentaje)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def elimina_lenguaje(self, lenguajedel):
        cursor = self.conexion.cursor()
        sql = '''DELETE FROM CountryLanguage WHERE Language = {}'''.format(lenguajedel)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def actualiza_lenguaje(self, codigopaisl, lenguaje, esofficial, porcentaje):
        cur = self.conexion.cursor()
        sql = '''UPDATE countrylanguage SET isOfficial='{}', percentage='{}'
        WHERE countryCode = '{}' and language='{}' '''.format(esofficial, porcentaje, codigopaisl, lenguaje)
        print(sql)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

    # -------------------------------Otros Metodos-------------------------------------------------------------------
    def get_column_names(self, table_name):
        """returns column names from a DB table"""
        cursor = self.conexion.cursor()
        query = '''SELECT column_name FROM information_schema.columns WHERE table_name= '{}' '''.format(table_name)
        cursor.execute(query)
        registro = cursor.fetchall()
        ans = []
        for column in registro:
            if column[0] == 'last_update':
                ans.clear()
            else:
                ans.append(column[0])
        return ans
