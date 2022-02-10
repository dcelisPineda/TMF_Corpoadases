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
  SELECT delito, esco_apro, esco_act,
  case 
    when  esco_apro = esco_act THEN 'No'
 ELSE 'Si'
  end continuidadEscolar,
  ocupacion
  FROM public.fact_corp f 
  """ 
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()    
   df = pd.DataFrame(mobile_records,columns=['delito', 'esco_apro','esco_act','continuidadEscolar','ocupacion'])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion6.csv', sep=',')
print("Archivo Generado")