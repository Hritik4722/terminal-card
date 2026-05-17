from fastapi import FastAPI, Query
from fastapi.responses import Response, HTMLResponse
from fastapi.staticfiles import StaticFiles
import httpx
import os
import pathlib
from app.themes import get_theme

app = FastAPI(title="Terminal Card API")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
BASE_DIR = pathlib.Path(__file__).parent.parent


async def fetch_github(username: str) -> dict:
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    result = {"name": None, "bio": None, "top_lang": None, "commits": None}
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(f"https://api.github.com/users/{username}", headers=headers)
            if r.status_code == 200:
                data = r.json()
                result["name"] = data.get("name")
                result["bio"] = data.get("bio", "")[:50] if data.get("bio") else None

            r2 = await client.get(
                f"https://api.github.com/users/{username}/repos?per_page=100&sort=pushed",
                headers=headers
            )
            if r2.status_code == 200:
                repos = r2.json()
                # Prefer accurate byte counts via the languages API for each repo
                lang_bytes = {}
                for repo in repos:
                    # attempt to use the languages_url provided by the repo
                    lang_url = repo.get("languages_url")
                    if lang_url:
                        try:
                            rl = await client.get(lang_url, headers=headers)
                            if rl.status_code == 200:
                                langs = rl.json()
                                for lname, bytes_count in langs.items():
                                    lang_bytes[lname] = lang_bytes.get(lname, 0) + int(bytes_count or 0)
                        except Exception:
                            # ignore per-repo language fetch errors
                            continue
                    else:
                        # fallback to the repo 'language' field (may be None)
                        lang = repo.get("language")
                        if lang:
                            lang_bytes[lang] = lang_bytes.get(lang, 0) + 1

                if lang_bytes:
                    # choose the language with the highest total bytes
                    result["top_lang"] = max(lang_bytes, key=lang_bytes.get)

            r3 = await client.get(
                f"https://api.github.com/search/commits?q=author:{username}&per_page=1",
                headers={**headers, "Accept": "application/vnd.github.cloak-preview"}
            )
            if r3.status_code == 200:
                result["commits"] = str(r3.json().get("total_count", ""))
    except Exception:
        pass
    return result


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def trunc(s: str, n: int) -> str:
    return s[:n] + ("…" if len(s) > n else "")


