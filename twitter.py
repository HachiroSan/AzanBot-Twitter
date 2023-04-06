import tweepy
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class Tweety:
    """Establish connection to twitter account based on configuration file keys"""

    def __init__(self):
        self.authenticate()

    def authenticate(self):
        # Authenticate to Twitter
        auth = tweepy.OAuth1UserHandler(
            API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
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

    def post_tweet(self, text):
        try:
            self.api.update_status(text)
            return True
        except tweepy.TweepError as e:
            print(f"Error posting tweet: {e}")
            return False
