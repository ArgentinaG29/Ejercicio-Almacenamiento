from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import requests


resp = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=1').json()

print(resp)
numero = ""

for i in range(len(resp)):
    if str(resp[i]) != "[" or str(resp[i]) != "]": 
        numero = numero + str(resp[i])

print(numero)

f = open(numero, "w")
f.write("1060420")
f.close()

#Creando servidor de Google
CLIENT_SECRET_FILE = "client.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#Carpeta de Drive para almacenar los archivos
folder_id = "1S1JtsQqNj-IN2aSjmJIx9x4_uF78kCRU"
file_names = numero
mime_types = ["text/plain"]

#Estableciendo nombre de archivos y carpeta de Drive
for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        "name": file_names,
        "parents": [folder_id]
    }

    #Subir archivo
    media = MediaFileUpload("./"+numero.format(file_name), mimetype=mime_type)
    
    #Creando servidor
    service.files().create(
        body = file_metadata,
        media_body = media,
        fields = "id"
    ).execute()
    
