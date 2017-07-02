import tweepy
import os

with open(os.path.join(os.path.dirname(__file__), '../api_keys/twitter_keys'), 'r') as f:
    keys = f.readlines()
keys = [key.strip() for key in keys]

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_TOKEN = keys[2]
ACCESS_TOKEN_SECRET = keys[3]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def load_api():
    return api
