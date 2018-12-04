import os
import click
import subprocess

from app import create_app
from instance.db import Model

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
model = Model()


@app.cli.command()
def migrate():
    """
    Run db migrate to initialize a connection
    :return:
    """
    model.init_app(app)
    model.create_table_user()
    model.create_table_incident()


@app.cli.command()
def drop():
    """
    Run db migrate to initialize a connection
    :return: Done
    """
    model.init_app(app)
    model.drop_tables()


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
@click.argument('path', default='app')
def flake8(path):
    """
    Run flake8 to analyze your code base.

    :param path: Test coverage path
    :return: Subprocess call result
    """

    cmd = 'flake8 {0}'.format(path)
    return subprocess.call(cmd, shell=True)
