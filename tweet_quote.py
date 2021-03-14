import os 
import json
import random
import twitter
from dotenv import load_dotenv

# Load up the env vars
load_dotenv()

# Generate a twitter client
api = twitter.Api(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token_key=os.getenv("ACCESS_TOKEN_KEY"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

# Load the quotes and select a random one that is less than 280 chars long.
with open("./quotes.json", "r") as f:
    quotes = json.load(f)

selected_quote = None
while selected_quote is None or len(selected_quote) > 280:
    selected_quote = random.choice(quotes)["text"]

# Tweet that shit
status = api.PostUpdate(selected_quote)
