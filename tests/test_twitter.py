import os
import warnings
import unittest
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


class TwitterTest(unittest.TestCase):

    def test_home_timeline(self):
        warnings.simplefilter("ignore")
        obj = HomeTimeLine()
        obj.execute()
        self.assertEqual(obj.home_timeline_status, True)

    def test_follow(self):
        obj = FollowUser()
        obj.execute(screen_name='kamaalrkhan')
        self.assertEqual(obj.follow_status, True)

    def test_unfollow(self):
        obj = UnfollowUser()
        obj.execute(screen_name='kamaalrkhan')
        self.assertEqual(obj.unfollow_status, True)

    def test_block_user(self):
        obj = BlockUser()
        obj.execute(screen_name='kamaalrkhan')
        self.assertEqual(obj.block_status, True)

    def test_update_profile_image(self):
        obj = UpdateProfileImage()
        filename = os.path.join(os.path.expanduser('~'), 'Documents/SJ.jpg')
        obj.execute(filename=filename)
        if os.path.exists(filename):
            self.assertEqual(obj.update_profile_status, True)
        else:
            self.assertEqual(obj.update_profile_status, False)

    def test_update_profile(self):
        obj = UpdateProfile()
        obj.execute(name='Prakash Rai')
        self.assertEqual(obj.update_profile_status, True)

    def test_send_message(self):
        obj = SendMessage()
        obj.execute(screen_name='ultronhasaccount',
                    text='Ultron sent a message to you')
        self.assertEqual(obj.send_message_status, True)

    def test_retrieve_message(self):
        obj = RetrieveMessage()
        obj.execute()
        self.assertEqual(obj.retrieve_message_status, True)

    def test_search_users(self):
        obj = SearchUsers()
        obj.execute(query='Python')
        self.assertEqual(obj.search_user_status, True)

    def test_fetch_details(self):
        obj = FetchDetails()
        obj.execute(screen_name='ultronhasaccount')
        self.assertEqual(obj.fetch_details_status, True)

    def test_status_update(self):
        obj = StatusUpdate()
        obj.execute(text='Ultron is being tested again')
        self.assertEqual(obj.status_update_status, True)

    def test_user_timeline(self):
        obj = UserTimeLineTweets()
        obj.execute(screen_name='ultronhasaccount')
        self.assertEqual(obj.user_timeline_tweets_status, True)
