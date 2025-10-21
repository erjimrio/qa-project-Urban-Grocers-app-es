import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,   # inserta la dirección URL completa
                         json=body,     #inserta el cuerpo de la solicitud
                         headers=data.headers)  # inserta los encabezados




