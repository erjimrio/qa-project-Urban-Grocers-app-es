import sender_stand_request
import data

# Función para crear un nuevo usuario
def test_create_new_user():
    response = sender_stand_request.post_new_user(data.user_body)
    # Comprueba si el código de estado es 201
    assert response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert response.json()["authToken"] != ""
    auth_token = response.json().get("authToken")
    assert auth_token != ""
    return auth_token
