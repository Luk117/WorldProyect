from ConexionDB import ConexionBD
from GUI import *
from Query import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conexion_db = ConexionBD('jd4130201')
        # Acciones de Boton

        # Mostrar todos los datos
        #   Solo es no poner nada en la barra de busqueda

        # Buscar dato
        self.ui.bt_buscarpais_A.clicked.connect(self.buscar_pais)
        self.ui.bt_buscarciudad_A.clicked.connect(self.buscar_ciudad)
        self.ui.bt_buscarlenguaje_A.clicked.connect(self.buscar_lenguaje)

        # busqueda avanzada
        self.ui.bt_busqueda_av.clicked.connect(self.busqueda_avanzada)

        # clear busqueda
        self.ui.bt_clear_busqueda.clicked.connect(self.clear_busqueda)

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
            self.ui.cbx_c_id: 'c.id',
            self.ui.cbx_c_name: 'c.name',
            self.ui.cbx_c_country: 'c.CountryCode',  # look into how to actually show the country not the code
            self.ui.cbx_c_district: 'c.District',
            self.ui.cbx_c_population: 'c.population',
        }

        self.cbxes_lang = {
            self.ui.cbx_l_lang: 'l.Language',
            self.ui.cbx_l_isOfficial: 'l.IsOfficial',
            self.ui.cbx_l_percentage: 'l.Percentage',
            self.ui.cbx_l_country: 'l.CountryCode',  # look into how to actually show the country not the code
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
        self.ui.codeCUpLanc.returnPressed.connect(self.autofill_lan)

        # Ingresar dato
        self.ui.bt_Addpais.clicked.connect(self.insert_pais)
        self.ui.bt_AddCiudad.clicked.connect(self.insert_ciudad)
        self.ui.bt_AddLenguaje.clicked.connect(self.insert_lenguaje)

        # Tamaño de Tablas
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

    # ------------------------------------Metodos para los paises------------------------------------------------------

    def buscar_pais(self):
        # set table and query
        sql = Query()
        sql.append_tables('country as p')

        # parameters
        if not set_parameters(sql, self.cbxes_pais):
            sql.append_parameters(self.conexion_db.get_column_names('country'))

        # set table
        set_tabla_busqueda(sql, self.ui.tabla_busqueda)

        # decide what to look for (with queries)
        input_p = self.ui.codigoPais_A.text()
        par_p = self.ui.comboBox_p.currentText()
        if not input_p.__eq__(''):
            sql.append_wheres("{} like '{}'".format(par_p, input_p))
        datos = self.conexion_db.buscar(sql.get_query())

        set_items(datos, self.ui.tabla_busqueda)

    def busqueda_avanzada(self):
        query = Query()

        # define which tables and parameters are being used
        name_p = self.ui.codigoPais_A.text()
        name_c = self.ui.codigoCiudad_A.text()
        name_l = self.ui.codigoLenguaje_A.text()

        country_used = set_parameters(query, self.cbxes_pais) or bool(name_p)
        city_used = set_parameters(query, self.cbxes_ciudad) or bool(name_c)
        language_used = set_parameters(query, self.cbxes_lang) or bool(name_l)

        if country_used or city_used or language_used:
            using_parameters = bool(query.parameters)
            if country_used:
                query.append_tables('country as p')
                if not using_parameters:
                    query.append_parameters(self.conexion_db.get_column_names('country'))
            if city_used:
                query.append_tables('city as c')
                if not using_parameters:
                    query.append_parameters(self.conexion_db.get_column_names('city'))
            if language_used:
                query.append_tables('countrylanguage as l')
                if not using_parameters:
                    query.append_parameters(self.conexion_db.get_column_names('countrylanguage'))

            # set table
            set_tabla_busqueda(query, self.ui.tabla_busqueda)

            # decide connections
            if country_used and city_used:
                query.append_wheres('p.code = c.countrycode')
            if country_used and language_used:
                query.append_wheres('p.code = l.countrycode')
            if city_used and language_used:
                query.append_wheres('c.countrycode = l.countrycode')

            # decide what to look for
            if bool(name_p):
                query.append_wheres("p.name like '{}'".format(name_p))
            if bool(name_c):
                query.append_wheres("c.name like '{}'".format(name_c))
            if bool(name_l):
                query.append_wheres("l.language like '{}'".format(name_l))

            datos = self.conexion_db.buscar(query.get_query())
            set_items(datos, self.ui.tabla_busqueda)
        else:
            self.error_msg("Debe seleccionar al menos un parametro o llenar un campo")

    def clear_busqueda(self):
        for par in self.cbxes_pais:
            par.setChecked(False)
        for par in self.cbxes_ciudad:
            par.setChecked(False)
        for par in self.cbxes_lang:
            par.setChecked(False)

        self.ui.codigoPais_A.setText('')
        self.ui.codigoCiudad_A.setText('')
        self.ui.codigoLenguaje_A.setText('')

        for i in range(24):
            self.ui.tabla_busqueda.setColumnHidden(i, True)

    def insert_pais(self):
        codigoadd = (self.ui.addCodep.text())
        if not codigoadd:
            self.error_msg("Ingrese un codigo")
            return -1
        nombrepadd = (self.ui.addNamep.text())
        if not nombrepadd:
            self.error_msg("Ingrese un Nombre")
            return -1
        continenteadd = (self.ui.addContientep.text()) or 'Asia'
        regionadd = (self.ui.addRegionp.text())
        surfaceareaadd = (self.ui.addSurfacep.text()) or '0'
        independenciaadd = (self.ui.addIndp.text()) or '0'
        poblacionpadd = (self.ui.addPoblacionp.text()) or '0'
        expectativaadd = (self.ui.addExpectp.text()) or '0'
        gnpadd = (self.ui.addGnpp.text()) or '0'
        gnpoldadd = (self.ui.addGnoid.text()) or '0'
        localnameadd = (self.ui.addNomlocalp.text())
        gobiernoadd = (self.ui.addFormGovp.text())
        cabezadeestadoadd = (self.ui.addCabEstp.text())
        capitaladd = (self.ui.addCapitalp.text()) or '0'
        codigo2add = (self.ui.addCode2p.text())

        try:
            self.conexion_db.agrega_pais(codigoadd, nombrepadd, continenteadd, regionadd, surfaceareaadd,
                                         independenciaadd,
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

            self.info_msg("Pais agregado exitosamente")
        except:
            self.error_msg("Error al agregar pais: \n Recuerda revisar que todos los tipos de dato sean los adecuados")

    def eliminar_pais(self):
        codigoel = self.ui.codigoEliminarp.text()
        codigoel = str("'" + codigoel + "'")

        resp = (self.conexion_db.elimina_pais(codigoel))

        if resp is None:
            self.ui.estatusPais.setText("NO EXISTE")
        elif resp == 0:
            self.ui.estatusPais.setText("NO EXISTE")

        else:
            self.ui.estatusPais.setText("SE ELIMINO")

    def actualizar_pais(self):
        if ((str(self.ui.codigoPaisUp.text()) == "")):
            msg = "¡Debe ingresar el código del país a actualizar!"
            self.error_msg(msg)
        else:

            codigoadd = (self.ui.codigoPaisUp.text())
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

            try:
                self.conexion_db.actualiza_pais(codigoadd, nombrepadd, continenteadd, regionadd, surfaceareaadd,
                                                independenciaadd, poblacionpadd, expectativaadd, gnpadd, gnpoldadd,
                                                localnameadd,
                                                gobiernoadd, cabezadeestadoadd, capitaladd, codigo2add)

                msg = "¡Se ha actualizado el país!"
                self.info_msg(msg)

                self.ui.codigoPaisUp.clear()
                self.ui.upNamep.clear()
                self.ui.upContientep.clear()
                self.ui.upRegionp.clear()
                self.ui.upSurfacep.clear()
                self.ui.upIndp.clear()
                self.ui.upPoblacionp.clear()
                self.ui.upGnpp.clear()
                self.ui.upGnoidp.clear()
                self.ui.upNomlocalp.clear()
                self.ui.upExpectp.clear()
                self.ui.upFormGovp.clear()
                self.ui.upCabEstp.clear()
                self.ui.upCapitalp.clear()
                self.ui.upCode2p.clear()
            except:
                self.error_msg("Asegurese de que todos los tipos de dato sean coherentes")

    def fillact_pais(self):
        codigorr = str(self.ui.codigoPaisUp.text())
        codigorr = ("'" + codigorr + "'")
        autofill = self.conexion_db.get_pais_by_code(codigorr)
        if not autofill:
            self.error_msg("No se encontraron datos")

        for data in autofill:
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
            sql.append_parameters(self.conexion_db.get_column_names('countrylanguage'))

        # set table
        set_tabla_busqueda(sql, self.ui.tabla_busqueda)

        input_l = self.ui.codigoLenguaje_A.text()
        par_l = self.ui.comboBox_l.currentText()
        if not input_l.__eq__(''):
            sql.append_wheres("{} like '{}'".format(par_l, input_l))
        datos = self.conexion_db.buscar(sql.get_query())

        set_items(datos, self.ui.tabla_busqueda)

    def insert_lenguaje(self):

        addcodigopaisl = self.ui.addCountryCodel.text()
        if not addcodigopaisl:
            self.error_msg("Ingrese un codigo de pais")
            return -1
        addlenguaje = self.ui.addLenguajel.text()
        if not addlenguaje:
            self.error_msg("Ingrese un Nombre para el lenguaje")
            return -1
        addesofficial = self.ui.addOfficiall.text() or 'F'
        addporcentaje = self.ui.addPorcentajel.text() or '0'

        try:
            self.conexion_db.agrega_lenguaje(addcodigopaisl, addlenguaje, addesofficial, addporcentaje)

            self.ui.addCountryCodel.clear()
            self.ui.addLenguajel.clear()
            self.ui.addOfficiall.clear()
            self.ui.addPorcentajel.clear()
            self.info_msg("Lenguaje agregado exitosamente")
        except:
            self.error_msg(
                "Error al agregar lenguaje: \n Recuerda revisar que todos los tipos de dato sean los adecuados")

    def eliminar_lenguaje(self):
        lenguajedel = self.ui.lineEdit_3.text()
        lenguajedel = ("'" + lenguajedel + "'")

        resp = (self.conexion_db.elimina_lenguaje(lenguajedel))

        if resp is None:
            self.ui.estatusLenguaje.setText("NO EXISTE")
        elif resp == 0:
            self.ui.estatusLenguaje.setText("NO EXISTE")
        else:
            self.ui.estatusLenguaje.setText("SE ELIMINO")

    def autofill_lan(self):

        if ((str(self.ui.codLenguaup.text()) == "") or (str(self.ui.codeCUpLanc.text()) == "")):
            msg = "¡Debe ingresar el código del país y el  lenguaje para poder autocompletar!"
            self.error_msg(msg)
        else:
            codigorr = str(self.ui.codLenguaup.text())
            codigorr = ("'" + codigorr + "'")
            codigo_pais = str(self.ui.codeCUpLanc.text())
            codigo_pais = ("'" + codigo_pais + "'")
            autofill = self.conexion_db.busca_lenguajeYpais(codigorr, codigo_pais)
            if not autofill:
                self.error_msg("No se encontraron datos")

            for data in autofill:

                if (str(data[2]) == "T"):
                    self.ui.radioSi_lan.setChecked(True)
                    self.ui.radioNo_lan.setChecked(False)
                elif (str(data[2]) == "F"):
                    self.ui.radioNo_lan.setChecked(True)
                    self.ui.radioSi_lan.setChecked(False)
                self.ui.upPorcentajel.setText(str(data[3]))

    def actualizar_lan(self):

        if ((str(self.ui.codLenguaup.text()) == "") or (str(self.ui.codeCUpLanc.text()) == "")):
            msg = "¡Debe ingresar el código del país y el  lenguaje a actualizar!"
            self.error_msg(msg)
        else:
            upcodigopaisl = self.ui.codeCUpLanc.text()
            uplenguaje = self.ui.codLenguaup.text()
            upporcentaje = self.ui.upPorcentajel.text()
            upesofficial = ''
            oficial = ''
            porcentaje = ''

            if (self.ui.radioSi_lan.isChecked() == True):
                upesofficial = 'T'
            elif (self.ui.radioNo_lan.isChecked() == True):
                upesofficial = 'F'

            autofill = self.conexion_db.busca_lenguajeYpais(("'" + uplenguaje + "'"), ("'" + upcodigopaisl + "'"))
            for data in autofill:
                oficial = data[2]
                porcentaje = data[3]

            if (upesofficial == oficial) and (upporcentaje == porcentaje):
                msg = "¡Tienes que cambiar alguno de los datos para actualizar!"
                self.error_msg(msg)
            else:
                try:
                    self.conexion_db.actualiza_lenguaje(upcodigopaisl, uplenguaje, upesofficial, upporcentaje)
                    msg = "¡Se ha actualizado el lenguaje de este país!"
                    self.info_msg(msg)
                except:
                    self.error_msg(
                        "Recuerda revisar que todos los tipos de dato sean los adecuados")

    # ------------------------------------Metodos para las ciudades------------------------------------------------------

    def buscar_ciudad(self):
        # set table and query
        sql = Query()
        sql.append_tables('city as c')

        # parameters
        set_parameters(sql, self.cbxes_ciudad)
        if not sql.parameters:
            sql.append_parameters(self.conexion_db.get_column_names('city'))

        # set tables
        set_tabla_busqueda(sql, self.ui.tabla_busqueda)

        # decide what to look for
        name_c = self.ui.codigoCiudad_A.text()
        par_c = self.ui.comboBox_c.currentText()
        if not name_c.__eq__(''):
            sql.append_wheres("{} like '{}'".format(par_c, name_c))
        datos = self.conexion_db.buscar(sql.get_query())

        set_items(datos, self.ui.tabla_busqueda)

    def insert_ciudad(self):

        nombrecadd = str(self.ui.addNombrec.text())
        if not nombrecadd:
            self.error_msg("Ingrese un Nombre")
            return -1
        codigopaiscadd = str(self.ui.addCountryCodec.text())
        if not codigopaiscadd:
            self.error_msg("Ingrese un codigo de pais")
            return -1
        distritoadd = str(self.ui.addDistritoc.text())
        poblacioncadd = str(self.ui.addPoblacionc.text()) or '0'

        try:
            self.conexion_db.agrega_ciudad(nombrecadd, codigopaiscadd, distritoadd, poblacioncadd)

            # self.ui.addIDc.clear()
            self.ui.addNombrec.clear()
            self.ui.addCountryCodec.clear()
            self.ui.addDistritoc.clear()
            self.ui.addPoblacionc.clear()
            self.info_msg("Ciudad agregada exitosamente")
        except:
            self.error_msg(
                "Error al agregar ciudad: \n Recuerda revisar que todos los tipos de dato sean los adecuados y que countrycode exista")

    def eliminar_ciudad(self):
        delid = self.ui.codigoEliminarc.text()
        delid = ("'" + delid + "'")

        try:
            resp = (self.conexion_db.elimina_ciudad(delid))

            if resp is None:
                self.ui.estatusCiudad.setText("NO EXISTE")
            elif resp == 0:
                self.ui.estatusCiudad.setText("NO EXISTE")
            else:
                self.ui.estatusCiudad.setText("SE ELIMINO")
        except:
            self.error_msg("Debe ingresar solo numeros en este espacio")



    def actualizar_ciudad(self):
        if ((str(self.ui.idCiudadup.text()) == "")):
            msg = "¡Debe ingresar el código de la ciudad a actualizar!"
            self.error_msg(msg)
        else:
            idadd = str(self.ui.idCiudadup.text())
            nombrecadd = str(self.ui.upNombrec.text())
            codigopaiscadd = str(self.ui.upCountryCodec.text())
            distritoadd = str(self.ui.upDistritoc.text())
            poblacioncadd = str(self.ui.upPoblacionc.text())

            try:
                self.conexion_db.actualiza_ciudad(idadd, nombrecadd, codigopaiscadd, distritoadd, poblacioncadd)
                msg = "¡Se ha actualizado la ciudad!"
                self.info_msg(msg)
            except:
                self.error_msg(
                    "Recuerda revisar que todos los tipos de dato sean los adecuados")

    def fillact_city(self):
        codigorr = str(self.ui.idCiudadup.text())
        codigorr = ("'" + codigorr + "'")
        autofill = self.conexion_db.get_ciudad_by_id(codigorr)
        if not autofill:
            self.error_msg("No se encontraron datos")

        for data in autofill:
            self.ui.upNombrec.setText(str(data[1]))
            self.ui.upCountryCodec.setText(str(data[2]))
            self.ui.upDistritoc.setText(str(data[3]))
            self.ui.upPoblacionc.setText(str(data[4]))

    # Metodo Pop Up Errores
    def error_msg(self, error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText(error)

        msg.setWindowTitle("Advertencia")

        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

    # Metodo Pop Up Informacion
    def info_msg(self, info):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(info)

        msg.setWindowTitle("Información")

        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()


# ---------------------------------------Metodos para eliminar codigo repetido-------------------------------------------
def set_items(datos, table):
    n_rows = len(datos)
    n_columns = 0
    try:
        n_columns = len(datos[0])
    except:
        print("No data was found")
        mi_app.error_msg("No se encontraron datos")

    table.setRowCount(n_rows)

    for tablerow, row in enumerate(datos):
        for j in range(n_columns):
            table.setItem(tablerow, j, QtWidgets.QTableWidgetItem(str(row[j])))


def set_parameters(query: Query, cbxes: dict):
    added_parameters = False
    for box in cbxes:
        if box.isChecked():
            added_parameters = True
            query.append_parameters(cbxes[box])
    return added_parameters


def set_tabla_busqueda(query: Query, tabla):
    parameters = query.get_parameters()
    i = 0
    for par in parameters:
        tabla.horizontalHeaderItem(i).setText(par)
        tabla.setColumnHidden(i, False)
        i += 1
    for j in range(i, 24):
        tabla.setColumnHidden(j, True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
