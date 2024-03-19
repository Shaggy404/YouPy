from pytube import YouTube
import os
import pyfiglet

result = pyfiglet.figlet_format("YouPy", font = "isometric3", justify = "center" ) 
print(result)
print("The lightweight Youtube Downloader made in Python")

def menu_download():
    print("1 - Download to MP3 (audio)")
    print("2 - Download to MP4 (Video)")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        mp3_download()
    elif choice == "2":
        mp4_download()
    else:
        print("Bad choice, please enter number 1 or 2")

# MP3 download script
def mp3_download():
    yt = YouTube(input("Enter the URL of the video \n"))
    video = yt.streams.filter(only_audio=True).first()

    home_directory = os.path.expanduser("~")
    destination = os.path.join(home_directory, "Music", "Youtube")

    out_file = video.download(output_path=destination)

    #Add .mp3 extension to the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print (yt.title + " has been successfully downloaded in MP3")

#MP4 donwload script
def mp4_download():
    yt = YouTube(input("Enter the URL of the video \n"))
    video = yt.streams.get_highest_resolution()

    home_directory = os.path.expanduser("~")
    destination = os.path.join(home_directory, "Music", "Youtube")

    out_file = video.download(output_path=destination)

    print(yt.title + " has been successfully downloaded in MP4")


menu_download()

'''
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <shaggy404@protonmail.ch> wrote this file. As long as you retain this notice
 * you can do whatever you want with this stuff. If we meet some day, and you
 * think this stuff is worth it, you can buy me a beer in return. Shaggy_404
 * ----------------------------------------------------------------------------
 */
'''
