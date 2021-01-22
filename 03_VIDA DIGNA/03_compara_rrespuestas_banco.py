import glob
import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame
import os
from datetime import datetime
import time
import cx_Oracle

hoy = str(datetime.now().date())
#CONULSTA EN BASE DE DATOS DE PERSONAS QUE ASOCIACION CBU

dsn = cx_Oracle.makedsn("cba1.gobiernocba.gov.ar", "1521", "cba1")
with cx_Oracle.connect(user = "d23445362", password = "d23445362", dsn=dsn) as connection:
	sql = """SELECT * from suaf.VT_CBU_DECLARADOS where CUIT is not null"""
	df_cbu = pd.read_sql(sql, con=connection)
    #cursor = connection.cursor()

#CARGO ARCHIVO DE RESPUESTAS DEL BANCO
lista_data = []
archivos_banco = glob.glob(r"R:\ADMINISTRACION\SECTORIAL TESORERIA\DATOS MAXI PROGRAMAS\ARCHIVOS PDF VIDA DIGNA\.hab VIDA DIGNA\*.hab")
for filename in archivos_banco:
	df_archivos_banco = pd.read_fwf(filename, widths = [3,5,2,1,9,18,8,5,6,22,2,22,43], header=None)
	df_archivos_banco = df_archivos_banco.loc[:,[6,9,11,12]]
	df_archivos_banco.columns = ['FECHA','CBU_pag','CUIT','RESPUESTA BANCO']
	lista_data.append(df_archivos_banco)
df_respuesta_banco = pd.concat(lista_data, ignore_index=True)
df_respuesta_banco['CUIT'] = df_respuesta_banco['CUIT'].str.slice(start = - 11)




