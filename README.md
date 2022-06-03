# rcc-ficoscore-pld-simulacion-client-python 

<p>Esta API simula: el reporte del historial crediticio; el cumplimiento de pago de los compromisos que la persona ha adquirido con entidades financieras, no financieras e instituciones comerciales que dan crédito o participan en actividades afines al crédito; y filtra contra listas de cumplimiento para Prevención de Lavado de Dinero. En esta versión se retornan los campos del Crédito Asociado a Nomina (CAN) en el nodo de créditos.<br/><img src='https://developer.circulodecredito.com.mx/sites/default/files/2020-10/circulo_de_credito-apihub.png' height='40' width='220'/></p><br/>


## Requisitos

Python 3.4+

## Instalación

### Setuptools

Instalacion via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` instala el paquete para todos los usuarios)

Then import the package:
```python
import rcc_fico_pld_simulacion_client
```

## Guía de inicio

### Paso 1. Agregar el producto a la aplicación

Al iniciar sesión seguir los siguientes pasos:

 1. Dar clic en la sección "**Mis aplicaciones**".
 2. Seleccionar la aplicación.
 3. Ir a la pestaña de "**Editar '@tuApp**' ".
    <p align="center">
      <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/edit_applications.jpg" width="900">
    </p>
 4. Al abrirse la ventana emergente, seleccionar el producto.
 5. Dar clic en el botón "**Guardar App**":
    <p align="center">
      <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/selected_product.jpg" width="400">
    </p>


### Paso 2. Capturar los datos de la petición

Los siguientes datos a modificar se encuentran en ***test/test_reporte_de_crdito_consolidado_fico_score_y_pld_api.py***

Es importante modificar el archivo config.ini que se encargará de inicializar la url. Modificar la URL ***('host')***, como se muestra en el siguiente fragmento de código:

```ini
    [API_CONFIG]
    host = https://services.circulodecredito.com.mx/sandbox
    x_api_key = YOUR XAPIKEY
```

De igual manera, en el archivo **test_reporte_de_crdito_consolidado_fico_score_y_pld_api.py**, se deberá modificar el siguiente fragmento de código con los datos correspondientes:

```python
 def test_get_reporte(self):
        body = PersonaPeticion(
            apellido_paterno="SESENTAYDOS",
            apellido_materno="PRUEBA",
            apellido_adicional=None,
            primer_nombre="JUAN",
            segundo_nombre=None,
            fecha_nacimiento="1965-08-09",
            rfc="SEPJ650809JG1",
            curp=None,
            nacionalidad="MX",
            residencia=None,
            estado_civil=None,
            sexo=None,
            clave_elector_ife=None,
            numero_dependientes=None,
            fecha_defuncion=None,
            domicilio=DomicilioPeticion( 
                direccion="PASADISO ENCONTRADO 58",
                colonia_poblacion="MONTEVIDEO", 
                delegacion_municipio="GUSTAVO A MADERO", 
                ciudad= "CIUDAD DE MÉXICO", 
                estado="CDMX", 
                cp="07730", 
                fecha_residencia=None, 
                numero_telefono=None, 
                tipo_domicilio=None, 
                tipo_asentamiento=None)
        )
        try:
   
            api_response=self.api.get_reporte( x_api_key=self.x_api_key,  request=body,x_full_report=True)
            print(api_response)
        except ApiException as e:
            print("Exception when calling TestReporteDeCrditoConsolidadoFICOScoreYPLDApi->test_get_reporte: %s\n" % e)


```

### Paso 3. Ejecutar la prueba unitaria

Teniendo los pasos anteriores ya solo falta ejecutar la prueba unitaria, con el siguiente comando:

```shell
python3 test_reporte_de_crdito_consolidado_fico_score_y_pld_api.py
```
 

---
[CONDICIONES DE USO, REPRODUCCIÓN Y DISTRIBUCIÓN](https://github.com/APIHub-CdC/licencias-cdc)

[1]: https://getcomposer.org/doc/00-intro.md#installation-linux-unix-macos