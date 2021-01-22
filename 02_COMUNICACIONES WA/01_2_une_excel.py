import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame

carpeta =r'C:\Users\Administrador\Documents\lecturas_chats_yudi'

#esto lo uso para unir los parseo cortados (pero luego lo laburo en excel, por ahora)
df_l1 = pd.read_excel(carpeta + r'\_mensajes_2021-01-19080034.xlsx')

df_l2 = pd.read_excel(carpeta + r'\_mensajes_2021-01-18220652.xlsx')




df_unidos = [df_l1,df_l2]

df_resultado = pd.concat(df_unidos)

df_resultado.to_excel('parseo_unidos_19.xlsx')

