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
    SELECT n.id Consumo,
    case  n.tratamiento
    WHEN  'Participacion grupos Apoyo'    THEN  2  
    WHEN  'Seguimiento con psicologia'    THEN  3 
    WHEN  'Participacion actividades Prevencion' THEN  1
    WHEN  'Tratamiento ambulatorio'    THEN  4
    WHEN  'Tratamiento intramural'     THEN  5
    ELSE 3
    end tratamiento,
    cast((SUBSTR(edad,1,2)) as int) edad
    FROM public.fact_corp F
    inner join public.dim_niv_consumo n
    ON f.niv_consu=n.nivel_consumo  
  """ 
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()    
   df = pd.DataFrame(mobile_records,columns=[ "niv_consu", 'tratamiento','edad'])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion11.csv', sep=',')
print("Archivo Generado")