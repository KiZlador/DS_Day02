import requests
import os

has_header = True
num_of_steps = 0
counts = 0
tails = 0
heads = 0
tails_prob = 0
heads_prob = 0
counts_rand = 0
tails_rand = 0
heads_rand = 0

text = """
Report

We have made {counts} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads. The probabilities are {tails_prob}% and {heads_prob}%, respectively. Our forecast is that in the next {counts_rand} observations we will have: {tails_rand} tails and {heads_rand} heads.'
"""

LOG_FILE = "analytics.log"
LOG_FORMAT = "%(asctime)s %(message)s"
celog = False

TELEGRAM_BOT_TOKEN = "TELEGRAM_BOT_TOKEN"

TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
response = requests.get(TELEGRAM_URL).json()

TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
if response["ok"]:
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]

TELEGRAM_CHAT_ID = chat_id
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
success = "The report has been successfully created"
failure = "The report hasn’t been created due to an error"

#@Sh21LogBot