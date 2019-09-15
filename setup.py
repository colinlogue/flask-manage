import os
import setuptools
import toml


def read_file(filepath):
    dirname = os.path.dirname(__file__)
    with open(filepath) as f:
        return f.read()

proj_config = toml.loads(read_file('project.toml'))


pkg_settings = {
    'python_requires': proj_config['dependencies']['python'],
    'packages': setuptools.find_packages(exclude=['dev']),
    'include_package_data': True,
    'entry_points': {
        'console_scripts': [
            'flask-manage = flask_manage.manage:main',
        ],
    },
    'long_description': read_file('README.md'),
    'long_description_content_type': 'text/markdown',
}

pkg_settings.update(proj_config['package'])


setuptools.setup(**pkg_settings)