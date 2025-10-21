import sender_stand_request
import data

# Función para cambiar el valor de "name"
def get_kit_body(name):
    # copia el diccionario kit_body
    current_kit_body = data.kit_body.copy()
    # Se reemplaza el valor del parámetro name
    current_kit_body["name"] = name
    return current_kit_body

# Función de prueba positiva
def positive_assert(name):
    # Se obtiene el dato para el campo name
    kit_body = get_kit_body(name)
    # Crear usuario
    response_user = sender_stand_request.post_new_user(data.user_body)
    # Comprueba si el código de estado es 201
    assert response_user.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert response_user.json()["authToken"] != ""
    auth_token = response_user.json().get("authToken")
    # Crea el kit para el usuario
    response_kit = sender_stand_request.post_new_kit(auth_token, kit_body)
    # Valida el status_code = 201
    assert response_kit.status_code == 201
    # Compara el valor enviado y el valor recibido como nombre del kit
    assert response_kit.json()["name"] == name

# Función de prueba positiva
def negative_assert(name):
    # Se obtiene el dato para el campo name
    kit_body = get_kit_body(name)
    # Crear usuario
    response_user = sender_stand_request.post_new_user(data.user_body)
    # Comprueba si el código de estado es 400
    assert response_user.status_code == 400
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert response_user.json()["authToken"] != ""
    auth_token = response_user.json().get("authToken")
    # Crea el kit para el usuario
    response_kit = sender_stand_request.post_new_kit(auth_token, kit_body)
    # Valida el status_code = 400
    assert response_kit.status_code == 400

# ********** Inicio de pruebas **********

# Prueba 1. Creación de un nuevo kit - Prueba Positiva
# El parámetro "name" contiene un caracter, límite inferior
name = data.p1_kit_body["name"]
def test_kit_body_has_1_letter_in_name_get_success_response():
    positive_assert(name)

# Prueba 2. Creación de un nuevo kit - Prueba positiva
# El parámetro "name" contiene 511 caracteres, límite superior

name = data.p2_kit_body["name"]
def test_kit_body_has_511_letters_in_name_get_success_response():
    positive_assert(name)

# Prueba 3. Creación de un nuevo kit - Prueba negativa
# El parámetro "name" no contiene caracteres, por debajo del límite inferior

name = data.p3_kit_body["name"]
def test_kit_body_has_none_letter_in_name_get_unsuccess_response():
    negative_assert(name)

# Prueba 4. Creación de un nuevo kit - Prueba negativa
# El parámetro "name" contiene 512 caracteres por encima del límite superior

name = data.p4_kit_body["name"]
def test_kit_body_has_512_letters_in_name_get_unsuccess_response():
    negative_assert(name)

# Prueba 5. Creación de un nuevo kit - Prueba positiva
# El parámetro "name" contiene caracteres especiales

name = data.p5_kit_body["name"]
def test_kit_body_has_special_characters_in_name_get_success_response():
    positive_assert(name)

# Prueba 6. Creación de un nuevo kit - Prueba positiva
# El parámetro "name" permite espacios

name = data.p6_kit_body["name"]
def test_kit_body_has_space_in_name_get_success_response():
    positive_assert(name)
