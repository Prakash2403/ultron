from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class BlockUser(Action):
    def __init__(self):
        self.api = load_api()
        self.block_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Blocks a user.
        :param args: Currently, no use.
        :param kwargs: Keyword arguments, only 'screen_name'
        is accepted, which indicated the screen name of user
        to be blocked.
        :return: None
        """
        try:
            self.api.create_block(screen_name=kwargs['screen_name'])
        except TweepError as block_exception:
            print(block_exception)
            self.block_status = 1

    def post_execute(self, *args, **kwargs):
        if self.block_status:
            print(kwargs['name'] + ' Blocked')
