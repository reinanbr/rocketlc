from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='rocketlc',
    version='0.1.2',
    url='https://github.com/reinanbr/rocketlc',
    license='BSD v3',
    author='Reinan Br',
    #entry_points = {
    #    'console_scripts': ['getmusic=tubemp3.get_music_line:main'],
    #},
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='rocket launch schedule',
    description=u"Library for getting schedule launch rocket",
    packages=find_packages(),
    install_requires=['requests','mechanicalsoup','cssutils','bs4'],)
