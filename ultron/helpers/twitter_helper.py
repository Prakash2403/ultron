import tweepy
import os

from tweepy import TweepError, RateLimitError

from ultron.exception import NoSecretFileException, InvalidAPIException
from ultron.exception.twitterexceptions import MaximumLimitCrossedException


class APIHandler:
    """
    This class handles twitter api creation and validation.
    """
    _api = None

    @staticmethod
    def create_api():
        if APIHandler._api is None:
            try:
                with open(os.path.join(os.path.dirname(__file__), '../api_keys/twitter_keys'), 'r') as f:
                    keys = f.readlines()
            except FileNotFoundError:
                raise NoSecretFileException("File containing twitter OAuth keys doesn't exists. "
                                            "Please create a file named twitter_keys "
                                            "containing your OAuth credentials "
                                            "in ultron/ultron/api_keys directory.")
            keys = [key.strip() for key in keys]
            if len(keys) != 4:
                raise InvalidAPIException('Twitter requires 4 keys. But, '
                                          + str(len(keys)) +
                                          ' are present. Please ensure '
                                          'that keys are placed in same order '
                                          'as mentioned in README')
            else:
                consumer_key = keys[0]
                consumer_secret = keys[1]
                access_token = keys[2]
                access_token_secret = keys[3]
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                APIHandler._api = tweepy.API(auth)
        try:
            APIHandler._api.verify_credentials()
        except RateLimitError:
            raise MaximumLimitCrossedException('Rate limit for API is reached. '
                                               'Please wait for 15 minutes.')
        except TweepError:
            raise InvalidAPIException('Invalid or expired token')
        return APIHandler._api


def load_api():
    return APIHandler.create_api()
