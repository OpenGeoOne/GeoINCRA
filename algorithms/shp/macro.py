#https://github.com/rafaelhlima/LibOCon_2021_SFCalc/blob/main
#https://help.libreoffice.org/latest/en-US/text/sbasic/shared/03/sf_document.html
from scriptforge import CreateScriptService

def create_table(args=None):
	doc = CreateScriptService("Calc")

	doc.activate("identificacao")
	doc.setValue("B2", "Natureza do serviço")
	doc.setValue("B5", "Tipo de pessoa")
	doc.setValue("B6", "Nome")
	#doc.setValue("B7", "CPF")
	doc.setValue("B10", "Denominação") # denominação
	doc.setValue("B11", "Situação")
	doc.setValue("B12", "Natureza da area") # natureza da área
	doc.setValue("B13", "Codigo do Imovel") # código do imóvel
	doc.setValue("B14", "Codigo do cartorio") # código cartório
	doc.setValue("B15", "Matricula") # matrícula
	doc.setValue("B17", "Municipio")

#copy_sheet
	
	doc.activate("perimetro_1")
#table_1

#activate_sheet


	NewURL = ("output_path")

	doc.SaveCopyAs(NewURL, overwrite = True)
	doc.CloseDocument(False)
	
