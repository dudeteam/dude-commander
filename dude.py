import click
import logging
from errors import CommandError
from commands.update import update
from commands.status import status
from commands.create import create
from commands.release import release


logger = logging.getLogger(__name__)


@click.group()
@click.option('--log-level', '-l', default='INFO')
def dude(log_level):
    logging.basicConfig(format="%(levelname)s:  %(message)s", level=log_level)


dude.add_command(update)
dude.add_command(status)
dude.add_command(create)
dude.add_command(release)

if __name__ == "__main__":
    try:
        dude()
    except CommandError as e:
        logger.error(e.message)
