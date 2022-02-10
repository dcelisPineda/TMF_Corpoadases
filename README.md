# TMF_Corpoadases
# Etl para el Procesamiento Información
Etl para el Procesamiento Información
Para el desarrollo del procesamiento de la información se realizará usando el programa PENTAHO y para el almacenamiento el motor de base de datos POSTGRESQL.

<h4>Inicio</h4>
Job Inicial con el que arranca el procesamiento de información el cual Tiene como primer paso el arranque del proceso Star,
continuando con el procesamiento de la información y finalmente la generación de los modelos Analíticos.

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/Inicio.JPG)

<h4>TFM_DWH</h4>
Este paso se incluye el procesamiento de la información, se inicia con la validación de los archivos, continuando con la carga de las dimensiones y continua con la limpieza de datos.

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/dwh_inicio.JPG)

<h4>CARGAR INFORMACION</h4>
<table class="default">
  <tr>
    <td><b>Proceso</b></td>
    <td>CargaInformacion.ktr</td>
  </tr>
  <tr>
    <td><b>Origen</b></td>
    <td>Archivo Excel Base_[Enumerado]</td>
  </tr>
  <tr>
    <td><b>Destino</b></td>
    <td><p>Public.COR_IN_BASE</p>
        <p>Public.log_estrcuturaarchivos</p>
    </td>
  </tr>
  <tr>
    <td><b>Descripción</b></td>
    <td>Carga la información del archivo plano Base validando lo siguiente:        
Numero Documento que sea numérico.
Tipo de sanción contenga los valores Meses, Días.
Si alguno de los dos (2) campos no cumple con las reglas se enviará la tabla log_estrcuturaarchivos, 
de lo contrario pasaran los registros en la tabla Public.COR_IN_BASE.</td>
  </tr>
</table>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/CargueInformacion.JPG)
<h4>DIMENSIONES</h4>
<table class="default">
  <tr>
    <td><b>Proceso</b></td>
    <td>Dimensiones.ktr</td>
  </tr>
  <tr>
    <td><b>Origen</b></td>
    <td><p>dim_delito.csv</p>
		<p>dim_tip_familiar.csv</p>
		<p>dim_niv_consumo.csv</p>
		<p>dim_escolaridad.csv</p>
		<p>dim_sit_joven.csv</p>
		<p>dim_genero.csv</p>
		<p>dim_ocupacion.csv</p>
</td>
  </tr>
  <tr>
    <td><b>Destino</b></td>
    <td>
	    <p>Public.DIM_DELITOS</p>
		<p>Public. DIM_TIP_FAMILIAR</p>
		<p>Public.DIM_NIV_CONSUMO</p>
		<p>Public.DIM_ESCOLARIDAD</p>
		<p>Public.DIM_SIT_JOVEN</p>
		<p>Public.DIM_GENERO</p>
		<p>Public.DIM_OCUPACION</p>
		<p>Public.LOG_DIM_DELITOS</p>
		<p>Public.LOG_DIM_TIPOfAMILIAR</p>
		<p>Public.LOG_ DIM_NIVELCONSUMO</p>
		<p>Public.LOG_DIM_ESCOLAPR</p>
		<p>Public.LOG_DIM_SITJOVEN</p>
		<p>Public.LOG_DIM_GENERO</p>
		<p>Public.LOG_DIM_OCUPACION</p>
    </td>
  </tr>
  <tr>
    <td><b>Descripción</b></td>
    <td>En este proceso se crean archivos paramétricos de extensión .CSV, 
	que contiene el campo id y descripción de las variables: Delitos, Tipo_Familia, Nivel_Consumo, Escolaridad,
	Situación_Joven, Genero, Ocupación. Esto usado para los procesos de homologación y limpieza de los datos 
	que se cargan desde los archivos Excel que suministra la corporación,
	finalizado el paso los registros se insertaran en las tablas Destino mencionados en este apartado.</td>
  </tr>
</table>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/dimension.JPG)
