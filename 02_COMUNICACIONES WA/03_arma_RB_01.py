import pandas as pd
from pandas import DataFrame
from datetime import datetime
import time

programa = "Vida Digna"
hoy = str(datetime.now().date())

key = '1KpXu1rtMftOgpV4h37pUCMgu5rRrwz0IKKUpjK5wPcc'
hoja = 'Sheet1'
url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(key,hoja)
#df_respuestas = pd.read_csv(url, usecols =['Quien','Dni','Contacto','Mensajes','Apellido, Nombres','Atajo','Respuesta Frecuente'])


df_respuestas = pd.read_excel(r'C:\Users\Administrador\Desktop\VIDA_DIGNA_parseo_15_prioritarios.xlsx')
print(df_respuestas)

df_respuestas = df_respuestas[df_respuestas['Atajo'].notnull()]

print(df_respuestas['Atajo'].value_counts())

df_respuestas['adjunto'] = ""
df_respuestas['estado'] = ""
df_respuestas['Marca temporal'] = df_respuestas.index + 2
df_respuestas['id'] = ""
df_respuestas['ORIGEN'] = 'Celu 6 (VIDA DIGNA)'
df_respuestas['PROGRAMA'] = programa

print(df_respuestas.columns)

df_rb = df_respuestas.loc[:,['estado','Contacto','Apellido, Nombres','Respuesta Frecuente','adjunto', 'Dni']]
df_rb.to_excel("RB" + programa + hoy + ".xlsx", index = False) 



#Marca temporal	ID GESTIÓN	ORIGEN DE LA COMUNICACIÓN	PROGRAMA	FECHA DE CONSULTA	CELU BENEFICIARIO	DNI O CUIL BENEFICIARIO	NOMBRE Y APELLIDO	CONSULTA	¿QUIEN ATENDIÓ LA CONSULTA?	ATAJO RF	RESPUESTA FRECUENTE	RESPUESTA PARTICULAR	ESTADO DE LA GESTIÓN	ENLACE DIRECTO A RESPUESTA

#Estado	Contacto	Nombre	Mensaje	Adjunto	ID-DNI





