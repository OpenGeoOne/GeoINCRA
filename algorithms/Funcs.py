# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GeoINCRA - Functions
                                 A QGIS plugin
        begin                : 2026-01-06
        copyright            : (C) 2026 by Tiago Prudencio and Leandro França
        email                : contato@geoone.com.br
***************************************************************************/
"""

__author__ = 'Tiago Prudencio and Leandro França'
__date__ = '2026-01-06'
__copyright__ = '(C) 2026 by Tiago Prudencio and Leandro França'

from qgis.core import *
from qgis.PyQt.QtCore import QVariant
import platform


def ImportarPyPDF(feedback=None):
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
    return True


def LerPDF(pdf_path, feedback = None):
    ok = ImportarPyPDF(feedback)
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

    chaves = list(dic.keys())

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
                dic_cod[lista_cod[-1]] = {'lon':'', 'lat':'', 'h':'', 'cns':'', 'matr':'', 'confr': '', 'az': '', 'dist': '', 'texto_confr': ''}
            if cont == 2:
                dic_cod[lista_cod[-1]]['lon'] = line.strip()
            if cont == 3:
                dic_cod[lista_cod[-1]]['lat'] = line.strip()
            if cont == 4:
                dic_cod[lista_cod[-1]]['h'] = line.strip()
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
    
    return dic, lista_cod, dic_cod