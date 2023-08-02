# 2.08.2023

# General import
import requests, os

def main(url):

    print("--> DOWNLOAD YT-DLP")
    r = requests.get("https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe")
    open("yt-dlp.exe", "wb").write(r.content)

    if(r.status_code):

        print("--> TRY DOWNLOAD VIDEO")
        os.system("yt-dlp.exe " + url)
        print("--> END DOWNLOAD VIDEO")

main(input("URL => "))