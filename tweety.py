import tweepy
import configparser

# Read the INI file
config = configparser.ConfigParser()
config.read("config.ini")

# Replace with INI file keys
consumer_key = config["configuration"]["API_KEY"]
consumer_secret = config["configuration"]["API_SECRET_KEY"]
access_token = config["configuration"]["ACCESS_TOKEN_KEY"]
access_token_secret = config["configuration"]["ACCESS_TOKEN_SECRET"]


class Tweety:
    """Establish connection to twitter account based on configuration file keys"""

    def __init__(self):
        self.authenticate()

    def authenticate(self):
        # Authenticate to Twitter
        auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
        self.api = tweepy.API(auth)
        self.me = self.api.verify_credentials()
        self.get_username()



    def get_username(self):
        return self.me.screen_name

    def get_favourites_count(self):
        return str(self.me.favourites_count)

    def get_followers_count(self):
        return str(self.me.followers_count)

    def get_bio(self):
        return str(self.me.description)

    def get_id(self):
        return str(self.me.id)

    def get_location(self):
        return str(self.me.location)

    def get_status_count(self):
        return str(self.me.statuses_count)
