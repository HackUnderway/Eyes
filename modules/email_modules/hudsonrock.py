from lib.requests import Requests
from datetime import datetime

API = "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email"


async def hudsonrock(email: str):
    try:
        r = await Requests(API, params={"email": email}).get()

        if r.status_code != 200:
            return None

        data = r.json()
        stealers = data.get("stealers", [])

        if not stealers:
            return None

        s = stealers[0]

        # Convert date
        date_iso = s.get("date_compromised")
        if date_iso:
            dt = datetime.fromisoformat(date_iso.replace("Z", "+00:00"))
            date = dt.strftime("%Y-%m-%d %H:%M:%S")
        else:
            date = "/"

        return {
            "total_corporate": s.get("total_corporate_services", "/"),
            "total_user": s.get("total_user_services", "/"),
            "date": date,
            "computer": s.get("computer_name", "/"),
            "os": s.get("operating_system", "/"),
            "ip": s.get("ip", "/"),
            "passwords": s.get("top_passwords", []),
            "logins": s.get("top_logins", [])
        }

    except Exception:
        return None
