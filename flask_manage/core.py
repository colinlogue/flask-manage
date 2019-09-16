import pkgutil
import importlib
from flask_manage.utils import list_submodules


def register_mods(app):
    """Registers each module with the flask app.

    Each submodule of `app.modules` can have a `register`
    function that will perform any necessary setup to the app
    (e.g. registering blueprints). `register_mods` is called
    from `flask_manage.core.register`, by default from the
    `create_app` function in `app.factory`.
    """

    mod_names = list_submodules('app/modules')
    for mod_name in mod_names:
        mod = importlib.import_module(f'app.modules.{mod_name}')
        register = getattr(mod, 'register', None)
        if register is not None:
            register(app)