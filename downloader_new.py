from __future__ import unicode_literals
from sys import argv
import youtube_dl 
import os


# downloader options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }
    ]
}

# ? Think of customised file/folder names for different download sessions
input_filename = f'{argv[1]}'

# checks if the output folder exists
if not os.path.exists(input_filename):
    os.mkdir(input_filename)
    os.chdir(input_filename)
else:
    os.chdir(input_filename)

# reading file and saving songs in output folder
# ? How do I skip /n lines??
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    with open(f'../{input_filename}.txt', 'r') as f:
        yt_links = f.readlines()
        for link in yt_links:
            # print(song)
            ydl.download([link])