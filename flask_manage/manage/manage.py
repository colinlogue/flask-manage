import os
import shutil

def newproject(args):
    if 'dest' in args:
        dest = args.dest
    else:
        dest = os.path.join(os.getcwd(), 'new_project')
    src = os.path.join(os.path.dirname(__file__), 'project_template')
    shutil.copytree(src, dest)