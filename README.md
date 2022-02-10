# TMF_Corpoadases
# Etl para el Procesamiento Información
Etl para el Procesamiento Información

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
<h4>STG1_HECHOS</h4>
<table class="default">
  <tr>
    <td><b>Proceso</b></td>
    <td>STG1_Hechos.ktr</td>
  </tr>
  <tr>
    <td><b>Origen</b></td>
    <td><p>Public.cor_in_base</p>
		<p>public.dim_delitos</p>	
</td>
  </tr>
  <tr>
    <td><b>Destino</b></td>
    <td>
	    <p>Public.STG1_Hechos</p>
		<p>Public.log_stg1_hechos</p>	
    </td>
  </tr>
  <tr>
    <td><b>Descripción</b></td>
    <td>Este proceso cruza la información de la tabla <b>COR_IN_BASE</b>, limpiando y validando el campo
	Nombre del Delito con la tabla DIM_DELITO, los registros que no crucen se envían a una tabla(<b>log_stg1_hechos</b>)
	para que el equipo de trabajo pueda revisarlos y de ser necesario arreglarlos para  volver a procesar la información,
	(Se tiene un control para evitar la inserción de duplicados), de lo contrato se insertan los 
	registros en la tabla <b>STG1_Hechos</b>.</td>
  </tr>
</table>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/stg1.JPG)

<h4>STG2_Hechos</h4>
<table class="default">
  <tr>
    <td><b>Proceso</b></td>
    <td>STG2_Hechos.ktr</td>
  </tr>
  <tr>
    <td><b>Origen</b></td>
    <td><p>Public.STG2_HECHOS</p>
		<p>public.dim_tip_familiar</p>	
</td>
  </tr>
  <tr>
    <td><b>Destino</b></td>
    <td>
	    <p>Public.STG1_Hechos</p>
		<p>Public.log_stg1_hechos</p>	
    </td>
  </tr>
  <tr>
    <td><b>Descripción</b></td>
    <td>Este proceso cruza la información de la tabla STG1_Hechos, limpiando y validando
	el campo Nombre Tipo Familia con la tabla <b>DIM_TIP_FAMILIAR</b>, los registros que no crucen se
	envían a una tabla(<b>log_stg2_hechos</b>) que el equipo de trabajo pueda revisarlos y de ser necesario 
	arreglarlos para volver a procesar la información,de lo contrato se insertan
	los registros en la tabla <b>STG2_HECHOS</b>.</td>
  </tr>
</table>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/stg2.JPG)
