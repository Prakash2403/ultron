import os
import shutil

from ultron.actions import Action
import youtube_dl

from ultron.actions.youtube.searchvideo import SearchVideo
from ultron.exception import NotAbsolutePathException, UnknownException


class DownloadVideo(Action):
    """
    post_execute method raises some errors and exceptions,
    so if you are going to use this class anywhere, make
    sure that they are handled properly.

    For more information on error, look the documentation of
    post_execute method
    """

    def __init__(self, query, filename=None,
                 storage_directory='/home/prakash/Downloads'):
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

        Raises following errors and exceptions:
        1. UnknownException: This exception is raised when everything went smoothly,
        but suddenly your python interpreter decides to f**k you.
        2. PermissionError : This is raised when user doesn't have permission to
        create/store the file in destination directory.
        3. FileExistsError: This error is raised when a file with same name as source
        file exists in destination folder.
        4. NotAbsolutePathException: This exception is raised when address of
        destination directory is not an absolute address

        If due to any reason, video is not copied to destination directory, then
        it will be stored in the directory from where script has been executed.
        """
        if not os.path.abspath(self.storage_directory):
            self.download_status = False
            raise NotAbsolutePathException('Destination is not an absolute path.')
        if not os.path.exists(self.storage_directory):
            if os.access(os.path.dirname(self.storage_directory), mode=os.W_OK):
                os.makedirs(self.storage_directory)
            else:
                self.download_status = False
                raise PermissionError('You are not allowed to create'
                                      ' a directory at ' +
                                      os.path.dirname(self.storage_directory) +
                                      ' .Storing video in current directory.')
        curr_path = os.getcwd() + '/' + self.options['outtmpl']
        if os.path.exists(self.storage_directory + '/' + self.options['outtmpl']):
            self.download_status = False
            raise FileExistsError('File already exists at storage directory.')
        else:
            if os.path.exists(curr_path):
                if os.access(self.storage_directory, os.W_OK):
                    shutil.move(curr_path, self.storage_directory)
                else:
                    self.download_status = False
                    raise PermissionError('You are not allowed to access. ' +
                                          self.storage_directory +
                                          '. Storing video in current directory.')
            else:
                self.download_status = False
                raise UnknownException('Your interpreter is drunk. Please retry')
