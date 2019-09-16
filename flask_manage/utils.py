import pkgutil

def list_submodules(pkg_path):
    return [name for _, name, _ in pkgutil.iter_modules([pkg_path])]