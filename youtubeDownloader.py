#!/usr/bin/env python3

import sys
import urllib.request
from urllib.request import urlopen, FancyURLopener
from urllib.parse import urlparse, parse_qs, unquote

class UndercoverURLopener(FancyURLopener):
    version = "Python 3.2.3"
urllib.request._urlopener = UndercoverURLopener()

def youtube_download(video_url):
    video_id = parse_qs(urlparse(video_url).query)['v'][0]

    url_data = urlopen('http://www.youtube.com/get_video_info?&video_id=' + video_id).read()
    url_info = parse_qs(unquote(url_data.decode('utf-8')))
    token_value = url_info['token'][0]

    download_url = "http://www.youtube.com/get_video?video_id={0}&t={1}&fmt=18".format(
        video_id, token_value)

    video_title = url_info['title'][0] if 'title' in url_info else ''
    # Unicode filenames are more trouble than they're worth
    filename = video_title.encode('ascii', 'ignore').decode('ascii').replace("/", "-") + '.mp4'

    print("\t Downloading '{}' to '{}'...".format(video_title, filename))

    try:
        download = urlopen(download_url).read()
        f = open(filename, 'wb')
        f.write(download)
        f.close()
    except Exception as e:
        print("\t Downlad failed! {}".format(str(e)))
        print("\t Skipping...")
    else:
        print("\t Done.")

def main():
    print("\n--------------------------")
    print (" Youtube Video Downloader")
    print ("--------------------------\n")

    try:
        video_url = sys.argv[1]
    except:
        video_url = input('Enter (space-separated) video URLs: ')
        youtube_download(video_url)
        print("\n Done.")

if __name__ == '__main__':
    main()
