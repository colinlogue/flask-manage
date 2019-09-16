from argparse import ArgumentParser
from flask_manage.commands import add_parsers_to

__version__ = '0.0.1-dev6'

def main(argv):
    parser = ArgumentParser(
        prog='flask-manage',
        description='Create flask project template.')
    parser.add_argument('--version', '-v', action='version', version=__version__)
    subparsers = parser.add_subparsers(dest='command', required=True)
    add_parsers_to(subparsers)

    args = parser.parse_args(argv)
    args.command(args)

def register_modules(app):
    pass