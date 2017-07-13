import click
import colorama

from mit.commands.checkout import Checkout
from mit.commands.fetch import Fetch
from mit.commands.pull import Pull
from mit.commands.status import Status


@click.group()
@click.version_option()
def cli():
    """Mit.

    Python tool for batch execution of git commands
    """
    colorama.init()


@cli.command()
def status():
    Status().run()


@cli.command()
def pull():
    Pull().run()


@cli.command()
@click.argument('branch')
def checkout(branch):
    Checkout(branch).run()


@cli.command()
def fetch():
    Fetch().run()
