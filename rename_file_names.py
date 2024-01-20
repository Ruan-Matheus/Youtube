import os
import re


def order_videos_names(path, pattern, file_extension = '.mp4'):
    names_error = {}
    os.chdir(path)
    file_list = os.listdir()
    for i, file in enumerate(file_list):
        print(f"Processando...\t - {i + 1} de {len(file_list)}")
        try:
            match = (re.search(pattern, file))
            new_name = f'Day {match.groups()[1].split()[1]} - {match.groups()[0]}{file_extension}'
            os.rename(file, new_name)
        except AttributeError as e:
            names_error[file] = e
            
    print(f"\nProcessamento Concluído. \nHouve {len(names_error)} erros")
    if names_error:
        print(names_error)
    