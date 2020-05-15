import logging
import pandas as pd
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time
connect_str="DefaultEndpointsProtocol=https;AccountName=tataskyprojectdemo1;AccountKey=swNqvogwrn0fEePGIAGecHZvQ8BYQyqrtRtcdv+k5UvFGLTkwYZLV+Ao7d4UznOZ/v358Pc9Mb0FANCTlJkgTQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


def main(myblob):
    filename=str((str(myblob.name))[4:(len(myblob.name)-5)])
    logging.error(filename)
    blob_client_read = blob_service_client.get_blob_client(container="new", blob=(str(filename)+".xls"))
    
    excel=pd.ExcelFile(blob_client_read.download_blob().readall())
    for i in excel.sheet_names:
        sheet=excel.parse(i)
        blob_client_write = blob_service_client.get_blob_client(container="new", blob='{}_{}.csv'.format(str(filename),str(i)))
        csvdata=sheet.to_csv()
        blob_client_write.upload_blob(csvdata)

