from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Set up YouTube API credentials
load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

def get_youtube_urls(query, max_results=1):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results
    ).execute()

    video_urls = []
    for item in search_response['items']:
        video_id = item['id'].get('videoId')
        video_urls.append(f'https://www.youtube.com/watch?v={video_id}')

    return video_urls

# #Example usage:
# song_title = 'Take Back the Night by Captain Sparkles'
# video_urls = get_youtube_urls(song_title, 5)
# print(video_urls)
