# 🎙️ Quick Reference Guide

## Common Tasks

### Manually Trigger Update (Anytime)
1. Go to GitHub repo
2. Click **Actions** tab
3. Click **"Update Podcast Transcripts"** workflow
4. Click **"Run workflow"** button
5. Wait 2-3 minutes
6. Check your site!

### Change Update Frequency
Edit `.github/workflows/update-transcripts.yml` line 5:

```yaml
# Current: Every Monday at 9 AM UTC
- cron: '0 9 * * 1'

# Options:
- cron: '0 6 * * *'      # Daily at 6 AM
- cron: '0 0 * * 0'      # Every Sunday midnight
- cron: '0 12 */3 * *'   # Every 3 days at noon
- cron: '0 9 * * 1,4'    # Monday & Thursday at 9 AM
```

### View Transcript Page URLs
- **All episodes:** `artificialinsanity.com/transcriptions/`
- **Individual episode:** `artificialinsanity.com/transcriptions/episode-[VIDEO-ID].html`

### Check Automation Status
**GitHub Actions:**
- GitHub repo → Actions tab
- Click latest run to see logs

**Netlify Deployment:**
- Netlify dashboard → Deploys tab
- See build logs and status

### Pause Automation
To temporarily stop weekly updates:
1. GitHub repo → Actions
2. Click workflow name
3. Click "..." menu → "Disable workflow"

To resume:
- Same steps → "Enable workflow"

### Test Locally (Optional)
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export YOUTUBE_API_KEY="your-key-here"

# Run script
python fetch_transcripts.py

# Check generated files
ls transcriptions/
```

## File Structure

```
artificial-insanity-website/
├── .github/
│   └── workflows/
│       └── update-transcripts.yml    # Automation workflow
├── transcriptions/                    # Auto-generated
│   ├── index.html                     # Episode listing
│   └── episode-*.html                 # Individual episodes
├── index.html                         # Your homepage
├── about.html
├── resist.html
├── contact.html
├── *.png                              # Images
├── fetch_transcripts.py               # Main script
├── requirements.txt                   # Python dependencies
└── .gitignore
```

## SEO Benefits

✅ **Searchable text content** - Google can index every word
✅ **Schema markup** - Rich podcast results in search
✅ **Individual episode pages** - More pages = more traffic
✅ **Keywords** - Transcripts naturally contain your topics
✅ **Long-form content** - Google loves detailed pages

## Monitoring

**Check these weekly:**
- GitHub Actions tab (workflow ran successfully?)
- Netlify Deploys tab (site deployed?)
- `artificialinsanity.com/transcriptions/` (new episodes showing?)

**Google Search Console (after a few weeks):**
- See which transcript pages are getting traffic
- Monitor search impressions/clicks
- Check for crawl errors

## Need to Update?

**Update Python script:**
1. Edit `fetch_transcripts.py` in GitHub web editor
2. Commit changes
3. Workflow will use new version next run

**Update page styling:**
1. Edit HTML templates in `fetch_transcripts.py`
2. Manually trigger workflow to regenerate all pages

## That's It!

Your system is fully automated. Just publish podcasts as normal and transcripts appear automatically! 🎉
