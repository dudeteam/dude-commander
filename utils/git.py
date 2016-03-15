import subprocess
import os
import json
from errors import CommandError


def get_branch(name):
    """
    Returns the latest version for the given element.
    :param name: the bower element's name
    """
    p = subprocess.Popen(("git", "-C", os.path.join("..", name), "rev-parse", "--abbrev-ref", "HEAD"),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if not out:
        raise CommandError(json.loads(err)[0]["message"])
    return out.strip()


def release(name):
    print "release %s" % name
