from setuptools import setup

setup(name='Augustins',
    version = '0.5',
    description  = 'Managing the Augustins mass-upload to Wikimedia Commons.',
    author       = 'Jean-Frederic',
    author_email = 'JeanFred@github',
    #packages=[''],
    install_requires = ['MassUploadLibrary'],
    dependency_links = ['https://github.com/JeanFred/MassUploadLibrary/archive/master.tar.gz#egg=MassUploadLibrary'],
    )
