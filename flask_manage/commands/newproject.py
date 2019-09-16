import os
import shutil
from flask_manage import PROJECT_TEMPLATE_PATH

def ignore_pycache(current_dir, contents):
    return ['__pycache__']


parser_args = {
    '_constructor': {},
    'add_argument': [
        ( ['label'], {
            'help': 'name of the project to be created',
        } ),
        ( ['dest'], {
            'nargs': '?',
            'default': '.',
            'help': 'location to install project (default currest directory)',
        } ),
    ],
}

def execute(args):
    dest = os.path.join(args.dest, args.label)
    src = os.path.join(PROJECT_TEMPLATE_PATH)
    shutil.copytree(src, dest, ignore=ignore_pycache)