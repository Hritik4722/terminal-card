# 📚 Documentation Index

Welcome to Terminal Card! Choose where you want to go:

## 🚀 **I Want To Deploy NOW**
→ See [QUICK_START.md](QUICK_START.md) (2 minutes)

## 📖 **I Want Full Documentation**  
→ See [README.md](README.md) (comprehensive guide)

## 🛠️ **I Want Step-by-Step Deployment**
→ See [DEPLOY.md](DEPLOY.md) (multiple platforms)

## ✅ **I Want Pre-Deployment Checklist**
→ See [PRE_DEPLOYMENT.md](PRE_DEPLOYMENT.md) (verify everything)

## 📊 **I Want Project Overview**
→ See [PROJECT_STATUS.md](PROJECT_STATUS.md) (what's included)

## 💻 **I Want To Test Locally**
- **Windows:** `run.bat`
- **Mac/Linux:** `bash run.sh`

## 📋 **Common Questions**

### "What is this?"
Terminal Card lets anyone embed a GitHub-themed terminal card in their README.md by just adding a markdown snippet.

### "How do I use it?"
1. Visit the deployed URL
2. Enter your GitHub username
3. Copy the markdown snippet
4. Paste in your README.md
5. Done!

### "Can I customize it?"
Yes! Via URL parameters:
- Theme: `?theme=dracula`
- Title: `?title=AI%20Engineer`
- Location: `?location=San%20Francisco`
- And more...

### "Do I need to code?"
No! Just use the web UI at your deployed URL.

### "Can I self-host?"
Yes! Run locally with `run.bat` (Windows) or `bash run.sh` (Mac/Linux).

### "Where do I deploy?"
- **Render** (recommended): Free, 750 hrs/month, 1-click
- **Railway**: Free $5/month, 1-click
- **Heroku**: Paid, but still works
- **Docker**: Self-hosted anywhere

## 🎨 Features

✅ Auto-fetch GitHub profile data  
✅ 3 beautiful themes (Catppuccin, Dracula, GitHub Light)  
✅ Customizable terminal display  
✅ Live preview builder  
✅ One-click deploy  
✅ CORS enabled for any README  
✅ Fast & cached  

## 📁 Project Structure

```
terminal-card/
├── app/                 # Backend code
│   ├── main.py         # FastAPI server
│   └── themes.py       # Color themes
├── public/
│   └── index.html      # Web UI
├── requirements.txt    # Dependencies
├── README.md           # Full documentation
├── QUICK_START.md      # Quick guide
├── DEPLOY.md           # Deployment guide
├── PRE_DEPLOYMENT.md   # Pre-deploy checklist
└── [other config files]
```

## 🚀 Get Started in 30 Seconds

### Local Testing
```bash
# Windows
run.bat

# Mac/Linux
bash run.sh

# Then visit: http://localhost:8000
```

### Deploy to Cloud
1. Push to GitHub
2. Go to [render.com](https://render.com)
3. Connect repo
4. Deploy
5. Share your URL!

## 📞 Still Have Questions?

1. Check [README.md](README.md) for detailed docs
2. Check [DEPLOY.md](DEPLOY.md) for deployment help
3. Check [PRE_DEPLOYMENT.md](PRE_DEPLOYMENT.md) for checklist
4. See the code comments in `app/main.py` and `app/themes.py`

---

## 🎯 Recommended Order

**For Users:**
1. QUICK_START.md (copy-paste examples)
2. Test with your GitHub username
3. Deploy following DEPLOY.md

**For Developers:**
1. README.md (full understanding)
2. Local test with `run.bat`/`bash run.sh`
3. Read the code (`app/main.py`, `app/themes.py`)
4. Deploy with PRE_DEPLOYMENT.md checklist

**For Contributors:**
1. Read README.md
2. Read the code
3. Add new themes in `app/themes.py`
4. Submit PR

---

Start here: [QUICK_START.md](QUICK_START.md) →

---

Happy coding! 🚀
