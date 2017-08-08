from tweepy import TweepError
from ultron.actions import Action
from ultron.exception.twitterexceptions import InvalidUserException
from ultron.helpers.twitter_helper import load_api


class FollowUser(Action):
    def __init__(self, screen_name):
        self.api = load_api()
        self.follow_status = False
        self.screen_name = screen_name

    def pre_execute(self):
        pass

    def execute(self):
        """
        Follows a user.
        """
        try:
            self.api.create_friendship(screen_name=self.screen_name)
        except TweepError:
            raise InvalidUserException
        self.follow_status = True

    def post_execute(self):
        if self.follow_status:
            print('You have followed ' + self.screen_name)
