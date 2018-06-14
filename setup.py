from setuptools import setup
setup(
    name = "Alpheus",
    version = "0.1",
    packages = ['alpheus'],

    install_requires = ['lxml'],
    
    entry_points = {
        'console_scripts': ['alpheus = alpheus:main']
    }
)
