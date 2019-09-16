import os
import sys
from argparse import ArgumentParser
from flask_manage.commands import add_parsers_to

__version__ = '0.0.1-dev11'
PROJECT_TEMPLATE_PATH = os.path.join(__path__[0], 'project_template')

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = ArgumentParser(
        prog='flask-manage',
        description='Create flask project template.')
    parser.add_argument('--version', '-v', action='version', version=__version__)
    subparsers = parser.add_subparsers(dest='command', required=True)
    add_parsers_to(subparsers)

    args = parser.parse_args(argv)
    args.command(args)