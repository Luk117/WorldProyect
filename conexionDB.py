import mysql.connector
import self as self


class Registro_Datos():

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

    def busca_pais(self, codigo):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM country WHERE Code = {}".format(codigo)
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
        sql = '''DELETE FROM productos WHERE NOMBRE = {}'''.format(codigo)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def actualiza_pais(self, codigo, nombrep, continente, region, surfacearea, idependencia, poblacionp, expectativa,
                       gnp, gnpold, localname, gobierno, cabezadeestado, capital, codigo2):
        cur = self.conexion.cursor()
        sql = '''UPDATE productos SET Name = '{}', Continent = '{}', Region = '{}', SurfaceArea = '{}', IndepYear = 
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
        sql = "SELECT * FROM country WHERE ID = {}".format(id)
        cursor.execute(sql)
        nombreC = cursor.fetchall()
        cursor.close()
        return nombreC

    def agrega_ciudad(self, id, nombrec, codigopaisc, distrito, poblacionc):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO country (ID,Name,CountryCode,District,Population) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(id, nombrec, codigopaisc, distrito, poblacionc)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def elimina_ciudad(self, id):
        cursor = self.conexion.cursor()
        sql = '''DELETE FROM productos WHERE ID = {}'''.format(id)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a

    def actualiza_pais(self, id, nombrec, codigopaisc, distrito, poblacionc):
        cur = self.conexion.cursor()
        sql = '''UPDATE productos SET Name='{}',CountryCode='{}',District='{}',Population='{}'
        WHERE ID = '{}' '''.format(nombrec, codigopaisc, distrito, poblacionc, id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a
