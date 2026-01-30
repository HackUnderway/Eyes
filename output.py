from modules.email_modules import duolingo, gravatar, imgur, protonmail, bitmoji, x, github, mailru, pastebin, ig, hudsonrock, xposedornot
from lib.text import WHITE, CYAN
from lib.maileye import decomp, regex_check


async def eyes_output(email):
    past = 0

    print("#" * 15 + CYAN + email + WHITE + "#" * 15 + "\n")

    regex_check(email)

    name, domain = decomp(email)
    print(f"-🙋 Name : {name}")
    print(f"-🔎 Domain : {domain}\n")

    # -------- Services --------
    print(await protonmail.protonmail(email))
    print(await mailru.mailru(email))
    print(await duolingo.duolingo(email))
    print(await gravatar.gravatar(email))
    print(await imgur.imgur(email))
    print(await bitmoji.bitmoji(email))
    print(await x.x(email))
    await github.github(email)
    await ig.instagram(email)

    # -------- Pastebin --------
    print("[~] Paste :")
    for paste in await pastebin.pastebin(email):
        past += 1
        print("    ├── " + paste.replace("/raw", ""))
    if past == 0:
        print("[-] No paste found.")

    # -------- HudsonRock --------
    hr = await hudsonrock.hudsonrock(email)

    if hr:
        print(f"\n[{CYAN}HudsonRock{WHITE}] Email's result :")
        print("> Total service corporate :", hr["total_corporate"])
        print("> Total user services :", hr["total_user"])
        print("> Date compromised :", hr["date"])
        print("> Computer name :", hr["computer"])
        print("> Operating system :", hr["os"])
        print("> Ip address :", hr["ip"])

        if hr["passwords"]:
            print("> Top passwords :", ", ".join(hr["passwords"]))
        else:
            print("> Top passwords : /")

        if hr["logins"]:
            print("> Top logins :", ", ".join(hr["logins"]))
        else:
            print("> Top logins : /")
    else:
        print("\n❌ HudsonRock")

    # -------- XposedOrNot --------
    breaches = await xposedornot.xposedornot(email)

    print()

    if not breaches:
        print("✅ No se encontraron brechas conocidas para este correo")
    else:
        print(f"[{CYAN}XposedOrNot{WHITE}] Breaches found :")
        for b in breaches:
            print(f"> {b['site']} ({b['year']})")
