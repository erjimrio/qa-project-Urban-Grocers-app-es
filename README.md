# Proyecto Urban Grocers 
## Validación del campo `name` al crear un kit de productos

Este módulo contiene pruebas automatizadas para verificar el comportamiento del parámetro `name` en la solicitud de creación de un kit de productos, dentro de la API de Urban Grocers.

Las pruebas cubren distintos escenarios de entrada, incluyendo longitudes mínimas y máximas, caracteres especiales, espacios, números, omisión del parámetro y tipo incorrecto.

### Requisitos previos

Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes:

- [`pytest`](https://docs.pytest.org/en/latest/)
- [`requests`](https://docs.python-requests.org/en/latest/)

Puedes instalarlos con:

```bash
pip install pytest 
pip install requests 
```
### Pasos para ejecutar las pruebas 
1. Clona el repositorio o descarga los archivos del proyecto.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el siguiente comando para correr todas las pruebas:
```bash
pytest
```
4. Revisa los resultados en la terminal para verificar qué casos pasaron y cuáles fallaron.

### Casos automatizados
Este módulo valida el parámetro name en la creación de kits, incluyendo:
* Longitudes mínimas y máximas 
* Caracteres especiales, espacios y números 
* Omisión del parámetro y tipo incorrecto 
* Las pruebas están organizadas en dos grupos:
  * ✅Pruebas positivas: verifican que el campo name funciona correctamente cuando se envían valores válidos. 
  * ❌ Pruebas negativas: verifican que la API responde con errores cuando se envían valores inválidos.

Cada prueba utiliza assert para comparar el código de respuesta esperado (201 o 400) y, en los casos positivos, también se valida que el campo "name" en la respuesta coincida con el enviado.