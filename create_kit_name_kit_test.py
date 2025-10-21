import sender_stand_request
import data

# Función para crear un nuevo usuario
def test_create_new_user_and_kit():
    # Crear usuario
    response_user = sender_stand_request.post_new_user(data.user_body)
    # Comprueba si el código de estado es 201
    assert response_user.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert response_user.json()["authToken"] != ""
    auth_token = response_user.json().get("authToken")
    # Crear Kit con ese token
    response_kit = sender_stand_request.post_new_kit(auth_token)
    assert response_kit.status_code == 201