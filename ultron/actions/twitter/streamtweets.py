import tweepy
from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class StreamTweets(Action, tweepy.StreamListener):
    def __init__(self):
        super().__init__()
        self.api = load_api()

    @staticmethod
    def on_status(status, **kwargs):
        print(status.text)

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Tracks a given term in stream of tweets.
        :param args: No use, currently.
        :param kwargs: Keyword arguments. 'keyword'is only
        accepted keyword, which indicates the search term.
        :return: None
        """
        try:
            curr_stream = tweepy.Stream(auth=self.api.auth, listener=self)
            curr_stream.filter(track=[kwargs['keyword']], async=True)
        except TweepError as stream_error:
            print(stream_error)

    def post_execute(self, *args, **kwargs):
        pass
