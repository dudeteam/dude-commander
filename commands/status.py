import click
from terminaltables import AsciiTable
from utils import bower, git
from config import elements


@click.command(help="Show some status info on elements")
def status():
    rows = [
        ["name", "branch", "local version", "latest version"]
    ]
    for name in elements:
        rows.append([name, git.get_branch(name), bower.get_local(name)["version"], bower.get_latest_version(name)])
    print AsciiTable(rows).table
