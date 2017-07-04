from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class UnfollowUser(Action):
    def __init__(self):
        self.api = load_api()
        self.unfollow_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Un-follows a user.
        :param args: Currently, no use.
        :param kwargs: Keyword arguments, only 'screen_name'
        is accepted, which indicated the screen name of user
        to be un-followed.
        :return: None
        """
        try:
            self.api.destroy_friendship(screen_name=kwargs['screen_name'])
        except TweepError as unfollow_exception:
            print(unfollow_exception)
            self.unfollow_status = False

    def post_execute(self, *args, **kwargs):
        if self.unfollow_status:
            print('You have unfollowed ' + kwargs['name'])
