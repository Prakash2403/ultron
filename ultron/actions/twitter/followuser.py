from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class FollowUser(Action):
    def __init__(self):
        self.api = load_api()
        self.follow_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Follows a user.
        :param args: Currently, no use.
        :param kwargs: Keyword arguments, only 'screen_name'
        is accepted, which indicated the screen name of user
        to be followed.
        :return: None
        """
        try:
            self.api.create_friendship(screen_name=kwargs['screen_name'])
        except TweepError as follow_exception:
            print(follow_exception)
            self.follow_status = False

    def post_execute(self, *args, **kwargs):
        if self.follow_status:
            print('You have followed ' + kwargs['name'])
