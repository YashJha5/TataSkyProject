import logging
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time
connect_str="DefaultEndpointsProtocol=https;AccountName=tataskylogicapptest;AccountKey=pUgLe5JKMY9PqfQiurQNzN1Td7KdmhNc3j+mdpGmj2iLgA2GhTmLxZGW8L7qrcleiRu971xBrt+iU8u4jz6zuA==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
filename="test"
 
if __name__=="__main__":
    blob_client_read = blob_service_client.get_blob_client(container="container1", blob=(str(filename)+".xls"))
    
    excel=pd.ExcelFile(blob_client_read.download_blob().readall(),engine='xlrd')
    for i in excel.sheet_names:
        sheet=excel.parse(i)
        blob_client_write = blob_service_client.get_blob_client(container="container1", blob='{}_{}.csv'.format(str(filename),str(i)))
        csvdata=sheet.to_csv()
        blob_client_write.upload_blob(csvdata)