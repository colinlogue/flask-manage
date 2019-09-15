import os
import shutil

def newproject(args):
    dest = os.path.join(args.dest, args.label)
    src = os.path.join(os.path.dirname(__file__), 'project_template')
    shutil.copytree(src, dest)