import sys
from GUI import *
from conexionDB import *
from PyQt5.QtWidgets import QTableWidgetItem


# test

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

        # Eliminar
        self.ui.bt_EliminarPais.clicked.connect(self.eliminar_pais)
        self.ui.bt_EliminarCiudad.clicked.connect(self.eliminar_ciudad)

        # Ingresar dato
        self.ui.bt_Addpais.clicked.connect(self.insert_pais)
        self.ui.bt_AddCiudad.clicked.connect(self.insert_ciudad)
        self.ui.pushButton.clicked.connect(self.insert_lenguaje)

        # Tanaño de Tablas
        self.ui.tabla_pais.setColumnWidth(0, 100)
        self.ui.tabla_pais.setColumnWidth(1, 100)
        self.ui.tabla_pais.setColumnWidth(2, 100)
        self.ui.tabla_pais.setColumnWidth(3, 150)
        self.ui.tabla_pais.setColumnWidth(4, 150)
        self.ui.tabla_pais.setColumnWidth(5, 98)
        self.ui.tabla_pais.setColumnWidth(6, 98)
        self.ui.tabla_pais.setColumnWidth(7, 98)
        self.ui.tabla_pais.setColumnWidth(8, 98)
        self.ui.tabla_pais.setColumnWidth(9, 98)
        self.ui.tabla_pais.setColumnWidth(10, 98)
        self.ui.tabla_pais.setColumnWidth(11, 98)
        self.ui.tabla_pais.setColumnWidth(12, 98)
        self.ui.tabla_pais.setColumnWidth(13, 98)
        self.ui.tabla_pais.setColumnWidth(14, 200)
        self.ui.tabla_pais.setColumnWidth(15, 200)

        self.ui.tableLenguaje.setColumnWidth(0, 100)
        self.ui.tableLenguaje.setColumnWidth(1, 100)
        self.ui.tableLenguaje.setColumnWidth(2, 100)
        self.ui.tableLenguaje.setColumnWidth(3, 100)

        self.ui.tableCiudad.setColumnWidth(0, 100)
        self.ui.tableCiudad.setColumnWidth(1, 100)
        self.ui.tableCiudad.setColumnWidth(2, 100)
        self.ui.tableCiudad.setColumnWidth(3, 100)
        self.ui.tableCiudad.setColumnWidth(4, 100)

    # ------------------------------------Metodos para los paises------------------------------------------------------

    def buscar_pais(self):
        codigop = self.ui.codigoPais_A.text()
        codigop = str("'" + codigop + "'")
        if codigop != '\'\'':
            datos = self.datosTotal.busca_pais(codigop)
        else:
            datos = self.datosTotal.buscar_paises()

        set_items(datos, self.ui.tabla_pais)

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

        set_items(datos, self.ui.tabla_pais)

        if resp is None:
            self.ui.estatusPais.setText("NO EXISTE")
        elif resp == 0:
            self.ui.estatusPais.setText("NO EXISTE")

        else:
            self.ui.estatusPais.setText("SE ELIMINO")

    # ------------------------------------Metodos para los lenguajes------------------------------------------------------


    def buscar_lenguaje(self):
        nomlenguaje = self.ui.idLenguaje.text()
        nomlenguaje = str("'" + nomlenguaje + "'")

        if nomlenguaje != '\'\'':
            datos = self.datosTotal.busca_lenguaje(nomlenguaje)
        else:
            datos = self.datosTotal.buscar_lenguajes()

        set_items(datos, self.ui.tableLenguaje)

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

    # ------------------------------------Metodos para las ciudades------------------------------------------------------

    def buscar_ciudad(self):
        busid = self.ui.lineEdit_2.text()
        busid = str("'" + busid + "'")

        if busid != '\'\'':
            datos = self.datosTotal.busca_ciudad(busid)
        else:
            datos = self.datosTotal.buscar_ciudades()

        set_items(datos, self.ui.tableCiudad)

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
        idel = self.ui.codigoEliminarc.text()
        idel = str("'" + idel + "'")

        resp = (self.datosTotal.elimina_pais(idel))
        datos = self.datosTotal.buscar_ciudades()

        set_items(datos, self.ui.tableCiudad)

        if resp is None:
            self.ui.estatusCiudad.setText("NO EXISTE")
        elif resp == 0:
            self.ui.estatusCiudad.setText("NO EXISTE")

        else:
            self.ui.estatusCiudad.setText("SE ELIMINO")


# ---------------------------------------Metodos para eliminar codigo repetido-------------------------------------------
def set_items(datos, table):
    n_rows = len(datos)
    n_columns = len(datos[0])
    table.setRowCount(n_rows)

    for tablerow, row in enumerate(datos):
        for j in range(n_columns):
            table.setItem(tablerow, j, QtWidgets.QTableWidgetItem(str(row[j])))


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
