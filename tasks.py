'''Handling build tasks'''
import multiprocessing

import invoke
import path


def _get_py_files():
    top_path = path.Path(".")
    top_dirs = top_path.dirs()
    for top_dir in top_dirs:
        if top_dir.joinpath("__init__.py").exists():
            yield top_dir
    yield from (x for x in top_path.files("*.py"))


def _get_pylint_args():
    num_cpus = multiprocessing.cpu_count()
    return " ".join(_get_py_files()) + " -j%i" % num_cpus


@invoke.task
# pylint: disable=W0613
def pylint(ctx):
    '''Invoke pylint'''
    invoke.run("pylint " + _get_pylint_args(), echo=True)


@invoke.task
# pylint: disable=W0613
def pep8(ctx):
    '''Invoke pep8'''
    invoke.run("pep8 " + " ".join(_get_py_files()), echo=True)


@invoke.task
# pylint: disable=W0613
def check(ctx):
    '''Invoke pep8 pylint & test'''
    pep8(ctx)
    pylint(ctx)
    # TODO: Add task integrating for test


@invoke.task
# pylint: disable=W0613
def gunicorn(ctx):
    '''Invoke gunicorn server'''
    ctx.run("gunicorn wsgi", echo=True)


@invoke.task
# pylint: disable=W0613,W0622
def help(ctx):
    '''See supported tasks'''
    print("invoke <task>\nSupported Tasks: pep8, pylint, check, gunicorn")
