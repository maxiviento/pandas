import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame

carpeta =r'C:\Users\Administrador\Documents\lecturas_chats_yudi'

#esto lo uso para unir los parseo cortados (pero luego lo laburo en excel, por ahora)
df_l1 = pd.read_excel(carpeta + r'\_mensajes_2021-01-13154843.xlsx')

df_l2 = pd.read_excel(carpeta + r'\_mensajes_2021-01-13194036.xlsx')

df_l3 = pd.read_excel(carpeta + r'\_mensajes_2021-01-13213858.xlsx')

df_l4 = pd.read_excel(carpeta + r'\_mensajes_2021-01-13221545.xlsx')



df_unidos = [df_l1,df_l2,df_l3,df_l4]

df_resultado = pd.concat(df_unidos)
df_resultado['Númerofill'] = df_resultado['Número'].fillna(method = 'ffill')

df_resultado.to_excel('parseo_unidos_14.xlsx')

