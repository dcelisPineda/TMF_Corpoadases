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
   escoApro,
   CicloEscoApro idCicloEscoApro,
   case CicloEscoApro
	    when  1  then 'Primaria'
	    when  2  then 'Primaria'
	    when  3  then 'Primaria'
	    when  4  then 'Primaria'
	    when  5  then 'Primaria'
	    when  6  then 'secundaria'
	    when  7  then 'secundaria'
	    when  8  then 'secundaria'
	    when  9  then 'secundaria'
	    when  10 then 'secundaria'
	    when  11 then 'secundaria'
	    when  12  then 'secundaria'
	    when  13  then 'superior'
	    when  14  then 'superior'
	    when  15  then 'superior'
	    when  16  then 'superior'
  end CicloEscoApro,  
   escoActu,
   CicloEscoAct idCicloEscoAct,
   case CicloEscoAct
	    when  1  then 'Primaria'
	    when  2  then 'Primaria'
	    when  3  then 'Primaria'
	    when  4  then 'Primaria'
	    when  5  then 'Primaria'
	    when  6  then 'secundaria'
	    when  7  then 'secundaria'
	    when  8  then 'secundaria'
	    when  9  then 'secundaria'
	    when  10 then 'secundaria'
	    when  11 then 'secundaria'
	    when  12  then 'secundaria'
	    when  13  then 'superior'
	    when  14  then 'superior'
	    when  15  then 'superior'
	    when  16  then 'superior'
  end CicloescoActu,
  continuidadEscolar
FROM (
SELECT 
     public."ValidarNombreEscolaridad"(public."ValidarEscolaridadID"(f.esco_apro)) escoApro,
     public."ValidarNombreEscolaridad"(public."ValidarEscolaridadID"(f.esco_act))  escoActu,
     public."ValidarEscolaridad"(f.esco_apro) CicloEscoApro,      
     public."ValidarEscolaridad"(f.esco_act) CicloEscoAct ,
     f.delito,
     case 
	when  esco_apro = esco_act THEN 'No'
     ELSE 'Si'
  end continuidadEscolar
FROM public.fact_corp f 
ORDER BY 
    f.delito
) T 
ORDER BY T.delito asc
  """ 
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()    
   df = pd.DataFrame(mobile_records,columns=['delito', 'escoApro','idCicloEscoApro','CicloEscoApro','escoActu','idCicloEscoAct','CicloescoActu','continuidadEscolar'])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion5.csv', sep=',')
print("Archivo Generado")