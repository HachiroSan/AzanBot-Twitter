from requests_oauthlib import OAuth1Session
import os
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class TwitterPoster:
    def __init__(self):
        self._consumer_key = API_KEY
        self._consumer_secret = API_SECRET_KEY
        self.authenticator = TwitterAuthenticator(
            self._consumer_key, self._consumer_secret
        )
        self.auth = self.authenticator.get_authentication_session()

    def post_tweet(self, tweet_text):
        payload = {"text": tweet_text}

        # Making the request
        response = self.auth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                f"Request returned an error: {response.status_code} {response.text}"
            )


class TwitterAuthenticator:
    def __init__(self, consumer_key, consumer_secret):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret

    def get_authentication_session(self):
        # Get request token
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        oauth = OAuth1Session(self._consumer_key, client_secret=self._consumer_secret)

        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")
        print("Got OAuth token:", resource_owner_key)

        # Get authorization
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)
        print("Please go here and authorize:", authorization_url)
        verifier = input("Paste the PIN here: ")

        # Get the access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            self._consumer_key,
            client_secret=self._consumer_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        return OAuth1Session(
            self._consumer_key,
            client_secret=self._consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )
