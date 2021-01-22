import sqlite3

class Base(object):
    def __init__(self):
        self.conn = sqlite3.connect('D:/dPython/pdf_to_excel/padron2019.db')
        self.c = self.conn.cursor()
        #self.c.execute('''CREATE TABLE padron
        #              (circuito text, dni text, sexo text, nombre VARCHAR(60), direccion VARCHAR(60), tipo VARCHAR(10))''')
        #self.conn.commit()
        #self.conn.close()

padron = Base()

f = open (r'D:\07-tribuna\01-DATASETS2019\escrutiño2019\NACIONALES 2019\interior2019-2b.txt','r', encoding="utf8")
r = open(r"D:\07-tribuna\01-DATASETS2019\escrutiño2019\NACIONALES 2019\interior2019-2b_resultado.txt","w") 
mensaje = f.read().splitlines()
f.close()
for i, linea in enumerate(mensaje, start=0):
    linea = linea.replace("'","")
    c = linea.find("CIRCUITO:")
    if c != -1:
        circuito = linea[c:c+30]
        circuito = circuito.split()
        pass
    N = linea.find("NRO. ORDEN")
    if N != -1 and len(linea)>20:
        nombres = linea.split("NRO. ORDEN")
        coma = nombres[1].count(",")
        if coma > 1:
            nombres2 = nombres[1].split("  ")
            nombres = [nom for nom in nombres2 if nom.find(",")!=-1]
            #print(nombres)
            pass
        if mensaje[i+1].find("NRO. ORDEN")==-1:
            direcciones = mensaje[i+1].split("  ")
        else:
            direcciones = mensaje[i+2].split("  ")
        dnis_clase = mensaje[i+3].split()
        if dnis_clase[0]!="DOC.":
            dnis_clase = mensaje[i+4].split()
        n = [nom.replace("  ","") for nom in nombres]
        d = [dir for dir in direcciones if len(dir)>1]
        dni = [doc for doc in dnis_clase if doc.find(".")!=-1]
        dni = [doc.replace(".","") for doc in dni]
        clase = [a for a in dnis_clase if a.isdigit() == True and len(a)==4]
        if len(n)<3:
            if len(dni) == 4:
                l1 = [circuito[1],dni[1],clase[0],n[0],d[0],dni[0]]
                try:
                    l2 = [circuito[1],dni[3],clase[1], n[1],d[1],dni[2]]
                except Exception as e:
                    l2 = "linea {} error {} | ".format(str(i), str(e))
                    r.writelines(str(l2)+"\n")
            else:
                try:
                    l1 = [circuito[1],dni[1],clase[0],n[1],d[0],dni[0]]
                except Exception as e:
                    l1 = "linea {} error {} | ".format(str(i), str(e))
                    r.writelines(str(l1)+"\n")
        else:
            try:
                l1 = [circuito[1],dni[1],clase[0],n[1],d[0],dni[0]]
            except Exception as e:
                l1 = "linea {} error {} |".format(str(i), str(e))
                r.writelines(str(l1)+"\n")
            try:
                l2 = [circuito[1],dni[3],clase[1],n[2],d[1],dni[2]]
            except Exception as e:
                l2 = "linea {} error {} |".format(str(i), str(e))
                r.writelines(str(l2)+"\n")
        try:
            sql = "INSERT INTO padron2019 VALUES ('{}','{}','{}','{}','{}','{}');".format(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5])
            padron.c = padron.conn.cursor()
            padron.c.execute(sql)
        except Exception as e: 
            print(str(e)+ "linea " + str(i))
        
        try:
            sql = "INSERT INTO padron2019 VALUES ('{}','{}','{}','{}','{}','{}');".format(l2[0],l2[1],l2[2],l2[3],l2[4],l2[5])
            padron.c = padron.conn.cursor()
            padron.c.execute(sql)
        except Exception as e: 
            print(str(e) + "linea " + str(i))
padron.conn.commit()
padron.c.close()
r.close()