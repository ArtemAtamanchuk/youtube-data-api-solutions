# Built-in.
import os
import csv

# Google Cloud API.
import googleapiclient.errors
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

# Gloabals.
DEVELOPER_KEY = 'YOUR_DEV_KEY'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CHANNEL_ID = 'CHANNEL_ID'

# Create the service object.
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)

# Get the id of the playlist has all published videos of the channel.
uploaded_videos_playlist_id = 'UU' + CHANNEL_ID[2:]

# Make the request and the data list of the uploaded videos from that playlist.
videos = []    
part = 'snippet'
fields = {
    'playlistId': uploaded_videos_playlist_id,
    'maxResults': 50
    }      
request = youtube.playlistItems().list(part=part, **fields)
response = request.execute()
playlist_size = response['pageInfo']['totalResults']
 
i = 0
for item in response['items']:
    videos.append([
        i+1,
        f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}",
        item['snippet']['title'],
        f"{item['snippet']['publishedAt']}"
        ])
    print(videos[i])
    i += 1

while i != playlist_size:
    fields = {
        'playlistId': uploaded_videos_playlist_id,
        'maxResults': 50,
        'pageToken': response['nextPageToken']
        }
    request = youtube.playlistItems().list(part=part, **fields)
    response = request.execute()
    
    for item in response['items']:
        videos.append([
            i+1,
            f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}",
            item['snippet']['title'],
            f"{item['snippet']['publishedAt']}"
            ])
        print(videos[i])
        if i == playlist_size:
            break        
        i += 1

# Get the channel's title.
fields = {
    'id': CHANNEL_ID
    }
request = youtube.channels().list(part=part, **fields)
channel_title = request.execute()['items'][0]['snippet']['title']
        
youtube.close()  # Close the socket.

# Make the file has the output data.
with (open(f'The list videos from {channel_title}.csv', 'w',
           newline='', encoding='utf-16') as list_videos): 
    writer = csv.writer(list_videos, delimiter=',')
    videos.append(['#', 'URL', 'Title', 'Published'])
    
    for video in videos[::-1]:
        writer.writerow(video)
    
print('Done.')
