# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GeoINCRA - Functions
                                 A QGIS plugin
        begin                : 2026-01-06
        copyright            : (C) 2026 by Tiago Prudencio and Leandro França
        email                : suporte@geoone.com.br
***************************************************************************/
"""

__author__ = 'Tiago Prudencio and Leandro França'
__date__ = '2026-01-06'
__copyright__ = '(C) 2026 by Tiago Prudencio and Leandro França'

from qgis.core import *
from qgis.PyQt.QtCore import QVariant
import platform, re
from numpy import radians, arctan, pi, sin, cos, sqrt, degrees, array, diag, ones, zeros, floor
from numpy.linalg import norm, pinv, inv
from qgis.core import QgsEllipsoidUtils
from datetime import datetime, timedelta
import datetime as dt
import numpy as np
import math

# Funções obtidas do plugin LFTools

def distEuclidiana2D(p1, p2):
    return float(np.sqrt((p1.x() - p2.x())**2 + (p1.y() - p2.y())**2))

def distEuclidiana3D(p1, p2):
    return float(np.sqrt((p1.x() - p2.x())**2 + (p1.y() - p2.y())**2  + (p1.z() - p2.z())**2))

def areaGauss(coords):
    soma = 0
    tam = len(coords)
    for k in range(tam):
        P1 = coords[ -1 if k==0 else k-1]
        P2 = coords[k]
        P3 = coords[ 0 if k==(tam-1) else (k+1)]
        soma += P2.x()*(P1.y() - P3.y())
    return soma/2


def Distancia(coords, dim):
    soma = 0
    tam = len(coords)
    for k in range(tam-1):
        P1 = coords[k]
        P2 = coords[k+1]
        if dim.lower() == '3d':
            soma += distEuclidiana3D(P1,P2)
        else: # '2d'
            soma += distEuclidiana2D(P1,P2)
    return float(soma)


def geom2PointList(geom):
    """
    Converte uma QgsGeometry em listas de QgsPoint, considerando seu tipo:
    - Point: retorna QgsPoint ou lista de QgsPoint
    - Line: retorna lista de pontos ou lista de listas de pontos
    - Polygon: retorna lista de anéis, cada um como lista de QgsPoint
    """
    tipo = geom.type()

    if tipo == 0:  # Ponto
        if geom.isMultipart():
            const1 = geom.constGet()
            return [const1.childGeometry(k) for k in range(len(geom.asMultiPoint()))]
        else:
            return geom.constGet()

    elif tipo == 1:  # Linha
        const1 = geom.constGet()
        if geom.isMultipart():
            return [
                [const1.childGeometry(k).childPoint(m) for m in range(len(linha))]
                for k, linha in enumerate(geom.asMultiPolyline())
            ]
        else:
            return [const1.childPoint(k) for k in range(len(geom.asPolyline()))]

    elif tipo == 2:  # Polígono
        const1 = geom.constGet()
        if geom.isMultipart():
            return [
                [
                    [const1.childGeometry(k).childGeometry(m).childPoint(n)
                     for n in range(len(anel))]
                    for m, anel in enumerate(poligono)
                ]
                for k, poligono in enumerate(geom.asMultiPolygon())
            ]
        else:
            return [
                [const1.childGeometry(k).childPoint(m)
                 for m in range(len(anel))]
                for k, anel in enumerate(geom.asPolygon())
            ]

# Conversão de coordenadas geodésicas para geocêntricas
def geod2geoc(lon, lat, h, a, f):
    lon = radians(lon)
    lat = radians(lat)
    e2 = f*(2-f) # primeira excentricidade
    N = a/sqrt(1-(e2*sin(lat)**2))
    X = (N+h)*cos(lat)*cos(lon)
    Y = (N+h)*cos(lat)*sin(lon)
    Z = (N*(1-e2)+h)*sin(lat)
    return (X,Y,Z)

# Conversão de coordenadas geocêntricas para geodésicas
def geoc2geod(X, Y, Z, a, f):
    b = a*(1-f)
    e2 = f*(2-f) # primeira excentricidade
    e2_2 = e2/(1-e2) # segunda excentricidade
    tg_u = (a/b)*Z/sqrt(X**2 + Y**2)
    sen_u = tg_u/sqrt(1+tg_u**2)
    cos_u = 1/sqrt(1+tg_u**2)
    lon = arctan(Y/X)
    lat = arctan( (Z+ e2_2 * b * sen_u**3) / (sqrt(X**2 + Y**2) - e2 * a * cos_u**3))
    N = a/sqrt(1-(e2*sin(lat)**2))
    h = sqrt(X**2 + Y**2)/cos(lat) - N
    lon = lon/pi*180
    lat = lat/pi*180
    return (lon, lat, h)

# Conversão de Coordenadas Geocêntrica para Topocêntricas
def geoc2enu(X, Y, Z, lon0, lat0, Xo, Yo, Zo):
    lon = radians(lon0)
    lat = radians(lat0)

    M = array(
    [
    [  -sin(lon),                     cos(lon),                 0 ],
    [  -sin(lat)*cos(lon),   -sin(lat)*sin(lon),          cos(lat)],
    [   cos(lat)*cos(lon),    cos(lat)*sin(lon),          sin(lat)]
    ]
    )

    T = array(
    [[X - Xo], [Y-Yo], [Z-Zo]]
    )

    Fo = array([[15e4],[25e4],[0]]) # False E and N

    R = M@T + Fo
    return (R[0,0], R[1,0], R[2,0])


def OrigemSGL(lon0, lat0, h0, crsGeo):
    ellipsoid_id = crsGeo.ellipsoidAcronym()
    ellipsoid = QgsEllipsoidUtils.ellipsoidParameters(ellipsoid_id)
    a = ellipsoid.semiMajor
    f_inv = ellipsoid.inverseFlattening
    f = 1/f_inv
    X0, Y0, Z0 = geod2geoc(lon0, lat0, h0, a, f)
    return (X0, Y0, Z0, a, f)


# Area no SGL
def AreaPerimetroParteSGL(coordsXYZ, crsGeo):
    lon,lat,alt = [],[],[]
    for pnt in coordsXYZ[:-1]:
        lon +=[pnt.x()]
        lat +=[pnt.y()]
        if str(pnt.z()) != 'nan':
            alt += [pnt.z()]
        else:
            alt += [0]
    lon0 = np.array(lon).mean()
    lat0 = np.array(lat).mean()
    h0 = np.array(alt).mean()
    Xo, Yo, Zo, a, f = OrigemSGL(lon0, lat0, h0, crsGeo)
    # CONVERSÃO DAS COORDENADAS
    coordsSGL = []
    for coord in coordsXYZ:
        lon = coord.x()
        lat = coord.y()
        h = coord.z() if str(coord.z()) != 'nan' else 0
        X, Y, Z = geod2geoc(lon, lat, h, a, f)
        E, N, U = geoc2enu(X, Y, Z, lon0, lat0, Xo, Yo, Zo)
        coordsSGL += [QgsPointXY(E, N)]
    return (abs(areaGauss(coordsSGL)), Distancia(coordsSGL, '2D'))


def areaSGL(geomGeo, crsGeo):
    if geomGeo.isMultipart():
        coordsXYZ = geom2PointList(geomGeo)
        area_final = 0
        for coordsGeo in coordsXYZ:
            area_final += AreaPerimetroParteSGL(coordsGeo[0], crsGeo)[0]
            n_aneis = len(coordsGeo)
            if n_aneis > 1:
                for w in range(1, n_aneis):
                    area_final -= AreaPerimetroParteSGL(coordsGeo[w], crsGeo)[0]
    else:
        coordsGeo = geom2PointList(geomGeo)
        area_final = AreaPerimetroParteSGL(coordsGeo[0], crsGeo)[0]
        n_aneis = len(coordsGeo)
        if n_aneis > 1:
            for w in range(1, n_aneis):
                area_final -= AreaPerimetroParteSGL(coordsGeo[w], crsGeo)[0]
    print(area_final)
    return area_final


def perimetroSGL(geomGeo, crsGeo):
    if geomGeo.isMultipart():
        coordsXYZ = geom2PointList(geomGeo)
        perimetroSGL = 0
        for coordsGeo in coordsXYZ:
            perimetroSGL += AreaPerimetroParteSGL(coordsGeo[0], crsGeo)[1]
    else:
        coordsGeo = geom2PointList(geomGeo)
        perimetroSGL = AreaPerimetroParteSGL(coordsGeo[0], crsGeo)[1]
    return float(perimetroSGL)


# Azimute de Puissant
def AzimutePuissant(lat1, lon1, lat2, lon2, a = 6378137, f = 1/298.257222101):
    """
    Calcula o azimute segundo Puissant entre dois pontos geodésicos.

    Parâmetros:
    lat1, lon1: Latitude e longitude do ponto inicial em graus.
    lat2, lon2: Latitude e longitude do ponto final em graus.
    a: Semi-eixo maior do elipsoide (padrão: 6378137 metros).
    f: Achatamento do elipsoide (padrão: 1/298.257222101).

    Retorna:
    Azimute em graus.
    """
    e2 = 2*f - f**2 # Calcula a excentricidade quadrada (e^2) a partir do achatamento (f)
    seno_1segundo = math.sin(math.radians(1/3600))

    lat_media = (math.radians(lat1) + math.radians(lat2)) / 2
    seno_lat_media = math.sin(lat_media)
    cos_lat_media = math.cos(lat_media)
    pow_seno_20 = math.pow(seno_lat_media, 2)
    Nm = a / (math.pow(1 - (e2 * pow_seno_20), 0.5))
    delta_lat = (lat2 - lat1) * 3600
    delta_lon = (lon2 - lon1) * 3600

    Mm = (a * (1 - e2)) / math.pow(1 - (e2 * pow_seno_20), 1.5)
    Bm = 1 / (Mm * seno_1segundo)

    x = delta_lon * cos_lat_media * Nm * seno_1segundo
    y = delta_lat * math.cos(math.radians(delta_lon / 7200))/Bm

    F = (1 / 12) * seno_lat_media * cos_lat_media * cos_lat_media * seno_1segundo * seno_1segundo
    gamma = (delta_lon * seno_lat_media * (1 / math.cos(math.radians(delta_lat / 7200))) + (F * delta_lon * delta_lon * delta_lon))
    Azimute = math.degrees(math.atan2(x, y)) - (gamma / 7200)
    return (Azimute + 360)%360


def dd2dms(dd, n_digits):
    if dd != 0:
        graus = int(floor(abs(dd)))
        resto1 = round(abs(dd) - graus, 10)
        minutos = 60*resto1
        if n_digits >= 0:
            minutos = int(floor(minutos))
            resto2 = round(resto1*60 - minutos, 10)
            segundos = resto2*60
            if round(segundos,n_digits) == 60:
                minutos += 1
                segundos = 0
            if minutos == 60:
                graus += 1
                minutos = 0
        else:
            mindec = -1*(n_digits+1)
            if round(minutos,mindec) == 60:
                graus += 1
                minutos = 0
        if dd < 0:
            texto = '-' + str(graus) + '°'
        else:
            texto = str(graus) + '°'

        if n_digits < -1: # graus e minutos decimais
            texto = texto + ('{:0' + str(3+mindec) + '.' + str(mindec) + 'f}').format(minutos) + "'"
        elif n_digits == -1: # graus e minutos inteiros
            texto = texto + '{:02d}'.format(round(minutos)) + "'"
        else: # graus, minutos e segundos
            texto = texto + '{:02d}'.format(minutos) + "'"

        if n_digits == 0: # segundos inteiros
            texto = texto + '{:02d}'.format(round(segundos)) + '"'
        elif n_digits > 0: # segundos decimais
            texto = texto + ('{:0' + str(3+n_digits) + '.' + str(n_digits) + 'f}').format(segundos) + '"'
        return texto
    else:
        if n_digits > 0:
            return "0°00'" + ('{:0' + str(3+n_digits) + '.' + str(n_digits) + 'f}').format(0) + '"'
        elif n_digits == 0:
            return "0°00'" + '"'
        elif n_digits == -1:
            return "0°00'"
        else:
            mindec = -1*(n_digits+1)
            return "0°" + ('{:0' + str(3+mindec) + '.' + str(mindec) + 'f}').format(0) + "'"


def str2HTML(texto):
    if texto:
        dicHTML = {'Á': '&Aacute;',	'á': '&aacute;',	'Â': '&Acirc;',	'â': '&acirc;',	'À': '&Agrave;',	'à': '&agrave;',	'Å': '&Aring;',	'å': '&aring;',	'Ã': '&Atilde;',	'ã': '&atilde;',	'Ä': '&Auml;',	'ä': '&auml;', 'ú': '&uacute;', 'Ú': '&Uacute;', 'Æ': '&AElig;',	'æ': '&aelig;',	'É': '&Eacute;',	'é': '&eacute;',	'Ê': '&Ecirc;',	'ê': '&ecirc;',	'È': '&Egrave;',	'è': '&egrave;',	'Ë': '&Euml;',	'ë': '&Euml;',	'Ð': '&ETH;',	'ð': '&eth;',	'Í': '&Iacute;',	'í': '&iacute;',	'Î': '&Icirc;',	'î': '&icirc;',	'Ì': '&Igrave;',	'ì': '&igrave;',	'Ï': '&Iuml;',	'ï': '&iuml;',	'Ó': '&Oacute;',	'ó': '&oacute;',	'Ô': '&Ocirc;',	'ô': '&ocirc;',	'Ò': '&Ograve;', 'Õ': '&Otilde;', 'õ': '&otilde;',	'ò': '&ograve;',	'Ø': '&Oslash;',	'ø': '&oslash;',	'Ù': '&Ugrave;',	'ù': '&ugrave;',	'Ü': '&Uuml;',	'ü': '&uuml;',	'Ç': '&Ccedil;',	'ç': '&ccedil;',	'Ñ': '&Ntilde;',	'ñ': '&ntilde;',	'Ý': '&Yacute;',	'ý': '&yacute;',	'"': '&quot;', '”': '&quot;',	'<': '&lt;',	'>': '&gt;',	'®': '&reg;',	'©': '&copy;',	'\'': '&apos;', 'ª': '&ordf;', 'º': '&ordm;', '°':'&deg;', '²':'&sup2;', '¿':'&iquest;', '¡':'&iexcl;', '–': '&ndash;'}
        for item in dicHTML:
            if item in texto:
                texto = texto.replace(item, dicHTML[item])
        return texto
    else:
        return ''
    

def LerPDF(pdf_path, feedback = None):
    
    # Detectando o sistema operacional e instalando PyPDF2
    system_os = platform.system()
    if system_os == "Linux":
        import subprocess
        import sys
        try:
            from PyPDF2 import PdfReader
        except:
            feedback.pushInfo('PyPDF2 não está instalado. Tentando instalar "PyPDF2" utilizando "pip"...')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"],
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL)
                from PyPDF2 import PdfReader
            except subprocess.CalledProcessError as e:
                feedback.reportError(f"Erro ao instalar o pacote pacote PyPDF2. Você pode tentar instalar manualmente via OSGeo4W Shell:\n"
                            f"python3 -m pip install PyPDF2")
                raise QgsProcessingException(f"Falha ao instalar o pacote PyPDF2: {e}")
    else: # "Windows","Darwin" (MacOS)
        import pip
        try:
            from PyPDF2 import PdfReader
        except ImportError:
            feedback.pushInfo('PyPDF2 não está instalado. Tentando instalar "PyPDF2" utilizando "pip"...')
            try:
                # Executa o pip usando subprocess
                pip.main(["install","PyPDF2"])
                from PyPDF2 import PdfReader
            except Exception as e:
                feedback.reportError(f"Erro ao instalar o pacote pacote PyPDF2. Você pode tentar instalar manualmente via OSGeo4W Shell:\n"
                            f"pip install PyPDF2")
                raise QgsProcessingException(f"Falha ao instalar o pacote PyPDF2: {e}")
    feedback.pushInfo('Biblioteca PyPDF2 importada com sucesso...')

    # Lendo arquivo PDF
    reader = PdfReader(pdf_path)
    text = ''
    # Iterar por cada página do PDF
    for page_num, page in enumerate(reader.pages):
        text += page.extract_text()

    dic = {
    'Denominação:': '',
    'Proprietário:': '',
    'Proprietário(a):': '',
    'Matrícula do imóvel:': '',
    'Transcrição do imóvel:': '',
    'Natureza da Área:': '',
    'CPF:': '',
    'CNJP:': '',
    'Município/UF:': '',
    'Código INCRA/SNCR:': '',
    'Responsável Técnico:': '',
    'Responsável Técnico(a):': '',
    'Formação:': '',
    'Conselho Profissional:': '',
    'Código de credenciamento:': '',
    'Documento de RT:': '',
    'Cartório (CNS):': '',
    'Área (Sistema Geodésico Local)': '',
    'Perímetro (m)': '',
    'Data Certificação:': '',
    'Data da Geração:' : '',
    }

    lista_cod = []
    dic_cod = {}
    ind_encravado = []

    # Dividir o texto em linhas
    lines = text.splitlines()
    sentinela = False
    sentinela2 = False
    cont = 0
    pattern = r'\s*[A-Z0-9]{3,4}-[PMOV]-[A-Z0-9]{1,6}(?:,\s*[A-Z0-9]{3,4}-[PMOV]-[A-Z0-9]{1,6})*'

    for line in lines:
        
        if sentinela:
            dic[item] = line
            sentinela = False

        for item in dic:
            if item in line:
                sentinela = True
                break

        if cont == 8:
            cont = 0
            sentinela2 = False

        if bool(re.fullmatch(pattern, line)):
            if cont == 0:
                codigo = line.strip()
                lista_cod.append(codigo)
                sentinela2 = True

        if 'Área encravada' in line:
            ind_encravado.append(len(lista_cod))

        elif sentinela2:
            cont += 1
            if cont == 1:
                dic_cod[lista_cod[-1]] = {'lon':'', 'lat':'', 'h':'', 'cns':'', 'matr':'', 'confr': '', 'az': '', 'dist': '', 'texto_confr': '', 'vante': ''}
            if cont == 2:
                dic_cod[lista_cod[-1]]['lon'] = line.strip()
            if cont == 3:
                dic_cod[lista_cod[-1]]['lat'] = line.strip()
            if cont == 4:
                dic_cod[lista_cod[-1]]['h'] = line.strip()
            if cont == 5:
                dic_cod[lista_cod[-1]]['vante'] = line.strip()
            if cont == 6:
                dic_cod[lista_cod[-1]]['az'] = line.strip()
            if cont == 7:
                dic_cod[lista_cod[-1]]['dist'] = line.strip()
            if cont == 8:
                try:
                    cns,mat,confr = line.strip().split('|')
                    cns = cns.split(':')[-1].strip()
                    matr = mat.strip().split()
                    if len(matr) == 2:
                        matr = matr[-1]
                    else:
                        matr = " ".join(matr[1:])
                    confr = confr.strip()
                    dic_cod[lista_cod[-1]]['cns'] = cns
                    dic_cod[lista_cod[-1]]['matr'] = matr
                    dic_cod[lista_cod[-1]]['confr'] = confr
                    dic_cod[lista_cod[-1]]['texto_confr'] = line
                except:
                    dic_cod[lista_cod[-1]]['confr'] = line.strip()
                    dic_cod[lista_cod[-1]]['texto_confr'] = line
    
    return dic, lista_cod, dic_cod, ind_encravado