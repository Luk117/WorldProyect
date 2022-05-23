from ConexionDB import *
from Query import *

conexion_db = ConexionBD('jd4130201')

codigoadd = ''
nombrepadd = ''
continenteadd = 'Asia'
regionadd = ''
surfaceareaadd = '0'
independenciaadd = '0'
poblacionpadd = '0'
expectativaadd = '0'
gnpadd = '0'
gnpoldadd = '0'
localnameadd = ''
gobiernoadd = ''
cabezadeestadoadd = ''
capitaladd = '0'
codigo2add = ''


conexion_db.agrega_pais(codigoadd, nombrepadd, continenteadd, regionadd, surfaceareaadd, independenciaadd,
                             poblacionpadd, expectativaadd, gnpadd, gnpoldadd, localnameadd, gobiernoadd,
                             cabezadeestadoadd, capitaladd, codigo2add)


