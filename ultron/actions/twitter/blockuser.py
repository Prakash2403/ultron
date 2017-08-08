from tweepy import TweepError

from ultron.actions import Action
from ultron.exception.twitterexceptions import InvalidUserException
from ultron.helpers.twitter_helper import load_api


class BlockUser(Action):
    def __init__(self, screen_name):
        self.api = load_api()
        self.block_status = False
        self.screen_name = screen_name

    def pre_execute(self):
        pass

    def execute(self):
        """
        Blocks a user.
        """
        try:
            self.api.create_block(screen_name=self.screen_name)
        except TweepError:
            raise InvalidUserException
        self.block_status = True

    def post_execute(self):
        if self.block_status:
            print(self.screen_name + ' Blocked')
