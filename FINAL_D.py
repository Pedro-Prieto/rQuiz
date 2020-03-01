from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.utils import iface
from qgis.core import *
from qgis.gui import *
from PyQt5.QtSql import QSqlDatabase
from osgeo import gdal
from datetime import datetime
import glob, os, processing, sqlite3
####################################
prj = QgsProject.instance()
#####
d = datetime.now()
d.isoformat()
fecha=(d.strftime("%d-%m-%Y"))
####
proyectopath = prj.readPath("./")
proyectocod = prj.readPath("..")
proyectoparroquia=proyectocod[:-9]
amanzanadodisperso = proyectocod[proyectocod.rfind("/")+1:]
parroquian = proyectoparroquia[proyectoparroquia.rfind("/")+1:]
cantonruta = os.path.dirname(proyectoparroquia)
cantonn = cantonruta[cantonruta.rfind("/")+1:]
provinciaruta = os.path.dirname(cantonruta)
provincian = provinciaruta[provinciaruta.rfind("/")+1:]
#LISTADO INTERNO
path=proyectopath
file_list = os.listdir(path)
file_list= [file for file in os.listdir(path) if os.path.splitext(file)[1] == '.qgz']
val_a = 0
errores = 0
for file in file_list:
    proyectoext=file
    promaspath = (proyectopath + '/' + proyectoext)
    ####
    e=0
    codpro = file[:-4]
    codproj = codpro[0:12]
    codparr = str(codpro [0:6])
    #codsect = codproj[:12]
    ###ABRIR PROYECTO
    contadornumeros = 0
    for x in codproj:
        if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
            contadornumeros = contadornumeros + 1
    if contadornumeros >= 12:
        pa=0
        nsa=0
        nft=0
        
        ###
        prj.read(promaspath)
        ####Remover capas
        prj.removeAllMapLayers()
        #Borrar grupos
        root = prj.layerTreeRoot()
        for group in [child for child in root.children() if child.nodeType() == 0]:
            root.removeChildNode(group)
        #LISTADO INTERNO
        path=proyectopath
        file_list = os.listdir(path)
        file_list= [file for file in os.listdir(path) if os.path.splitext(file)[1] == '.qgz']
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
        ############CARGAR
        #FUENTE
        carpetaestilos = (r"C:\Users\rsgis\Desktop\sty\ESTILOS_ORIGINALES\DISPERSO")
        #RIO_A
        capaimportar = 'RIO_A'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            RIO_A = prj.mapLayersByName("RIO_A")[0]
        except:
            RIO_A = "!RIO_A"
        #ISLA_A
        capaimportar = 'ISLA_A'#
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            ISLA_A = prj.mapLayersByName("ISLA_A")[0]
        except:
            ISLA_A = "!ISLA_A"
        #ANEXO_A
        capaimportar = 'ANEXO_A'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        #Filtro localidad
        localidad = (('\"sec" LIKE '+'\''+ codproj+'%''\''))
        vlayer.setSubsetString(localidad)
        try:
            ANEXO_A = prj.mapLayersByName("ANEXO_A")[0]
        except:
            ANEXO_A = "!ANEXO_A"
        #RIO_L
        capaimportar = 'RIO_L'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            RIO_L = prj.mapLayersByName("RIO_L")[0]
        except:
            RIO_L = "!RIO_L"
        #ADICIONALES_L
        capaimportar = 'ADICIONALES_L'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            ADICIONALES_L = prj.mapLayersByName("ADICIONALES_L")[0]
        except:
            ADICIONALES_L = "!ADICIONALES_L"
        #ADICIONALES_P
        capaimportar = 'ADICIONALES_P'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            ADICIONALES_P = prj.mapLayersByName("ADICIONALES_P")[0]
        except:
            ADICIONALES_P = "!ADICIONALES_P"
        #VIA_RUTA_L
        capaimportar = 'VIA_RUTA_L'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            VIA_RUTA_L = prj.mapLayersByName("VIA_RUTA_L")[0]
        except:
            VIA_RUTA_L = "!VIA_RUTA_L"
        #SEC_L
        capaimportar = 'SEC_L'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            SEC_L = prj.mapLayersByName("SEC_L")[0]
        except:
            SEC_L = "!SEC_L"
        #LOC_P
        capaimportar = 'LOC_P'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        #Filtro localidad
        localidad = (('\"loc" LIKE '+'\''+ codproj+'%''\''))
        vlayer.setSubsetString(localidad)
        try:
            LOC_P = prj.mapLayersByName("LOC_P")[0]
        except:
            LOC_P = "!LOC_P"
        #GEO_CAB
        capaimportar = 'GEO_CAB'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            GEO_CAB = prj.mapLayersByName("GEO_CAB")[0]
        except:
            GEO_CAB = "!GEO_CAB"
        ########I_PUNTO_ACOTADO
        capaimportar = 'I_PUNTO_ACOTADO'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            I_PUNTO_ACOTADO = prj.mapLayersByName("I_PUNTO_ACOTADO")[0]
        except:
            pa=pa+1
        ########PUNTO_ACOTADO
        capaimportar = 'PUNTO_ACOTADO'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            QgsProject.instance().addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            PUNTO_ACOTADO = prj.mapLayersByName("PUNTO_ACOTADO")[0]
        except:
            pa=pa+1
        ########PUNTO_ACOTADO
        ###I_NOMBRES_FORMAS_TIERRA
        capaimportar = 'I_NOMBRES_FORMAS_TIERRA'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            QgsProject.instance().addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            I_NOMBRES_FORMAS_TIERRA = prj.mapLayersByName("I_NOMBRES_FORMAS_TIERRA")[0]
        except:
            nft=nft+1

        #NOMBRES_FORMAS_TIERRA
        capaimportar = 'NOMBRES_FORMAS_TIERRA'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj().addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            NOMBRES_FORMAS_TIERRA = prj.mapLayersByName("NOMBRES_FORMAS_TIERRA")[0]
        except:
            nft=nft+1

        #I_NOMBRES_SITIOS_AREAS
        capaimportar = 'I_NOMBRES_SITIOS_AREAS'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            I_NOMBRES_SITIOS_AREAS = prj.mapLayersByName("I_NOMBRES_SITIOS_AREAS")[0]
        except:
            nsa=nsa+1

        #NOMBRES_SITIOS_AREAS
        capaimportar = 'NOMBRES_SITIOS_AREAS'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        try:
            NOMBRES_SITIOS_AREAS = prj.mapLayersByName("NOMBRES_SITIOS_AREAS")[0]
        except:
            nsa=nsa+1

        #VERTICES_P
        capaimportar = 'VERTICES_P'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        #FILTRO VERTICES
        sector = (('\"sector" LIKE '+'\''+ codproj+'%''\''))
        vlayer.setSubsetString(sector)
        try:
            VERTICES_P = prj.mapLayersByName("VERTICES_P")[0]
        except:
            VERTICES_P = "!VERTICES_P"
        #VIV_P
        capaimportar = 'VIV_P'
        uri = QgsDataSourceUri()
        uri.setDatabase(proyectoparroquia + '/' + codparr + '.sqlite')
        schema = ''
        table = capaimportar
        geom_column = 'geom'
        uri.setDataSource(schema, table, geom_column)
        display_name = capaimportar
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        if vlayer.isValid():
            prj.addMapLayer(vlayer)
        vlayer.loadNamedStyle(carpetaestilos + '/' + capaimportar + '.qml')
        vlayer.setSubsetString(localidad)
        try:
            VIV_P = prj.mapLayersByName("VIV_P")[0]
        except:
            VIV_P = "!VIV_P"
        #########ZOOM
        mc = iface.mapCanvas()
        mc.setExtent(VERTICES_P.extent())
        mc.refresh
        ####final guardar
        e = e+1
        prj.write(promaspath)
