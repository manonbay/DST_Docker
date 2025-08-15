import os
import requests
from datetime import datetime
import pytz

# définition de l'adresse de l'API
api_address = '127.0.0.2'
# port de l'API
api_port = 8000

success_ids_to_test = ['alice', 'bob']
success_passwords_to_test = ['wonderland', 'builder']

fail_ids_to_test = ['clementine']
fail_passwords_to_test = ['mandarine']


time = ({datetime.now(tz=pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d %H:%M:%S')})

def log_writing(output): 
    """
    Fonction asynchrone pour écrire dans un fichier de log.
    """
    with open('log.txt', 'a') as file:
        file.write(output)


# affichage des résultats dont le résulat est successfuly 200 :

for i in range(len(success_ids_to_test)):
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
                params={
            'username': success_ids_to_test[i],
            'password': success_passwords_to_test[i]
        }
    )
    status_code = r.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = f"{time} : Test for user {success_ids_to_test[i]} {status_code} {test_status}\n"
    log_writing(output)

    
# affichage des résultats dont le résulat est successfuly 403 :  
for i in range(len(fail_ids_to_test)):
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params={
            'username': fail_ids_to_test[i],
            'password': fail_passwords_to_test[i]
        }
    )
    status_code = r.status_code
    if status_code == 403:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = f"{time} : Test for user {fail_ids_to_test[i]} {status_code} {test_status}\n"
    log_writing(output)
    
