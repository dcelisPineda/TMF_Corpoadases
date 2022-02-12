# TMF_Corpoadases
# Visualizaciones Power BI.

<table class="default">
	<tr> 
		<td><p><a href="https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/README.md"><h5><b>Principal</b></h5></a><p></td>
		<td><p><a href="https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/README_dwh.md"><h5><b>ETL</b></h5></a><p></td>
		<td><p><a href="https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/README_modelos.md"><h5><b>Modelos</b></h5></a><p></td>
	</tr>
</table>

<h4>Visualizacion 1</h4>

Resuelve la siguiente pregunta: <b>Cuáles son los motivos de Ingreso de adolescentes y jóvenes con sanciones penales</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion1.JPG)

<table class="default">
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

<h4>Visualizacion 2</h4>

Resuelve la siguiente pregunta: <b>Cuál es la Edad Promedio de ingreso de Jóvenes con sanciones penales</b>

![alt text](https://github.com/dcelisPineda/TMF_Corpoadases/blob/main/IMG/pbvisualizacion2.JPG)

<table class="default">
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
	 <p>Visualizar la distribución de la edad de los adolescentes y jóvenes que ingresan a la corporación resaltando la media.</p>
	 </td>
  </tr>
</table>

<table class="default">
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
  <tr>
	 <td><b>Objetivo</b></td>
         <td>
	 <p>Comparar el porcentaje de edad de los adolescentes y jóvenes e identificar la cantidad de jóvenes agrupados por la edad y el delito.</p>
	 </td>
  </tr>
</table>


