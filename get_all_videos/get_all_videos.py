# Built-in.
import os
import csv
import json

# Google Cloud API.
import googleapiclient.errors
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

# DEVELOPER_KEY = 'YOUR_API_KEY'
DEVELOPER_KEY = 'AIzaSyDEXF1aVan3YHibkg0_eiYwXIg_2n28ZoM'

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Create the service object.
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)

# Send the request to YouTube Data API v3.
channel_id = 'UC7yMBOeBTcPhlTdI-PS-_Xg'  # The id of the channel.
part = 'contentDetails'
fields = {
    'id': channel_id
    }

# Get the id of the playlist has all published videos of the channel.
uploaded_videos_playlist_id = 'UU' + channel_id[2:]

# Make the data list of the uploaded videos from that playlist.
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
        item['snippet']['title'],
        f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}",
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
            item['snippet']['title'],
            f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}",
            f"{item['snippet']['publishedAt']}"
            ])
        print(videos[i])
        if i == playlist_size:
            break        
        i += 1
        
youtube.close()  # Close the socket.

with (open('list_videos.csv', 'w',
           newline='', encoding='utf-16') as list_videos): 
    writer = csv.writer(list_videos, delimiter=',')
    videos.append(['#', 'Title', 'URL', 'Published'])
    
    for video in videos[::-1]:
        writer.writerow(video)
    
print('Done.')