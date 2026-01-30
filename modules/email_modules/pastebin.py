"""
Robust Pastebin email detection
Community-maintained version
"""

import re
from lib.requests import Requests

DUCKDUCKGO = "https://duckduckgo.com/html/?q={query}"

# Pastes conocidos / recientes (se puede ampliar)
KNOWN_PASTES = [
    "d2UfiSPy"
]


async def fetch_raw(paste_id: str) -> str | None:
    url = f"https://pastebin.com/raw/{paste_id}"
    try:
        r = await Requests(url).get()
        if r.status_code == 200:
            return r.text
    except Exception:
        pass
    return None


async def pastebin(email: str) -> list:
    found = []

    # ---------
    # 1️⃣ Modo directo (pastes conocidos)
    # ---------
    for pid in KNOWN_PASTES:
        data = await fetch_raw(pid)
        if data and email.lower() in data.lower():
            found.append(f"https://pastebin.com/raw/{pid}")

    # ---------
    # 2️⃣ Modo pasivo (DuckDuckGo)
    # ---------
    query = f'site:pastebin.com "{email}"'
    search_url = DUCKDUCKGO.format(query=query.replace(" ", "+"))

    try:
        r = await Requests(search_url).get()
        html = r.text

        links = set(
            re.findall(r'https://pastebin\.com/([A-Za-z0-9]+)', html)
        )

        for pid in links:
            raw = await fetch_raw(pid)
            if raw and email.lower() in raw.lower():
                found.append(f"https://pastebin.com/raw/{pid}")

    except Exception:
        pass

    return list(set(found))
