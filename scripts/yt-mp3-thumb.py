import os

file = open('music-mp3.txt', 'r')
lines = file.readlines()

count = 0
for line in lines:
    count += 1
    os.system(f"youtube-dl --format bestaudio -x --audio-format mp3 -k --embed-thumbnail --add-metadata {line}")