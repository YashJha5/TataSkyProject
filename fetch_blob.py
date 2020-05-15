import logging
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time
import csv
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse

connect_str="DefaultEndpointsProtocol=https;AccountName=blobazurerenew;AccountKey=d/Wd4CScD3bkkh/yS8HxI+dIDCh+qCZlUOlDpOkMl/XeWXoYIpY0t/5ANJHYKtY0LvdWcifT+CPmrruMNOEDBw==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
filename="Demo2"
#print(blob_service_client)
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Reads in an HTML and attempts to convert all tables into CSV files.')
    parser.add_argument('--delimiter', '-d', action='store', default=',',help="Character with which to separate CSV columns")
    parser.add_argument('--quotechar', '-q', action='store', default='"',help="Character within which to nest CSV text")
    parser.add_argument('filename',nargs="?",help="HTML file from which to extract tables")
    args = parser.parse_args()
    blob_client_read = blob_service_client.get_blob_client(container="demo-02", blob=(str(filename)+".html"))
    data = BeautifulSoup(blob_client_read.download_blob().readall())
    #soup = BeautifulSoup(html, "html.parser")
    table = data.findAll("table")[0]
    #rows = table.findAll("tr")
    #df = pd.read_html(table)
    tablecount = -1
    for table in data.findAll("table"):
        tablecount += 1
        
        #with open('output.csv','w',newline='') as csvfile:
            #fout = csv.writer(csvfile,delimiter=args.delimiter,quotechar=args.quotechar, quoting=csv.QUOTE_MINIMAL)
        blob_client_write = blob_service_client.get_blob_client(container="container1", blob='{}.csv'.format("tataskytest"))    
        for row in table.findAll('tr'):
            
            cols = row.findAll(['td','th'])
            if cols :
                cols = [str(x.text).strip() for x in cols]
                #fout.writerow(cols)
                blob_client_write.upload_blob(cols)