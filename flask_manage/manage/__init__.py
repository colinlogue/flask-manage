from argparse import ArgumentParser
from .manage import newproject

def main(argv=None):
    parser = ArgumentParser(
        prog='flask-manage',
        description='Create flask project template.')
    subparsers = parser.add_subparsers(title="commands")

    parser_newproject = subparsers.add_parser('newproject')
    parser_newproject.add_argument(
        'dest',
        nargs='?',
        default='.',
        help='location to install project template (default current directory)')
    parser_newproject.set_defaults(func=newproject)

    if argv is not None:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()
    args.func(args)