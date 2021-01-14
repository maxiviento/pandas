import pandas as pd
from pandas import DataFrame
from datetime import datetime
import time

programa = "Vida Digna"
hoy = str(datetime.now().date())

key = '1ki6jAFYcOkS3OGp4fWotqouVOJQki6AwlL7rin4xBXk'
hoja = 'Sheet'
url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(key,hoja)
df_respuestas = pd.read_csv(url, usecols =['Quien','Dni','Contacto','Mensajes','Apellido, Nombres','Atajo','Respuesta frecuente'])

#df_respuestas = pd.read_excel(r'D:\DESARROLLO\PANDAS_CRUCES\PARSEO VIDA DIGNA 11-1-21.xlsx')
df_respuestas = df_respuestas[df_respuestas['Atajo'].notnull() | df_respuestas['Atajo'] !='YA RESUELTA']

print(df_respuestas['Atajo'].value_counts())

df_respuestas['adjunto'] = ""
df_respuestas['estado'] = ""
df_respuestas['Marca temporal'] = df_respuestas.index + 2
df_respuestas['id'] = ""
df_respuestas['ORIGEN'] = 'Celu 6 (VIDA DIGNA)'
df_respuestas['PROGRAMA'] = programa

print(df_respuestas.columns)

df_rb = df_respuestas.loc[:,['estado','Contacto','Apellido, Nombres','Respuesta frecuente','adjunto', 'Dni']]
df_rb.to_excel("RB" + programa + hoy + ".xlsx", index = False) 



#Marca temporal	ID GESTIÓN	ORIGEN DE LA COMUNICACIÓN	PROGRAMA	FECHA DE CONSULTA	CELU BENEFICIARIO	DNI O CUIL BENEFICIARIO	NOMBRE Y APELLIDO	CONSULTA	¿QUIEN ATENDIÓ LA CONSULTA?	ATAJO RF	RESPUESTA FRECUENTE	RESPUESTA PARTICULAR	ESTADO DE LA GESTIÓN	ENLACE DIRECTO A RESPUESTA

#Estado	Contacto	Nombre	Mensaje	Adjunto	ID-DNI





