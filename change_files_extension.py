import re
import os

def convert_ext(new, path = r'.\\'):
    files = os.listdir(path)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension != new:
            lista = [filename, new]
            os.rename(file, ''.join(lista))