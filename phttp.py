import http.client, json, calendar, os, time, base64
from datetime import datetime


app_token = "NDQ0NTAxMzc3NjU4NjUwNjUz.DfBrog.eg2yOzAb1bfIoYUEX6ETLOe1t3I"
channel_id = "430462706559090691"
web_hk = "api/webhooks/444503005740531714/1r7MT6IfPRwplxY3s3AW3PkwqlGgQltOQfZLA-UbBFLNafkrjDdXreKOt8PmogmPUKTo"
latest_timestamp = ""

def query_server():
    global app_token, channel_id, latest_timestamp

    response = 'Processing...'


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

        if(timestamp <= latest_timestamp) :
            break

        print(comment)

        if(comment['content'] == 'Go!') :

            print('parsing command')

            style_comment = conversation[i]
            if style_comment['attachments'] == [] :
                response = 'Missing style image'
                break

            content_comment = conversation[i + 1]
            if content_comment['attachments'] == []:
                response = 'Missing content image'
                break


            conn = http.client.HTTPSConnection("cdn.discordapp.com")
            current_time_int = str(int(time.mktime(datetime.utcnow().timetuple())))


            # download style image
            url = style_comment['attachments'][0]['url']
            img_path = url.split("https://cdn.discordapp.com")[1]

            t = url.split("/")
            style_img_filename = current_time_int + "-" + t[-1]

            conn.request("GET", img_path, "", headers)
            r1 = conn.getresponse().read()

            style_file = open(style_img_filename, "wb")
            style_file.write(base64.encodebytes(r1))
            style_file.close()
            os.chmod(style_img_filename, 0o777)

            # download content image
            url = content_comment['attachments'][0]['url']
            img_path = url.split("https://cdn.discordapp.com")[1]

            t = url.split("/")
            content_img_filename = current_time_int + "-" + t[-1]

            conn.request("GET", img_path, "", headers)
            r1 = conn.getresponse().read()

            content_file = open(content_img_filename, "wb")
            content_file.write(base64.encodebytes(r1))
            content_file.close()
            os.chmod(content_img_filename, 0o777)

            output_img_filename = current_time_int + "-output.jpg"


            cmd = "python neural_style.py --content {} --styles {} --output {} --width 500".format(content_img_filename, style_img_filename, output_img_filename)

            print(cmd)
            os.system(cmd)

            break

    print(response)

query_server()
