import tweepy
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class StreamTweets(Action, tweepy.StreamListener):
    def __init__(self, keyword):
        super().__init__()
        self.api = load_api()
        self.keyword = keyword

    @staticmethod
    def on_status(status, **kwarg):
        print(status.text)

    def pre_execute(self):
        pass

    def execute(self):
        """
        Tracks a given term in stream of tweets.
        """
        curr_stream = tweepy.Stream(auth=self.api.auth, listener=self)
        curr_stream.filter(track=[self.keyword], async=True)

    def post_execute(self):
        pass
