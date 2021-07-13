#!/usr/bin/env python3

import youtube_dl
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'audio-format':'mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print("Usage: yt_to_mp3.py Youtube_url_or_ID")
        print("Eg: ./yt_to_mp3.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        exit(0)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1:]
        ydl.download(filenames)

