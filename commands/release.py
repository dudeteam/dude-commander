import click
from commands.update import update
from utils import bower, git


@click.command(help="Release a new version of the element")
@click.argument("name")
def release(name):
    # check if master
    # check no changes + up to date with remote
    bower.increase_version(name)
    git.release(name)
    update(name)
