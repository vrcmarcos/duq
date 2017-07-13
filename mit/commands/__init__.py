import os
from abc import ABCMeta, abstractmethod


class Command(object):

    __metaclass__ = ABCMeta

    __GIT_FOLDER_NAME = ".git"

    def run(self):
        for repo, folder in self._get_git_folders().items():
            self.run_for_each_repo(repo, folder)

    @abstractmethod
    def run_for_each_repo(self, repo, folder):
        raise NotImplementedError("You MUST implement this method!")

    @classmethod
    def _get_git_folders(cls):
        current_folder = os.getcwd()
        repo_folders = {}
        for folder in os.listdir(current_folder):
            repo_folder = os.path.join(current_folder, folder)
            package_git_folder = os.path.join(repo_folder, cls.__GIT_FOLDER_NAME)
            if os.path.exists(package_git_folder):
                repo_folders[folder] = repo_folder
        return repo_folders
