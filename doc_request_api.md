Test d'authentification avec curl : 
    curl -X 'GET' \
  'http://127.0.0.1:8000/permissions?username=alice&password=wonderland' \
  -H 'accept: application/json'
Test d'authentification en requete HTTP : 
    http://127.0.0.1:8000/permissions?username=alice&password=wonderland