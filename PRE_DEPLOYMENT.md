# Pre-Deployment Checklist

Before deploying to production, verify these items:

## ✅ Local Testing

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run locally**
   - Windows: `run.bat`
   - Mac/Linux: `bash run.sh`
   - Or: `python -m uvicorn app.main:app --reload`

3. **Test in browser**
   - Visit: `http://localhost:8000`
   - Try different themes in the dropdown
   - Test with your GitHub username
   - Verify the preview updates

4. **Test API directly**
   ```
   http://localhost:8000/api/terminal?username=hritik4722&theme=dracula
   ```
   Should return an SVG image, not an error.

5. **Check all features**
   - ✅ Theme switching works
   - ✅ GitHub data fetches correctly
   - ✅ Live preview updates
   - ✅ Copy snippet works
   - ✅ Mobile responsive

## 🔧 Configuration

1. **GitHub Token (Optional)**
   - Create at: https://github.com/settings/tokens
   - Create a "Personal access token" (classic)
   - Scopes needed: `public_repo` (only to see public data, not required)
   - Copy token and save for deployment

2. **.env file**
   ```bash
   cp .env.example .env
   # Add your GITHUB_TOKEN if you have one
   # Leave empty to use unauthenticated (60 req/hr limit)
   ```

## 📦 Deployment Choice

Choose ONE platform:

| Platform | Free Tier | Setup Time | Recommendation |
|----------|-----------|------------|---|
| **Render** | 750 hrs/mo | 2 min | ⭐ Best for FastAPI |
| **Railway** | $5/mo | 2 min | ⭐ Simple & fast |
| **Heroku** | ❌ Paid | 5 min | Legacy, still works |
| **Docker** | DIY | 10 min | Self-hosted |

## 🚀 Deploy to Render (Recommended)

1. Push code to GitHub (fork or your own repo)
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Go to https://render.com
   - Sign up with GitHub
   - Click "New Web Service"
   - Select your repository
   - Render auto-detects Python

3. Render will auto-configure:
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn app.main:app --host 0.0.0.0`

4. Add environment variables (optional):
   - Click "Environment"
   - Add key: `GITHUB_TOKEN`
   - Add value: Your GitHub token (if you have one)

5. Deploy!
   - Click "Create Web Service"
   - Render deploys in 30-60 seconds
   - You get a free URL like: `terminal-card-abc123.onrender.com`

## 🌐 After Deployment

1. **Test the live URL**
   ```
   https://your-deployed-url.com/api/terminal?username=hritik4722
   ```

2. **Share with others**
   ```markdown
   [![Terminal Card](https://your-deployed-url.com/api/terminal?username=YOUR_USERNAME)](https://github.com/YOUR_USERNAME)
   ```

3. **Add to your README**
   - Use the interactive builder at your deployed URL
   - Or copy the markdown snippet

## ⚠️ Troubleshooting

**Module import error on deploy?**
- Check `requirements.txt` is in root directory
- Check `app/__init__.py` exists

**Can't access the URL?**
- Deployment takes 30-60 seconds
- Check Render/Railway dashboard for errors
- Look at build and runtime logs

**GitHub API errors?**
- Verify your username is correct
- GitHub API doesn't like bots (respect their limits)
- Add a token for higher limits

**Colors look wrong?**
- Verify browser cache is cleared
- Try `?theme=dracula` parameter
- Different browsers may render slightly different

## 📝 Notes

- Free tier is sufficient for most users
- Expected uptime: 99%+ (Render/Railway SLA)
- Data persists if service restarts
- GitHub data is cached for 30 minutes

## ✨ You're Ready!

Once deployed and tested, share your terminal card with the world! 🚀

---

**Questions?** See README.md or DEPLOY.md for more details.
