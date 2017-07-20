import os
import unittest


from ultron.actions.youtube.downloadvideo import DownloadVideo
from ultron.actions.youtube.searchvideo import SearchVideo
from ultron.exception import NotAbsolutePathException


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
        except FileExistsError as fee:
            print(str(fee))
        except PermissionError as pe:
            print(str(pe))
        except NotAbsolutePathException as nape:
            print(str(nape))
        self.assertEqual(download_video.download_status, True)

        # Test case 2
        download_video = DownloadVideo(query='1 second Video',
                                       filename='onesecvid.mp4')
        try:
            download_video.pre_execute(test=True)
            download_video.execute()
            download_video.post_execute()
        except FileExistsError as fee:
            print(str(fee))
        except PermissionError as pe:
            print(str(pe))
        except NotAbsolutePathException as nape:
            print(str(nape))
        self.assertEqual(download_video.download_status, True)

        # Test case 3
        # If you are going to change storage_directory,
        # make sure that you have changed it in print
        # statement where we are handling shutil.Error.

        download_video = DownloadVideo(query='1 second Video',
                                       filename='1sv.mp4',
                                       storage_directory=os.path.expanduser('~'))
        try:
            download_video.pre_execute(test=True)
            download_video.execute()
            download_video.post_execute()
        except FileExistsError as fee:
            print(str(fee))
        except PermissionError as pe:
            print(str(pe))
        except NotAbsolutePathException as nape:
            print(str(nape))
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
        except FileExistsError as fee:
            print(str(fee))
        except PermissionError as pe:
            print(str(pe))
        except NotAbsolutePathException as nape:
            print(str(nape))
        self.assertEqual(download_video.download_status, False)

        # Test case 5
        download_video = DownloadVideo(query='1 second Video',
                                       filename='1SV.mp4',
                                       storage_directory=os.path.expanduser('~')
                                       + "/This path doesn't exists yet")
        try:
            download_video.pre_execute(test=True)
            download_video.execute()
            download_video.post_execute()
        except FileExistsError as fee:
            print(str(fee))
        except PermissionError as pe:
            print(str(pe))
        except NotAbsolutePathException as nape:
            print(str(nape))
        self.assertEqual(download_video.download_status, True)
