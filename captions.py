from pytube import YouTube
import os
import re



def downlaod_captions(url, path = '.', language = 'en-IN'):
    yt = YouTube(url)
    yt.bypass_age_gate()

    # A caption object
    caption = yt.captions[language]
    caption.xml_captions
    caption = caption.generate_srt_captions()
    caption_title = yt.title
    print(caption_title)

    pattern = re.compile(r"[\\/:*?\"<>|\.]")
    caption_title = re.sub(pattern, "", caption_title)
    
    with open(caption_title + '.srt', 'w', encoding= 'UTF8') as f:
        f.write(caption)




def teste():
    url = r'https://www.youtube.com/watch?v=qxPMmW93eDs&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=5&pp=iAQB'
    downlaod_captions(url)

teste()