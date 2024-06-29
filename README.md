# Spotify to MP3
Legally download your favorite Spotify playlists in mp3 format (via YouTube) for free!

This project goes out to my Vivo Music 3 Garmin watch ✊. I didn't want to pay for Spotify Premium to listen to music on it so I built this tool out of spite last night-- and now I can upload my playlists to my watch at the low low cost of nothing :D.

## How To
### Pre-requisites:
- Download and install [FFmpeg](https://ffmpeg.org/download.html). The yt-dlp library uses FFmpeg to convert YouTube audio to MP3. This [guide](https://www.hostinger.com/tutorials/how-to-install-ffmpeg) got me through it-- within the guide Ctr/Cmd+f to find your operating system!

- Get a **Google API key** from https://console.cloud.google.com/apis/library ![[Guide](https://elfsight.com/blog/how-to-get-youtube-api-key-tutorial/)](images/youtube-api-infographic.webp)

- Get a **Client ID** and a **Client secret** from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) by making an "App". Here's a [how-to resource](https://developer.spotify.com/documentation/web-api/concepts/apps).

### Setting up spotify_to_mp3:
- After you've downloaded this repository, open a command line within `/spotify_to_mp3` and **run the following command** to download all necessary Python dependencies:
```
pip install -r requirements.txt
```
If pip is not recognized as a command, you might need to (re)install [Python](https://www.python.org/).

- Next, follow the instructions in the `/spotify_to_mp3/env.txt` file, copying over your Google API, Client ID, and Client secret keys from before to their appropriate places. Rename the file from 'env.txt` to '.env' when you are done.

### Use spotify_to_mp3:
In a command line, again within `/spotify_to_mp3`, **run**:
```
python3 main.py [replace with Spotify playlist ID (without the brackets)]
```
or, alternatively, you could run it with one or both of the **optional arguments**:
```
python3 main.py [replace with Spotify playlist ID (without the brackets)] --playlist_name [replace with whatever you want to call your output directory (without the brackets)] --max_results [replace with a whole number e.g. 5]
```
*max_results* tells the program, on a per-song basis, how many of the different YouTube video audio tracks to try downloading before giving up. This is necessary because, in my experience, the yt-dlp API is occasionally unable to download the audio from some videos, thus, increasing this number betters the odds of all songs being downloaded successfully. However, the farther down the list of links the program tries, the less relevant results become, the longer the program will take to run, and (I presume) the more YouTube API units you will use. This value is set to 3 by default; feel free to leave it as such, it has worked perfectly well for me.

### [Finding your Spotify playlist ID](https://clients.caster.fm/knowledgebase/110/How-to-find-Spotify-playlist-ID.html#:~:text=To%20find%20the%20Spotify%20playlist,Link%22%20under%20the%20Share%20menu.&text=The%20playlist%20id%20is%20the,after%20playlist%2F%20as%20marked%20above.): 
![[Guide](https://clients.caster.fm/knowledgebase/110/How-to-find-Spotify-playlist-ID.html#:~:text=To%20find%20the%20Spotify%20playlist,Link%22%20under%20the%20Share%20menu.&text=The%20playlist%20id%20is%20the,after%20playlist%2F%20as%20marked%20above.)](images/playlist-id-image.JPG)

## Notes
### Known limitations
- Because of Google API requests' daily rate limits, you're only able to do playlists with ~100 songs (I'm guestimating) at a time before you run out of units for the day. One workaround is splitting up your playlists and either waiting a day between downloading or using additional Google API key(s) (made on alternate Google accounts) per playlist section.

### Potential Future Updates
- Figuring out how to work around YouTube API limits more efficiently so that converting multiple and larger playlists at a time is possible
- Building a front-end, implementing the Spotify API such that users can log in with their Spotify accounts and simply click on the playlist they want to download as MP3
- If the previous bullet is accomplished, I'd like to set up a server to host this service and increase its accessibility!

I probably won't get around to these all that soon (but I'm totally open to collaboration 👀!) 
