from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class UserTimeLineTweets(Action):
    def __init__(self):
        self.api = load_api()
        self.user_timeline_tweets_status = True
        self.timeline_tweets = None

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
            Retrieves latest 20 tweets from given user's timeline.
            :param args: Currently, no use.
            :param kwargs: keyword arguments, only 'screen_name'
            is accepted, where 'screen_name' is screen
            name of target user.
            :return: None
        """
        try:
            self.timeline_tweets = self.api.user_timeline(
                kwargs['screen_name'])
        except TweepError as user_timeline_error:
            print(user_timeline_error)
            self.user_timeline_tweets_status = False

    def post_execute(self, *args, **kwargs):
        if self.user_timeline_tweets_status:
            for status in self.timeline_tweets:
                print(status.text+"  :tweeted by: "+status.author.screen_name)
