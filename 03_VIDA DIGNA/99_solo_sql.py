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

df_cbu.to_excel("PRUEBA" + hoy + ".xlsx", index = False)




