import os
from distutils.core import setup

os.system("touch /tmp/rce")

setup(name="pip-rce", version="0.0.1", description="PIP RCE test")
