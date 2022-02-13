# TMF_Corpoadases
# Visualizaciones Power BI.

<table class="default">
	<tr> 
		<td><p><a href="https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/README.md"><h5><b>Principal</b></h5></a><p></td>
		<td><p><a href="https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/README_dwh.md"><h5><b>ETL</b></h5></a><p></td>
		<td><p><a href="https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/README_modelos.md"><h5><b>Modelos</b></h5></a><p></td>
	</tr>
</table>

tablacontenido
==============

<!--ts-->
 * [visualizacion1](#visualizacion1)
 * [visualizacion2](#visualizacion2)    
 * [visualizacion3](#visualizacion3)  
 * [visualizacion4](#visualizacion4) 
 * [visualizacion5](#visualizacion5) 
 * [visualizacion6](#visualizacion6) 
 * [visualizacion7](#visualizacion7) 
 * [visualizacion8](#visualizacion8) 
<!--te-->


visualizacion1 
==============
<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>Cuáles son los motivos de Ingreso de adolescentes y jóvenes con sanciones penales</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion1.JPG)

<table>
  <tr>
	  <td colspan="2"><b>Motivo de Ingreso al Programa de Responsabilidad Penal</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	        <p>dim_delito</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Delito</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Barras</p>
	 </td>
  </tr>
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
	 <p>Representar, Comparar y diferenciar cada uno de los delitos.</p>
	 </td>
  </tr>
</table>

visualizacion2  
==============

<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>Cuál es la Edad Promedio de ingreso de Jóvenes con sanciones penales</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion2.JPG)

<table borde="1" width="100%">
  <tr>
	  <td colspan="2"><b>Edad Promedio de ingreso de Jóvenes con sanciones penales</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Edad</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Histograma</p>
	 </td>
  </tr>
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
	 <p>Visualizar la distribución de la edad de los adolescentes y jóvenes que ingresan a la</p>
         <p>corporación resaltando la media.</p>
	 </td>
  </tr>
</table>


<table>
  <tr>
	  <td colspan="2"><b>Edad por Delito</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Delito</p>
		<p>Edad</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Gráfico de Tarta</p>
		<p>Tabla</p>
	 </td>
  </tr>
  <tr  width="100%">
	 <td><b>Objetivo</b></td>
         <td>
	 <p>Comparar el porcentaje de edad de los adolescentes y jóvenes e identificar la cantidad</p>
	 <p>de jóvenes agrupados por la edad y el delito.</p>
	 </td>
  </tr>
</table>

visualizacion3
==============
<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>Cuál es la tipología Familiar de los Jóvenes con sanciones penales</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion3.JPG)

<table>
  <tr>
	  <td colspan="2"><b>Tipología Familiar de los Jóvenes con sanciones penales</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	        <p>Delito</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Delito</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Gráfico de Barras Apiladas</p>
		<p>Tabla</p>
		<p>Tarjeta</p>
	 </td>
  </tr>
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
	 <p>Identificar el porcentaje de distribución de la tipología familiar y 
	  la agrupación por delito.</p>
	 </td>
  </tr>
</table>

visualizacion4
==============
<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>Nivel de Consumo de los Jóvenes con sanciones penales.</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion4.JPG)

<table>
  <tr>
	  <td colspan="2"><b>Visualizacion Nivel de Consumo de Jóvenes con sanciones penales</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	        <p>dim_niv_consumo</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Niv_consumo</p>
		<p>Edad</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Histograma</p>
		<p>Tabla</p>
		<p>Gráfico Barras Apiladas</p>
		<p>Gráfico de Anillos</p>
	 </td>
  </tr>
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
	  <p>Representar, comparar la proporción y distribución de la variable nivel 
           de consumo y edad.</p>
          <p>Agrupar los jóvenes por delito y Nivel de consumo.</p>
	 </td>
  </tr>
</table>

visualizacion5
==============
<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>Nivel de Escolaridad de los Jóvenes con sanciones penales.</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion5.JPG)

<table>
  <tr>
	  <td colspan="2"><b>Nivel de Escolaridad de los Jóvenes Con sanciones penales</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Delito</p>
		<p>EscoApro</p>
		<p>EscoAct</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Gráfico de Tarta</p>
		<p>Gráfico de Barras Apiladas</p>
		<p>Tabla</p>
	 </td>
  </tr>
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
	  <p>Representar el porcentaje de los jóvenes que continúan y no continúan con sus estudios.</p>
          <p>Identificar por delito el nivel de escolaridad Aprobado vrs Actual.</p>
          <p>Agrupar los jóvenes por nivel de escolaridad aprobada, actual y el delito.</p>
	 </td>
  </tr>
</table>

visualizacion6
==============
<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>¿Existe alguna relación entre tipología Familiar Vs Reincidencia en Delito?</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion6.JPG)

<table>
  <tr>
	  <td colspan="2"><b>Relación Tipología Familiar vrs Reincidencia en Delito</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Tip_familiar</p>
		<p>Rein_delito</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Gráfico de Barras Agrupadas</p>
		<p>Distribución Chi-Cuadrado</p>
	 </td>
  </tr>
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
	  <p>Comparar la variable Tip_familiar entre los jóvenes que reinciden y no Reinciden para determinar</p>
          <p>si existe o no relación entre estas 2 variables usando el método chi-cuadrado para determinar la relación</p>
          <p>entre las variables.</p>
	 </td>
  </tr>
</table>

visualizacion7
==============
<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>Está asociado el Nivel de consumo con la reincidencia en un delito.</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion61.JPG)

<table>
  <tr>
	  <td colspan="2"><b>Relación Nivel de Consumo vrs Reincidencia de Delito</b>
  </tr>
   <tr>
	 <td><b>Tabla Origen</b></td>
         <td>
		<p>fact_corp</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Variables</b></td>
         <td>
		<p>Niv_consumo</p>
		<p>Rein_delito</p>
	 </td>
  </tr>
   <tr>
	 <td><b>Tipo grafico</b></td>
         <td>
		<p>Gráfico de Barras Agrupadas</p>
		<p>Distribución Chi-Cuadrado</p>
	 </td>
  </tr>
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
		 <p>Comparar la variable Niv_consumo entre los jóvenes que reinciden y no Reinciden para</p>
		 <p>determinar si existe o no relación entre estas 2 variables usando el método chi-cuadrado</p>
		 <p>para determinar la relación..</p>
	 </td>
  </tr>
</table>

visualizacion8
==============
<!--ts-->
 * [tablacontenido](#tablacontenido)
<!--te-->

Resuelve la siguiente pregunta: <b>Cuál es la probabilidad de reincidencia de un Joven que tiene sanciones penales.</b>

Para el entrenamiento se han seleccionado las siguientes variables por recomendación del equipo de trabajo de la corporación:
<p>Delito</p>
<p>Nivel de Consumo</p>
<p>Ocupación</p>

Se descargar la tipología Familiar ya que esta no se relaciona con la reincidencia del delito.
<b><p>Variable Salida</p></b>
<p>0 – No Reincide</p>
<p>1 – Reincide</p>

<b>se aplica los siguientes Modelos:</b>

<p>Random Forest</p>
<p>Regresión Logística</p>
<p>SVM</p>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion7.JPG)



