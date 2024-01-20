import os
from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import VideoUnavailable
import re

name_pattern = re.compile(r"(.*)(.mp4)$")
pattern = re.compile(r'.mp4$')
os.chdir(r"music")

def rename_file_extension(pattern, replacement):
    musicas = os.listdir()
    for music_name in musicas:
        match = name_pattern.search(music_name)
        print(match.groups())
        new_music_name = re.sub(pattern, replacement, music_name)
        os.rename(music_name, new_music_name)
            

# yt = YouTube('https://youtu.be/9bZkp7q19f0')
viole = Playlist('https://www.youtube.com/playlist?list=PLQYxbWW1sY2tfTeKDJd__JA-m3iesg-sa')
erros = []

print(f"Playlist name {viole.title}\n".center(35))
for i, vd in enumerate(viole.videos):
    if i == 3:
        break
    video_title = vd.title
    video_number = f'Nº:{i + 1} de {len(viole.videos)}'
    print(f"{video_title:<}{video_number:.>40}")
    try:
        vd.streams.get_audio_only().download()
    except VideoUnavailable:
        erros.append(vd.title)
        
rename_file_extension(pattern, '.mp3')

print("\nDownload finalizado")
print(f"Houve {len(erros)} erros durante o processo!")
if erros:
    print(erros)
