import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from change_files_extension import convert_ext as cext

def downlaod_youtube(url, path = '.\\', mp3 = False, hd = True):
    old_path = os.getcwd()
    os.chdir(path)
    
    erro = []
    
    try:
        yt = YouTube(url)
        print(f"Video name: --- {yt.title} ---\nIniciando download...".center(35))
        if mp3:
            yt.streams.get_audio_only().download()
        elif hd:
            yt.streams.get_highest_resolution().download()
        else:
            yt.streams.first().download()
    except Exeption as err:
        erro.append(err)
        
    if mp3:
        cext(".mp4", ".mp3")
    
    if erro:
        print(erro)
    else:
        print("\nProcesso finalizado")
    os.chdir(old_path)



def teste():
    path = r'C:\Users\Ruan\Desktop\Youtube\tim-selenium'
    url = r'https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim'
    downlaod_youtube(url, path, hd = True)
    