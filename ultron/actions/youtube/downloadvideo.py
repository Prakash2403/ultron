import os
import shutil

from ultron.actions import Action
import youtube_dl

from ultron.actions.youtube.searchvideo import SearchVideo


class DownloadVideo(Action):
    """
    post_execute method raises 2 errors, so if you are going
    to use this class anywhere, make sure that the errors are
    handled properly.

    For more information on error, look the documentation of
    post_execute method
    """

    def __init__(self, query, filename=None, storage_directory=None):
        """
        :param query: Search query.
        :param filename: Filename in which video will be saved.
        For default filename, see explanation in documentation
        of pre_execute method.
        :param storage_directory: Directory where user wants to save the file.
        Default storage directory is directory from where script is executed.
        """
        self.url = None
        self.filename = filename
        self.storage_directory = storage_directory
        self.query = query
        self.options = {'outtmpl': filename}
        self.download_status = True

    def pre_execute(self, *args, **kwargs):
        """
        Creates SearchVideo objects and search for the give query.
        For testing, we need not to show the search results, so results
        are displayed only when kwargs['test'] is True.
        If kwargs['test'] is False, then
        Displays search results title along with a number
        Asks user to enter the index number of video which they want to download.
        Then extracts the URL of the video which user has asked.
        Second last line checks whether user has given any
        filename for downloaded video or not.
        If no name is given by the user, last line provides a
        default filename to save the video, which is title of that video.
        """
        search_video = SearchVideo(self.query)
        search_video.execute()
        search_results = search_video.get_search_results()
        if not kwargs.get('test', False):
            for i in range(len(search_results)):
                print("[" + str(i + 1) + "] " +
                      search_results[i]['title'])
            choice = input("\nEnter the index number of video "
                           "which you want to download\n")
        else:
            choice = 1
        self.url = 'https://www.youtube.com' + \
                   search_results[int(choice) - 1]['href']
        if self.options['outtmpl'] is None:
            self.options['outtmpl'] = \
                search_results[int(choice) - 1]['title'] + '.mp4'

    def execute(self, *args, **kwargs):
        """
        Downloads the video.
        """
        with youtube_dl.YoutubeDL(self.options) as ydl:
            ydl.download([self.url])

    def post_execute(self, *args, **kwargs):
        """
        It deals with moving the downloaded file to directory given by
        user. If no storage directory is provided, youtube-dl stores
        the video from where script has been executed.

        Raises two errors:
        1. shutil.Error : This error is raised when a file with same name exists
        in directory pointed by user.
        2. FileNotFoundError: This error is raised when directory given by user
        is incorrect.

        In both case, video is saved in default directory, i.e. the directory from
        where the script is being executed.
        """
        if self.storage_directory is not None:
            if os.path.exists(self.storage_directory):
                curr_path = os.getcwd() + '/' \
                            + self.options['outtmpl']
                if os.path.exists(self.storage_directory + '/' + self.options['outtmpl']):
                    self.download_status = False
                    raise shutil.Error
                else:
                    if os.path.exists(curr_path):
                        shutil.move(curr_path, self.storage_directory)
                    else:
                        self.download_status = False
            else:
                self.download_status = False
                raise FileNotFoundError
