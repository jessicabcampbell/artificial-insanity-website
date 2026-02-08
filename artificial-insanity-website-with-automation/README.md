# Artificial Insanity Website - Setup Guide

## ✅ All Fixed!

### What Was Updated:
1. ✅ **Sophie and Jessica images** - Swapped correctly
2. ✅ **Logo seamless** - Removed drop-shadow effect
3. ✅ **YouTube embed** - Ready for your video

---

## 🎥 HOW TO ADD YOUR YOUTUBE VIDEO

The YouTube embed is currently set to a placeholder. Here's how to add your latest video:

### Option 1: Quick Method (Easiest)
1. Go to your latest YouTube video
2. Click the **"Share"** button below the video
3. Click **"Embed"**
4. Copy the URL that looks like: `https://www.youtube.com/embed/ABC123XYZ`
5. Open `index.html` in a text editor
6. Find this line:
   ```html
   src="https://www.youtube.com/embed/VIDEO_ID_HERE"
   ```
7. Replace `VIDEO_ID_HERE` with your actual video ID (the part after `/embed/`)
8. Save the file!

### Option 2: Manual Method
1. Go to any of your YouTube videos
2. Look at the URL in your browser: `https://www.youtube.com/watch?v=ABC123XYZ`
3. Copy the part after `v=` (that's your video ID)
4. Open `index.html` in a text editor
5. Replace `VIDEO_ID_HERE` with your video ID
6. Save!

**Example:**
- Your video URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- Your video ID: `dQw4w9WgXcQ`
- Final embed URL: `https://www.youtube.com/embed/dQw4w9WgXcQ`

---

## 📧 CONTACT FORM SETUP - SENDS TO YOUR EMAIL

Your contact form is already configured and ready to go! It uses **Netlify Forms** which keeps your email address completely hidden from spam bots.

### Setup Steps (Takes 2 minutes):

1. **Deploy to Netlify** (see section below)
2. **Configure Email Notifications:**
   - After deploying, go to your Netlify dashboard
   - Click on your site
   - Go to **Forms** in the left sidebar
   - Click **Form notifications**
   - Click **Add notification** → **Email notification**
   - Enter the email where you want to receive messages: **aiforhotties@gmail.com**
   - Click **Save**

**That's it!** Your email stays hidden in the code (secure from spam bots), and all form submissions will be sent to that email address.

### How It Works:
- Form submits → Netlify receives it → Emails you automatically
- Built-in spam protection (honeypot field included)
- Form disappears and shows punk-style "Thanks for reaching out!" message
- 100% FREE (up to 100 submissions/month)

---

## 🚀 DEPLOYING TO NETLIFY (FREE)

1. Go to [netlify.com](https://netlify.com) and sign up
2. Drag your entire website folder onto their dashboard
3. Your site goes live instantly at: `yoursite.netlify.app`
4. When you buy `artificialinsanity.com`, connect it in Netlify settings
5. Free SSL certificate included!

---

## 📁 FILE STRUCTURE

Make sure all files stay in the same folder:
```
website/
├── index.html
├── about.html
├── resist.html
├── contact.html
├── Logo_3.png
├── AI-Pod-Photos-217-no-bg.png
├── AI-Pod-Photos-247-canva-psd-no-bg.png
├── AI-Pod-Photos-261-canva-psd-no-bg.png
├── AI-Pod-Photos-387-canva-psd-no-bg.png
├── AI-Pod-Photos-389-canva-no-bg.png
├── AI-Pod-Photos-54-canva-psd-no-bg.png
└── UNSUBSCRIBE-header.png
```

---

## 🤘 QUESTIONS?

Need help? Just ask!

---

**Built with punk rock energy and zero corporate bullshit.**
