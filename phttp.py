import http.client, json
app_token = "NDQ0NTAxMzc3NjU4NjUwNjUz.DeOtQA.kvh4om4oBfHQjcRUZOVhH5fc4Ps"
channel_id = "430462706559090691"
web_hk = "api/webhooks/444503005740531714/1r7MT6IfPRwplxY3s3AW3PkwqlGgQltOQfZLA-UbBFLNafkrjDdXreKOt8PmogmPUKTo"
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
