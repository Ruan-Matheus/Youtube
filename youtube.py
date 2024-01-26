import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from change_files_extension import convert_ext as cext
import re


# TODO: Subtitles
def downlaod_youtube(url, path = '.', mp3 = False, hd = True, caption = None):
    """Download a single video/music from YouTube.

    Args:
        url (_type_): The URL of the YouTube video
        path (str, optional): The path of a folder on your computer. Defaults to '.'.
        mp3 (bool, optional): A flag indicating if the video should be converted to mp3 extension. Defaults to False.
        hd (bool, optional):  A flag indicating to download the highest video resolution available. Defaults to True.
        caption (str, optional): The code of languague captions. Defaults to None.
    """

    # Saving the current path to return to it later
    old_path = os.getcwd()
    
    # TODO: Context manager?
    os.chdir(path)
    
    erro = []
    
    try:
        yt = YouTube(url, on_progress_callback=print_progress)
        yt.bypass_age_gate()
        
        pattern = re.compile(r"[\\/:*?\"<>|\.,#]")
        video_title = yt.title
        video_title = re.sub(pattern, "", video_title)
        
        # Downloading the caption
        if caption:
                try:
                    caption = yt.captions[caption]
                    caption.xml_captions
                    caption = caption.generate_srt_captions()

                    with open(video_title + '.srt', 'w', encoding= 'UTF8') as f:
                        f.write(caption)
                except KeyError:
                    print("Caption not available for the mentioned code!")
        
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
    path = r'C:\Users\Ruan\Documents\Codes\Python\Pytube\test'
    url = r'https://www.youtube.com/watch?v=qxPMmW93eDs&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=5&ab_channel=CodeWithHarry'
    downlaod_youtube(url, path, caption='en-IN')
teste()