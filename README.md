# Terminal Card

Generate terminal-style SVG cards for your GitHub README. Perfect for showcasing your profile in style!

![Example](https://terminal-card.onrender.com/api/terminal?username=hritik4722&theme=catppuccin&stats=true)

LINK : https://terminal-card.onrender.com — use the hosted API to generate cards without running anything locally.

## Features

✨ **Beautiful Terminal Styling** - Modern, customizable terminal-like SVG cards  
🎨 **Multiple Themes** - Catppuccin, Dracula, Nord, GitHub Light  
📊 **GitHub Integration** - Auto-fetch commits, top language, and profile info  
🚀 **Simple API** - Generate cards with just a URL  
📱 **Responsive** - Works in README.md and anywhere you embed SVG  

## Usage

### 1. Quick Start (Copy-Paste)

Add this to your `README.md`:

```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=YOUR_USERNAME)](https://github.com/YOUR_USERNAME)
```

Replace `YOUR_USERNAME` with your actual GitHub username. Done!

### 2. Customize Your Card

**Change Theme:**
```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=YOUR_USERNAME&theme=dracula)](https://github.com/YOUR_USERNAME)
```

Available themes: `catppuccin`, `dracula`, `nord`, `github`

**Add Custom Details:**
```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=YOUR_USERNAME&title=Full%20Stack%20Developer&location=San%20Francisco&status=open%20to%20work)](https://github.com/YOUR_USERNAME)
```

**Change Commands:**
```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=YOUR_USERNAME&cmd1=python%20--version&cmd2=npm%20run%20build)](https://github.com/YOUR_USERNAME)
```

### 3. API Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `username` | hritik4722 | GitHub username |
| `theme` | catppuccin | Color theme: `catppuccin`, `dracula`, `nord`, `github` |
| `name` | (auto-fetched) | Display name |
| `title` | Developer | Your title/role |
| `location` | (empty) | Your location |
| `focus` | (auto-fetched from bio) | What you're focusing on |
| `status` | open to interesting problems | Current status |
| `cmd1` | whoami | First command |
| `cmd2` | cat current_focus.txt | Second command |
| `cmd3` | cat stats.json | Third command |
| `cmd4` | echo $STATUS | Fourth command |
| `stats` | true | Show GitHub stats (commits + top language) |

### 4. URL Encoding

Space becomes `%20`, other special characters need encoding:

```
Location: San Francisco  →  Location%3A%20San%20Francisco
Status: Open & available  →  Status%3A%20Open%20%26%20available
```

Most markdown renderers handle this automatically.

## Examples

### Example 1: Minimalist (just username)
```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=hritik4722)](https://github.com/hritik4722)
```

### Example 2: Full Custom
```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=hritik4722&theme=dracula&title=ML%20Engineer&location=India&focus=Building%20AI%20products&status=shipping%20fast&stats=true)](https://github.com/hritik4722)
```

### Example 3: GitHub Light Theme (no stats)
```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=octocat&theme=github&stats=false)](https://github.com/octocat)
```

## Themes

### Catppuccin (Default)
Dark theme with purple accents. Great for modern profiles.

### Dracula
Dark theme with pink accents. Bold and vibrant.

### Nord
Dark theme with cool blue accents. Calm and professional.

### GitHub Light
Light theme. Perfect if your README has a light background.

## Local Development

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/hritik4722/terminal-card.git
cd terminal-card
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy environment file:
```bash
cp .env.example .env
```

5. Run the server:
```bash
uvicorn app.main:app --reload
```

The server will start at `http://localhost:8000`

### Access the Web UI

Visit `http://localhost:8000` to use the interactive builder.

## Deployment

### Deploy to Render (Recommended)

1. Fork this repository on GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" and select "Web Service"
4. Connect your GitHub repo
5. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0`
   - **Environment:** Add `GITHUB_TOKEN` (optional, for higher rate limits)
6. Deploy!

### Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click "Start New Project"
3. Connect GitHub repo
4. It auto-detects Python and runs. Done!

### Deploy to Vercel

Not recommended (requires serverless architecture changes), but you can use the API endpoint on any of the above platforms.

## API Endpoint

**Endpoint:** `GET /api/terminal`

**Returns:** SVG image

**Example:**
```
https://terminal-card.onrender.com/api/terminal?username=hritik4722&theme=dracula
```

## Interactive Builder

Visit the live instance at `https://terminal-card.onrender.com` to use the interactive UI builder.

## Project Structure

```
terminal-card/
├── app/
│   ├── main.py         # FastAPI server
│   └── themes.py       # Color themes
├── public/
│   └── index.html      # Web UI
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
└── README.md           # This file
```

## FAQ

**Q: Does it work without GitHub username?**  
A: Yes, but auto-fetched data (name, bio, commits, top language) won't be available.

**Q: Can I use my own domain?**  
A: Yes! Deploy to your own server using the same code.

**Q: Can I customize colors?**  
A: Currently supports 3 built-in themes. Custom colors coming soon!

**Q: Is there a rate limit?**  
A: No hard limits currently. Be reasonable with requests.

**Q: Can I self-host?**  
A: Absolutely! Just follow the local development setup and deploy to any Python-capable hosting.

## Contributing

Found a bug or want a feature? Open an issue or PR!

## License

MIT License - feel free to use this for anything!

## Support

Need help? Open an issue on GitHub or reach out!
