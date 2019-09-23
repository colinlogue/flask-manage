import os
import shutil

from jinja2 import Environment, FileSystemLoader

from flask_manage import PROJECT_TEMPLATE_PATH

TEMPLATE_EXTS = ['.j2']

def ignore_pycache(current_dir, contents):
    return ['__pycache__']


def setup_parser(parser):
    parser.add_argument(
        'label',
        help='name of the project to be created')
    parser.add_argument(
        'dest',
        nargs='?',
        default='.',
        help='location to install project (default current directory')

def copy_template_dir(src, dest, root=None, env=None, context=None, ignore=None):
    if context is None:
        context = {}
    if ignore is None:
        ignore = []
    if root is None:
        root = src
    if env is None:
        env = Environment(loader=FileSystemLoader(root))
    for item in os.listdir(src):
        if not item in ignore:
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)
            if os.path.isdir(src_path):
                os.mkdir(dest_path)
                copy_template_dir(
                    src_path,
                    dest_path,
                    root=root,
                    env=env,
                    context=context,
                    ignore=ignore)
            else:
                # if is template file, render
                # otherwise, copy
                src_root, src_ext = os.path.splitext(src_path)
                if src_ext in TEMPLATE_EXTS:
                    rel_src_path = os.path.relpath(src_path, src)
                    template = env.get_template(rel_src_path)
                    with open(dest_path, 'w') as f:
                        f.write(template.render(**context))
                else:
                    shutil.copyfile(src_path, dest_path)

def execute(args):
    dest = os.path.join(args.dest, args.label)
    src = os.path.join(PROJECT_TEMPLATE_PATH)
    shutil.copytree(src, dest, ignore=ignore_pycache)
    # walk files and replace all .j2.py with .py by rendering templates
    copy_template_dir(src, dest, context, ignore=['__pycache__'])