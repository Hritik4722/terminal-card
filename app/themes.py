"""Color themes for terminal cards"""

THEMES = {
    "catppuccin": {
        "name": "Catppuccin",
        "bg": "#1e1e2e",
        "surface": "#2a2a3d",
        "muted": "#6c7086",
        "text": "#cdd6f4",
        "accent": "#cba6f7",
        "green": "#a6e3a1",
        "blue": "#89b4fa",
    },
    "dracula": {
        "name": "Dracula",
        "bg": "#282a36",
        "surface": "#44475a",
        "muted": "#6272a4",
        "text": "#f8f8f2",
        "accent": "#ff79c6",
        "green": "#50fa7b",
        "blue": "#8be9fd",
    },
    "github": {
        "name": "GitHub Light",
        "bg": "#ffffff",
        "surface": "#f6f8fa",
        "muted": "#57606a",
        "text": "#24292f",
        "accent": "#fd7e14",
        "green": "#1a7f37",
        "blue": "#0969da",
    },
    "nord": {
        "name": "Nord",
        "bg": "#2e3440",
        "surface": "#3b4252",
        "muted": "#4c566a",
        "text": "#eceff4",
        "accent": "#88c0d0",
        "green": "#a3be8c",
        "blue": "#81a1c1",
    },
}

def get_theme(theme_name: str = "catppuccin") -> dict:
    """Get theme by name, defaults to catppuccin"""
    return THEMES.get(theme_name.lower(), THEMES["catppuccin"])
