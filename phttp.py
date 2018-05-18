import http.client, json


conn = http.client.HTTPSConnection("discordapp.com")
headers = {"authorization": "Bot MzEyNjQzMTMyNzA3NTY5NjY1.C_eEfQ.8DVBHgDEV3BQu98HtsxwHdNFp8w"}
conn.request("GET", "/api/channels/312640514405171200/messages", "", headers)
r1 = conn.getresponse()

status = r1.reason
print(status)

r = r1.read().decode('utf-8')
conversation = json.loads(r)

print(conversation[0]["timestamp"])

