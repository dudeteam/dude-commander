import click
from commands.update import update


@click.command(help="Release a new version of the element")
@click.argument("name")
def release(name):
    # - increase version in bower.json
    # - create a new release
    update(name)
