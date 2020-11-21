import requests, zipfile, io

url = "https://www.meso-star.com/projects/solstice/downloads/Solstice-0.9.0-Win64.zip"
folder = "solstice"


def download_extract(url, folder):
    """ Downloads and extracts zip file to specified folder"""
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(folder)

