import sqlite3

class Base(object):
    def __init__(self):
        self.conn = sqlite3.connect('D:/desarrollo/pdf_to_excel/pagos_benef.db')
        self.c = self.conn.cursor()
        #self.c.execute('''CREATE TABLE T_OP_SUAF
        #              (mep text, op text, razon_social text, cuit VARCHAR(11), sucursal number(3), cuenta VARCHAR(22), nombre_cuenta text, monto text, programa text)''')
        #self.conn.commit()
        #self.conn.close()

CARPETA = r'R:\ADMINISTRACION\SECTORIAL TESORERIA\DATOS MAXI PROGRAMAS\ARCHIVOS PDF VIDA DIGNA'
programa = 'VIDA DIGNA'
PAGOS_BENEF = Base()



f = open (CARPETA + r'\PRC_PLANILLAS_VIDA DIGNA PAGO 25 11.txt','r', encoding="utf8")
mensaje = f.read().splitlines()
f.close()
for i, linea in enumerate(mensaje, start=0):
    linea = linea.replace("'","")
    c = linea.find("O.P.")
    if c != -1:
        row = linea.split('   ')
        pass
        reg = [r.replace("  ","") for r in row if r != ""]
        pass
        sql = "INSERT INTO T_OP_SUAF VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(*reg, programa)
        PAGOS_BENEF.c = PAGOS_BENEF.conn.cursor()
        PAGOS_BENEF.c.execute(sql)
PAGOS_BENEF.conn.commit()