import mysql.connector



class RegistroDatos():

    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost",
                                                database="world",
                                                user="root",
                                                passwd="Seguridad225")

    def buscar_paises(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM country"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_pais(self, codigop):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM country WHERE Code = {}".format(codigop)
        cursor.execute(sql)
        nombreP = cursor.fetchall()
        cursor.close()
        return nombreP

    def agrega_pais(self, codigo, nombrep, continente, region, surfacearea, idependencia, poblacionp, expectativa, gnp,
                    gnpold, localname, gobierno, cabezadeestado, capital, codigo2):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO country (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, 
        LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2) VALUES('{}', '{}','{}', 
        '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(codigo, nombrep, continente, region,
                                                                               surfacearea, idependencia, poblacionp,
                                                                               expectativa, gnp, gnpold, localname,
                                                                               gobierno, cabezadeestado, capital,
                                                                               codigo2)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def elimina_pais(self, codigo):
        cursor = self.conexion.cursor()
        sql = '''DELETE FROM country WHERE Code = {}'''.format(codigo)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def actualiza_pais(self, codigo, nombrep, continente, region, surfacearea, idependencia, poblacionp, expectativa,
                       gnp, gnpold, localname, gobierno, cabezadeestado, capital, codigo2):
        cur = self.conexion.cursor()
        sql = '''UPDATE country SET Name = '{}', Continent = '{}', Region = '{}', SurfaceArea = '{}', IndepYear = 
        '{}', Population = '{}', LifeExpectancy = '{}', GNP = '{}', GNPOld = '{}', LocalName = '{}, GovernmentForm= 
        '{}', HeadOfState = '{}', Capital = '{}', Code2 = '{}' WHERE Code = '{}' '''.format(nombrep, continente,
                                                                                            region, surfacearea,
                                                                                            idependencia, poblacionp,
                                                                                            expectativa,
                                                                                            gnp, gnpold, localname,
                                                                                            gobierno, cabezadeestado,
                                                                                            capital, codigo2, codigo)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

    def buscar_ciudades(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM city"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_ciudad(self, id):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM city WHERE ID = {}".format(id)
        cursor.execute(sql)
        nombreC = cursor.fetchall()
        cursor.close()
        return nombreC

    def agrega_ciudad(self, id, nombrec, codigopaisc, distrito, poblacionc):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO city (ID,Name,CountryCode,District,Population) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(id, nombrec, codigopaisc, distrito, poblacionc)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def elimina_ciudad(self, id):
        cursor = self.conexion.cursor()
        sql = '''DELETE FROM city WHERE ID = {}'''.format(id)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def actualiza_ciudad(self, id, nombrec, codigopaisc, distrito, poblacionc):
        cur = self.conexion.cursor()
        sql = '''UPDATE city SET Name='{}',CountryCode='{}',District='{}',Population='{}'
        WHERE ID = '{}' '''.format(nombrec, codigopaisc, distrito, poblacionc, id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

    def buscar_lenguajes(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Countrylanguage"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_lenguaje(self, lenguaje):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM CountryLanguage WHERE Language = {}".format(lenguaje)
        cursor.execute(sql)
        nombreL = cursor.fetchall()
        cursor.close()
        return nombreL

    def agrega_lenguaje(self, codigopaisl, lenguaje, esofficial, porcentaje):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO CountryLanguage (CountyCode, Language, IsOfficial, Percentage) 
        VALUES('{}', '{}','{}', '{}')'''.format(codigopaisl, lenguaje, esofficial, porcentaje)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def elimina_lenguaje(self,lenguaje):
        cursor = self.conexion.cursor()
        sql = '''DELETE FROM CountryLanguage WHERE ID = {}'''.format(lenguaje)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def actualiza_lenguaje(self, codigopaisl, lenguaje, esofficial, porcentaje):
        cur = self.conexion.cursor()
        sql = '''UPDATE CountryLanguage SET CountryCode='{}',IsOfficial='{}', Percentage='{}'
        WHERE Language = '{}' '''.format(codigopaisl, lenguaje, esofficial, porcentaje)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a
