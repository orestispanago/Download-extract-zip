import tarfile
import urllib.request

url = "https://www.meso-star.com/projects/solstice/downloads/Solstice-0.9.0-GNU-Linux64.tar.gz"
folder = "solstice"

def download_extract(url, folder)
    tar = tarfile.open(urllib.request.urlretrieve(url, filename=None)[0])
    tar.extractall(folder)

