from tweepy import TweepError

from ultron.actions import Action
from ultron.exception.twitterexceptions import InvalidUserException
from ultron.helpers.twitter_helper import load_api


class UserTimeLineTweets(Action):
    def __init__(self, screen_name):
        self.api = load_api()
        self.user_timeline_tweets_status = True
        self.timeline_tweets = None
        self.screen_name = screen_name

    def pre_execute(self):
        pass

    def execute(self):
        """
        Retrieves latest 20 tweets from given user's timeline.
        """
        try:
            self.timeline_tweets = self.api.user_timeline(
                self.screen_name)
        except TweepError:
            raise InvalidUserException
        self.user_timeline_tweets_status = True

    def post_execute(self, *args, **kwargs):
        if self.user_timeline_tweets_status:
            for status in self.timeline_tweets:
                print(status.text+"  :tweeted by: "+status.author.screen_name)
