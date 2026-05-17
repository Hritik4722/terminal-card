from fastapi import FastAPI, Query
from fastapi.responses import Response, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import httpx
import os
import pathlib

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
                lang_count = {}
                for repo in repos:
                    lang = repo.get("language")
                    if lang:
                        lang_count[lang] = lang_count.get(lang, 0) + 1
                if lang_count:
                    result["top_lang"] = max(lang_count, key=lang_count.get)

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


def build_svg(p: dict) -> str:
    username   = esc(p["username"])
    name       = esc(trunc(p["name"], 40))
    title      = esc(trunc(p["title"], 30))
    location   = esc(trunc(p["location"], 20))
    focus      = esc(trunc(p["focus"], 56))
    status     = esc(trunc(p["status"], 50))
    cmd1       = esc(p["cmd1"])
    cmd2       = esc(p["cmd2"])
    cmd3       = esc(p["cmd3"])
    cmd4       = esc(p["cmd4"])
    out1       = esc(trunc(p["out1"], 56))
    out2       = esc(trunc(p["out2"], 56))
    out3       = esc(trunc(p["out3"], 56))
    out4       = esc(trunc(p["out4"], 56))
    commits    = esc(p["commits"])
    top_lang   = esc(p["top_lang"])
    show_stats = p["show_stats"]

    height = 370 if show_stats else 320

    stats_block = ""
    if show_stats:
        stats_block = f"""
  <text x="28" y="231" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#6c7086">❯</text>
  <text x="44" y="231" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#cdd6f4" font-weight="500">{cmd3}</text>
  <text x="44" y="254" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#a6adc8">commits: <tspan fill="#a6e3a1">{commits}</tspan>   top_lang: <tspan fill="#89b4fa">{top_lang}</tspan></text>

  <text x="28" y="284" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#6c7086">❯</text>
  <text x="44" y="284" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#cdd6f4" font-weight="500">{cmd4}</text>
  <text x="44" y="307" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#a6e3a1">→ {status}</text>

  <text x="28" y="337" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#6c7086">❯</text>
  <rect x="44" y="324" width="8" height="15" fill="#cdd6f4" opacity="0.9">
    <animate attributeName="opacity" values="0.9;0;0.9" dur="1.2s" repeatCount="indefinite"/>
  </rect>"""
    else:
        stats_block = f"""
  <text x="28" y="231" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#6c7086">❯</text>
  <text x="44" y="231" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#cdd6f4" font-weight="500">{cmd3}</text>
  <text x="44" y="254" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#a6e3a1">→ {status}</text>

  <text x="28" y="284" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#6c7086">❯</text>
  <rect x="44" y="271" width="8" height="15" fill="#cdd6f4" opacity="0.9">
    <animate attributeName="opacity" values="0.9;0;0.9" dur="1.2s" repeatCount="indefinite"/>
  </rect>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="680" height="{height}" viewBox="0 0 680 {height}">
  <rect width="680" height="{height}" rx="12" ry="12" fill="#1e1e2e"/>
  <rect width="680" height="38" rx="12" ry="12" fill="#2a2a3d"/>
  <rect y="12" width="680" height="26" fill="#2a2a3d"/>

  <circle cx="22" cy="19" r="6" fill="#ff5f57"/>
  <circle cx="42" cy="19" r="6" fill="#febc2e"/>
  <circle cx="62" cy="19" r="6" fill="#28c840"/>
  <text x="340" y="24" text-anchor="middle" font-family="'Fira Code', 'Courier New', monospace" font-size="12" fill="#888aaa">{username}@dev ~ profile.sh</text>

  <text x="28" y="72" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#6c7086">❯</text>
  <text x="44" y="72" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#cdd6f4" font-weight="500">{cmd1}</text>
  <text x="44" y="95" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#a6adc8">{name} — {title}, {location}</text>

  <text x="28" y="125" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#6c7086">❯</text>
  <text x="44" y="125" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#cdd6f4" font-weight="500">{cmd2}</text>
  <text x="44" y="148" font-family="'Fira Code', 'Courier New', monospace" font-size="13" fill="#a6adc8">{focus}</text>
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
):
    gh = await fetch_github(username)

    params = {
        "username":   username,
        "name":       name       or gh["name"]     or username,
        "title":      title      or "Developer",
        "location":   location   or "",
        "focus":      focus      or gh["bio"]      or "Building cool things",
        "status":     status,
        "cmd1":       cmd1,
        "cmd2":       cmd2,
        "cmd3":       cmd3,
        "cmd4":       cmd4,
        "out1":       out1,
        "out2":       out2,
        "out3":       out3,
        "out4":       out4,
        "commits":    gh["commits"]  or "—",
        "top_lang":   gh["top_lang"] or "—",
        "show_stats": stats,
    }

    svg = build_svg(params)
    return Response(content=svg, media_type="image/svg+xml", headers={
        "Cache-Control": "max-age=1800, s-maxage=1800",
        "Access-Control-Allow-Origin": "*",
    })


@app.get("/", response_class=HTMLResponse)
async def builder():
    html_path = BASE_DIR / "public" / "index.html"
    return HTMLResponse(content=html_path.read_text())