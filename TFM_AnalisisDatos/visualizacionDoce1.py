import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import psycopg2
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import array
try:
   connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="DWH")
   cursor = connection.cursor()
   postgreSQL_select_Query = """
SELECT  d.clasificacion_grado,
       f.delito,
      c.id nivelConsumo,
      f. niv_consu des_niv_consu,
      o.id ocupacion  ,   
      f.ocupacion des_ocupacion,
      public."ValidarEscolaridad"(f.esco_apro) escoApro,      
      f.esco_apro des_esco_apro,
      public."ValidarEscolaridad"(f.esco_act) escoActu ,
      f.esco_act des_esco_act
     FROM public.fact_corp f 
     inner join public.dim_delitos d
     on f.delito=d.delito   
     inner join  public.dim_niv_consumo c
     on f.niv_consu=c.nivel_consumo    
     inner join  public.dim_ocupacion o
     on f.ocupacion=o.ocupacion_joven
     WHERE o.id   NOT IN (4)
  """ 
   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()    
   df = pd.DataFrame(mobile_records,columns=['clasificacion_grado','delito', 'nivelConsumo','des_niv_consu','ocupacion','des_ocupacion','escoApro','des_esco_apro','escoActu','des_esco_act'])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
df.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/CSV_Visualizacion12.csv', sep=',')
print("Archivo Generado")  
feature =pd.read_csv(r'D:/Maestria/TFM/Datos/OUTPUT/CSV_Visualizacion12.csv')
dt=pd.DataFrame(feature) 
######ATENCION psicologica######
Delito = ctrl.Antecedent(np.arange(1,29,1),'Delito')       
menores = [1,1,8]
Leves =   [1,9,29]
Agravados =[17,29,29]
Delito['Menores']=fuzz.trimf(Delito.universe,menores)
Delito['Leves']=fuzz.trimf(Delito.universe,Leves)
Delito['Agravados']=fuzz.trimf(Delito.universe,Agravados)
Consumo = ctrl.Antecedent(np.arange(1,6,1),'Consumo') 
Bajo = [1,1,2]
Medio =[1,2,6]
Alto = [4,6,6]
Consumo['Bajo']=fuzz.trimf(Consumo.universe,Bajo) 
Consumo['Medio']=fuzz.trimf(Consumo.universe,Medio)
Consumo['Alto']=fuzz.trimf(Consumo.universe,Alto)
AtencionPsico = ctrl.Consequent(np.arange(1,100,1),'AtencionPsicologica') 
Baja = [0,0,50]
Media = [0,50,100]
Prioritaria = [50,100,100]
AtencionPsico['Baja']=fuzz.trimf(AtencionPsico.universe,Baja)
AtencionPsico['Media']=fuzz.trimf(AtencionPsico.universe,Media)
AtencionPsico['Prioritaria']=fuzz.trimf(AtencionPsico.universe,Prioritaria)
r1=ctrl.Rule(Delito['Menores'] & Consumo['Bajo'], AtencionPsico['Baja'])
r2=ctrl.Rule(Delito['Menores'] & Consumo['Medio'],AtencionPsico['Baja'])
r3=ctrl.Rule(Delito['Menores'] & Consumo['Alto'], AtencionPsico['Media'])
r4=ctrl.Rule(Delito['Leves'] & Consumo['Bajo'],   AtencionPsico['Media'])
r5=ctrl.Rule(Delito['Leves'] & Consumo['Medio'],   AtencionPsico['Prioritaria'])
r6=ctrl.Rule(Delito['Leves'] & Consumo['Alto'],   AtencionPsico['Prioritaria'])
r7=ctrl.Rule(Delito['Agravados'] & Consumo['Bajo'],   AtencionPsico['Media'])
r8=ctrl.Rule(Delito['Agravados'] & Consumo['Medio'],   AtencionPsico['Media'])
r9=ctrl.Rule(Delito['Agravados'] & Consumo['Alto'],   AtencionPsico['Prioritaria'])
AtencionPsico_ctrl = ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8,r9])
AtencionPsico_simulador=ctrl.ControlSystemSimulation(AtencionPsico_ctrl)
dt = dt.reset_index()
atencion = []
for i in dt.index: 
    AtencionPsico_simulador.input['Delito']=[i]
    AtencionPsico_simulador.input['Consumo']= dt["nivelConsumo"][i]
    AtencionPsico_simulador.compute()
    resultado=AtencionPsico_simulador.output
    for key, value in resultado.items():
        atencion.append(value.astype(int))
