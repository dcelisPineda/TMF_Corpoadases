import psycopg2
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt  
try:
   connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="DWH")
   cursor = connection.cursor()
   postgreSQL_select_Query ="""
    SELECT f.id id_tip_fam,f.tip_familiar , CASE 
    WHEN c.rein_delito ='SI' THEN 1
    ELSE 0 END rein_delito
    FROM public.fact_corp c inner join public.dim_tip_familiar f  
    ON c.tip_familiar=f.tip_familiar 
"""
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()   
   df = pd.DataFrame(mobile_records,columns=["id_tip_fam","tip_familiar", "rein_delito"])
   x=df['id_tip_fam']
   y=df['rein_delito']
   c =np.corrcoef(x,y)
   print("las variables se relacionan" , c)
except (Exception, psycopg2.Error) as error :
    print ("Error Cargando Informacion", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL conexion cerrada")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion7.csv', sep=',')
print("Archivo Generado")


