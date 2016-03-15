import click


@click.command(help="Create a new element")
@click.argument("name")
def create(name):
    print name
    # - clone dude-seed
    # - s/dude-seed/name/
    # - remote .git
    # - create repo on github (via github api?)
    # - push repo
    # - register to bower registry
    # - add repo in commander config
