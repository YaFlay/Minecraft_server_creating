from setuptools import setup

from my_pip_package import __version__

setup(
    name='minecraft_server_installer',
    version=__version__,

    url='https://github.com/YaFlay/Minecraft_server_creating',
    author='Dima YaFlay',
    author_email='yaflay@vk.com',

    py_modules=['minecraft_server_installer'],
)
