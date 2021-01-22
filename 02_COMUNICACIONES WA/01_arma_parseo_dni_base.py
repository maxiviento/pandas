import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame


df_consultas = pd.read_excel(r'C:\Users\Administrador\Documents\lecturas_chats_yudi\_mensajes_2021-01-21091124.xlsx', converters={'Dni':str})
#df_benef = pd.read_excel(r'LISTADO SEGUNDAS CUOTAS CAPITAL e INTERIOR.xlsx', usecols =['Dni','NOMBRES','APELLIDOS','REPORTE DE LLAMADO'], converters={'Dni':str})


#CARGA BENEF DE GOOGLE DRIVE
key = '1HODwblDChV6NNKvrAp2j7Bj4u37id8p7l_a9IB9GavQ'
hoja = 'Sheet'
url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(key,hoja)
df_benef = pd.read_csv(url, usecols =['Dni','NOMBRES','APELLIDOS','REPORTE DE LLAMADO'], converters={'Dni':str})

#df_benef = df_benef.rename(columns={'NRO_DOCUMENTO':'Dni'})
#df_benef = df_benef['REPORTE DE LLAMADO'].fillna("SIN ESTADO")


#CRUZO LAS CONSULTAS DEL WA CON LA BASE DE BENEFICIARIOS
df = df_consultas.merge(df_benef, how="left")

#CONCATENO APELLIDO Y NOMBRE
df['Apellido, Nombres'] = df['APELLIDOS'] + ', ' + df['NOMBRES']
df['Quien'] = ""
df['Númerofill'] = df['Número'].fillna(method = 'ffill')

#ARMO LAS COLUMNA QUE DESEO A LA SALIDA
df = df.loc[:,['Quien','Númerofill', 'Número','Fecha, hora','Contacto','Mensajes','Dni', 'Apellido, Nombres', 'REPORTE DE LLAMADO']]

#FILTRO LOS PRIORITARIOS. SON LOS QUE SE HALLARON EN LA CONSULTA ANTERIOR
df_prioritarios = df[df['Apellido, Nombres'].notnull()]
#SOLO ME INTERESA 1 COLUMNA, QUE ES LA DEL CONTACTO
df_prioritarios = df_prioritarios.loc[:,['Númerofill']]
#QUITO DUPLICADOS PARA QUE QUEDEN NUMEROS UNICOS
df_prioritarios = df_prioritarios.drop_duplicates(subset='Númerofill', keep='last')
#A LA COLUMNA LE AGREGO EL ESTADO DE PRIORITARIOS
df_prioritarios['estado'] = 'prioritarios'
#CRUZO DE NUEVO EL DF_FINAL PARA OBETNER EL ESTADO EN CADA LINEA DONDE APAREZCA EL NUMERO
df_final = df.merge(df_prioritarios, how="left")

#Filtro PRIORITARIOS por un lado y no PRIORITARIOS por otro, DEL DF_FINAL
df_prioritarios_FINAL = df_final[df_final['estado'] == 'prioritarios']
df_noEnBase = df_final[df_final['estado'] != 'prioritarios']


df_prioritarios_FINAL.to_excel("parseo_21_prioritarios.xlsx", index=False)
df_noEnBase.to_excel("parseo_21_noEnBase.xlsx", index=False)