dtclasificacion_grado =dt["clasificacion_grado"]
dtnivelConsumo =dt["nivelConsumo"]
dtdelito =dt["delito"]
dtnivelConsumoDes=dt["des_niv_consu"]
dtatencion=atencion
dfAtencionPsicolo = pd.DataFrame({
                    'clasificacion_grado':dtclasificacion_grado ,
                    'delito':dtdelito,
                   'nivelConsumo':dtnivelConsumo ,
                   'Des_NivelConsumo':dtnivelConsumoDes,
                   'AtencionPsic': dtatencion}) 
dfAtencionPsicolo.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/salidas_modelos/dfAtencionPsicolo.csv')  
print("Archivo Generado")
######ATENCION TERAPIAOCUPACION######
EscolaridadActual = ctrl.Antecedent(np.arange(1,15,1),'EscActual') 
primaria = [1,1,5]
secundaria =   [1,6,15]
superior=[12,15,15]
EscolaridadActual['primaria']=fuzz.trimf(EscolaridadActual.universe,primaria) 
EscolaridadActual['secundaria']=fuzz.trimf(EscolaridadActual.universe,secundaria)
EscolaridadActual['superior']=fuzz.trimf(EscolaridadActual.universe,superior)
EscolaridadApro = ctrl.Antecedent(np.arange(1,15,1),'EscApro') 
primaria = [1,1,5]
secundaria =   [1,6,15]
superior=[12,15,15]
EscolaridadApro['primaria']=fuzz.trimf(EscolaridadApro.universe,primaria) 
EscolaridadApro['secundaria']=fuzz.trimf(EscolaridadApro.universe,secundaria)
EscolaridadApro['superior']=fuzz.trimf(EscolaridadApro.universe,superior)
Ocupacion= ctrl.Antecedent(np.arange(1,5,1),'Ocupacion') 
NoRealizaActividad = [1,1,5]
RealizaActividad=[2,5,5]
Ocupacion['RealizaActividad']=fuzz.trimf(Ocupacion.universe,RealizaActividad) 
Ocupacion['NoRealizaActividad']=fuzz.trimf(Ocupacion.universe,NoRealizaActividad)
AtencionTerapia = ctrl.Consequent(np.arange(1,100,1),'AtencionTerapia')
Baja = [0,0,50]
Media = [0,50,100]
Prioritaria = [50,100,100]
AtencionTerapia['Baja']=fuzz.trimf(AtencionTerapia.universe,Baja)
AtencionTerapia['Media']=fuzz.trimf(AtencionTerapia.universe,Media)
AtencionTerapia['Prioritaria']=fuzz.trimf(AtencionTerapia.universe,Prioritaria)
rTer1=ctrl.Rule(EscolaridadActual['primaria'] & EscolaridadApro['primaria'] &  Ocupacion['RealizaActividad'] ,   AtencionTerapia['Media'])
rTer2=ctrl.Rule(EscolaridadActual['primaria'] & EscolaridadApro['primaria'] &  Ocupacion['NoRealizaActividad'] , AtencionTerapia['Prioritaria'])
rTer3=ctrl.Rule(EscolaridadActual['primaria'] & EscolaridadApro['secundaria'] & Ocupacion['RealizaActividad'],   AtencionTerapia['Baja'])
rTer4=ctrl.Rule(EscolaridadActual['primaria'] & EscolaridadApro['secundaria'] & Ocupacion['NoRealizaActividad'], AtencionTerapia['Prioritaria'])
rTer5=ctrl.Rule(EscolaridadActual['primaria'] & EscolaridadApro['superior'] & Ocupacion['RealizaActividad'],   AtencionTerapia['Baja'])
rTer6=ctrl.Rule(EscolaridadActual['primaria'] & EscolaridadApro['superior'] & Ocupacion['NoRealizaActividad'],   AtencionTerapia['Media'])
rTer7=ctrl.Rule(EscolaridadActual['secundaria'] & EscolaridadApro['primaria'] &   Ocupacion['RealizaActividad'] ,  AtencionTerapia['Media'])
rTer8=ctrl.Rule(EscolaridadActual['secundaria'] & EscolaridadApro['primaria'] &   Ocupacion['NoRealizaActividad'],AtencionTerapia['Prioritaria'])
rTer9=ctrl.Rule(EscolaridadActual['secundaria'] & EscolaridadApro['secundaria'] & Ocupacion['RealizaActividad'],   AtencionTerapia['Baja'])
rTer10=ctrl.Rule(EscolaridadActual['secundaria'] & EscolaridadApro['secundaria'] & Ocupacion['NoRealizaActividad'], AtencionTerapia['Prioritaria'])
rTer11=ctrl.Rule(EscolaridadActual['secundaria'] & EscolaridadApro['superior'] &   Ocupacion['RealizaActividad'],   AtencionTerapia['Baja'])
rTer12=ctrl.Rule(EscolaridadActual['secundaria'] & EscolaridadApro['superior'] &   Ocupacion['NoRealizaActividad'], AtencionTerapia['Media'])
rTer13=ctrl.Rule(EscolaridadActual['superior'] & EscolaridadApro['primaria'] &   Ocupacion['RealizaActividad'] ,  AtencionTerapia['Prioritaria'])
rTer14=ctrl.Rule(EscolaridadActual['superior'] & EscolaridadApro['primaria'] &   Ocupacion['NoRealizaActividad'], AtencionTerapia['Prioritaria'])
rTer15=ctrl.Rule(EscolaridadActual['superior'] & EscolaridadApro['secundaria'] & Ocupacion['RealizaActividad'],   AtencionTerapia['Prioritaria'])
rTer16=ctrl.Rule(EscolaridadActual['superior'] & EscolaridadApro['secundaria'] & Ocupacion['NoRealizaActividad'], AtencionTerapia['Prioritaria'])
rTer17=ctrl.Rule(EscolaridadActual['superior'] & EscolaridadApro['superior'] &   Ocupacion['RealizaActividad'],   AtencionTerapia['Baja'])
rTer18=ctrl.Rule(EscolaridadActual['superior'] & EscolaridadApro['superior'] &   Ocupacion['NoRealizaActividad'], AtencionTerapia['Media'])
AtencionTerapia_ctrl = ctrl.ControlSystem([rTer1,rTer2,rTer3,rTer4,rTer5,rTer6,rTer7,rTer8,rTer9,rTer10,rTer11,rTer12,rTer13,rTer14,rTer15,rTer16,rTer17,rTer18])
AtencionTerapia_simulador=ctrl.ControlSystemSimulation(AtencionTerapia_ctrl)
atencionT = []
for i in dt.index: 
    AtencionTerapia_simulador.input['EscActual']=dt["escoActu"][i]    
    AtencionTerapia_simulador.input['EscApro']= dt["escoApro"][i]
    AtencionTerapia_simulador.input['Ocupacion']= dt["ocupacion"][i]
    AtencionTerapia_simulador.compute()
    resultadoT=AtencionTerapia_simulador.output
    for key, value in resultadoT.items():
        atencionT.append(value.astype(int))
dtescActual =dt["escoActu"]
dtescActualDes=dt["des_esco_act"]
dtescoApro =dt["escoApro"]
dtescAproDes=dt["des_esco_apro"]
dtocupacionjoven =dt["ocupacion"]
dtOcupacionDes=dt["des_ocupacion"]
dtatenciont=atencionT
dfAtencionTerapia = pd.DataFrame({
                    'esActual':dtescActual,
                    "descripcion_act":dtescActualDes,
                    'esAproba':dtescoApro ,
                    "descripcion_apro":dtescAproDes,
                    "ocupacion":dtocupacionjoven,
                    "descripcion_ocu":dtOcupacionDes,
                   'AtencionTerapia': dtatenciont})
dfAtencionTerapia.to_csv('D:/Maestria/TFM/DATOS/OUTPUT/salidas_modelos/dfAtencionTerapia.csv')