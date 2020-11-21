import os
import zip
import tar_gz

url = "https://www.meso-star.com/projects/solstice/downloads/Solstice-0.9.0-Win64.zip"
folder = "solstice"


def mkdir_if_not_exists(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def check_extension_and_call(url, folder):
    if url.split(".")[-1] == "zip":
        zip.download_extract(url, folder)
    elif url.split(".")[-1] == "gz":
        tar_gz.download_extract(url, folder)
    print("Not .zip or .gz file extension")


mkdir_if_not_exists(folder)
if len(os.listdir(folder)) == 0:
    check_extension_and_call()
else:
    print(f"{folder} directory not empty...aborting")
