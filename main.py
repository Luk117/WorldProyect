import sys
from GUI import *
from conexionDB import *
from Query import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.datosTotal = RegistroDatos()

        # Acciones de Boton

        # Mostrar todos los datos
        #   Solo es no poner nada en la barra de busqueda

        # Buscar dato
        self.ui.bt_buscarpais_A.clicked.connect(self.buscar_pais)
        self.ui.bt_buscarciudad_A.clicked.connect(self.buscar_ciudad)
        self.ui.bt_buscarlenguaje_A.clicked.connect(self.buscar_lenguaje)

        # self.ui.bt_buscarpais_A.clicked.connect(self.busqueda('country as p'))
        # self.ui.bt_buscarciudad_A.clicked.connect(self.busqueda('city as c'))
        # self.ui.bt_buscarlenguaje_A.clicked.connect(self.busqueda('countrylanguage'))

        # CheckBoxes busqueda
        self.cbxes_pais = {
            self.ui.cbx_p_name: 'p.name',
            self.ui.cbx_p_area: 'p.SurfaceArea',
            self.ui.cbx_p_code: 'p.code',
            self.ui.cbx_p_continent: 'p.continent',
            self.ui.cbx_p_gobierno: 'p.GovernmentForm',
            self.ui.cbx_p_independence: 'p.IndepYear',
            self.ui.cbx_p_population: 'p.Population',
            self.ui.cbx_p_region: 'p.Region'
        }

        self.cbxes_ciudad = {
            self.ui.cbx_c_country: 'c.CountryCode',  # look into how to actually show the country not the code
            self.ui.cbx_c_district: 'c.District',
            self.ui.cbx_c_name: 'c.name',
            self.ui.cbx_c_population: 'c.population',
        }

        self.cbxes_lang = {
            self.ui.cbx_l_isOfficial: 'l.IsOfficial',
            self.ui.cbx_l_country: 'l.CountryCode',  # look into how to actually show the country not the code
            self.ui.cbx_l_lang: 'l.Language',
            self.ui.cbx_l_percentage: 'l.Percentage',
        }

        # Eliminar
        self.ui.bt_EliminarPais.clicked.connect(self.eliminar_pais)
        self.ui.bt_EliminarCiudad.clicked.connect(self.eliminar_ciudad)
        self.ui.bt_EliminarLenguaje.clicked.connect(self.eliminar_lenguaje)

        # Actualizar
        self.ui.upPais.clicked.connect(self.actualizar_pais)
        self.ui.upCiudad.clicked.connect(self.actualizar_ciudad)
        self.ui.upLengua.clicked.connect(self.actualizar_lan)

        # FillUpdates
        self.ui.codigoPaisUp.returnPressed.connect(self.fillact_pais)
        self.ui.idCiudadup.returnPressed.connect(self.fillact_city)
        self.ui.codeCUpLanc.returnPressed.connect(self.fillact_lan)

        # Ingresar dato
        self.ui.bt_Addpais.clicked.connect(self.insert_pais)
        self.ui.bt_AddCiudad.clicked.connect(self.insert_ciudad)
        self.ui.bt_AddLenguaje.clicked.connect(self.insert_lenguaje)

        # Tanaño de Tablas
        self.ui.tabla_busqueda.setColumnWidth(0, 100)
        self.ui.tabla_busqueda.setColumnWidth(1, 100)
        self.ui.tabla_busqueda.setColumnWidth(2, 100)
        self.ui.tabla_busqueda.setColumnWidth(3, 150)
        self.ui.tabla_busqueda.setColumnWidth(4, 150)
        self.ui.tabla_busqueda.setColumnWidth(5, 98)
        self.ui.tabla_busqueda.setColumnWidth(6, 98)
        self.ui.tabla_busqueda.setColumnWidth(7, 98)
        self.ui.tabla_busqueda.setColumnWidth(8, 98)
        self.ui.tabla_busqueda.setColumnWidth(9, 98)
        self.ui.tabla_busqueda.setColumnWidth(10, 98)
        self.ui.tabla_busqueda.setColumnWidth(11, 98)
        self.ui.tabla_busqueda.setColumnWidth(12, 98)
        self.ui.tabla_busqueda.setColumnWidth(13, 98)
        self.ui.tabla_busqueda.setColumnWidth(14, 200)
        self.ui.tabla_busqueda.setColumnWidth(15, 200)

        self.ui.tableLenguaje.setColumnWidth(0, 100)
        self.ui.tableLenguaje.setColumnWidth(1, 100)
        self.ui.tableLenguaje.setColumnWidth(2, 100)
        self.ui.tableLenguaje.setColumnWidth(3, 100)

        self.ui.tableCiudad.setColumnWidth(0, 100)
        self.ui.tableCiudad.setColumnWidth(1, 100)
        self.ui.tableCiudad.setColumnWidth(2, 100)
        self.ui.tableCiudad.setColumnWidth(3, 100)
        self.ui.tableCiudad.setColumnWidth(4, 100)

    # def busqueda(self, tables):
    #     sql = Query()
    #     sql.append_tables(tables)
    #
    # ------------------------------------Metodos para los paises------------------------------------------------------

    def buscar_pais(self):
        # set table and query
        sql = Query()
        sql.append_tables('country as p')

        # parameters
        set_parameters(sql, self.cbxes_pais)
        if not sql.parameters:
            sql.append_parameters(self.datosTotal.get_column_names('country'))

        # set table
        set_tabla_busqueda(sql, self.ui.tabla_busqueda)

        # decide what to look for (with queries)
        name_p = self.ui.codigoPais_A.text()
        if not name_p.__eq__(''):
            sql.append_wheres("p.name like '{}'".format(name_p))
        datos = self.datosTotal.buscar(sql.get_query())

        set_items(datos, self.ui.tabla_busqueda)

    def insert_pais(self):
        codigoadd = (self.ui.addCodep.text())
        nombrepadd = (self.ui.addNamep.text())
        continenteadd = (self.ui.addContientep.text())
        regionadd = (self.ui.addRegionp.text())
        surfaceareaadd = (self.ui.addSurfacep.text())
        independenciaadd = (self.ui.addIndp.text())
        poblacionpadd = (self.ui.addPoblacionp.text())
        expectativaadd = (self.ui.addExpectp.text())
        gnpadd = (self.ui.addGnpp.text())
        gnpoldadd = (self.ui.addGnoid.text())
        localnameadd = (self.ui.addNomlocalp.text())
        gobiernoadd = (self.ui.addFormGovp.text())
        cabezadeestadoadd = (self.ui.addCabEstp.text())
        capitaladd = (self.ui.addCapitalp.text())
        codigo2add = (self.ui.addCode2p.text())

        self.datosTotal.agrega_pais(codigoadd, nombrepadd, continenteadd, regionadd, surfaceareaadd, independenciaadd,
                                    poblacionpadd, expectativaadd, gnpadd, gnpoldadd, localnameadd, gobiernoadd,
                                    cabezadeestadoadd, capitaladd, codigo2add)

        self.ui.addCodep.clear()
        self.ui.addNamep.clear()
        self.ui.addContientep.clear()
        self.ui.addRegionp.clear()
        self.ui.addSurfacep.clear()
        self.ui.addIndp.clear()
        self.ui.addPoblacionp.clear()
        self.ui.addGnpp.clear()
        self.ui.addGnoid.clear()
        self.ui.addNomlocalp.clear()
        self.ui.addExpectp.clear()
        self.ui.addFormGovp.clear()
        self.ui.addCabEstp.clear()
        self.ui.addCapitalp.clear()
        self.ui.addCode2p.clear()

    def eliminar_pais(self):
        codigoel = self.ui.codigoEliminarp.text()
        codigoel = str("'" + codigoel + "'")

        resp = (self.datosTotal.elimina_pais(codigoel))
        datos = self.datosTotal.buscar_paises()

        set_items(datos, self.ui.tabla_busqueda)

        if resp is None:
            self.ui.estatusPais.setText("NO EXISTE")
        elif resp == 0:
            self.ui.estatusPais.setText("NO EXISTE")

        else:
            self.ui.estatusPais.setText("SE ELIMINO")

    def actualizar_pais(self):

        codigoadd = (self.ui.upCodep.text())
        nombrepadd = (self.ui.upNamep.text())
        continenteadd = (self.ui.upContientep.text())
        regionadd = (self.ui.upRegionp.text())
        surfaceareaadd = (self.ui.upSurfacep.text())
        independenciaadd = (self.ui.upIndp.text())
        poblacionpadd = (self.ui.upPoblacionp.text())
        expectativaadd = (self.ui.upExpectp.text())
        gnpadd = (self.ui.upGnpp.text())
        gnpoldadd = (self.ui.upGnoidp.text())
        localnameadd = (self.ui.upNomlocalp.text())
        gobiernoadd = (self.ui.upFormGovp.text())
        cabezadeestadoadd = (self.ui.upCabEstp.text())
        capitaladd = (self.ui.upCapitalp.text())
        codigo2add = (self.ui.upCode2p.text())

        self.datosTotal.actualiza_pais(codigoadd, nombrepadd, continenteadd, regionadd, surfaceareaadd,
                                       independenciaadd, poblacionpadd, expectativaadd, gnpadd, gnpoldadd, localnameadd,
                                       gobiernoadd, cabezadeestadoadd, capitaladd, codigo2add)

    def fillact_pais(self):
        codigorr = str(self.ui.codigoPaisUp.text())
        codigorr = ("'" + codigorr + "'")
        autofill = self.datosTotal.busca_pais(codigorr)

        for data in autofill:
            self.ui.upCodep.setText(str(data[0]))
            self.ui.upNamep.setText((data[1]))
            self.ui.upContientep.setText((data[2]))
            self.ui.upRegionp.setText(data[3])
            self.ui.upSurfacep.setText(str(data[4]))
            self.ui.upIndp.setText(str(data[5]))
            self.ui.upPoblacionp.setText(str(data[6]))
            self.ui.upExpectp.setText(str(data[7]))
            self.ui.upGnpp.setText(str(data[8]))
            self.ui.upGnoidp.setText(str(data[9]))
            self.ui.upNomlocalp.setText(str(data[10]))
            self.ui.upFormGovp.setText(str(data[11]))
            self.ui.upCabEstp.setText(str(data[12]))
            self.ui.upCapitalp.setText(str(data[13]))
            self.ui.upCode2p.setText(str(data[14]))

    # ------------------------------------Metodos para los lenguajes------------------------------------------------------

    def buscar_lenguaje(self):
        # set table and query
        sql = Query()
        sql.append_tables('countrylanguage as l')

        # parameters
        set_parameters(sql, self.cbxes_lang)
        if not sql.parameters:
            sql.append_parameters(self.datosTotal.get_column_names('countrylanguage'))

        # set table
        set_tabla_busqueda(sql, self.ui.tabla_busqueda)

        name_l = self.ui.codigoLenguaje_A.text()
        if not name_l.__eq__(''):
            sql.append_wheres("l.language like '{}'".format(name_l))
        datos = self.datosTotal.buscar(sql.get_query())

        set_items(datos, self.ui.tabla_busqueda)

    def insert_lenguaje(self):

        addcodigopaisl = self.ui.addCountryCodel.text()
        addlenguaje = self.ui.addLenguajel.text()
        addesofficial = self.ui.addOfficiall.text()
        addporcentaje = self.ui.addPorcentajel.text()

        self.datosTotal.agrega_lenguaje(addcodigopaisl, addlenguaje, addesofficial, addporcentaje)

        self.ui.addCountryCodel.clear()
        self.ui.addLenguajel.clear()
        self.ui.addOfficiall.clear()
        self.ui.addPorcentajel.clear()

    def eliminar_lenguaje(self):
        lenguajedel = self.ui.lineEdit_3.text()
        lenguajedel = ("'" + lenguajedel + "'")

        resp = (self.datosTotal.elimina_lenguaje(lenguajedel))
        datos = self.datosTotal.buscar_lenguajes()
        i = len(datos)

        self.ui.tableLenguaje.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tableLenguaje.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableLenguaje.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableLenguaje.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableLenguaje.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

        if resp == None:
            self.ui.estatusLenguaje.setText("NO EXISTE")
        elif resp == 0:
            self.ui.estatusLenguaje.setText("NO EXISTE")

        else:
            self.ui.estatusLenguaje.setText("SE ELIMINO")

    def fillact_lan(self):
        codigorr = str(self.ui.codLenguaup.text())
        codigorr = ("'" + codigorr + "'")
        codigopais = str(self.ui.codeCUpLanc.text())
        codigopais = ("'" + codigopais + "'")
        autofill = self.datosTotal.busca_lenguajeYpais(codigorr, codigopais)

        for data in autofill:
            self.ui.upCountryCodel.setText(str(data[0]))
            self.ui.upLenguajel.setText(str(data[1]))
            if (str(data[2]) == "T"):
                self.ui.radioSi_lan.setChecked(True)
                self.ui.radioNo_lan.setChecked(False)
            elif (str(data[2]) == "F"):
                self.ui.radioNo_lan.setChecked(True)
                self.ui.radioSi_lan.setChecked(False)
            self.ui.upOfficiall.setText(str(data[2]))
            self.ui.upPorcentajel.setText(str(data[3]))

    def actualizar_lan(self):

        upcodigopaisl = self.ui.upCountryCodel.text()
        uplenguaje = self.ui.upLenguajel.text()
        upporcentaje = self.ui.upPorcentajel.text()

        if (self.ui.radioSi_lan.isChecked() == True):
            upesofficial = 'T'
        elif (self.ui.radioNo_lan.isChecked() == True):
            upesofficial = 'F'

        self.datosTotal.actualiza_lenguaje(upcodigopaisl, uplenguaje, upesofficial, upporcentaje)

    # ------------------------------------Metodos para las ciudades------------------------------------------------------

    def buscar_ciudad(self):
        # set table and query
        sql = Query()
        sql.append_tables('city as c')

        # parameters
        set_parameters(sql, self.cbxes_ciudad)
        if not sql.parameters:
            sql.append_parameters(self.datosTotal.get_column_names('city'))

        # set tables
        set_tabla_busqueda(sql, self.ui.tabla_busqueda)

        # decide what to look for
        name_c = self.ui.codigoCiudad_A.text()
        if not name_c.__eq__(''):
            sql.append_wheres("c.name like '{}'".format(name_c))
        datos = self.datosTotal.buscar(sql.get_query())

        set_items(datos, self.ui.tabla_busqueda)

    def insert_ciudad(self):

        idadd = str(self.ui.addIDc.text())
        nombrecadd = str(self.ui.addNombrec.text())
        codigopaiscadd = str(self.ui.addCountryCodec.text())
        distritoadd = str(self.ui.addDistritoc.text())
        poblacioncadd = str(self.ui.addPoblacionc.text())

        self.datosTotal.agrega_ciudad(idadd, nombrecadd, codigopaiscadd, distritoadd, poblacioncadd)

        self.ui.addIDc.clear()
        self.ui.addNombrec.clear()
        self.ui.addCountryCodec.clear()
        self.ui.addDistritoc.clear()
        self.ui.addPoblacionc.clear()

    def eliminar_ciudad(self):
        delid = self.ui.codigoEliminarc.text()
        delid = ("'" + delid + "'")

        resp = (self.datosTotal.elimina_ciudad(delid))
        datos = self.datosTotal.buscar_ciudades()

        set_items(datos, self.ui.tableCiudad)

        if resp is None:
            self.ui.estatusCiudad.setText("NO EXISTE")
        elif resp == 0:
            self.ui.estatusCiudad.setText("NO EXISTE")

        else:
            self.ui.estatusCiudad.setText("SE ELIMINO")

    def modificar_ciudades(self):
        id_producto = self.ui.id_producto.text()
        id_producto = str("'" + id_producto + "'")
        nombreXX = self.datosTotal.busca_producto(id_producto)

        if nombreXX != None:

            self.ui.id_buscar.setText("ACTUALIZAR")

            codigoM = self.ui.codigo_actualizar.text()
            nombreM = self.ui.nombre_actualizar.text()
            modeloM = self.ui.modelo_actualizar.text()
            precioM = self.ui.precio_actualizar.text()
            cantidadM = self.ui.cantidad_actualizar.text()

            act = self.datosTotal.actualiza_productos(codigoM, nombreM, modeloM, precioM, cantidadM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.codigo_actualizar.clear()
                self.ui.nombre_actualizar.clear()
                self.ui.modelo_actualizar.clear()
                self.ui.precio_actualizar.clear()
                self.ui.cantidad_actualizar.clear()
                self.ui.id_producto.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")

    def actualizar_ciudad(self):

        idadd = str(self.ui.upIDc.text())
        nombrecadd = str(self.ui.upNombrec.text())
        codigopaiscadd = str(self.ui.upCountryCodec.text())
        distritoadd = str(self.ui.upDistritoc.text())
        poblacioncadd = str(self.ui.upPoblacionc.text())

        self.datosTotal.actualiza_ciudad(idadd, nombrecadd, codigopaiscadd, distritoadd, poblacioncadd)

    def fillact_city(self):
        codigorr = str(self.ui.idCiudadup.text())
        codigorr = ("'" + codigorr + "'")
        autofill = self.datosTotal.busca_ciudad(codigorr)

        for data in autofill:
            self.ui.upIDc.setText(str(data[0]))
            self.ui.upNombrec.setText(str(data[1]))
            self.ui.upCountryCodec.setText(str(data[2]))
            self.ui.upDistritoc.setText(str(data[3]))
            self.ui.upPoblacionc.setText(str(data[4]))


# if __name__ == "__main__":
# import sys
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())

# ---------------------------------------Metodos para eliminar codigo repetido-------------------------------------------
def set_items(datos, table):
    n_rows = len(datos)
    n_columns = 0
    try:
        n_columns = len(datos[0])
    except:
        print("No data was found")

    table.setRowCount(n_rows)

    for tablerow, row in enumerate(datos):
        for j in range(n_columns):
            table.setItem(tablerow, j, QtWidgets.QTableWidgetItem(str(row[j])))


def set_parameters(query: Query, cbxes: dict):
    for box in cbxes:
        if box.isChecked():
            query.append_parameters(cbxes[box])


def set_tabla_busqueda(query: Query, tabla):
    parameters = query.get_parameters()
    i = 0
    for par in parameters:
        tabla.horizontalHeaderItem(i).setText(par)
        tabla.setColumnHidden(i, False)
        i += 1
    for j in range(i, 15):
        tabla.setColumnHidden(j, True)


# if __name__ == "__main__":
# import sys
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
