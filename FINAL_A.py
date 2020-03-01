from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.utils import iface
from qgis.core import *
from qgis.gui import *
from PyQt5.QtSql import QSqlDatabase
from osgeo import gdal
from datetime import datetime
import glob, os, processing, sqlite3#, sys
####################################
prj = QgsProject.instance()
###
d = datetime.now()
d.isoformat()
fecha=(d.strftime("%d-%m-%Y"))
####
proyectopath = prj.readPath("./")
proyectocod = prj.readPath("..")
proyectoparroquia = proyectocod[:-11]
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
    codproj = codpro[0:15]
    codparr = str(codpro [0:6])
    codsect = codproj[:12]
    ###ABRIR PROYECTO
    contadornumeros = 0
    for x in codproj:
        if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
            contadornumeros = contadornumeros + 1
    if contadornumeros >= 12:
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
        #FUENTE ESTILOS
        carpetaestilos = (r"C:\Users\rsgis\Desktop\sty\ESTILOS_ORIGINALES\AMANZANADO")
        #rio_a
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
        #manzanas
        capaimportar = 'MAN_A'
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
        #FILTRO MAN
        man = (('\"man" != '+'\''+ codproj+'%''\''))
        vlayer.setSubsetString(man)
        try:
            MAN_A = prj.mapLayersByName("MAN_A")[0]
        except:
            MAN_A = "!MAN_A"
        #CA04_A
        capaimportar = 'CA04_A'
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
        #FILTRO MAN
        man = (('\"man" LIKE '+'\''+ codproj+'%''\''))
        vlayer.setSubsetString(man)
        try:
            CA04_A = prj.mapLayersByName("CA04_A")[0]
        except:
            CA04_A = "!CA04_A"
        ###ADICIONALES_L
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
        #EJES_L
        capaimportar = 'EJES_L'
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
            EJES_L = prj.mapLayersByName("EJES_L")[0]
        except:
            EJES_L = "!EJES_L"
        #
        capaimportar = 'INGRESOS_L'
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
        vlayer.setSubsetString(man)
        try:
            INGRESOS_L = prj.mapLayersByName("INGRESOS_L")[0]
        except:
            INGRESOS_L = "!INGRESOS_L"
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
        sector = (('\"sector" LIKE '+'\''+ codsect+'%''\''))
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
        vlayer.setSubsetString(man)
        try:
            VIV_P = prj.mapLayersByName("VIV_P")[0]
        except:
            VIV_P = "!VIV_P"
        ######ZOOM
        mc = iface.mapCanvas()
        mc.setExtent(CA04_A.extent())
        mc.refresh
        e = e+1
        ###final guardar
        prj.write(promaspath)
###################################
    val_a =  val_a + 1
###################################
    if val_a == 1:
        if RIO_A == "!RIO_A":
            E_RIO = "FALTA RIO"
            errores = errores + 1
        else:
            E_RIO = ""
        if MAN_A == "!MAN_A":
            E_MAN = "FALTA MAN"
            errores = errores + 1
        else:
            E_MAN = ""
        if CA04_A == "!CA04_A":
            E_CA04 = "FALTA CA04"
            errores = errores + 1
        else:
            E_CA04 = ""
        if ADICIONALES_L == "!ADICIONALES_L":
            E_ADICIONALES = "FALTA ADICIONALES_L"
            errores = errores + 1
        else:
            E_ADICIONALES = ""
        if EJES_L == "!EJES_L":
            E_EJES = "FALTA EJES"
            errores = errores + 1
        else:
            E_EJES = ""
        if SEC_L == "!SEC_L":
            E_SEC = "FALTA SEC_L"
            errores = errores + 1
        else:
            E_SEC = ""
        if INGRESOS_L == "!INGRESOS_L":
            E_INGRESOS = "FALTA INGRESOS"
            errores = errores + 1
        else:
            E_INGRESOS = ""
        if VERTICES_P == "!VERTICES_P":
            E_VERTICES = "FALTA VERTICES"
            errores = errores + 1
        else:
            E_VERTICES = ""
        if VIV_P == "!VIV_P":
            E_VIV = "FALTA VIV"
            errores = errores + 1
        else:
            E_VIV = ""
            
        if errores >= 1:
            estadocapas = [E_RIO, E_MAN, E_CA04, E_ADICIONALES, E_EJES, E_SEC, E_INGRESOS, E_VERTICES, E_VIV]
            archivoerrora = (r"C:\FINAL\REGISTRO\ERRORES_A.txt")
            with open(archivoerrora, "a+") as file_object:
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
print("…a")