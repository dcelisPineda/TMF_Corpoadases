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
  SELECT 
  delito,
  niv_consu,
  case 
    WHEN CicloEscoApro != CicloEscoAct THEN 1
     ELSE 0
    END ContinuidadEscolar,
    ocupacion,
   rein_delito    
 FROM ( 
 SELECT  d.id  delito,  
         c.id niv_consu,   
         s.id ocupacion, 
         public."ValidarEscolaridad"(f.esco_apro) CicloEscoApro,      
         public."ValidarEscolaridad"(f.esco_act) CicloEscoAct ,
    CASE rein_delito
      WHEN 'SI' THEN 1
      ELSE '0'
     END rein_delito
     FROM public.fact_corp f 
     inner join public.dim_delitos d
     on f.delito=d.delito
      inner join public.dim_escolaridad e
     on f.esco_apro=e.escolaridad 
     inner join  public.dim_niv_consumo c
     on f.niv_consu=c.nivel_consumo
     INNER JOIN public.dim_sit_joven s
     on f.sit_acutual=s.sit_joven
     inner join  public.dim_ocupacion o
     on f.ocupacion=o.ocupacion_joven
     ) ramdom
    """
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()    
   df = pd.DataFrame(mobile_records,columns=[ 'delito','niv_consu','ContinuidadEscolar','ocupacion','rein_delito'])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion10.csv', sep=',')
print("Archivo Generado")