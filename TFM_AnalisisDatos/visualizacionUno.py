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
   postgreSQL_select_Query =   """
   SELECT initcap(delito), count(1) cantidad,SUBSTR(edad,1,2) edad 
   FROM public.fact_corp GROUP BY delito,Edad 
  """
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()   
   df = pd.DataFrame(mobile_records,columns=['DELITO', "CANTDAD","EDAD"])
except (Exception, psycopg2.Error) as error :
    print ("Error Cargando Informacion", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL conexion cerrada")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion1.csv', sep=',')
print("Archivo Generado")