import click
from utils import bower
from config import elements


@click.command(help="Update the element to the latest version in all elements")
@click.argument("name")
def update(name):
    for element_name in elements:
        if name != element_name:
            bower.update_element(name, element_name)
