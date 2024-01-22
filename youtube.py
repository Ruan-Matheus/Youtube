import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from change_files_extension import convert_ext as cext

def downlaod_youtube(url, path = '.', mp3 = False, hd = True):
    
    '''Download a single video/music from YouTube.
    
    :param url: The URL of the YouTube video
    :type url: str
    :param path: The path of a folder on your computer (default is current directory)
    :type path: str
    :param mp3: A flag indicating if the video should be converted to mp3 extension (default is False)
    :type mp3: bool
    :param hd: A flag indicating to download the highest video resolution available (default is True)
    :returns None 
    '''
    
    
    # Saving the current path to return to it later
    old_path = os.getcwd()
    
    # TODO: Context manager?
    os.chdir(path)
    
    erro = []
    
    try:
        yt = YouTube(url, on_progress_callback=print_progress)
        print(f"Video name: {yt.title}\n".center(35))
        
        # Selecting the stream with the mp3 and hd arguments
        if mp3:
            yt.streams.get_audio_only().download()
        elif hd:
            yt.streams.get_highest_resolution().download()
        else:
            yt.streams.first().download()
    
    # Catching errs of download to show to the user
    # TODO: Refine the errors catching, age restriction, video unavailable, etc
    except Exception as err:
        erro.append(err)

    # All the donwloads above return a file with the mp4 extension
    # This function will change the extension the mp3   
    
    # TODO: Refine the mp3 function
    if mp3:
        cext(".mp4", ".mp3")
    
    if erro:
        print(erro)
    else:
        print("\nProcesso finalizado")

    # Returning to the previous path after download
    os.chdir(old_path)




def print_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    percent = (100 * (size - bytes_remaining)) / size
    print(f"Download Progress: {percent:.2f}%", end='\r')


# Example usage    
def teste():
    path = r'C:\Users\Ruan\Desktop\Youtube'
    url = r'https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim'
    downlaod_youtube(url)
teste()