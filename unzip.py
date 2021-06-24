import zipfile
import os
import fnmatch

files = fnmatch.filter(os.listdir('.'), '*.zip')

for datei in files:
    with zipfile.ZipFile(datei, 'r') as zip_ref:
        zip_ref.extractall('.')
