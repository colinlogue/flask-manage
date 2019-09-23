import subprocess
import sys

#currently just installs with pip and adds package to list in modules.py

def install(package):
    subprocess.call([sys.executable, '-m', 'pip', 'install', package])


def setup_parser(parser):
    parser.add_argument(
        'name',
        help='name of the package in the repository')
    parser.add_argument(
        'version',
        help='which version to install')

def execute(args):
    pass