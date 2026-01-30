import aiohttp
from lib.text import WHITE, CYAN


API = "https://api.xposedornot.com/v1/breach-analytics"


async def xposedornot(email: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(API, params={"email": email}) as resp:
            if resp.status != 200:
                return []

            try:
                data = await resp.json()
            except Exception:
                return []

    exposed = data.get("ExposedBreaches")

    # 🔴 Caso: la API devuelve null
    if not exposed:
        return []

    details = exposed.get("breaches_details", [])
    if not details:
        return []

    breaches = []
    for breach in details:
        name = breach.get("breach")
        year = breach.get("xposed_date")

        if name and year:
            breaches.append({
                "site": name,
                "year": year
            })

    return breaches
