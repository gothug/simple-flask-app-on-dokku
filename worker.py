import httplib
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

def send_sample_email():
    basepath = "/api/1.0"

    send_email_json = {
        "key" : "BAXsOmtwxAELZKVQWohlzQ",
        "message" : {
            "html" : "<p>Example HTML content</p>",
            "text" : "Example text content",
            "subject" : "example subject",
            "from_email" : "kojuhovskiy@gmail.com",
            "from_name" : "Example Name",
            "to" : [
                {
                    "email" : "kojuhovskiy@gmail.com",
                    "name" : "Vasek",
                    "type" : "to"
                }
            ],
            "headers" : {
                "Reply-To" : "kojuhovskiy@gmail.com"
            },
        }
    }

    conn = httplib.HTTPSConnection("mandrillapp.com")

    ####
    json_str = json.dumps(send_email_json)
    conn.request("POST", basepath + "/messages/send.json", json_str)
    res = conn.getresponse().read()
    print res

print "Worker running.."
print "Sending email.."

send_sample_email()

# res_json = json.loads(res)
# send_id = str(res_json[0]['_id'])

# ####
# get_email_status_json = {
#     "key" : "BAXsOmtwxAELZKVQWohlzQ",
#     "id" : send_id
# }
# json_str = json.dumps(get_email_status_json)
# conn.request("POST", basepath + "/messages/info.json", json_str)
# res = conn.getresponse().read()
# print res

# ####
# email_search_json = {
#     "key" : "BAXsOmtwxAELZKVQWohlzQ",
#     "date_from": "2013-01-15",
#     "date_to": "2013-01-15",
# }
# json_str = json.dumps(email_search_json)
# conn.request("POST", basepath + "/messages/search.json", json_str)
# res = conn.getresponse().read()
# print res
