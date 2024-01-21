import re
import os

def convert_ext(old, new, path = r'.\\'):
    files = os.listdir(path)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        print(filename + file_extension)
        if file_extension != new:
            lista = [filename, new]
            os.rename(file, ''.join(lista))
    
convert_ext('.mp4', '.mp3')