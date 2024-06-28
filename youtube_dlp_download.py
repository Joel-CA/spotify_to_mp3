import yt_dlp
import os

def download_youtube_to_mp3(video_urls, output_directory='downloads'):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    #try all provided URLs until success (or no more URLs to try)
    i = 0
    while i < len(video_urls):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_urls[i]])
                return # Exit function on successful download
        except yt_dlp.utils.DownloadError as e:
            i+=1
            if i >= len(video_urls):
                print("All URLs failed to download.")
                break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

# #Example usage:
# video_urls = [
#     'https://www.youtube.com/watch?v=Kwwl9jiJ1A4'
# ]
# output_directory = 'downloads'  # This will create a 'downloads' folder in the current working directory
# download_youtube_to_mp3(video_urls, output_directory)

