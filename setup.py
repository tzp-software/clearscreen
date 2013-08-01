try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'clearscreen',
    'version': '1.0.1',
    'author': 'Kyle Roux',
    'author_email': 'jstacoder@gmail.com',
    'description': 'common function with cool options',
    'long_description': open('README','r').read(),
    'packages': ['clearscreen'],
    'entry_points': {'console_scripts':['clear-screen = clearscreen.main:main']},
    }

setup(**config)
	
