import requests
import random
import datetime
import time
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Azure Storage account connection string
connect_str = 'CONNECTION_STRING'
container_name = 'CONTAINER_NAME'

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

x = range(1000)
temp = 30

for n in x:
    y = random.uniform(-1, 1)
    temp = temp + y
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')

    myobj = [
        {
            "Temperature": temp,
            "Timestamp": ts
        }
    ]

    # Create a folder structure based on the current date and time
    folder_path = now.strftime('temperature_raw/%Y/%m/%d/%H/%M')
    blob_name = f'{folder_path}/temperature{now.strftime("%S")}.json'
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Upload the JSON object to the blob
    blob_client.upload_blob(json.dumps(myobj), overwrite=True)

    
    time.sleep(1)
    print(myobj)
    print(f'Uploaded to Azure Blob Storage: {blob_name}')