from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import csv
import random
import time
api_id = ########
api_hash = '###########################'
phone = '#########'

SLEEP_TIME = 30
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

input_file = sys.argv[1] #takes a csv file passed along with this code
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

mode = int(input("Enter 1 to send by user ID or 2 to send by username: "))

messages= ["Hi {}, Are you looking to travel/study abroad? Are you abroad and searching for JOB opportunities or looking to settle in the new environment? Or are you a travel agency trying to connect with scholars or tourists in need of your services? \n\nI found this really great app that helps you connect with Professional bodies and International Student Advisors. \n\nConnectExpat \nYou can connect with Businesses in USA, Canada, UK and other countries for free. \nCheck it Out! \niOS: https://apps.apple.com/us/app/connectexpat/id1565493401 \nAndroid: https://play.google.com/store/apps/details?id=com.connectexpat \n\nDownload and register."]

for user in users:
    if mode == 2:
        if user['username'] == "":
            continue
        receiver = client.get_input_entity(user['username'])
    elif mode == 1:
        receiver = InputPeerUser(user['id'],user['access_hash'])
    else:
        print("Invalid Mode. Exiting.")
        client.disconnect()
        sys.exit()
    message = random.choice(messages)
    try:
        print("Sending Message to:", user['name'])
        client.send_message(receiver, message.format(user['name']))
        print("Waiting {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        client.disconnect()
        sys.exit()
    except Exception as e:
        print("Error:", e)
        print("Trying to continue...")
        continue
client.disconnect()
print("Done. Message sent to all users.")
