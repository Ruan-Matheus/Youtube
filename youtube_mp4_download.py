from pytube import Playlist
import os
    
# A flag, telling if the users wish to convert the videos to mp3
def download_mp4_playlist(path: str, url: str): 
    
    # Import inside out out?
    # I shouldn't change the current diretory. I have to, or chang the download path.
    
    erros = []
    filenames = []
    for file in os.listdir(path):
        filename, file_extension = os.path.splitext(file)
        print(filename, file_extension)
        filenames.append(filename)


    play = Playlist(url)
    
    # Nome da playlist...
    # Numero de arquivos...
    # When the file is already download verification is not working properly


    for i, video in enumerate(play.videos):
        try:
            video_name = video.title
            video_n = f"nº:{i+ 1} de {len(play.videos)}"
            print(f'\n{video_name}, {video_n:.>20}')
            if video.title not in filenames:
                print("Baixando video...\n")
                video.streams.first().download()
            else:
                print("Video já baixado!\n")
        except error as e:
            erros.append(e)
            print(erros)
            
    print(f"Processo Concluído. \nOs seu vídeos foram baixados no seguinte diretório: \n{path}")
    print(erros)
  