from argparse import ArgumentParser
from flask_manage.commands import newproject

def main(argv):
    parser = ArgumentParser(
        prog='flask-manage',
        description='Create flask project template.')
    subparsers = parser.add_subparsers(title='commands')

    parser_newproject = subparsers.add_parser('newproject')
    parser_newproject.add_argument(
        'label',
        help='name of the project to be created. used as the new directory name.')
    parser_newproject.add_argument(
        'dest',
        nargs='?',
        default='.',
        help='location to install project template (default current directory)')
    parser_newproject.set_defaults(command=newproject)

    args = parser.parse_args(argv)
    args.command.execute(args)

def register_modules(app):
    pass