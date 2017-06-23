import os
from glob import iglob, glob
import zipfile

import shutil


def combine_files(path, file_name):
    files_to_zip = glob(os.path.join(path, file_name + '-data.zip.*'))
    if len(list(files_to_zip)) > 0:
        destination = open(os.path.join(path, file_name + '-data.zip'), 'wb')
        for filename in files_to_zip:
            shutil.copyfileobj(open(filename, 'rb'), destination)
        destination.close()
        return True
    else:
        return False


def extract_files(path_to_zip_file, directory_to_extract_to):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
