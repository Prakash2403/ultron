from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class UpdateProfile(Action):
    def __init__(self):
        self.api = load_api()
        self.update_profile_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Updates profile of authenticated user.
        :param args: Currently, no use.
        :param kwargs: Keyword arguments, 'name', 'url',
        'location', 'descriptions' are accepted.
        :return: None
        """
        try:
            self.api.update_profile(name=kwargs.get('name', None),
                                    location=kwargs.get('location', None),
                                    url=kwargs.get('url', None),
                                    description=kwargs.get('description', None))
        except TweepError as profile_update_error:
            print(profile_update_error)
            self.update_profile_status = False

    def post_execute(self, *args, **kwargs):
        if self.update_profile_status:
            print("Profile updated")
