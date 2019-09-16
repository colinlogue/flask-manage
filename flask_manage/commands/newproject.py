import os
import shutil

PROJECT_TEMPLATE_PATH = 'flask_manage/project_template'

def ignore_pycache(current_dir, contents):
    return ['__pycache__']

def execute(args):
    dest = os.path.join(args.dest, args.label)
    src = os.path.join(PROJECT_TEMPLATE_PATH)
    shutil.copytree(src, dest, ignore=ignore_pycache)