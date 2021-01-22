
import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame
import os

archivo_banco = r"D:\01 - Ministerio de Empleo\banco de la gente\bbdd\TODOS_RESPUETAS_BANCO.txt"


#CARGO ARCHIVO DE RESPUESTAS DEL BANCO
df_archivo_banco = pd.read_fwf(archivo_banco, widths = [3,5,2,1,9,18,8,5,6,22,2,22,43], header=None)
df_archivo_banco = df_archivo_banco.loc[:,[5,6,9,11,12]]
df_archivo_banco.columns = ['MONTO','FECHA','CBU_pag','CUIT','RESPUESTA BANCO']
df_archivo_banco['CUIT'] = df_archivo_banco['CUIT'].str.slice(start = - 11)

df_archivo_banco.to_excel('pagados banco de la gente.xlsx')
