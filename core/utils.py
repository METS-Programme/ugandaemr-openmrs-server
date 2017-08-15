import os
from glob import iglob
import zipfile

import shutil


def combine_files(path, file_name):
    files_to_zip = iglob(os.path.join(path, file_name + '-data.zip*'))
    l = list(files_to_zip)
    if len(l) > 0:
        destination = open(path + '/' + file_name + '-data.zip', 'wb')
        for f in l:
            shutil.copyfileobj(open(f, 'rb'), destination)
        destination.close()
        return True
    else:
        return False


def extract_files(path_to_zip_file, directory_to_extract_to):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
