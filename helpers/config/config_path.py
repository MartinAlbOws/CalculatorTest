from configparser import ConfigParser
import os
from os.path import normpath, join


def config_path():
    config = ConfigParser()
    config.read(server_normpath('./config.ini'))
    return config

def server_normpath(path):
    """
    This method is class specific and can't be moved during the code refactor.
    Method is returning current path based on working directory
    :param path:
    :return:
    """
    return normpath(join(os.path.dirname(os.path.abspath(__file__)), path))