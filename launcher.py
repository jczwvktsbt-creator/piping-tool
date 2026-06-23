"""
=============================================================
  EDIT THIS FILE BEFORE RUNNING build.py
  Add your team's Windows usernames to ALLOWED_USERS below
=============================================================
  To find someone's Windows username:
  Ask them to open Command Prompt and type:  whoami
  It shows:  DOMAIN\john.smith  → add "john.smith"
=============================================================
"""

import os, sys, webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

# ══════════════════════════════════════════════════════════════
#  AUTHORISED USERS — Edit this list to control who can access
#  Use lowercase Windows usernames (the part after the \ in whoami)
# ══════════════════════════════════════════════════════════════
ALLOWED_USERS = [
    "admin",
    "engineer1",
    "engineer2",
    "reviewer",
    # Add your team below — one username per line:
    # "firstname.lastname",
    # "john.smith",
    # "ahmed.ali",
]
# ══════════════════════════════════════════════════════════════

# Locate HTML file next to the exe
if getattr(sys, "frozen", False):
    BASE = Path(sys.executable).parent
else:
    BASE = Path(__file__).parent

HTML_FILE = BASE / "piping_loading_tool.html"

def get_username():
    return os.environ.get("USERNAME", "").strip().lower()

def show_denied(username):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror(
        "Access Denied",
        f"Access Denied\n\n"
        f"User '{username}' is not authorised to use this tool.\n\n"
        f"Please contact your administrator to request access."
    )
    root.destroy()

def show_error(msg):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror("Error", msg)
    root.destroy()

def main():
    username = get_username()

    if username not in ALLOWED_USERS:
        show_denied(username or "(unknown)")
        sys.exit(1)

    if not HTML_FILE.exists():
        show_error(
            f"Tool file not found:\n{HTML_FILE}\n\n"
            f"Make sure 'piping_loading_tool.html' is in the same folder as this .exe."
        )
        sys.exit(1)

    webbrowser.open(HTML_FILE.as_uri())

if __name__ == "__main__":
    main()
