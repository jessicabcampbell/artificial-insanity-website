# 🎥 QUICK FIX: YouTube Video Embed

## The Problem
You're seeing an error because the website needs a real video ID from your YouTube channel.

## The 30-Second Fix

### Step 1: Get Your Video ID
1. Go to YouTube.com
2. Find ANY of your Artificial Insanity videos
3. Click on the video
4. Look at the URL in your browser
5. Copy the part after `v=`

**Example:**
- Full URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- Video ID: `dQw4w9WgXcQ` ← **This part!**

### Step 2: Add It to Your Website
1. Open `index.html` in any text editor (Notepad, TextEdit, etc.)
2. Press `Ctrl+F` (or `Cmd+F` on Mac) and search for: `XXXXXXXXXXXX`
3. Replace `XXXXXXXXXXXX` with your actual video ID
4. Save the file

**Before:**
```html
src="https://www.youtube.com/embed/XXXXXXXXXXXX"
```

**After (example):**
```html
src="https://www.youtube.com/embed/dQw4w9WgXcQ"
```

### Step 3: Test It
1. Open `index.html` in your browser
2. The video should now play!

---

## Can't Find a Video ID?

If you don't have any videos published yet:
1. Upload your first video to YouTube
2. Make it public
3. Then follow the steps above

---

**That's it!** Super simple. Just one line to change. 🤘
