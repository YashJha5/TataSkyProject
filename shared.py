# External Modules
from bs4 import BeautifulSoup
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient
# Internal modules
import logging
import csv
import re
import io
import json

connect_str = "DefaultEndpointsProtocol=https;AccountName=blobazurerenew;AccountKey=d/Wd4CScD3bkkh/yS8HxI+dIDCh+qCZlUOlDpOkMl/XeWXoYIpY0t/5ANJHYKtY0LvdWcifT+CPmrruMNOEDBw==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

filename = "Demo2"

# read client of blob storage
blob_client_read = blob_service_client.get_blob_client(
    container="demo-02", blob=(str(filename)+".html"))

# write client of blob storage
blob_client_write = blob_service_client.get_blob_client(
    container="demo-02", blob='{}_new.csv'.format(str(filename)))

if __name__ == "__main__":
    try:
        # setup soup
        soup = BeautifulSoup(
            blob_client_read.download_blob().readall(), "html.parser")
        table = soup.select_one("table")
        headers = [str(re.sub('\n', '', th.text))
                   for th in table.select("tr th")]
        # set csvdata var as a IO file obj--string
        csvdata = io.StringIO()
        wr = csv.writer(csvdata)
        wr.writerow(headers)
        wr.writerows([[str(re.sub('\n', '', td.text))
                       for td in row.find_all("td")] for row in table.select("tr")])
        # upload the csv data
        # print(csvdata.getvalue())
        blob_client_write.upload_blob(csvdata.getvalue(), overwrite=True)
        logging.info("Writing file")
    except Exception as err:
        logging.error(err)
