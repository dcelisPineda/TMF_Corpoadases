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
   postgreSQL_select_Query = """
    SELECT c.id id_Consumo, 
      f.niv_consu,
    CASE 
      WHEN f.rein_delito ='SI' THEN 1
      ELSE 0 END rein_delito
      FROM public.fact_corp f
      inner join public.dim_niv_consumo c
      on f.niv_consu=c.nivel_consumo   
  """ 
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()    
   df = pd.DataFrame(mobile_records,columns=['id_Consumo', 'niv_consu','rein_delito'])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion8.csv', sep=',')
print("Archivo Generado")