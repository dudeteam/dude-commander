import subprocess
import json
import os
import logging
from errors import CommandError

logger = logging.getLogger(__name__)


def get_latest_version(name):
    """
    Returns the latest version for the given element.
    :param name: the bower element's name
    """
    p = subprocess.Popen(("bower", "info", "-j", name), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if not out:
        raise CommandError(json.loads(err)[0]["message"])
    return json.loads(out)["versions"][0]


def get_local(name):
    """
    Get the bower.json file of the given local element.
    :param name: the bower element's name
    """
    with open(os.path.join("..", name, "bower.json")) as bower_json:
        return json.load(bower_json)


def update_element(name, element_name):
    """
    Update the given element to its latest version.
    :param name: The name of the dependency to update
    :param element_name: The name of the element on which the update will be done
    """
    local_json = get_local(element_name)
    if "dependencies" in local_json and name in local_json["dependencies"]:
        logging.info("Updating %s dependency in %s" % (name, element_name))
        os.chdir(os.path.join("..", element_name))
        p = subprocess.Popen(("bower", "install", "--save", "-j", name), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if not out:
            raise CommandError(json.loads(err)[0]["message"])
        logging.debug(out)

