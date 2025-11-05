# 🛵 Proyecto Urban Grocers - Validación del campo `name` al crear un kit de productos
## 📌 Descripción del proyecto

Este proyecto corresponde al **Sprint 8 del Bootcamp de QA Engineer de TripleTen**.     
Consiste en desarrollar pruebas automatizadas para validar el comportamiento del parámetro `name` en la solicitud de creación de un kit de productos dentro de la API de **Urban Grocers**.

El objetivo principal es verificar que la API maneje correctamente distintos tipos de entrada para el campo `name`, incluyendo casos válidos y no válidos, conforme a las reglas de negocio y validación esperadas.

Las pruebas cubren distintos escenarios de entrada, incluyendo longitudes mínimas y máximas, caracteres especiales, espacios, números, omisión del parámetro y tipo incorrecto.

---

## ⚠️ Aviso de atribución

Este proyecto fue desarrollado como parte del programa educativo de **TripleTen**.  
El contenido, estructura y objetivos del ejercicio fueron proporcionados por TripleTen con fines formativos.  
**Todos los derechos sobre el diseño original de la API y los escenarios de prueba pertenecen a TripleTen.**

---

## 📦 Requisitos previos

Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes:

- [`pytest`](https://docs.pytest.org/en/latest/)
- [`requests`](https://docs.python-requests.org/en/latest/)

Puedes instalarlos con:

```bash
pip install pytest 
pip install requests 
```
---

## 🧪 Tecnologías y técnicas utilizadas

- **Lenguaje:** Python 3  
- **Framework de pruebas:** Pytest  
- **Cliente HTTP:** `requests`  
- **Validación de API:** Asserts, status codes, y estructura de respuesta  
- **Cobertura de pruebas:** Casos límite, entradas inválidas, omisión de parámetros

---

## 📁 Estructura del proyecto

```plaintext
qa-project-Urban-Grocers-app-es/
├── .gitignore                    # Archivos y carpetas ignoradas por Git
├── README.md                     # Documentación del proyecto
├── configuration.py              # Rutas base y endpoints de la API
├── data.py                       # Cuerpos de solicitud para pruebas (kit_body)
├── sender_stand_request.py       # Funciones para enviar solicitudes POST (usuarios y kits)
└── create_kit_name_kit_test.py   # Pruebas automatizadas para el campo "name" del kit
```
---

## ▶️ Pasos para ejecutar las pruebas
 
1. Clona el repositorio o descarga los archivos del proyecto.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el siguiente comando para correr todas las pruebas:
```bash
pytest
```
4. Revisa los resultados en la terminal para verificar qué casos pasaron y cuáles fallaron.

---

## 🤖 Casos automatizados

Este módulo valida el parámetro name en la creación de kits, incluyendo:
* Longitudes mínimas y máximas 
* Caracteres especiales, espacios y números 
* Omisión del parámetro y tipo incorrecto 
* Las pruebas están organizadas en dos grupos:
  * ✅Pruebas positivas: verifican que el campo name funciona correctamente cuando se envían valores válidos. 
  * ❌ Pruebas negativas: verifican que la API responde con errores cuando se envían valores inválidos.

Cada prueba utiliza assert para comparar el código de respuesta esperado (201 o 400) y, en los casos positivos, también se valida que el campo "name" en la respuesta coincida con el enviado.

---

## ✍️ Autor

**Erick Jiménez del Río**  
QA Engineer en transición a SDET   
📍 CDMX, México  
🔗 [GitHub](https://github.com/erjimrio)  
🔗 [LinkedIn](https://www.linkedin.com/in/erjimrio)