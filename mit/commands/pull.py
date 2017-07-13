# coding=utf-8

from colorama import Fore
from git import Repo
from git.exc import GitCommandError

from mit.commands import Command
from mit.commands.printer import Printer
from mit.commands.status import Status


class Pull(Command):

    def run_for_each_repo(self, repo, folder):
        git_repo = Repo(folder)
        try:
            git_repo.git.pull("--rebase")
            Status().run_for_each_repo(repo, folder)
        except GitCommandError:
            branch_name = git_repo.active_branch.name
            message = Printer.get_prefix(repo) + Fore.LIGHTWHITE_EX + " (" + branch_name + ")"
            message += " - " + Fore.LIGHTRED_EX + "✘ could not pull rebase!"
            Printer.p(message)
