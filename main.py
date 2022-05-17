
import sys
from GUI import *
from conexionDB import*
from PyQt5.QtWidgets import QTableWidgetItem


class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.datosTotal = RegistroDatos()

        #Acciones de Boton

        #Mostrar todos los datos
        self.ui.bt_refreshpais.clicked.connect(self.m_pais)
        self.ui.bt_buscarTodosl.clicked.connect(self.m_lenguaje)
        self.ui.bt_buscarTodosc.clicked.connect(self.m_ciudad)

        #Buscar dato especifico
        self.ui.bt_buscarpais.clicked.connect(self.buscar_pais)
        self.ui.bt_buscarciudad.clicked.connect(self.buscar_ciudad)
        self.ui.bt_buscarlenguaje.clicked.connect(self.buscar_lenguaje)

        #Ingresar dato
        self.ui.bt_Addpais.clicked.connect(self.insert_pais)


        #Tanaño de Tablas
        self.ui.tabla_pais.setColumnWidth(0,100)
        self.ui.tabla_pais.setColumnWidth(1,100)
        self.ui.tabla_pais.setColumnWidth(2,100)
        self.ui.tabla_pais.setColumnWidth(3,150)
        self.ui.tabla_pais.setColumnWidth(4,150)
        self.ui.tabla_pais.setColumnWidth(5,98)
        self.ui.tabla_pais.setColumnWidth(6,98)
        self.ui.tabla_pais.setColumnWidth(7,98)
        self.ui.tabla_pais.setColumnWidth(8,98)
        self.ui.tabla_pais.setColumnWidth(9,98)
        self.ui.tabla_pais.setColumnWidth(10,98)
        self.ui.tabla_pais.setColumnWidth(11,98)
        self.ui.tabla_pais.setColumnWidth(12,98)
        self.ui.tabla_pais.setColumnWidth(13,98)
        self.ui.tabla_pais.setColumnWidth(14,200)
        self.ui.tabla_pais.setColumnWidth(15,200)

        self.ui.tableLenguaje.setColumnWidth(0,100)
        self.ui.tableLenguaje.setColumnWidth(1,100)
        self.ui.tableLenguaje.setColumnWidth(2,100)
        self.ui.tableLenguaje.setColumnWidth(3,100)

        self.ui.tableCiudad.setColumnWidth(0,100)
        self.ui.tableCiudad.setColumnWidth(1,100)
        self.ui.tableCiudad.setColumnWidth(2,100)
        self.ui.tableCiudad.setColumnWidth(3,100)
        self.ui.tableCiudad.setColumnWidth(4,100)



    #------------------------------------Metodos para los paises------------------------------------------------------

    def m_pais(self):
        datos = self.datosTotal.buscar_paises()
        i = len(datos)

        self.ui.tabla_pais.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_pais.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_pais.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_pais.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tabla_pais.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tabla_pais.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tabla_pais.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tabla_pais.setItem(tablerow,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.ui.tabla_pais.setItem(tablerow,7,QtWidgets.QTableWidgetItem(str(row[7])))
            self.ui.tabla_pais.setItem(tablerow,8,QtWidgets.QTableWidgetItem(str(row[8])))
            self.ui.tabla_pais.setItem(tablerow,9,QtWidgets.QTableWidgetItem(str(row[9])))
            self.ui.tabla_pais.setItem(tablerow,10,QtWidgets.QTableWidgetItem(str(row[10])))
            self.ui.tabla_pais.setItem(tablerow,11,QtWidgets.QTableWidgetItem(str(row[11])))
            self.ui.tabla_pais.setItem(tablerow,12,QtWidgets.QTableWidgetItem(str(row[12])))
            self.ui.tabla_pais.setItem(tablerow,13,QtWidgets.QTableWidgetItem(str(row[13])))
            self.ui.tabla_pais.setItem(tablerow,14,QtWidgets.QTableWidgetItem(str(row[14])))
            tablerow += 1

    def buscar_pais(self):
        codigop = self.ui.codigoPais.text()
        codigop = str("'" + codigop + "'")

        codigoPais = self.datosTotal.busca_pais(codigop)
        i = len(codigoPais)

        self.ui.tabla_pais.setRowCount(i)
        tablerow = 0
        for row in codigoPais:
            self.ui.tabla_pais.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_pais.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_pais.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tabla_pais.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tabla_pais.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tabla_pais.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tabla_pais.setItem(tablerow,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.ui.tabla_pais.setItem(tablerow,7,QtWidgets.QTableWidgetItem(str(row[7])))
            self.ui.tabla_pais.setItem(tablerow,8,QtWidgets.QTableWidgetItem(str(row[8])))
            self.ui.tabla_pais.setItem(tablerow,9,QtWidgets.QTableWidgetItem(str(row[9])))
            self.ui.tabla_pais.setItem(tablerow,10,QtWidgets.QTableWidgetItem(str(row[10])))
            self.ui.tabla_pais.setItem(tablerow,11,QtWidgets.QTableWidgetItem(str(row[11])))
            self.ui.tabla_pais.setItem(tablerow,12,QtWidgets.QTableWidgetItem(str(row[12])))
            self.ui.tabla_pais.setItem(tablerow,13,QtWidgets.QTableWidgetItem(str(row[13])))
            self.ui.tabla_pais.setItem(tablerow,14,QtWidgets.QTableWidgetItem(str(row[14])))
            tablerow += 1

    def insert_pais(self):
        codigoadd = self.ui.addCodep.text()
        nombrepadd = self.ui.addNamep.text()
        continenteadd = self.ui.addContientep.text()
        regionadd = self.ui.addRegionp.text()
        surfaceareaadd = self.ui.addSurfacep.text()
        independenciaadd = self.ui.addIDc.text()
        poblacionpadd = self.ui.addPoblacionp.text()
        gnpadd = self.ui.addGnpp.text()
        gnpoldadd= self.ui.addGnoid.text()
        localnameadd = self.ui.addNomlocalp.text()
        expectativaadd = self.ui.addExpectp.text()
        gobiernoadd = self.ui.addFormGovp.text()
        cabezadeestadoadd = self.ui.addCabEstp.text()
        capitaladd = self.ui.addCapitalp.text()
        codigo2add = self.ui.addCode2p.text()

        self.datosTotal.agrega_pais(codigoadd, nombrepadd, continenteadd, regionadd,
                                         surfaceareaadd, independenciaadd, poblacionpadd,
                                         expectativaadd, gnpadd, gnpoldadd, localnameadd,
                                         gobiernoadd, cabezadeestadoadd, capitaladd,
                                         codigo2add)
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




    #------------------------------------Metodos para los lenguajes------------------------------------------------------



    def m_lenguaje(self):
        datos = self.datosTotal.buscar_lenguajes()
        i = len(datos)

        self.ui.tableLenguaje.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tableLenguaje.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableLenguaje.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableLenguaje.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableLenguaje.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

    def buscar_lenguaje(self):
        nomlenguaje = self.ui.idLenguaje.text()
        nomlenguaje = str("'" + nomlenguaje + "'")

        idLenguaje = self.datosTotal.busca_lenguaje(nomlenguaje)
        i = len(idLenguaje)

        self.ui.tableLenguaje.setRowCount(i)
        tablerow = 0
        for row in idLenguaje:
            self.ui.tableLenguaje.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableLenguaje.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableLenguaje.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableLenguaje.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1



    #------------------------------------Metodos para las ciudades------------------------------------------------------

    def m_ciudad(self):
        datos = self.datosTotal.buscar_ciudades()
        i = len(datos)

        self.ui.tableCiudad.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tableCiudad.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableCiudad.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableCiudad.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableCiudad.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableCiudad.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            tablerow += 1

    def buscar_ciudad(self):
        busid = self.ui.lineEdit_2.text()
        busid = str("'" + busid + "'")

        lineEdit_2 = self.datosTotal.busca_ciudad(busid)
        i = len(lineEdit_2)

        self.ui.tableCiudad.setRowCount(i)
        tablerow = 0
        for row in lineEdit_2:
            self.ui.tableCiudad.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableCiudad.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableCiudad.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableCiudad.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableCiudad.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            tablerow += 1

#if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())


