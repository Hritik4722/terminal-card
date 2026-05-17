# Quick Start (2 Minutes)

## The Absolute Simplest Way

### Step 1: Get Your Card URL

The live API is at: `https://terminal-card.onrender.com/api/terminal`

### Step 2: Build Your URL

Replace these in the URL:
- `YOUR_USERNAME` → your GitHub username
- `YOUR_TITLE` → your job title

```
https://terminal-card.onrender.com/api/terminal?username=YOUR_USERNAME&title=YOUR_TITLE
```

**Example:**
```
https://terminal-card.onrender.com/api/terminal?username=hritik4722&title=AI%20Engineer
```

### Step 3: Add to Your README.md

Copy this to your GitHub profile README:

```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=hritik4722&title=AI%20Engineer)](https://github.com/hritik4722)
```

### Step 4: Done! 🎉

Your README now has a terminal card. That's it.

---

## Common Customizations

### Change Theme

Add `&theme=dracula` or `&theme=github` to your URL:

```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=hritik4722&theme=dracula)](https://github.com/hritik4722)
```

### Hide GitHub Stats

Add `&stats=false`:

```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=hritik4722&stats=false)](https://github.com/hritik4722)
```

### Add Location & Status

Add `&location=CITY&status=YOUR_STATUS`:

```markdown
[![Terminal Card](https://terminal-card.onrender.com/api/terminal?username=hritik4722&location=San%20Francisco&status=open%20to%20work)](https://github.com/hritik4722)
```

---

## URL Space Encoding

GitHub's markdown auto-converts spaces. But if needed:
- Space = `%20`
- `&` = `%26`
- `/` = `%2F`

Most markdown renderers handle this automatically, so you usually don't need to worry.

---

## All Parameters

| Param | Example | Notes |
|-------|---------|-------|
| `username` | `hritik4722` | Required - your GitHub username |
| `title` | `Full%20Stack%20Developer` | Your job title (URL encoded) |
| `location` | `New%20York` | Your city/location |
| `focus` | `Building%20AI%20products` | What you're focusing on |
| `status` | `open%20to%20opportunities` | Current availability |
| `theme` | `catppuccin` or `dracula` or `github` | Color scheme |
| `stats` | `true` or `false` | Show GitHub stats |

---

## Troubleshooting

**Card shows error?**
- Double-check your GitHub username is spelled correctly
- The username is case-sensitive (use lowercase)

**Want to use a live instance?**
- You can deploy your own to Render/Railway for free
- See [DEPLOY.md](DEPLOY.md)

**Want more customization?**
- Use the interactive builder at `https://terminal-card.onrender.com`
- Or see [README.md](README.md) for advanced options

---

Done! Go update your README! 🚀
