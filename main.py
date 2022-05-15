
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
        self.ui.bt_refreshpais.clicked.connect(self.m_pais)
        self.ui.bt_buscarpais.clicked.connect(self.buscar_pais)

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


