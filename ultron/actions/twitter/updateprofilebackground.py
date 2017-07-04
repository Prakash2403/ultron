from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class UpdateProfileBackground(Action):
    # Some error is present. Created a PR in tweepy to fix it.
    # TODO Fix error here
    def __init__(self):
        self.api = load_api()
        self.update_background_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Updates background image of authenticated user.
        :param args: Currently, no use.
        :param kwargs: Keyword arguments, only 'filename'
        is accepted, which indicated the path of file.
        Path must be absolute and reside on local machine.
        :return: None
        """
        try:
            self.api.update_profile_background_image(
                filename=kwargs['filename'])
        except TweepError as update_background_error:
            print(update_background_error)
            self.update_background_status = False

    def post_execute(self, *args, **kwargs):
        if self.update_background_status:
            print('Background image updated')
