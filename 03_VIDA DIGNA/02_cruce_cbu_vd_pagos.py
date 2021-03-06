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
print(df_respuesta_banco)

archivo_cbu_posibles = r"D:\01 - Ministerio de Empleo\vida digna\PAGO FIN DE AÑO\VIDA DIGNA Salidas Capital-interior.xlsx"
archivo_total = r'D:\01 - Ministerio de Empleo\vida digna\SEGUNDAS CUOTAS A PAGAR VIDA DIGNA TOTAL.xlsx'


df_benef = pd.read_excel(archivo_total, usecols=['APELLIDOS', 'NOMBRES', 'CUIT'], na_values= ['null'], converters={'CUIT':str})
df_benef = df_benef[df_benef['CUIT'].notnull()]


#CARGA EL ARCHIVO CON DATOS DE CBU
df_cbu_posible = pd.read_excel(archivo_cbu_posibles, "CBU_PESOS", index_col=None, na_values=["NA"], usecols =['CUIT','PRODUCTO','EST_ACT','Nro_CBU'], converters={'CUIT':str})
df_cbu_posible = df_cbu_posible[df_cbu_posible['PRODUCTO'].notnull()]

df = df_benef.merge(df_cbu, how="left")
df_benef_cbu_posibles = df.merge(df_cbu_posible, how="left")


resultado = df_benef_cbu_posibles.merge(df_respuesta_banco, how="left")
resultado.to_excel("VIDA_DIGNA-CBU" + hoy + ".xlsx", index = False)




