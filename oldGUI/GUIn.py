# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tablaCiudad = QtWidgets.QTabWidget(self.centralwidget)
        self.tablaCiudad.setGeometry(QtCore.QRect(0, 90, 921, 641))
        self.tablaCiudad.setMovable(False)
        self.tablaCiudad.setObjectName("tablaCiudad")
        self.tabPais = QtWidgets.QWidget()
        self.tabPais.setObjectName("tabPais")
        self.tabla_pais = QtWidgets.QTableWidget(self.tabPais)
        self.tabla_pais.setGeometry(QtCore.QRect(20, 120, 841, 471))
        self.tabla_pais.setObjectName("tabla_pais")
        self.tabla_pais.setColumnCount(15)
        self.tabla_pais.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_pais.setHorizontalHeaderItem(14, item)
        self.bt_refreshpais = QtWidgets.QPushButton(self.tabPais)
        self.bt_refreshpais.setGeometry(QtCore.QRect(740, 70, 121, 41))
        self.bt_refreshpais.setObjectName("bt_refreshpais")
        self.label = QtWidgets.QLabel(self.tabPais)
        self.label.setGeometry(QtCore.QRect(30, 70, 61, 21))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.codigoPais = QtWidgets.QLineEdit(self.tabPais)
        self.codigoPais.setGeometry(QtCore.QRect(80, 70, 113, 22))
        self.codigoPais.setInputMask("")
        self.codigoPais.setText("")
        self.codigoPais.setObjectName("codigoPais")
        self.bt_buscarpais = QtWidgets.QPushButton(self.tabPais)
        self.bt_buscarpais.setGeometry(QtCore.QRect(200, 70, 75, 24))
        self.bt_buscarpais.setObjectName("bt_buscarpais")
        self.tablaCiudad.addTab(self.tabPais, "")
        self.tabLenguaje = QtWidgets.QWidget()
        self.tabLenguaje.setObjectName("tabLenguaje")
        self.tableLenguaje = QtWidgets.QTableWidget(self.tabLenguaje)
        self.tableLenguaje.setGeometry(QtCore.QRect(390, 100, 401, 361))
        self.tableLenguaje.setObjectName("tableLenguaje")
        self.tableLenguaje.setColumnCount(4)
        self.tableLenguaje.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableLenguaje.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLenguaje.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLenguaje.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLenguaje.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(self.tabLenguaje)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 51, 16))
        self.label_2.setObjectName("label_2")
        self.idLenguaje = QtWidgets.QLineEdit(self.tabLenguaje)
        self.idLenguaje.setGeometry(QtCore.QRect(100, 130, 113, 22))
        self.idLenguaje.setObjectName("idLenguaje")
        self.bt_buscarlenguaje = QtWidgets.QPushButton(self.tabLenguaje)
        self.bt_buscarlenguaje.setGeometry(QtCore.QRect(240, 130, 75, 24))
        self.bt_buscarlenguaje.setObjectName("bt_buscarlenguaje")
        self.bt_buscarTodosl = QtWidgets.QPushButton(self.tabLenguaje)
        self.bt_buscarTodosl.setGeometry(QtCore.QRect(680, 470, 111, 41))
        self.bt_buscarTodosl.setObjectName("bt_buscarTodosl")
        self.tablaCiudad.addTab(self.tabLenguaje, "")
        self.tabCiudad = QtWidgets.QWidget()
        self.tabCiudad.setObjectName("tabCiudad")
        self.tableCiudad = QtWidgets.QTableWidget(self.tabCiudad)
        self.tableCiudad.setGeometry(QtCore.QRect(340, 80, 501, 441))
        self.tableCiudad.setObjectName("tableCiudad")
        self.tableCiudad.setColumnCount(5)
        self.tableCiudad.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableCiudad.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCiudad.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCiudad.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCiudad.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCiudad.setHorizontalHeaderItem(4, item)
        self.label_3 = QtWidgets.QLabel(self.tabCiudad)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 49, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tabCiudad)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 130, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.bt_buscarciudad = QtWidgets.QPushButton(self.tabCiudad)
        self.bt_buscarciudad.setGeometry(QtCore.QRect(200, 130, 75, 24))
        self.bt_buscarciudad.setObjectName("bt_buscarciudad")
        self.bt_buscarTodosc = QtWidgets.QPushButton(self.tabCiudad)
        self.bt_buscarTodosc.setGeometry(QtCore.QRect(730, 530, 111, 41))
        self.bt_buscarTodosc.setObjectName("bt_buscarTodosc")
        self.tablaCiudad.addTab(self.tabCiudad, "")
        self.agregarCampo = QtWidgets.QWidget()
        self.agregarCampo.setObjectName("agregarCampo")
        self.label_4 = QtWidgets.QLabel(self.agregarCampo)
        self.label_4.setGeometry(QtCore.QRect(100, 70, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.agregarCampo)
        self.label_5.setGeometry(QtCore.QRect(100, 100, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.agregarCampo)
        self.label_6.setGeometry(QtCore.QRect(100, 130, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.agregarCampo)
        self.label_7.setGeometry(QtCore.QRect(100, 160, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.agregarCampo)
        self.label_8.setGeometry(QtCore.QRect(100, 190, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.agregarCampo)
        self.label_9.setGeometry(QtCore.QRect(100, 220, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.agregarCampo)
        self.label_10.setGeometry(QtCore.QRect(100, 250, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.agregarCampo)
        self.label_11.setGeometry(QtCore.QRect(100, 280, 101, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.agregarCampo)
        self.label_12.setGeometry(QtCore.QRect(100, 310, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.agregarCampo)
        self.label_13.setGeometry(QtCore.QRect(100, 340, 101, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.agregarCampo)
        self.label_14.setGeometry(QtCore.QRect(100, 370, 101, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.agregarCampo)
        self.label_15.setGeometry(QtCore.QRect(100, 400, 101, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.agregarCampo)
        self.label_16.setGeometry(QtCore.QRect(100, 430, 101, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.agregarCampo)
        self.label_17.setGeometry(QtCore.QRect(100, 460, 101, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.agregarCampo)
        self.label_18.setGeometry(QtCore.QRect(100, 490, 101, 16))
        self.label_18.setObjectName("label_18")
        self.addCodep = QtWidgets.QLineEdit(self.agregarCampo)
        self.addCodep.setGeometry(QtCore.QRect(210, 70, 113, 22))
        self.addCodep.setObjectName("addCodep")
        self.addNamep = QtWidgets.QLineEdit(self.agregarCampo)
        self.addNamep.setGeometry(QtCore.QRect(210, 100, 113, 22))
        self.addNamep.setObjectName("addNamep")
        self.addContientep = QtWidgets.QLineEdit(self.agregarCampo)
        self.addContientep.setGeometry(QtCore.QRect(210, 130, 113, 22))
        self.addContientep.setObjectName("addContientep")
        self.addRegionp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addRegionp.setGeometry(QtCore.QRect(210, 160, 113, 22))
        self.addRegionp.setObjectName("addRegionp")
        self.addSurfacep = QtWidgets.QLineEdit(self.agregarCampo)
        self.addSurfacep.setGeometry(QtCore.QRect(210, 190, 113, 22))
        self.addSurfacep.setObjectName("addSurfacep")
        self.addIndp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addIndp.setGeometry(QtCore.QRect(210, 220, 113, 22))
        self.addIndp.setObjectName("addIndp")
        self.addPoblacionp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addPoblacionp.setGeometry(QtCore.QRect(210, 250, 113, 22))
        self.addPoblacionp.setObjectName("addPoblacionp")
        self.addExpectp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addExpectp.setGeometry(QtCore.QRect(210, 280, 113, 22))
        self.addExpectp.setObjectName("addExpectp")
        self.addGnpp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addGnpp.setGeometry(QtCore.QRect(210, 310, 113, 22))
        self.addGnpp.setObjectName("addGnpp")
        self.addGnoid = QtWidgets.QLineEdit(self.agregarCampo)
        self.addGnoid.setGeometry(QtCore.QRect(210, 340, 113, 22))
        self.addGnoid.setObjectName("addGnoid")
        self.addNomlocalp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addNomlocalp.setGeometry(QtCore.QRect(210, 370, 113, 22))
        self.addNomlocalp.setObjectName("addNomlocalp")
        self.addFormGovp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addFormGovp.setGeometry(QtCore.QRect(210, 400, 113, 22))
        self.addFormGovp.setObjectName("addFormGovp")
        self.addCabEstp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addCabEstp.setGeometry(QtCore.QRect(210, 430, 113, 22))
        self.addCabEstp.setObjectName("addCabEstp")
        self.addCapitalp = QtWidgets.QLineEdit(self.agregarCampo)
        self.addCapitalp.setGeometry(QtCore.QRect(210, 460, 113, 22))
        self.addCapitalp.setObjectName("addCapitalp")
        self.addCode2p = QtWidgets.QLineEdit(self.agregarCampo)
        self.addCode2p.setGeometry(QtCore.QRect(210, 490, 113, 22))
        self.addCode2p.setObjectName("addCode2p")
        self.bt_Addpais = QtWidgets.QPushButton(self.agregarCampo)
        self.bt_Addpais.setGeometry(QtCore.QRect(160, 530, 75, 24))
        self.bt_Addpais.setObjectName("bt_Addpais")
        self.label_19 = QtWidgets.QLabel(self.agregarCampo)
        self.label_19.setGeometry(QtCore.QRect(380, 70, 49, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.agregarCampo)
        self.label_20.setGeometry(QtCore.QRect(380, 100, 49, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.agregarCampo)
        self.label_21.setGeometry(QtCore.QRect(380, 130, 71, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.agregarCampo)
        self.label_22.setGeometry(QtCore.QRect(380, 160, 71, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.agregarCampo)
        self.label_23.setGeometry(QtCore.QRect(380, 190, 71, 16))
        self.label_23.setObjectName("label_23")
        self.addIDc = QtWidgets.QLineEdit(self.agregarCampo)
        self.addIDc.setGeometry(QtCore.QRect(460, 70, 113, 22))
        self.addIDc.setObjectName("addIDc")
        self.addNombrec = QtWidgets.QLineEdit(self.agregarCampo)
        self.addNombrec.setGeometry(QtCore.QRect(460, 100, 113, 22))
        self.addNombrec.setObjectName("addNombrec")
        self.addCountryCodec = QtWidgets.QLineEdit(self.agregarCampo)
        self.addCountryCodec.setGeometry(QtCore.QRect(460, 130, 113, 22))
        self.addCountryCodec.setObjectName("addCountryCodec")
        self.addDistritoc = QtWidgets.QLineEdit(self.agregarCampo)
        self.addDistritoc.setGeometry(QtCore.QRect(460, 160, 113, 22))
        self.addDistritoc.setObjectName("addDistritoc")
        self.addPoblacionc = QtWidgets.QLineEdit(self.agregarCampo)
        self.addPoblacionc.setGeometry(QtCore.QRect(460, 190, 113, 22))
        self.addPoblacionc.setObjectName("addPoblacionc")
        self.label_24 = QtWidgets.QLabel(self.agregarCampo)
        self.label_24.setGeometry(QtCore.QRect(640, 70, 71, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.agregarCampo)
        self.label_25.setGeometry(QtCore.QRect(640, 100, 71, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.agregarCampo)
        self.label_26.setGeometry(QtCore.QRect(640, 130, 71, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.agregarCampo)
        self.label_27.setGeometry(QtCore.QRect(640, 160, 71, 16))
        self.label_27.setObjectName("label_27")
        self.addCountryCodel = QtWidgets.QLineEdit(self.agregarCampo)
        self.addCountryCodel.setGeometry(QtCore.QRect(730, 70, 113, 22))
        self.addCountryCodel.setObjectName("addCountryCodel")
        self.addLenguajel = QtWidgets.QLineEdit(self.agregarCampo)
        self.addLenguajel.setGeometry(QtCore.QRect(730, 100, 113, 22))
        self.addLenguajel.setObjectName("addLenguajel")
        self.addOfficiall = QtWidgets.QLineEdit(self.agregarCampo)
        self.addOfficiall.setGeometry(QtCore.QRect(730, 130, 113, 22))
        self.addOfficiall.setObjectName("addOfficiall")
        self.addPorcentajel = QtWidgets.QLineEdit(self.agregarCampo)
        self.addPorcentajel.setGeometry(QtCore.QRect(730, 160, 113, 22))
        self.addPorcentajel.setObjectName("addPorcentajel")
        self.bt_AddCiudad = QtWidgets.QPushButton(self.agregarCampo)
        self.bt_AddCiudad.setGeometry(QtCore.QRect(430, 230, 91, 24))
        self.bt_AddCiudad.setObjectName("bt_AddCiudad")
        self.pushButton = QtWidgets.QPushButton(self.agregarCampo)
        self.pushButton.setGeometry(QtCore.QRect(690, 220, 111, 24))
        self.pushButton.setObjectName("pushButton")
        self.tablaCiudad.addTab(self.agregarCampo, "")
        self.eliminarCampo = QtWidgets.QWidget()
        self.eliminarCampo.setObjectName("eliminarCampo")
        self.label_28 = QtWidgets.QLabel(self.eliminarCampo)
        self.label_28.setGeometry(QtCore.QRect(50, 90, 71, 16))
        self.label_28.setObjectName("label_28")
        self.codigoEliminarp = QtWidgets.QLineEdit(self.eliminarCampo)
        self.codigoEliminarp.setGeometry(QtCore.QRect(130, 90, 161, 22))
        self.codigoEliminarp.setObjectName("codigoEliminarp")
        self.bt_EliminarPais = QtWidgets.QPushButton(self.eliminarCampo)
        self.bt_EliminarPais.setGeometry(QtCore.QRect(130, 130, 75, 24))
        self.bt_EliminarPais.setObjectName("bt_EliminarPais")
        self.estatusPais = QtWidgets.QPushButton(self.eliminarCampo)
        self.estatusPais.setGeometry(QtCore.QRect(210, 130, 75, 24))
        self.estatusPais.setObjectName("estatusPais")
        self.label_29 = QtWidgets.QLabel(self.eliminarCampo)
        self.label_29.setGeometry(QtCore.QRect(50, 220, 49, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.eliminarCampo)
        self.label_30.setGeometry(QtCore.QRect(50, 340, 49, 16))
        self.label_30.setObjectName("label_30")
        self.codigoEliminarc = QtWidgets.QLineEdit(self.eliminarCampo)
        self.codigoEliminarc.setGeometry(QtCore.QRect(130, 340, 161, 22))
        self.codigoEliminarc.setObjectName("codigoEliminarc")
        self.bt_EliminarCiudad = QtWidgets.QPushButton(self.eliminarCampo)
        self.bt_EliminarCiudad.setGeometry(QtCore.QRect(120, 380, 91, 24))
        self.bt_EliminarCiudad.setObjectName("bt_EliminarCiudad")
        self.estatusCiudad = QtWidgets.QPushButton(self.eliminarCampo)
        self.estatusCiudad.setGeometry(QtCore.QRect(220, 380, 75, 24))
        self.estatusCiudad.setObjectName("estatusCiudad")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.eliminarCampo)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 220, 161, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.eliminarCampo)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 250, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.eliminarCampo)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 250, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tablaCiudad.addTab(self.eliminarCampo, "")
        self.actualizarPais = QtWidgets.QWidget()
        self.actualizarPais.setObjectName("actualizarPais")
        self.upContientep = QtWidgets.QLineEdit(self.actualizarPais)
        self.upContientep.setGeometry(QtCore.QRect(200, 150, 113, 22))
        self.upContientep.setObjectName("upContientep")
        self.label_61 = QtWidgets.QLabel(self.actualizarPais)
        self.label_61.setGeometry(QtCore.QRect(90, 150, 101, 16))
        self.label_61.setObjectName("label_61")
        self.upGnpp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upGnpp.setGeometry(QtCore.QRect(200, 330, 113, 22))
        self.upGnpp.setObjectName("upGnpp")
        self.upNamep = QtWidgets.QLineEdit(self.actualizarPais)
        self.upNamep.setGeometry(QtCore.QRect(200, 120, 113, 22))
        self.upNamep.setObjectName("upNamep")
        self.upSurfacep = QtWidgets.QLineEdit(self.actualizarPais)
        self.upSurfacep.setGeometry(QtCore.QRect(200, 210, 113, 22))
        self.upSurfacep.setObjectName("upSurfacep")
        self.upGnoidp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upGnoidp.setGeometry(QtCore.QRect(200, 360, 113, 22))
        self.upGnoidp.setObjectName("upGnoidp")
        self.upCodep = QtWidgets.QLineEdit(self.actualizarPais)
        self.upCodep.setGeometry(QtCore.QRect(200, 90, 113, 22))
        self.upCodep.setObjectName("upCodep")
        self.upRegionp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upRegionp.setGeometry(QtCore.QRect(200, 180, 113, 22))
        self.upRegionp.setObjectName("upRegionp")
        self.upIndp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upIndp.setGeometry(QtCore.QRect(200, 240, 113, 22))
        self.upIndp.setObjectName("upIndp")
        self.label_62 = QtWidgets.QLabel(self.actualizarPais)
        self.label_62.setGeometry(QtCore.QRect(90, 360, 101, 16))
        self.label_62.setObjectName("label_62")
        self.upFormGovp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upFormGovp.setGeometry(QtCore.QRect(200, 420, 113, 22))
        self.upFormGovp.setObjectName("upFormGovp")
        self.upNomlocalp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upNomlocalp.setGeometry(QtCore.QRect(200, 390, 113, 22))
        self.upNomlocalp.setObjectName("upNomlocalp")
        self.label_63 = QtWidgets.QLabel(self.actualizarPais)
        self.label_63.setGeometry(QtCore.QRect(90, 450, 101, 16))
        self.label_63.setObjectName("label_63")
        self.upPoblacionp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upPoblacionp.setGeometry(QtCore.QRect(200, 270, 113, 22))
        self.upPoblacionp.setObjectName("upPoblacionp")
        self.label_64 = QtWidgets.QLabel(self.actualizarPais)
        self.label_64.setGeometry(QtCore.QRect(90, 390, 101, 16))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.actualizarPais)
        self.label_65.setGeometry(QtCore.QRect(90, 120, 101, 16))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.actualizarPais)
        self.label_66.setGeometry(QtCore.QRect(90, 90, 111, 16))
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.actualizarPais)
        self.label_67.setGeometry(QtCore.QRect(90, 300, 101, 16))
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.actualizarPais)
        self.label_68.setGeometry(QtCore.QRect(90, 210, 101, 16))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.actualizarPais)
        self.label_69.setGeometry(QtCore.QRect(90, 480, 101, 16))
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.actualizarPais)
        self.label_70.setGeometry(QtCore.QRect(90, 180, 101, 16))
        self.label_70.setObjectName("label_70")
        self.upExpectp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upExpectp.setGeometry(QtCore.QRect(200, 300, 113, 22))
        self.upExpectp.setObjectName("upExpectp")
        self.label_71 = QtWidgets.QLabel(self.actualizarPais)
        self.label_71.setGeometry(QtCore.QRect(90, 240, 101, 16))
        self.label_71.setObjectName("label_71")
        self.upCode2p = QtWidgets.QLineEdit(self.actualizarPais)
        self.upCode2p.setGeometry(QtCore.QRect(200, 510, 113, 22))
        self.upCode2p.setObjectName("upCode2p")
        self.label_72 = QtWidgets.QLabel(self.actualizarPais)
        self.label_72.setGeometry(QtCore.QRect(90, 420, 101, 16))
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.actualizarPais)
        self.label_73.setGeometry(QtCore.QRect(90, 330, 101, 16))
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(self.actualizarPais)
        self.label_74.setGeometry(QtCore.QRect(90, 510, 101, 16))
        self.label_74.setObjectName("label_74")
        self.upCapitalp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upCapitalp.setGeometry(QtCore.QRect(200, 480, 113, 22))
        self.upCapitalp.setObjectName("upCapitalp")
        self.label_75 = QtWidgets.QLabel(self.actualizarPais)
        self.label_75.setGeometry(QtCore.QRect(90, 270, 101, 16))
        self.label_75.setObjectName("label_75")
        self.upCabEstp = QtWidgets.QLineEdit(self.actualizarPais)
        self.upCabEstp.setGeometry(QtCore.QRect(200, 450, 113, 22))
        self.upCabEstp.setObjectName("upCabEstp")
        self.label_76 = QtWidgets.QLabel(self.actualizarPais)
        self.label_76.setGeometry(QtCore.QRect(380, 210, 71, 16))
        self.label_76.setObjectName("label_76")
        self.upDistritoc = QtWidgets.QLineEdit(self.actualizarPais)
        self.upDistritoc.setGeometry(QtCore.QRect(460, 180, 113, 22))
        self.upDistritoc.setObjectName("upDistritoc")
        self.label_77 = QtWidgets.QLabel(self.actualizarPais)
        self.label_77.setGeometry(QtCore.QRect(380, 120, 49, 16))
        self.label_77.setObjectName("label_77")
        self.upCountryCodec = QtWidgets.QLineEdit(self.actualizarPais)
        self.upCountryCodec.setGeometry(QtCore.QRect(460, 150, 113, 22))
        self.upCountryCodec.setObjectName("upCountryCodec")
        self.label_78 = QtWidgets.QLabel(self.actualizarPais)
        self.label_78.setGeometry(QtCore.QRect(380, 180, 71, 16))
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.actualizarPais)
        self.label_79.setGeometry(QtCore.QRect(380, 90, 49, 16))
        self.label_79.setObjectName("label_79")
        self.upIDc = QtWidgets.QLineEdit(self.actualizarPais)
        self.upIDc.setGeometry(QtCore.QRect(460, 90, 113, 22))
        self.upIDc.setObjectName("upIDc")
        self.label_80 = QtWidgets.QLabel(self.actualizarPais)
        self.label_80.setGeometry(QtCore.QRect(380, 150, 71, 16))
        self.label_80.setObjectName("label_80")
        self.upNombrec = QtWidgets.QLineEdit(self.actualizarPais)
        self.upNombrec.setGeometry(QtCore.QRect(460, 120, 113, 22))
        self.upNombrec.setObjectName("upNombrec")
        self.upPoblacionc = QtWidgets.QLineEdit(self.actualizarPais)
        self.upPoblacionc.setGeometry(QtCore.QRect(460, 210, 113, 22))
        self.upPoblacionc.setObjectName("upPoblacionc")
        self.upLenguajel = QtWidgets.QLineEdit(self.actualizarPais)
        self.upLenguajel.setGeometry(QtCore.QRect(730, 120, 113, 22))
        self.upLenguajel.setObjectName("upLenguajel")
        self.label_81 = QtWidgets.QLabel(self.actualizarPais)
        self.label_81.setGeometry(QtCore.QRect(640, 120, 71, 16))
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.actualizarPais)
        self.label_82.setGeometry(QtCore.QRect(640, 90, 71, 16))
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.actualizarPais)
        self.label_83.setGeometry(QtCore.QRect(640, 150, 71, 16))
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.actualizarPais)
        self.label_84.setGeometry(QtCore.QRect(640, 180, 71, 16))
        self.label_84.setObjectName("label_84")
        self.upPorcentajel = QtWidgets.QLineEdit(self.actualizarPais)
        self.upPorcentajel.setGeometry(QtCore.QRect(730, 180, 113, 22))
        self.upPorcentajel.setObjectName("upPorcentajel")
        self.upOfficiall = QtWidgets.QLineEdit(self.actualizarPais)
        self.upOfficiall.setGeometry(QtCore.QRect(730, 150, 113, 22))
        self.upOfficiall.setObjectName("upOfficiall")
        self.upCountryCodel = QtWidgets.QLineEdit(self.actualizarPais)
        self.upCountryCodel.setGeometry(QtCore.QRect(730, 90, 113, 22))
        self.upCountryCodel.setObjectName("upCountryCodel")
        self.label_86 = QtWidgets.QLabel(self.actualizarPais)
        self.label_86.setGeometry(QtCore.QRect(100, 50, 91, 16))
        self.label_86.setObjectName("label_86")
        self.codigoPaisUp = QtWidgets.QLineEdit(self.actualizarPais)
        self.codigoPaisUp.setGeometry(QtCore.QRect(190, 50, 113, 22))
        self.codigoPaisUp.setObjectName("codigoPaisUp")
        self.idCiudadup = QtWidgets.QLineEdit(self.actualizarPais)
        self.idCiudadup.setGeometry(QtCore.QRect(450, 50, 113, 22))
        self.idCiudadup.setObjectName("idCiudadup")
        self.codLenguaup = QtWidgets.QLineEdit(self.actualizarPais)
        self.codLenguaup.setGeometry(QtCore.QRect(720, 50, 113, 22))
        self.codLenguaup.setObjectName("codLenguaup")
        self.label_85 = QtWidgets.QLabel(self.actualizarPais)
        self.label_85.setGeometry(QtCore.QRect(390, 50, 61, 16))
        self.label_85.setObjectName("label_85")
        self.label_87 = QtWidgets.QLabel(self.actualizarPais)
        self.label_87.setGeometry(QtCore.QRect(650, 50, 49, 16))
        self.label_87.setObjectName("label_87")
        self.upPais = QtWidgets.QPushButton(self.actualizarPais)
        self.upPais.setGeometry(QtCore.QRect(150, 550, 101, 24))
        self.upPais.setObjectName("upPais")
        self.upCiudad = QtWidgets.QPushButton(self.actualizarPais)
        self.upCiudad.setGeometry(QtCore.QRect(430, 250, 111, 24))
        self.upCiudad.setObjectName("upCiudad")
        self.upLengua = QtWidgets.QPushButton(self.actualizarPais)
        self.upLengua.setGeometry(QtCore.QRect(700, 250, 111, 24))
        self.upLengua.setObjectName("upLengua")
        self.tablaCiudad.addTab(self.actualizarPais, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 121))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(101, 62, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_88 = QtWidgets.QLabel(self.frame)
        self.label_88.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.label_88.setObjectName("label_88")
        self.frame.raise_()
        self.tablaCiudad.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tablaCiudad.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tabla_pais.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tabla_pais.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabla_pais.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Continente"))
        item = self.tabla_pais.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Region"))
        item = self.tabla_pais.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Surface Area"))
        item = self.tabla_pais.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "indepepyear"))
        item = self.tabla_pais.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Poblacion"))
        item = self.tabla_pais.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Expectativa"))
        item = self.tabla_pais.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "GNP"))
        item = self.tabla_pais.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "GNPOid"))
        item = self.tabla_pais.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Nombre Local"))
        item = self.tabla_pais.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Forma de Gob"))
        item = self.tabla_pais.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Cabeza de Estado"))
        item = self.tabla_pais.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Capital"))
        item = self.tabla_pais.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Codigo2"))
        self.bt_refreshpais.setText(_translate("MainWindow", "Buscar Todos"))
        self.label.setText(_translate("MainWindow", "Codigo:"))
        self.bt_buscarpais.setText(_translate("MainWindow", "Buscar"))
        self.tablaCiudad.setTabText(self.tablaCiudad.indexOf(self.tabPais), _translate("MainWindow", "Consultar Pais"))
        item = self.tableLenguaje.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "countrycode"))
        item = self.tableLenguaje.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "language"))
        item = self.tableLenguaje.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableLenguaje.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "percentage"))
        self.label_2.setText(_translate("MainWindow", "Lenguaje"))
        self.bt_buscarlenguaje.setText(_translate("MainWindow", "Buscar"))
        self.bt_buscarTodosl.setText(_translate("MainWindow", "Buscar Todos"))
        self.tablaCiudad.setTabText(self.tablaCiudad.indexOf(self.tabLenguaje), _translate("MainWindow", "Consultar Lenguaje"))
        item = self.tableCiudad.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableCiudad.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableCiudad.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "countrycode"))
        item = self.tableCiudad.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "district"))
        item = self.tableCiudad.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "population"))
        self.label_3.setText(_translate("MainWindow", "ID:"))
        self.bt_buscarciudad.setText(_translate("MainWindow", "Buscar"))
        self.bt_buscarTodosc.setText(_translate("MainWindow", "Buscar Todos"))
        self.tablaCiudad.setTabText(self.tablaCiudad.indexOf(self.tabCiudad), _translate("MainWindow", "Consultar Ciudad"))
        self.label_4.setText(_translate("MainWindow", "Codigo (3 digitos)"))
        self.label_5.setText(_translate("MainWindow", "Nombre"))
        self.label_6.setText(_translate("MainWindow", "Contienente"))
        self.label_7.setText(_translate("MainWindow", "Region"))
        self.label_8.setText(_translate("MainWindow", "Surface Area"))
        self.label_9.setText(_translate("MainWindow", "Independencia"))
        self.label_10.setText(_translate("MainWindow", "poblacion"))
        self.label_11.setText(_translate("MainWindow", "Expectativa de vida"))
        self.label_12.setText(_translate("MainWindow", "GNP"))
        self.label_13.setText(_translate("MainWindow", "GNPOID"))
        self.label_14.setText(_translate("MainWindow", "Nombre Local"))
        self.label_15.setText(_translate("MainWindow", "Forma de Gobierno"))
        self.label_16.setText(_translate("MainWindow", "Cabeza de Estado"))
        self.label_17.setText(_translate("MainWindow", "Capital"))
        self.label_18.setText(_translate("MainWindow", "codigo2 (2Dig)"))
        self.bt_Addpais.setText(_translate("MainWindow", "Agregar Pais"))
        self.label_19.setText(_translate("MainWindow", "ID"))
        self.label_20.setText(_translate("MainWindow", "Nombre"))
        self.label_21.setText(_translate("MainWindow", "CountryCode"))
        self.label_22.setText(_translate("MainWindow", "Distrito"))
        self.label_23.setText(_translate("MainWindow", "Poblacion"))
        self.label_24.setText(_translate("MainWindow", "countryCodel"))
        self.label_25.setText(_translate("MainWindow", "Lenguaje"))
        self.label_26.setText(_translate("MainWindow", "Es Official?"))
        self.label_27.setText(_translate("MainWindow", "Porcentaje"))
        self.bt_AddCiudad.setText(_translate("MainWindow", "Agregar CIudad"))
        self.pushButton.setText(_translate("MainWindow", "Agregar Lenguaje"))
        self.tablaCiudad.setTabText(self.tablaCiudad.indexOf(self.agregarCampo), _translate("MainWindow", "Agregar Campo"))
        self.label_28.setText(_translate("MainWindow", "Codigo Pais:"))
        self.bt_EliminarPais.setText(_translate("MainWindow", "Eliminar pais"))
        self.estatusPais.setText(_translate("MainWindow", "ESTATUS"))
        self.label_29.setText(_translate("MainWindow", "Lenguaje"))
        self.label_30.setText(_translate("MainWindow", "ID ciudad"))
        self.bt_EliminarCiudad.setText(_translate("MainWindow", "Eliminar CIudad"))
        self.estatusCiudad.setText(_translate("MainWindow", "ESTATUS"))
        self.pushButton_2.setText(_translate("MainWindow", "ESTATUS"))
        self.pushButton_3.setText(_translate("MainWindow", "Eliminar Leng"))
        self.tablaCiudad.setTabText(self.tablaCiudad.indexOf(self.eliminarCampo), _translate("MainWindow", "Eliminar Campo"))
        self.label_61.setText(_translate("MainWindow", "Contienente"))
        self.label_62.setText(_translate("MainWindow", "GNPOID"))
        self.label_63.setText(_translate("MainWindow", "Cabeza de Estado"))
        self.label_64.setText(_translate("MainWindow", "Nombre Local"))
        self.label_65.setText(_translate("MainWindow", "Nombre"))
        self.label_66.setText(_translate("MainWindow", "Codigo (3 digitos)"))
        self.label_67.setText(_translate("MainWindow", "Expectativa de vida"))
        self.label_68.setText(_translate("MainWindow", "Surface Area"))
        self.label_69.setText(_translate("MainWindow", "Capital"))
        self.label_70.setText(_translate("MainWindow", "Region"))
        self.label_71.setText(_translate("MainWindow", "Independencia"))
        self.label_72.setText(_translate("MainWindow", "Forma de Gobierno"))
        self.label_73.setText(_translate("MainWindow", "GNP"))
        self.label_74.setText(_translate("MainWindow", "codigo2 (2Dig)"))
        self.label_75.setText(_translate("MainWindow", "poblacion"))
        self.label_76.setText(_translate("MainWindow", "Poblacion"))
        self.label_77.setText(_translate("MainWindow", "Nombre"))
        self.label_78.setText(_translate("MainWindow", "Distrito"))
        self.label_79.setText(_translate("MainWindow", "ID"))
        self.label_80.setText(_translate("MainWindow", "CountryCode"))
        self.label_81.setText(_translate("MainWindow", "Lenguaje"))
        self.label_82.setText(_translate("MainWindow", "countryCodel"))
        self.label_83.setText(_translate("MainWindow", "Es Official?"))
        self.label_84.setText(_translate("MainWindow", "Porcentaje"))
        self.label_86.setText(_translate("MainWindow", "Codigo del pais"))
        self.label_85.setText(_translate("MainWindow", "ID ciudad"))
        self.label_87.setText(_translate("MainWindow", "Lenguaje"))
        self.upPais.setText(_translate("MainWindow", "Actualizar Pais"))
        self.upCiudad.setText(_translate("MainWindow", "Actualizar Ciudad"))
        self.upLengua.setText(_translate("MainWindow", "Actualizar Lenguaje"))
        self.tablaCiudad.setTabText(self.tablaCiudad.indexOf(self.actualizarPais), _translate("MainWindow", "Actualizar Pais"))
        self.label_88.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">WORLD DB</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