def build_svg(p: dict, theme_colors: dict) -> str:
        username = esc(p["username"])
        name = esc(trunc(p["name"], 40))
        title = esc(trunc(p["title"], 30))
        location = esc(trunc(p["location"], 20))

        cmd1 = esc(p.get("cmd1", ""))
        cmd2 = esc(p.get("cmd2", ""))
        cmd3 = esc(p.get("cmd3", ""))
        cmd4 = esc(p.get("cmd4", ""))

        out1 = esc(trunc(p.get("out1", ""), 56))
        out2 = esc(trunc(p.get("out2", ""), 56))
        out3 = esc(trunc(p.get("out3", ""), 56))
        out4 = esc(trunc(p.get("out4", ""), 56))

        show_stats = p.get("show_stats", True)

        # theme colors
        bg = theme_colors["bg"]
        surface = theme_colors["surface"]
        muted = theme_colors["muted"]
        text = theme_colors["text"]
        green = theme_colors["green"]
        blue = theme_colors["blue"]
        accent = theme_colors["accent"]

        height = 310 if show_stats else 270

        stats_block = ""
        if show_stats:
                stats_block = f"""
    <text x="28" y="171" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{muted}">❯</text>
    <text x="44" y="171" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{accent}" font-weight="500">{cmd3}</text>
    <text x="44" y="194" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{text}">{out3}</text>

    <text x="28" y="224" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{muted}">❯</text>
    <text x="44" y="224" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{accent}" font-weight="500">{cmd4}</text>
    <text x="44" y="247" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{text}">{out4}</text>

    <text x="28" y="277" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{muted}">❯</text>
    <rect x="44" y="264" width="8" height="15" fill="{text}" opacity="0.9">
        <animate attributeName="opacity" values="0.9;0;0.9" dur="1.2s" repeatCount="indefinite"/>
    </rect>"""
        else:
                stats_block = f"""
    <text x="28" y="171" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{muted}">❯</text>
    <text x="44" y="171" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{accent}" font-weight="500">{cmd3}</text>
    <text x="44" y="194" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{text}">{out3}</text>

    <text x="28" y="224" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{muted}">❯</text>
    <rect x="44" y="211" width="8" height="15" fill="{text}" opacity="0.9">
        <animate attributeName="opacity" values="0.9;0;0.9" dur="1.2s" repeatCount="indefinite"/>
    </rect>"""

        return f"""<svg xmlns="http://www.w3.org/2000/svg" width="680" height="{height}" viewBox="0 0 680 {height}">
    <rect width="680" height="{height}" rx="12" ry="12" fill="{bg}"/>
    <rect width="680" height="38" rx="12" ry="12" fill="{surface}"/>
    <rect y="12" width="680" height="26" fill="{surface}"/>

    <circle cx="22" cy="19" r="6" fill="#ff5f57"/>
    <circle cx="42" cy="19" r="6" fill="#febc2e"/>
    <circle cx="62" cy="19" r="6" fill="#28c840"/>
    <text x="340" y="24" text-anchor="middle" font-family="'Fira Code', 'Courier New', monospace" font-size="12" fill="{muted}">{username}@dev ~ profile.sh</text>

    <text x="28" y="72" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{muted}">❯</text>
    <text x="44" y="72" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{accent}" font-weight="500">{cmd1}</text>
    <text x="44" y="95" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{text}">{name} — {title}, {location}</text>

    <text x="28" y="125" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{muted}">❯</text>
    <text x="44" y="125" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{accent}" font-weight="500">{cmd2}</text>
        <text x="44" y="148" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="{text}">{out2}</text>
    {stats_block}
</svg>"""


@app.get("/api/terminal")
async def terminal(
    username: str  = Query(default="hritik4722"),
    name:     str  = Query(default=""),
    title:    str  = Query(default=""),
    location: str  = Query(default=""),
    focus:    str  = Query(default=""),
    status:   str  = Query(default="open to interesting problems"),
    cmd1:     str  = Query(default="whoami"),
    cmd2:     str  = Query(default="cat current_focus.txt"),
    cmd3:     str  = Query(default="cat stats.json"),
    cmd4:     str  = Query(default="echo $STATUS"),
    out1:     str  = Query(default=""),
    out2:     str  = Query(default=""),
    out3:     str  = Query(default=""),
    out4:     str  = Query(default=""),
    stats:    bool = Query(default=True),
    theme:    str  = Query(default="catppuccin"),
):
    gh = await fetch_github(username)
    theme_colors = get_theme(theme)

    params = {
        "username":   username,
        "name":       name       or gh["name"]     or username,
        "title":      title      or "Developer",
        "location":   location   or "",
        # out2/out3/out4 are user-provided outputs for commands 2-4
        "cmd1":       cmd1,
        "cmd2":       cmd2,
        "cmd3":       cmd3,
        "cmd4":       cmd4,
        "out1":       out1,
        "out2":       out2,
        "out3":       out3,
        "out4":       out4,
        
        "show_stats": stats,
    }

    svg = build_svg(params, theme_colors)
    return Response(content=svg, media_type="image/svg+xml", headers={
        "Cache-Control": "max-age=1800, s-maxage=1800",
        "Access-Control-Allow-Origin": "*",
    })


@app.get("/api/themes")
async def themes_list():
    """List available themes"""
    from app.themes import THEMES
    return {"themes": {k: v["name"] for k, v in THEMES.items()}}


@app.get("/", response_class=HTMLResponse)
async def builder():
    html_path = BASE_DIR / "public" / "index.html"
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))
