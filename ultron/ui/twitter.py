from ultron.actions.twitter.hometimeline import HomeTimeLine
from ultron.actions.twitter.blockuser import BlockUser
from ultron.actions.twitter.fetchdetails import FetchDetails
from ultron.actions.twitter.followuser import FollowUser
from ultron.actions.twitter.unfollowuser import UnfollowUser
from ultron.actions.twitter.updateprofile import UpdateProfile
from ultron.actions.twitter.retrievemessage import RetrieveMessage
from ultron.actions.twitter.sendmessage import SendMessage
from ultron.actions.twitter.updateprofileimage import UpdateProfileImage
from ultron.actions.twitter.statusupdate import StatusUpdate
from ultron.actions.twitter.searchusers import SearchUsers
from ultron.actions.twitter.usertimeline import UserTimeLineTweets
from ultron.exception import NotAbsolutePathException, InvalidAPIException, NoSecretFileException
from ultron.exception.twitterexceptions import InvalidUserException
from ultron.ui import BaseInterpreter


class Twitter(BaseInterpreter):
    def __init__(self):
        super().__init__()
        self.prompt = "Twitter>>> "

    @staticmethod
    def run(twitter_obj):
        try:
            twitter_obj.run()
        except FileNotFoundError:
            print("Path entered for media file doesn't exists."
                  " Please enter a correct path.")
        except InvalidUserException:
            print('Screen name of user is invalid.')
        except NotAbsolutePathException:
            print('Path entered by you is not absolute.'
                  ' Please enter an absolute address.')
        except InvalidAPIException:
            print('OAuth keys are expired or invalid. '
                  'Please generate a new key. Instructions for generating'
                  'keys are given in README file.')
        except NoSecretFileException:
            print("File containing secret keys doesn't exists. "
                  "Please follow instructions written in readme.")

    def do_home_timeline(self, *args):
        home_time_line = HomeTimeLine()
        Twitter.run(home_time_line)

    def do_block_user(self, *args):
        screen_name = input(
            "Enter the screen name of user you want to block\n")
        block_user = BlockUser(screen_name=screen_name)
        Twitter.run(block_user)

    def do_user_timeline_details(self, *args):
        screen_name = input('Enter the screen name of user\n')
        user_timeline = UserTimeLineTweets(screen_name=screen_name)
        Twitter.run(user_timeline)

    def do_search_users(self, *args):
        keyword = input("Enter search keyword\n")
        search_users = SearchUsers(query=keyword)
        Twitter.run(search_users)

    def do_update_your_status(self, *args):
        status = input("Enter status text.\n")
        media_file = input("Enter absolute path of media file you want to attach. "
                           "Leave blank if you don't want to attach any media.\n")
        if len(media_file.strip()) == 0:
            status_update = StatusUpdate(text=status)
        else:
            status_update = StatusUpdate(text=status, media_file=media_file)
        Twitter.run(status_update)

    def do_update_your_profile(self, *args):
        profile_data = {}
        name = input('Enter your name. Leave blank to use previous.\n')
        if len(name.strip()) != 0:
            profile_data['name'] = name.strip()
        description = input(
            'Enter new description. Leave blank to use previous.\n')
        if len(description.strip()) != 0:
            profile_data['description'] = description.strip()
        url = input('Enter url of your website. Leave blank to use previous.\n')
        if len(url.strip()) != 0:
            profile_data['url'] = url.strip()
        location = input(
            'Enter your current location. Leave blank to use previous.\n')
        if len(location.strip()) != 0:
            profile_data['location'] = location.strip()
        update_profile = UpdateProfile(profile_data=profile_data)
        Twitter.run(update_profile)

    def do_follow_user(self, *args):
        screen_name = input('Enter screen name of user you want to follow\n')
        follow_user = FollowUser(screen_name=screen_name)
        Twitter.run(follow_user)

    def do_unfollow_user(self, *args):
        screen_name = input('Enter screen name of user you want to unfollow\n')
        unfollow_user = UnfollowUser(screen_name=screen_name)
        Twitter.run(unfollow_user)

    def do_send_message(self, *args):
        screen_name = input(
            'Enter screen name of user to whom you want to send message.\n')
        text = input('Enter message to be sent\n')
        send_message = SendMessage(screen_name=screen_name, text=text)
        Twitter.run(send_message)

    def do_retrieve_message(self, *args):
        retrieve_message = RetrieveMessage()
        Twitter.run(retrieve_message)

    def do_get_details_of_a_user(self, *args):
        screen_name = input('Enter screen name of user.\n')
        user_details = FetchDetails(screen_name=screen_name)
        Twitter.run(user_details)

    def do_update_profile_image(self, *args):
        media_file = input("Enter absolute path of image file.\n")
        update_profile_image = UpdateProfileImage(filename=media_file)
        Twitter.run(update_profile_image)
