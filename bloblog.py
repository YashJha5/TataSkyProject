#from azure.storage.blob import BlockBlobService
import time
import logging
import pandas as pd
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


#account_name = "tataskyprojectdemo1"
#account_key = "swNqvogwrn0fEePGIAGecHZvQ8BYQyqrtRtcdv+k5UvFGLTkwYZLV+Ao7d4UznOZ/v358Pc9Mb0FANCTlJkgTQ==" 

#source_container_name = "container2"
#source_file_path = "tataskytest.xls"


#target_container_name = "container1"
#target_file_path = ("tataskytest.csv", timestr)

#service = BlockBlobService(account_name, account_key)

#service.copy_blob(
#    target_container_name, 
#    target_file_path, 
#    f"https://tataskyprojectdemo1.blob.core.windows.net/container2/tataskytest.xls",
#)
