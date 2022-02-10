# TMF_Corpoadases
# Etl para el Procesamiento Información
Etl para el Procesamiento Información
Para el desarrollo del procesamiento de la información se realizará usando el programa PENTAHO y para el almacenamiento el motor de base de datos POSTGRESQL.

<b>Inicio</b>:
Job Inicial con el que arranca el procesamiento de información el cual Tiene como primer paso el arranque del proceso Star,
continuando con el procesamiento de la información y finalmente la generación de los modelos Analíticos.

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/Inicio.JPG)

<b>TFM_DWH</b>:
Este paso se incluye el procesamiento de la información, se inicia con la validación de los archivos, continuando con la carga de las dimensiones y continua con la limpieza de datos.
![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/dwh_inicio.JPG)

<b>Cargar Información</b>:
Proceso: CargaInformacion.ktr
Origen	Archivo Excel Base_[Enumerado]
Destino	Public.COR_IN_BASE
Public.log_estrcuturaarchivos
Descripción
Carga la información del archivo plano Base validando lo siguiente:        
Numero Documento que sea numérico.
Tipo de sanción contenga los valores Meses, Días.
Si alguno de los dos (2) campos no cumple con las reglas se enviará la tabla log_estrcuturaarchivos, 
de lo contrario pasaran los registros en la tabla Public. COR_IN_BASE.
![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/validador.JPG)
