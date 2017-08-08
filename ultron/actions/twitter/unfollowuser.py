from tweepy import TweepError

from ultron.actions import Action
from ultron.exception.twitterexceptions import InvalidUserException
from ultron.helpers.twitter_helper import load_api


class UnfollowUser(Action):
    def __init__(self, screen_name):
        self.api = load_api()
        self.unfollow_status = False
        self.screen_name = screen_name

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self):
        """
        Un-follows a user.
        """
        try:
            self.api.destroy_friendship(screen_name=self.screen_name)
        except TweepError:
            raise InvalidUserException
        self.unfollow_status = True

    def post_execute(self):
        if self.unfollow_status:
            print('You have unfollowed ' + self.screen_name)
