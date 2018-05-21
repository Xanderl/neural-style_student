import http.client, json
app_token = "NDI4NjEzOTAzOTY3MzIyMTEy.DeBn-Q.z_BgHph0_UoG8iglTEfpdhknzgI"
channel_id = "423897351422214146"
web_hk = "api/webhooks/447095306841227264/M77Jr-7jT4bIwHEToxNOw1HXzBe4q8-ZOdao6QHZw5ExbhYiVpu8fVKyZVz-Bc4UOQWZ"
latest_timestamp = ""

def query_server():
    global app_token, channel_id, latest_timestamp


    conn = http.client.HTTPSConnection("discordapp.com")
    headers = {"authorization": "Bot " + app_token }
    conn.request("GET", "/api/channels/" + channel_id +"/messages", "", headers)
    r1 = conn.getresponse()

    status = r1.reason
    print(status)

    r = r1.read()
    print(r)
    conversation = json.loads(r.decode('utf-8'))

#    print(json.dumps(conversation, indent=4, sort_keys=True))

    i = 0
    while i < len(conversation) :
        comment = conversation[i]
        i += 1

        timestamp = comment["timestamp"]

        if(timestamp < latest_timestamp) :
            break

        if comment['attachments'] == []:
            print("no attachments")
        else:
            print(comment['attachments'])

    latest_timestamp = conversation[0]["timestamp"]

print(latest_timestamp)
query_server()
print(latest_timestamp)
