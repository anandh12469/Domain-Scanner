import requests
import json
def scandomain(type, domain):
    url = "https://relicflare.p.rapidapi.com/"+ type

    payload = "{\n    \"url\": \""+ domain + "\"\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "f0d2385e03mshe2fe053832db1c8p1eac73jsn83677050dff0",
        'x-rapidapi-host': "relicflare.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(json.loads(response.text))

domain = input("Enter the domain you want to scan: ")
print("Enter the type of scan")
print("1. Time to First Byte \n"
        "2. Dns Record \n"
        "3. Loadtime\n"
        "4. HTTP-Protocol\n"
        "5. Is Site Up\n"
        "6. HTTP Header")
a = int(input("Enter the option number: "))
b = "ttfb"
c = "dnsrecord"
d = "loadtime"
e = "httpprotocol"
f = "up"
g = "httpheader"
if a == 1:
    scandomain(b, domain)
elif a == 2:
    scandomain(c, domain)
elif a == 3:
    scandomain(d, domain)
elif a == 4:
    scandomain(e, domain)
elif a == 5:
    scandomain(f, domain)
elif a == 6:
    scandomain(g, domain)
