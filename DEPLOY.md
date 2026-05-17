# Deployment Guide

## Quick Deploy Options

### Option 1: Render (Easiest, Recommended)

1. Fork this repository on GitHub
2. Go to [render.com](https://render.com) and sign up with GitHub
3. Create a new "Web Service"
4. Connect your forked repository
5. Render will auto-detect the Python project
6. Deployment completes automatically ✅

**Free tier includes:** 750 hours/month runtime (more than enough!)

### Option 2: Railway

1. Go to [railway.app](https://railway.app)
2. Click "Start New Project"
3. Select "Deploy from GitHub"
4. Connect your forked repository
5. Railway auto-detects Python
6. It deploys instantly ✅

**Free tier includes:** $5/month credit (usually 30+ days of running)

### Option 3: Heroku (Legacy, still works)

```bash
heroku create your-app-name
git push heroku main
heroku config:set GITHUB_TOKEN=your_token_here
```

### Option 4: Docker (Self-Hosted)

```bash
docker build -t terminal-card .
docker run -p 8000:8000 terminal-card
```

## Environment Variables

If using GitHub token for higher API rate limits:

1. Generate a GitHub personal access token at: https://github.com/settings/tokens
2. Add to your platform's environment variables:
   - **Key:** `GITHUB_TOKEN`
   - **Value:** Your token

Note: This is optional. The app works without it (with lower rate limits).

## Testing Your Deployment

After deployment, test with:

```
https://your-deployed-url.com/api/terminal?username=hritik4722&theme=dracula
```

If it returns an SVG image, you're live! 🎉

## Custom Domain

Most platforms support custom domains. Add your domain in the platform's settings:

- **Render:** Settings → Custom Domains
- **Railway:** Add your domain in project settings
- **Heroku:** `heroku domains:add yourdomain.com`

## Troubleshooting

**Issue:** "Module not found" error
- Solution: Check that `requirements.txt` exists and contains all packages

**Issue:** CORS errors when embedding in README
- Solution: Already handled in API response headers (Access-Control-Allow-Origin: *)

**Issue:** SVG not loading
- Verify the username is correct
- Check if GitHub API is accessible from the server

**Issue:** Rate limit errors
- Add a GitHub token to environment variables
- Without token: 60 requests/hour per IP
- With token: 5000 requests/hour per token

## Performance Notes

- SVG is cached for 30 minutes
- GitHub API calls are not cached (fresh data each request)
- First request for a user takes ~500ms (GitHub API call)
- Subsequent requests return instantly from cache

## Monitoring

Most platforms provide built-in monitoring:

- **Render:** Real-time logs and metrics
- **Railway:** Usage dashboard
- **Heroku:** Logs via `heroku logs --tail`

## Scaling (When You Become Famous)

If your card gets millions of views:

1. Upgrade to paid tier (usually just $7/month for entry level)
2. Consider caching responses in Redis
3. Implement rate limiting per IP

For now, free tier is more than sufficient!
