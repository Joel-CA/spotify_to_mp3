# main.py
import argparse
from youtube_dlp_download import download_youtube_to_mp3
from youtube_API import get_youtube_urls
from spotify_API import get_playlist_tracks

def main(playlist_id, playlist_name, max_results):
    song_querys = get_playlist_tracks(playlist_id)
    videos_urls = []
    for song_query in song_querys:
        videos_urls.append(get_youtube_urls(song_query, max_results))

    for video_urls in videos_urls:
        download_youtube_to_mp3(video_urls, playlist_name)

    print("All songs successfully downloaded!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process playlist ID and (optionally) desired playlist name')

    parser.add_argument('playlist_id', type=str, help="A valid playlist id")
    parser.add_argument('--playlist_name', default='playlist', help='Directory to save the downloaded MP3 files (default: playlist)')
    #increase max_results if it keeps failing to download (although even 1 result has been fine for me)
    parser.add_argument('--max_results', default=3, help='Number of youtube links to try per song')
    args = parser.parse_args()

    main(args.playlist_id, args.playlist_name, args.max_results)