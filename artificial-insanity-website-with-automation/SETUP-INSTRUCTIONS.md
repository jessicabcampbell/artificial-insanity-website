# 🎙️ Artificial Insanity - Automatic Transcript System Setup

This guide will walk you through setting up a fully automated system that:
- ✅ Checks YouTube weekly for new episodes
- ✅ Downloads transcripts automatically
- ✅ Generates SEO-optimized HTML pages
- ✅ Auto-deploys to your website

**Total setup time: ~15 minutes**

---

## 📋 STEP 1: Get Your YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **"Create Project"** (top bar)
   - Name it: "Artificial Insanity Transcripts"
   - Click **Create**
3. Once project is created, make sure it's selected (top bar)
4. Go to **APIs & Services → Library**
5. Search for **"YouTube Data API v3"**
6. Click on it, then click **ENABLE**
7. Go to **APIs & Services → Credentials**
8. Click **+ CREATE CREDENTIALS** → **API Key**
9. **Copy the API key** - you'll need this!
10. (Optional but recommended) Click **RESTRICT KEY**:
    - Under "API restrictions", select "Restrict key"
    - Choose "YouTube Data API v3"
    - Click **Save**

✅ **You now have your YouTube API Key!** Keep it safe.

---

## 📋 STEP 2: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **New Repository** (green button)
3. Repository name: `artificial-insanity-website`
4. Make it **Public** (required for free Netlify)
5. ✅ Check **"Add a README file"**
6. Click **Create repository**

✅ **Your repo is created!**

---

## 📋 STEP 3: Upload Your Website Files to GitHub

### Option A: Using GitHub Web Interface (Easiest)

1. In your new repo, click **"Add file"** → **"Upload files"**
2. Drag and drop your entire website folder contents:
   - `index.html`
   - `about.html`
   - `resist.html`
   - `contact.html`
   - All `.png` image files
   - `README.md`
3. Also upload these NEW files I just created:
   - `fetch_transcripts.py`
   - `requirements.txt`
   - `.github/workflows/update-transcripts.yml` (create folder structure first)
4. Scroll down, add commit message: "Initial website upload"
5. Click **Commit changes**

### Option B: Using Git Command Line

```bash
# Navigate to your website folder
cd /path/to/your/website

# Initialize git
git init
git add .
git commit -m "Initial commit"

# Connect to GitHub
git remote add origin https://github.com/YOUR-USERNAME/artificial-insanity-website.git
git branch -M main
git push -u origin main
```

✅ **Your website is on GitHub!**

---

## 📋 STEP 4: Add YouTube API Key to GitHub Secrets

1. In your GitHub repo, go to **Settings** (top menu)
2. In left sidebar: **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Name: `YOUTUBE_API_KEY`
5. Value: *[Paste your API key from Step 1]*
6. Click **Add secret**

✅ **API key is securely stored!**

---

## 📋 STEP 5: Connect Netlify to GitHub

### If you already have a Netlify site:

1. Go to [Netlify Dashboard](https://app.netlify.com/)
2. Find your current site
3. Go to **Site settings** → **Build & deploy**
4. Scroll to **"Build settings"**
5. Click **"Link to repository"**
6. Choose **GitHub**
7. Authorize Netlify to access your repos
8. Select: `artificial-insanity-website`
9. Branch: `main`
10. Build settings:
    - **Build command:** (leave empty)
    - **Publish directory:** `/`
11. Click **Deploy site**

### If you're starting fresh on Netlify:

1. Go to [Netlify](https://app.netlify.com/)
2. Click **"Add new site"** → **"Import an existing project"**
3. Choose **GitHub**
4. Select your repo: `artificial-insanity-website`
5. Branch: `main`
6. Build settings: (leave empty)
7. Click **Deploy site**

✅ **Netlify is connected!**

---

## 📋 STEP 6: Test the Automation

### Manual Test (Do this first!)

1. Go to your GitHub repo
2. Click **Actions** (top menu)
3. Click **"Update Podcast Transcripts"** workflow
4. Click **"Run workflow"** → **"Run workflow"** (green button)
5. Wait 2-3 minutes
6. Check **transcriptions/** folder in your repo
7. You should see:
   - `index.html`
   - `episode-XXXXX.html` (one per episode)

### Check Your Live Site

1. Go to: `https://your-site.netlify.app/transcriptions/`
2. You should see all your episodes listed!

✅ **It works!**

---

## 🎯 STEP 7: Set Your Custom Domain (Optional)

1. In Netlify: **Domain settings**
2. Click **"Add custom domain"**
3. Enter: `artificialinsanity.com`
4. Follow DNS instructions
5. Your transcripts will be at: `artificialinsanity.com/transcriptions/`

---

## 🔧 How It Works Now

**Every Monday at 9 AM UTC**, GitHub will automatically:
1. ✅ Check your YouTube channel
2. ✅ Download any new transcripts
3. ✅ Generate HTML pages
4. ✅ Commit to GitHub
5. ✅ Netlify auto-deploys (takes ~1 min)

**You do absolutely nothing!** 🎉

---

## 🛠️ Customization Options

### Change Update Schedule

Edit `.github/workflows/update-transcripts.yml`:

```yaml
# Every day at 6 AM
- cron: '0 6 * * *'

# Every Sunday at midnight
- cron: '0 0 * * 0'

# Every 3 days at noon
- cron: '0 12 */3 * *'
```

### Manual Trigger Anytime

1. Go to GitHub repo → **Actions**
2. Click **"Update Podcast Transcripts"**
3. Click **"Run workflow"**

---

## 🐛 Troubleshooting

### "API key not found" error
- Check GitHub Secrets: Settings → Secrets → Actions
- Make sure it's named exactly: `YOUTUBE_API_KEY`

### "Transcript not available"
- Not all YouTube videos have transcripts
- Make sure auto-captions are enabled on your videos

### Netlify not deploying
- Check: Site settings → Build & deploy → Deploy notifications
- Make sure GitHub integration is active

### Workflow not running
- Check: Actions tab → Look for errors
- Make sure workflow file is in: `.github/workflows/`

---

## 📞 Need Help?

If you get stuck, check:
1. GitHub Actions logs (Actions tab → Click on workflow run)
2. Netlify deploy logs (Deploys tab)

---

## 🎉 You're Done!

Your transcription system is now **100% automatic**!

**What happens next:**
- Every Monday, new episodes auto-appear
- Google can index all your transcripts
- SEO boost from searchable content
- Zero maintenance required

**Enjoy your hands-off transcript system!** 🚀
