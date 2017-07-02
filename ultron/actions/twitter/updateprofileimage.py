import os
from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class UpdateProfileImage(Action):
    def __init__(self):
        self.api = load_api()
        self.update_profile_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Updates the profile image of authenticated user.
        :param args: Currently, no use.
        :param kwargs: Keyword arguments, only 'filename'
        is accepted, which indicated the path of file.
        Path must be absolute and reside on local machine.
        :return: None
        """
        try:
            if not os.path.exists(kwargs['filename']):
                raise FileNotFoundError
            self.api.update_profile_image(filename=kwargs['filename'])
        except TweepError as update_profile_error:
            print(update_profile_error)
            self.update_profile_status = False
        except FileNotFoundError:
            print('File not found')
            self.update_profile_status = False

    def post_execute(self, *args, **kwargs):
        if self.update_profile_status:
            print('Updated Profile Picture')
