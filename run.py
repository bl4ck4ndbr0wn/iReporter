import os
import click
import subprocess

from app import create_app
from instance.db import Model

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.cli.command()
def migrate():
    """
    Run db migrate to initialize a connection
    :return:
    """
    Model().init_app(app)
    Model().create_table_user()
    Model().create_table_incident()


@app.cli.command()
def drop():
    """
    Run db migrate to initialize a connection
    :return: Done
    """
    Model().init_app(app)
    Model().drop_tables()


@app.cli.command()
@click.argument('path', default=os.path.join('app', 'tests'))
def test(path):
    """
    Run tests with Pytest.

    :param path: Test path
    :return: Subprocess call result
    """
    cmd = 'py.test -v {0}'.format(path)
    return subprocess.call(cmd, shell=True)


@app.cli.command()
@click.argument('path', default='app')
def cov(path):
    """
    Run a test coverage report.

    :param path: Test coverage path
    :return: Subprocess call result
    """

    cmd = 'py.test -v --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)


@app.cli.command()
@click.option('--skip-init/--no-skip-init', default=True,
              help='Skip __init__.py files?')
@click.argument('path', default='app')
def flake8(skip_init, path):
    """
    Run flake8 to analyze your code base.

    :param skip_init: Skip checking __init__.py files
    :param path: Test coverage path
    :return: Subprocess call result
    """
    flake8_flag_exclude = ''

    if skip_init:
        flake8_flag_exclude = ' --exclude __init__.py'

    cmd = 'flake8 {0}{1}'.format(path, flake8_flag_exclude)
    return subprocess.call(cmd, shell=True)
