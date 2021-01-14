import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame

#ABRE EXCEL Y USA DETERMINADAS COLUMNAS Y ME ASEGURO QUE LOS CAMPOS CLAVES SEAN STR
df_consolidado = pd.read_excel('CONSOLIDADO VIDA DIGNA.xlsx', usecols=['CUIL','DNI','APELLIDO', 'NOMBRE','SEGUNDA', 'DEPARTAMENTO'], converters={'CUIL':str})
df_noCoincide = pd.read_excel('Vida digna sin identificar..xlsx', converters={'CUIT':str})
df_providenicas = pd.read_excel('PROVIDENCIAS GABI.xlsx', usecols=['FECHA','CUIL','APELLIDO y NOMBRES','Localidad','Resolución Beneficiario'], converters={'CUIL':str})


#CAMBIO NOMBRE DE COLUMNA CLAVE
df_noCoincide = df_noCoincide.rename(columns={'CUIT':'CUIL'})
df_providenicas['CUIL'] = df_providenicas['CUIL'].replace(['-'],'')

#REALIZO 2 CRUCES CRUCE LEFT JOIN
#df = df_noCoincide.merge(df_consolidado, how="left")
#df_2 = df.merge(df_providenicas, how="left")

#df_3 = df.merge(df_providenicas, how="right")

df_4 = df_providenicas.merge(df_consolidado, how="left")

#GRABO EXCEL
#df_2.to_excel('cruce_con_consolidado_providencias.xlsx')
#df_3.to_excel('cruce_alreve.xlsx')
df_4.to_excel('cruce_providencia_consolidado.xlsx')