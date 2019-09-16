# Flask-Manage
Flask-Manage is a set of common templates and configuration options
that I use to make starting a flask project really easy.
This is (currently, at least) very much tailored to my idiosyncrasies,
but I will try to keep it well documented so it can be availabe, if
it is useful to anyone else.

As I'm writing, this is still mostly a plan, so it's likely to change
significantly as I implement it.

## Reason for existing
This package is intended to solve two problems:
1.  Provide a quick-start template with many of the common
    templates, static files, and utilities that I use across
    different projects.
2.  Allow easy loading of modules that will just work, without
    having to manually configure each time I add one.

## Usage
Installing the package will add a script to the system path to create
a new project directory from the template:
```shell
flask-manage newproject proj_name
```
That's sort of all that it does at the moment.

## To-do
Eventually it should be able to manage a set of modules that can have
their own blueprints, templates, static files, etc. These templates
should be registered automatically if they have the right requirements
(a `register(app)` function, at a minimum).

## Core module
A special module called `core` provides some base templates and layouts
and is installed automatically (can be disabled with `--nocore` flag
when calling `newproject`.