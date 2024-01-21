from pytube import Playlist
import os
import re
    
# Age restriction error!
# Old isn't doing anything!
def convert_ext(old, new, path = r'.\\'):
    files = os.listdir(path)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension != new:
            lista = [filename, new]
            os.rename(file, ''.join(lista))
            
            
def download_playlist(path: str, url: str, mp3 = False, hd = False):
    old_path = path
    os.chdir(path)
       
    erros = {}
    filenames = []
    for file in os.listdir(path):
        filename, file_extension = os.path.splitext(file)
        filenames.append(filename)

    play = Playlist(url)

    print(f"{play.title} {len(play.videos):.>20} videos\nVerificando arquivos...", end = '\n\n')
    for i, video in enumerate(play.videos):
        try:
            video_name = video.title
            video_name = re.sub(r"[\\/:*?\"<>|\.]", "", video_name)
            video_n = f"nº:{i+ 1} de {len(play.videos)}"
            print(f'{video_name} {video_n:.>20}')
            if video_name not in filenames:
                if mp3:
                    video.streams.filter(only_audio = True).first().download()
                elif hd:
                    video.streams.get_highest_resolution().download()
                else:
                    video.streams.first().download()
        except Exception as e:
            erros[video_name] = e
    if mp3:
        convert_ext(".mp4", ".mp3", path)
        
            
    print(f"\nProcesso Concluído. \nOs seu vídeos foram baixados no seguinte diretório: {path}")
    if erros: 
        print(f"Erros: {erros}")
    os.chdir(old_path)





def teste():
    path = r'C:\Users\Ruan\Music\Viole'
    url = r'https://www.youtube.com/playlist?list=PLQYxbWW1sY2tfTeKDJd__JA-m3iesg-sa'
    download_playlist(path, url, mp3 = True)