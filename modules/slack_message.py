import json

def build_slack_message(http_status, animal, site_url):
    if animal == "cat":
        image_url = "https://http.cat/{0}.jpg".format(http_status)
    if animal == "dog":
        image_url = "https://httpstatusdogs.com/img/{0}.jpg".format(http_status)

    slackMessage = {
        "response_type": "in_channel",
        "attachments": [{
            "title": "Status for: {0}".format(site_url),
            "color": "#3AA3E3",
            "attachment_type": "default",
            "image_url": image_url
        }]
    }

    return slackMessage