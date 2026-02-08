#!/usr/bin/env python3
"""
Artificial Insanity Podcast - Automatic Transcript Generator
Fetches episodes from YouTube and generates SEO-optimized transcript pages
Uses retry logic to handle intermittent blocking issues
"""

import os
import json
import requests
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from googleapiclient.discovery import build
import time

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

def get_transcript(video_id, retry_count=2):
    """
    Fetch transcript for a video with retry logic
    to handle intermittent blocking from GitHub Actions
    """
    for attempt in range(retry_count):
        try:
            if attempt > 0:
                print(f"  Retry {attempt}/{retry_count - 1} for {video_id}...")
                time.sleep(3)  # Brief delay between retries
            
            # Attempt to get transcript
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            
            if transcript_list:
                print(f"  ✓ Successfully retrieved transcript ({len(transcript_list)} segments)")
                return transcript_list
                
        except TranscriptsDisabled:
            print(f"  ⚠ Transcripts are disabled for this video")
            return None
        except NoTranscriptFound:
            print(f"  ⚠ No transcript found (captions may not be enabled yet)")
            return None
        except Exception as e:
            if "Too Many Requests" in str(e) or "429" in str(e):
                if attempt < retry_count - 1:
                    print(f"  ⚠ Rate limited, waiting before retry...")
                    time.sleep(5)
                    continue
            if attempt < retry_count - 1:
                print(f"  ⚠ Error on attempt {attempt + 1}: {str(e)[:100]}")
                continue
            else:
                print(f"  ✗ Failed after {retry_count} attempts")
                return None
    
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
        transcript_html = '''<p class="no-transcript">Transcript not yet available for this episode. 
        <br><br>This could be because:
        <br>• Captions haven't been generated yet (usually takes 24-48 hours after upload)
        <br>• Captions are disabled for this video
        <br>• The video is too new
        <br><br>Check back later or <a href="https://www.youtube.com/watch?v={}">watch on YouTube</a> to see if captions are available.</p>'''.format(video['video_id'])
    
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
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: #1a1a1a;
            padding: 2rem;
            border: 2px solid #00ff00;
        }}
        
        .back-link {{
            color: #00ff00;
            text-decoration: none;
            font-size: 14px;
            display: inline-block;
            margin-bottom: 1rem;
        }}
        
        .back-link:hover {{
            text-decoration: underline;
        }}
        
        h1 {{
            color: #00ff00;
            margin-bottom: 1rem;
            font-size: 2rem;
            border-bottom: 2px solid #00ff00;
            padding-bottom: 0.5rem;
        }}
        
        .meta {{
            color: #808080;
            margin-bottom: 2rem;
            font-size: 14px;
        }}
        
        .description {{
            background: #0a0a0a;
            padding: 1rem;
            margin-bottom: 2rem;
            border-left: 4px solid #00ff00;
            color: #c0c0c0;
            white-space: pre-wrap;
        }}
        
        .watch-link {{
            display: inline-block;
            background: #00ff00;
            color: #000000;
            padding: 0.5rem 1rem;
            text-decoration: none;
            font-weight: bold;
            margin-bottom: 2rem;
        }}
        
        .watch-link:hover {{
            background: #00cc00;
        }}
        
        h2 {{
            color: #00ff00;
            margin: 2rem 0 1rem;
            font-size: 1.5rem;
        }}
        
        .transcript-line {{
            margin-bottom: 0.5rem;
            color: #c0c0c0;
        }}
        
        .timestamp {{
            color: #00ff00;
            font-family: 'Courier New', monospace;
            margin-right: 0.5rem;
        }}
        
        .no-transcript {{
            color: #808080;
            font-style: italic;
            line-height: 1.8;
        }}
        
        .no-transcript a {{
            color: #00ff00;
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-link">← Back to All Transcripts</a>
        
        <h1>{video['title']}</h1>
        
        <div class="meta">
            Published: {formatted_date}
        </div>
        
        <div class="description">{video['description']}</div>
        
        <a href="https://www.youtube.com/watch?v={video['video_id']}" target="_blank" class="watch-link">
            ▶ WATCH ON YOUTUBE
        </a>
        
        <h2>Full Transcript</h2>
        
        <div class="transcript">
            {transcript_html}
        </div>
    </div>
</body>
</html>"""
    
    return html

def generate_index_page(videos):
    """Generate main index page listing all episodes"""
    
    episodes_html = ""
    for video in videos:
        pub_date = datetime.fromisoformat(video['published_at'].replace('Z', '+00:00'))
        formatted_date = pub_date.strftime('%B %d, %Y')
        safe_filename = f"episode-{video['video_id']}.html"
        
        title_escaped = video['title'].replace('"', '&quot;').replace("'", '&#39;')
        desc_snippet = video['description'][:200].replace('<', '&lt;').replace('>', '&gt;')
        
        episodes_html += f"""
        <div class="episode-card">
            <img src="{video['thumbnail']}" alt="{title_escaped}">
            <div class="episode-info">
                <h2><a href="{safe_filename}">{video['title']}</a></h2>
                <p class="date">{formatted_date}</p>
                <p class="description">{desc_snippet}...</p>
                <a href="{safe_filename}" class="read-transcript">Read Transcript →</a>
            </div>
        </div>
        """
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podcast Transcripts | Artificial Insanity</title>
    <meta name="description" content="Full transcripts of all Artificial Insanity podcast episodes">
    
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
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            margin-bottom: 3rem;
            border-bottom: 2px solid #00ff00;
            padding-bottom: 2rem;
        }}
        
        h1 {{
            font-size: 3rem;
            color: #00ff00;
            margin-bottom: 1rem;
        }}
        
        .subtitle {{
            color: #808080;
            font-size: 1.2rem;
        }}
        
        .home-link {{
            display: inline-block;
            background: #00ff00;
            color: #000000;
            padding: 0.5rem 1rem;
            text-decoration: none;
            font-weight: bold;
            margin-top: 1rem;
        }}
        
        .home-link:hover {{
            background: #00cc00;
        }}
        
        .episodes {{
            display: grid;
            gap: 2rem;
        }}
        
        .episode-card {{
            background: #1a1a1a;
            border: 2px solid #00ff00;
            padding: 1.5rem;
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 1.5rem;
        }}
        
        .episode-card img {{
            width: 100%;
            height: auto;
            border: 1px solid #00ff00;
        }}
        
        .episode-info h2 {{
            margin-bottom: 0.5rem;
        }}
        
        .episode-info h2 a {{
            color: #00ff00;
            text-decoration: none;
        }}
        
        .episode-info h2 a:hover {{
            text-decoration: underline;
        }}
        
        .date {{
            color: #808080;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }}
        
        .description {{
            color: #c0c0c0;
            margin-bottom: 1rem;
            line-height: 1.6;
        }}
        
        .read-transcript {{
            color: #00ff00;
            text-decoration: none;
            font-weight: bold;
        }}
        
        .read-transcript:hover {{
            text-decoration: underline;
        }}
        
        @media (max-width: 768px) {{
            .episode-card {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>PODCAST TRANSCRIPTS</h1>
            <p class="subtitle">Full searchable transcripts of every Artificial Insanity episode</p>
            <a href="../index.html" class="home-link">← BACK TO HOME</a>
        </header>
        
        <div class="episodes">
            {episodes_html}
        </div>
    </div>
</body>
</html>"""
    
    return html

def main():
    """Main execution function"""
    print("🎙️  Fetching Artificial Insanity episodes from YouTube...")
    
    # Create transcriptions directory if it doesn't exist
    os.makedirs(TRANSCRIPTIONS_DIR, exist_ok=True)
    
    # Get all videos
    videos = get_channel_videos()
    print(f"✓ Found {len(videos)} episodes")
    
    successful_transcripts = 0
    failed_transcripts = 0
    
    # Process each video
    for i, video in enumerate(videos, 1):
        print(f"\n📝 Processing {i}/{len(videos)}: {video['title'][:50]}...")
        
        # Get transcript with retry logic
        transcript = get_transcript(video['video_id'])
        
        if transcript:
            successful_transcripts += 1
        else:
            failed_transcripts += 1
        
        # Generate episode page
        episode_html = generate_episode_page(video, transcript)
        
        # Save episode page
        filename = f"episode-{video['video_id']}.html"
        filepath = os.path.join(TRANSCRIPTIONS_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(episode_html)
        
        print(f"  ✓ Generated: {filename}")
    
    # Generate index page
    print("\n📋 Generating index page...")
    index_html = generate_index_page(videos)
    index_path = os.path.join(TRANSCRIPTIONS_DIR, 'index.html')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"✓ Generated: index.html")
    print(f"\n🎉 Done! Processed {len(videos)} episodes")
    print(f"   ✓ {successful_transcripts} transcripts retrieved")
    print(f"   ⚠ {failed_transcripts} transcripts unavailable")
    print(f"\nAll pages generated in /{TRANSCRIPTIONS_DIR}/")
    print("\nNote: Some transcripts may be unavailable if captions aren't enabled yet.")
    print("YouTube usually generates captions within 24-48 hours of upload.")

if __name__ == "__main__":
    main()
