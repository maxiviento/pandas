import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame


#\\d035nt01\Grupos\ADMINISTRACION\SECTORIAL TESORERIA\DATOS MAXI PROGRAMAS\ARCHIVOS DE BD\cbu_declarados.csv

#CARGA BENEF DE GOOGLE DRIVE
key = '1CG-8PqNwHZsuDItqwt2lj1Rwvm18TN4N'
hoja = 'Sheet'
url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(key,hoja)
df_benef = pd.read_csv(url, usecols=['CUIT', 'APELLIDOS', 'NOMBRES'], na_values= ['null'])
df_benef = df_benef[df_benef['CUIT'].notnull()]

print(df_benef)

df_cbu = pd.read_csv(r'D:\01 - Ministerio de Empleo\vida digna\cbu_declarados.csv')
df_cbu = df_cbu[df_cbu['CUIT'].notnull()]

df_cbu_posible = pd.read_excel(r'D:\01 - Ministerio de Empleo\vida digna\PAGO FIN DE AÑO\VIDA DIGNA Salidas Capital-interior.xlsx', "CBU_PESOS", index_col=None, na_values=["NA"], usecols =['CUIT','PRODUCTO','EST_ACT','Nro_CBU'])
df_cbu_posible = df_cbu_posible[df_cbu_posible['PRODUCTO'].notnull()]

df = df_benef.merge(df_cbu, how="left")

resultado = df.merge(df_cbu_posible, how="left")

resultado.to_excel("SEGUIMIENTO CBU VD.xlsx") 




