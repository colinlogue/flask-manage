import importlib
from flask_manage.utils import list_submodules


# def add_parsers_to(subparsers):
#     pkg_path = __path__[0]
#     mod_names = list_submodules(pkg_path)
#     for mod_name in mod_names:
#         mod = importlib.import_module(f'flask_manage.commands.{mod_name}')
#         parser_args = getattr(mod, 'parser_args')
#         constr_args = {}
#         cleanup = None
#         if '_constructor' in parser_args:
#             constr_args = parser_args.pop('_constructor')
#         if '_cleanup' in parser_args:
#             cleanup = parser_args.pop('_cleanup')
#         parser = subparsers.add_parser(mod_name, **constr_args)
#         for attr, vals in parser_args.items():
#             func = getattr(parser, attr)
#             for args, kwargs in vals:
#                 func(*args, **kwargs)
#         parser.set_defaults(command=getattr(mod, 'execute'))
#         if cleanup is not None:
#             cleanup(parser)

def add_parsers_to(subparsers):
    mod_names = list_submodules(__path__)
    for mod_name in mod_names:
        mod = importlib.import_module(f'flask_manage.commands.{mod_name}')
        if hasattr(mod, 'constructor_args'):
            constructor_args = getattr(mod, 'constructor_args')
        else:
            constructor_args = {}
        parser = subparsers.add_parser(mod_name, **constructor_args)
        setup_parser = getattr(mod, 'setup_parser')
        setup_parser(parser)
        parser.set_defaults(command=getattr(mod, 'execute'))