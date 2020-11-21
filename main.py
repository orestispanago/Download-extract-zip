import os
import requests, zipfile, io

url = "https://www.meso-star.com/projects/solstice/downloads/Solstice-0.9.0-Win64.zip"
folder = "solstice"


def download_extract(url, folder):
    """ Downloads and extracts zip file to specified folder"""
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(folder)


def mkdir_if_not_exists(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

mkdir_if_not_exists(folder)
if len(os.listdir(folder)) == 0:
    download_extract(url, folder)
else:
    print(f"{folder} directory not empty")
