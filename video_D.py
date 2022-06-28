from pytube import YouTube

def video_download (download_folder, url, resolution):
    video = YouTube(url)
    if resolution == "Highest Resolution":
        video_stream = video.streams.get_highest_resolution()
    else:
        video_stream = video.streams.get_highest_resolution(resolution)

    video_stream.download(download_folder)
