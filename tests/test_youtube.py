import os
import unittest

import shutil

from ultron.actions.youtube.downloadvideo import DownloadVideo
from ultron.actions.youtube.searchvideo import SearchVideo


class YoutubeTest(unittest.TestCase):
    def test_search_video(self):
        search_video = SearchVideo('One second video')
        try:
            search_video.pre_execute()
            search_video.execute()
            search_video.post_execute()
        except Exception:
            pass
        self.assertEqual(search_video.search_status, True)

    def test_download_video(self):
        # Test case 1
        download_video = DownloadVideo(query='1 second Video')
        try:
            download_video.pre_execute(test=True)
            download_video.execute()
            download_video.post_execute()
        except shutil.Error:
            print('File with filename ' + download_video.filename
                  + ' already exists in destination directory')
        except FileNotFoundError:
            print("Destination directory doesn't exists")
        self.assertEqual(download_video.download_status, True)

        # Test case 2
        download_video = DownloadVideo(query='1 second Video',
                                       filename='onesecvid.mp4')
        try:
            download_video.pre_execute(test=True)
            download_video.execute()
            download_video.post_execute()
        except shutil.Error:
            print('File with filename ' + download_video.filename
                  + ' already exists in destination directory')
        except FileNotFoundError:
            print("Destination directory doesn't exists")
        self.assertEqual(download_video.download_status, True)

        # Test case 3
        download_video = DownloadVideo(query='1 second Video',
                                       filename='1sv.mp4',
                                       storage_directory=os.path.expanduser('~'))
        try:
            download_video.pre_execute(test=True)
            download_video.execute()
            download_video.post_execute()
        except shutil.Error:
            print('File with filename ' + download_video.filename
                  + ' already exists in destination directory')
        except FileNotFoundError:
            print("Destination directory doesn't exists")
        self.assertEqual(download_video.download_status, True)

        # Test case 4
        download_video = DownloadVideo(query='1 second Video',
                                       filename='1SV.mp4',
                                       storage_directory="This path "
                                                         "doesn't exists")
        try:
            download_video.pre_execute(test=True)
            download_video.execute()
            download_video.post_execute()
        except shutil.Error:
            print('File with filename ' + download_video.filename
                  + ' already exists in destination directory')
        except FileNotFoundError:
            print("Destination directory doesn't exists")
        self.assertEqual(download_video.download_status, False)
