#!/usr/bin/env python3
"""
Artificial Insanity Podcast - Automatic Transcript Generator
Fetches episodes from YouTube and generates SEO-optimized transcript pages
"""

import os
import json
import requests
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

# Configuration
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
CHANNEL_ID = 'UC1g-EKfoM_OblzPGBF0N6bQ'
TRANSCRIPTIONS_DIR = 'transcriptions'

def get_channel_videos():
    """Fetch all videos from the YouTube channel"""
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    videos = []
    next_page_token = None
    
    while True:
        # Get uploads playlist
        channel_response = youtube.channels().list(
            part='contentDetails',
            id=CHANNEL_ID
        ).execute()
        
        uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        # Get videos from uploads playlist
        playlist_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()
        
        for item in playlist_response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            published_at = item['snippet']['publishedAt']
            thumbnail = item['snippet']['thumbnails']['high']['url']
            
            videos.append({
                'video_id': video_id,
                'title': title,
                'description': description,
                'published_at': published_at,
                'thumbnail': thumbnail
            })
        
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
    
    return videos

def get_transcript(video_id):
    """Fetch transcript for a video"""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript_list
    except Exception as e:
        print(f"Could not fetch transcript for {video_id}: {e}")
        return None

def format_timestamp(seconds):
    """Convert seconds to MM:SS format"""
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def generate_episode_page(video, transcript):
    """Generate HTML page for individual episode"""
    
    # Format published date
    pub_date = datetime.fromisoformat(video['published_at'].replace('Z', '+00:00'))
    formatted_date = pub_date.strftime('%B %d, %Y')
    
    # Escape special characters in title and description
    title_escaped = video['title'].replace('"', '&quot;').replace("'", '&#39;')
    desc_escaped = video['description'].replace('"', '&quot;').replace("'", '&#39;')
    
    # Generate transcript HTML with timestamps
    transcript_html = ""
    if transcript:
        for entry in transcript:
            timestamp = format_timestamp(entry['start'])
            text = entry['text'].replace('<', '&lt;').replace('>', '&gt;')
            transcript_html += f'<p class="transcript-line"><span class="timestamp">[{timestamp}]</span> {text}</p>\n'
    else:
        transcript_html = '<p class="no-transcript">Transcript not available for this episode.</p>'
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_escaped} - Transcript | Artificial Insanity Podcast</title>
    <meta name="description" content="Full transcript of {title_escaped} from Artificial Insanity podcast">
    
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'MS Sans Serif', Arial, sans-serif;
            background: #000000;
            color: #00ff00;
            padding: 2rem;
