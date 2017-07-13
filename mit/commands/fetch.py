from git import Repo

from mit.commands import Command
from mit.commands.status import Status


class Fetch(Command):

    def run_for_each_repo(self, repo, folder):
        Repo(folder).git.fetch()
        Status().run_for_each_repo(repo, folder)
