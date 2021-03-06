import requests
import config as cfg

def send_complex_message(**fields):
    to = fields['payer_email']
    ebayID = fields['auction_buyer_id']
    name = fields['first_name']
    return requests.post(cfg.mailgun['url'],
        auth = ("api",cfg.mailgun['key']),
        data = {"from": "YOUR NAME <email@example.com>",
              "to": to,
              "cc": "customer_email@example.com",
              "subject": cfg.mailgun['msg'] + ebayID,
              "html": "Hi " + name  + cfg.messages['INFO']})

if __name__ == "__main__":
    send_complex_message()
