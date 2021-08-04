import tweepy
from configparser import ConfigParser
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# instantiate
config = ConfigParser()
config.read("config.ini")

consumer_key = config.get('configuration', 'API_KEY')
consumer_secret = config.get('configuration', 'API_SECRET_KEY')
access_token_key = config.get('configuration', 'ACCESS_TOKEN_KEY')
access_token_secret = config.get('configuration', 'ACCESS_TOKEN_SECRET')
zone_code = config.get('timezone', 'ZONE')

# # authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# # set access to user's access key and access secret 
auth.set_access_token(access_token_key, access_token_secret)
  
# # calling the api 
api = tweepy.API(auth)
  
# # posting the tweet
# api.update_status("Skynet tookover!")