###################################
    val_a =  val_a + 1
####################################
    if val_a == 1:
        if RIO_A == "!RIO_A":
            E_RIO = "FALTA RIO_A"
            errores = errores + 1
        else:
            E_RIO = ""
        if ANEXO_A == "!ANEXO_A":
            E_ANEXO =  "FALTA ANEXO"
            errores = errores + 1
        else:
            E_ANEXO = ""
        if RIO_L == "!RIO_L":
            E_RIO_L = "FALTA RIO_L"
            errores = errores + 1
        else:
            E_RIO_L = ""
        if ADICIONALES_L == "!ADICIONALES_L":
            E_ADICIONALES_L = "FALTA ADICIONALES_L"
            errores = errores + 1
        else:
            E_ADICIONALES_L = ""
        if VIA_RUTA_L == "!VIA_RUTA_L":
            E_RUTA = "VIA_RUTA_L"
            errores = errores + 1
        else:
            E_RUTA = ""
        if SEC_L == "!SEC_L":
            E_SEC_L = "FALTA SEC_L"
            errores = errores + 1
        else:
            E_SEC_L = ""
        if LOC_P == "!LOC_P":
            E_LOC = "FALTA LOC_P"
            errores = errores + 1
        else:
            E_LOC = ""
        if GEO_CAB == "!GEO_CAB":
            E_GEO_CAB = "FALTA GEO_CAB"
            errores = errores + 1
        else:
            E_GEO_CAB = ""
        if VERTICES_P == "!VERTICES_P":
            E_VERTICES = "FALTA VERTICES_P"
            errores = errores + 1
        else:
            E_VERTICES = ""
        if VIV_P == "!VIV_P":
            E_VIV_P = "FALTA VIV_P"
            errores = errores + 1
        else:
            E_VIV_P = ""
        ####
        if pa == 2:
            E_PUNTO_ACOTADO = "FALTA PUNTO_ACOTADO"
            errores = errores + 1
        else:
            E_PUNTO_ACOTADO = ""
        if nsa == 2:
            E_NOMBRES_SITIOS_AREAS = "FALTA NOMBRES_SITIOS_AREAS"
            errores = errores + 1
        else:
            E_NOMBRES_SITIOS_AREAS = ""
        if nft == 2:
            E_NOMBRES_FORMAS_TIERRA = "FALTA NOMBRES_FORMAS_TIERRA"
            errores = errores + 1
        else:
            E_NOMBRES_FORMAS_TIERRA = ""
    ####
        if errores >= 1:
            estadocapas = [E_RIO, E_ANEXO, E_RIO_L, E_ADICIONALES_L, E_RUTA, E_SEC_L, E_LOC, E_GEO_CAB, E_VERTICES, E_VIV_P, E_PUNTO_ACOTADO, E_NOMBRES_SITIOS_AREAS, E_NOMBRES_FORMAS_TIERRA]
            archivoerrord = ("C:\FINAL\REGISTRO\ERRORES_D.txt")
            with open(archivoerrord, "a+") as file_object:
                file_object.seek(0)
                file_object.write("\n")
                file_object.write(str(fecha)+";" + str(errores)+";" +str(codparr)+".sqlite;" + str(estadocapas))
            print(str(estadocapas))
            break
    archivopro = (r"C:\FINAL\REGISTRO\REG.txt")
    with open(archivopro, "a+") as file_object:
        file_object.seek(0)
        file_object.write("\n")
        file_object.write(str(fecha)+";"+str(codparr)+ ";"+ str(amanzanadodisperso)+";" + str(val_a) + ";" + str(e) + ";" + str(proyectoext))
if errores < 1:
    with open(r"C:\FINAL\REGISTRO\HECHO.txt", "a+") as file_object:
        file_object.seek(0)
        file_object.write("\n")
        file_object.write(str(fecha)+";" +str(provincian)+";" + str(cantonn)+";" + str(parroquian) + ";" + str(amanzanadodisperso))
print("…d")