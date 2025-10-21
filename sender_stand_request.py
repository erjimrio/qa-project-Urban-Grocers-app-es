import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,   # inserta la dirección URL completa
                         json=body,     #inserta el cuerpo de la solicitud
                         headers=data.headers)  # inserta los encabezados

def post_new_kit(auth_token, kit_body):
    headers= {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post (configuration.URL_SERVICE + configuration.KITS_PATH,
                          json=kit_body,
                          headers=headers)


